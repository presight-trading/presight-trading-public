"""从英文页生成日 / 越 / 泰三个语种，并统一各页的语言切换器。

为什么用生成而不是手写：条款这两个月改了三次，每次都要把同一句话在所
有语种里各改一遍。四个文件时靠人还盯得住，十个文件就一定会漏——而漏
掉的那一版会一直挂在线上，同一个活动出现两套互相矛盾的条款。

生成的规则很简单：**英文页是唯一的结构来源**，其它语种只提供文本。
结构由解析器保证一致，漏翻的片段会原样留下英文——看得见，但页面不会坏。

改条款的流程：
  1. 改 index.html / protection.html（中文）与 en/ 下的两份
  2. python3 tools/build.py     # 会列出所有没翻译的新片段
  3. 把新片段补进 tools/lang_*.py，再跑一次

用法：
  uv run --with beautifulsoup4 python tools/build.py          # 生成全部
  uv run --with beautifulsoup4 python tools/build.py ja       # 只生成日文
  uv run --with beautifulsoup4 python tools/build.py --check  # 只报告，不写文件
"""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup, Tag

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://presighttrading.com"

# 顺序就是切换器里的显示顺序。dir 为空表示站点根目录（中文）。
LANGS = [
    ("zh", "中", "", "zh-Hans"),
    ("en", "EN", "en", "en"),
    ("ja", "日本語", "ja", "ja"),
    ("vi", "Việt", "vi", "vi"),
    ("th", "ไทย", "th", "th"),
]
GENERATED = ("ja", "vi", "th")

# 判定叶子用「行内元素」白名单而不是「块级元素」黑名单：一句话里出现
# <a> 是常事（「完整细则 →」就在段落中间），把 a 当块级会让整段不再是
# 叶子，于是段落里那些直接的文本节点谁都不处理——既翻不到，也不会出现
# 在未翻列表里，是最坏的一种漏。
INLINE = {"a", "b", "i", "em", "strong", "span", "small", "sup", "sub",
          "br", "s", "u", "mark", "abbr", "cite", "q", "time", "var",
          "kbd", "samp", "wbr", "img", "svg", "path", "rect", "code"}
SKIP_TAGS = {"script", "style", "head", "html", "body",
             "svg", "rect", "path", "img", "code"}
TRANSLATABLE_ATTRS = ("aria-label", "alt", "placeholder")

# 品牌、栏标、技术标识：任何语种都保持原样。列在这里是为了让「未翻列表」
# 只剩下真正需要处理的东西——报告里混着二十条永远不该翻的，人就不看了。
NEVER = {
    "PRESIGHT ALPHA-1",
    '<span class="lt">PRESIGHT</span>\n<span class="lc">TRADING INSTITUTE</span>',
    '<span class="lt">PRESIGHT</span><span class="lc" style="color:#5B6883">'
    "TRADING INSTITUTE</span>",
    '<span class="lt">PRESIGHT</span><span class="lc">Trading Institute</span>',
    '<span style="top:120px">PROTECTION</span>',
    '<span style="top:120px">STRATEGY</span>',
    '<span style="top:120px">COMMUNITY</span>',
    '<span style="top:120px">PARTNER</span>',
    '<span class="dot"></span> LIVE · <span id="upd">—</span>',
}


# ----------------------------------------------------------------- 片段

def is_leaf(tag: Tag) -> bool:
    return not any(isinstance(c, Tag) and c.name not in INLINE
                   for c in tag.descendants)


def leaf_tags(soup: BeautifulSoup):
    """按文档顺序产出叶子块级元素，且不产出已被覆盖的子孙。

    不去重子孙的话，一句话里的 <b> 会被当成独立片段再处理一遍：翻译表里
    出现互相包含的两条，替换时后者会把前者的结果覆盖掉。跳过的元素也要
    连子孙一起去重——否则「不该翻的」被跳过后，它里面的 span 又会单独冒
    出来，未翻列表里全是 PRESIGHT、PROTECTION 这种噪音。
    """
    seen: set[int] = set()

    def swallow(tag: Tag) -> None:
        seen.add(id(tag))
        for d in tag.descendants:
            if isinstance(d, Tag):
                seen.add(id(d))

    for tag in soup.find_all(True):
        if id(tag) in seen:
            continue
        if tag.name in SKIP_TAGS or tag.find_parent("svg") is not None:
            continue
        if tag.name in ("title", "img"):
            swallow(tag)
            continue
        if "langsw" in (tag.get("class") or []):
            swallow(tag)
            continue
        if tag.decode_contents().strip() in NEVER:
            swallow(tag)
            continue
        # 叶子判断必须排在含 svg 的判断之前。反过来的话，<main> 里有 svg
        # 就会把整页吞掉——上一版正是这样，命中数从 140 掉到 13。
        if not is_leaf(tag):
            continue
        swallow(tag)
        if tag.find("svg") is not None:      # logo
            continue
        if tag.get_text(strip=True):         # 只有图标的容器没有可翻的文字
            yield tag


def set_inner(tag: Tag, html: str) -> None:
    tag.clear()
    for node in list(BeautifulSoup(html, "html.parser").contents):
        tag.append(node)


# ----------------------------------------------------------------- 头部

def rel(from_dir: str, to_dir: str, page: str, cur: bool) -> str:
    """站内相对链接。首页用锚点而不是文件名，跟原来的写法保持一致。"""
    if cur:
        return "#top" if page == "index.html" else "#"
    up = "../" if from_dir else ""
    tail = "" if page == "index.html" else page
    return f"{up}{to_dir}/{tail}" if to_dir else f"{up}{tail}" or "../"


def langsw(from_dir: str, page: str) -> str:
    parts = []
    for code, label, d, _ in LANGS:
        cur = (d == from_dir)
        href = rel(from_dir, d, page, cur)
        klass = ' class="cur"' if cur else ""
        parts.append(f'<a href="{href}"{klass}>{label}</a>')
    return "<span>/</span>".join(parts)


def hreflang(page: str) -> str:
    lines = []
    for _, _, d, tag in LANGS:
        url = f"{SITE}/{d + '/' if d else ''}{'' if page == 'index.html' else page}"
        lines.append(f'<link rel="alternate" hreflang="{tag}" href="{url}">')
    lines.append(f'<link rel="alternate" hreflang="x-default" href="{SITE}/">')
    return "\n".join(lines)


def patch_head(html: str, code: str, d: str, page: str, meta: dict) -> str:
    html = re.sub(r'<html lang="[^"]*"', f'<html lang="{code}"', html, count=1)

    block = hreflang(page)
    if 'hreflang' in html:
        html = re.sub(
            r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\s*'
            r'(?:<link rel="alternate" hreflang="[^"]*" href="[^"]*">\s*)*',
            block + "\n", html, count=1)
    else:                                   # protection.html 原来没有
        html = html.replace("<title>", block + "\n<title>", 1)

    url = f"{SITE}/{d + '/' if d else ''}{'' if page == 'index.html' else page}"
    html = re.sub(r'(<meta property="og:url" content=")[^"]*(")',
                  rf'\1{url}\2', html)

    key = "title_index" if page == "index.html" else "title_prot"
    if meta.get(key):
        html = re.sub(r"<title>.*?</title>", f"<title>{meta[key]}</title>",
                      html, count=1, flags=re.S)
    dkey = "desc_index" if page == "index.html" else "desc_prot"
    if meta.get(dkey):
        html = re.sub(r'(<meta name="description" content=")[^"]*(")',
                      lambda m: m.group(1) + meta[dkey] + m.group(2), html, count=1)
    for prop, k in (("og:title", "og_title"), ("og:description", "og_desc")):
        if meta.get(k):
            html = re.sub(rf'(<meta property="{prop}" content=")[^"]*(")',
                          lambda m: m.group(1) + meta[k] + m.group(2), html, count=1)
    return html


def patch_langsw(path: Path, d: str, page: str) -> None:
    """把某个已有页面的语言切换器换成完整的五种语言。"""
    html = path.read_text(encoding="utf-8")
    new = f'<div class="langsw">{langsw(d, page)}</div>'
    out = re.sub(r'<div class="langsw">.*?</div>', new, html, count=1, flags=re.S)
    if out != html:
        path.write_text(out, encoding="utf-8")
        print(f"  语言切换器已更新：{path.relative_to(ROOT)}")


# ----------------------------------------------------------------- 生成

def load_lang(code: str):
    spec = importlib.util.spec_from_file_location(
        f"lang_{code}", ROOT / "tools" / f"lang_{code}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def ordered_keys(src: Path) -> list[str]:
    """英文页里可翻译片段的规范顺序，供按序号写译文的语言文件使用。"""
    soup = BeautifulSoup(src.read_text(encoding="utf-8"), "html.parser")
    keys = []
    for tag in leaf_tags(soup):
        inner = tag.decode_contents().strip()
        if inner and any(c.isalpha() for c in inner):
            keys.append(inner)
    return keys


def expand_by_no(by_no: dict[int, str], src: Path) -> dict[str, str]:
    """把 {序号: 译文} 展开成 {英文原文: 译文}。

    新语种逐条抄英文原文当键太容易抄错（空格、&nbsp;、弯引号），所以允许
    按 tools/keys.py 打印的序号来写。序号越界直接报错，不静默丢弃——
    悄悄少一条译文，页面上就会突兀地冒出一句英文。
    """
    keys = ordered_keys(src)
    out = {}
    for no, text in by_no.items():
        if not 1 <= no <= len(keys):
            raise SystemExit(f"❌ 序号 {no} 超出范围（共 {len(keys)} 条）")
        out[keys[no - 1]] = text
    return out


def build_page(src: Path, out: Path, table: dict, meta: dict,
               page: str, check: bool) -> tuple[int, int, list[str]]:
    soup = BeautifulSoup(src.read_text(encoding="utf-8"), "html.parser")

    hit = miss = 0
    missing: list[str] = []
    for tag in leaf_tags(soup):
        inner = tag.decode_contents().strip()
        if not inner or not any(c.isalpha() for c in inner):
            continue
        if inner in table:
            set_inner(tag, table[inner])
            hit += 1
        else:
            miss += 1
            missing.append(inner)

    for tag in soup.find_all(True):
        for attr in TRANSLATABLE_ATTRS:
            val = tag.get(attr)
            if val and f"@{val}" in table:
                tag[attr] = table[f"@{val}"]

    # IB 分享链接指向本语种自己的页面，否则日文页发出去的链接落在英文页
    share = soup.find(id="partnerShare")
    if share is not None and meta.get("share"):
        url = meta["share"] if page == "index.html" else meta["share"]
        share.string = url

    html = str(soup)
    html = patch_head(html, meta["lang"], meta["dir"], page, meta)
    html = re.sub(r'<div class="langsw">.*?</div>',
                  f'<div class="langsw">{langsw(meta["dir"], page)}</div>',
                  html, count=1, flags=re.S)

    if not check:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
    return hit, miss, missing


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    check = "--check" in sys.argv
    full = "--full" in sys.argv        # 未翻片段打全文，方便直接粘进词表
    targets = args or list(GENERATED)

    # 已有的四个页面：切换器补齐到五种语言
    if not check:
        for d, page in (("", "index.html"), ("", "protection.html"),
                        ("en", "index.html"), ("en", "protection.html")):
            patch_langsw(ROOT / (f"{d}/{page}" if d else page), d, page)

    problems = 0
    for code in targets:
        mod = load_lang(code)
        meta = mod.META
        print(f"\n=== {code}（{meta['label']}）===")
        tables = {
            "index.html": dict(getattr(mod, "INDEX", {})),
            "protection.html": dict(getattr(mod, "PROTECTION", {})),
        }
        for page, attr in (("index.html", "INDEX_BY_NO"),
                           ("protection.html", "PROTECTION_BY_NO")):
            by_no = getattr(mod, attr, None)
            if by_no:
                tables[page].update(expand_by_no(by_no, ROOT / "en" / page))
        for page, table in tables.items():
            hit, miss, missing = build_page(
                ROOT / "en" / page, ROOT / meta["dir"] / page,
                table, meta, page, check)
            flag = "✅" if miss == 0 else "⚠️ "
            print(f"{flag} {meta['dir']}/{page}：已翻 {hit}，未翻 {miss}")
            problems += miss
            for m in missing:
                # repr で出す：空白や改行の一文字違いでキーが当たらない、
                # というのがこの手の作業で一番よくある詰まり方
                print(f"\n    {m!r}:\n        ," if full
                      else f"     未翻：{m[:110]}")
        unused = [k for k in {**tables["index.html"],
                              **tables["protection.html"]}
                  if not k.startswith("@")]
        # 只提示，不当错误：同一句话在两个页面都出现是正常的
        print(f"   词条 {len(unused)} 条")

    if problems:
        print(f"\n共有 {problems} 个片段没有翻译，这些位置会留下英文原文。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
