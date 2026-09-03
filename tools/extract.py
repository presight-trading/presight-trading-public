"""从英文页生成其它语种的页面。

不手抄整份 HTML，而是把「可翻译片段」抽出来、翻完再塞回去：结构由
解析器保证一致，漏翻的片段会原样留下英文——看得见，但不会把页面弄坏。
这比手抄 380 行 HTML 安全得多。

片段的粒度是「叶子块级元素的 innerHTML」，句子里夹着的 <b> 一起带上。
按文本节点切会把一句话拆成几段，而日语、越南语、泰语的语序跟英语不
一样，拆开就没法翻。
"""
from __future__ import annotations

import sys
from bs4 import BeautifulSoup, NavigableString, Tag

# 这些标签一旦出现在后代里，当前元素就不是叶子，继续往下找
BLOCKISH = {"p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "ul", "ol",
            "dl", "dt", "dd", "div", "section", "details", "summary",
            "table", "tr", "td", "th", "nav", "header", "footer", "main",
            "figure", "form", "button", "a"}
# 只有内容的这些元素才算需要翻译（纯代码、纯数字的不算）
SKIP_EXACT = {"", "&rarr;", "→"}
TRANSLATABLE_ATTRS = ("aria-label", "alt", "placeholder", "title")


def is_leaf(tag: Tag) -> bool:
    return not any(isinstance(c, Tag) and c.name in BLOCKISH
                   for c in tag.descendants)


def segments(soup: BeautifulSoup):
    """按文档顺序产出 (元素, innerHTML)。"""
    seen = set()
    for tag in soup.find_all(True):
        if tag.name in ("script", "style", "head", "html", "body",
                        "svg", "rect", "path", "img", "code"):
            continue
        if tag.find_parent("svg") is not None:
            continue
        if not is_leaf(tag):
            continue
        if id(tag) in seen:
            continue
        html = tag.decode_contents().strip()
        if not html or html in SKIP_EXACT:
            continue
        if not any(ch.isalpha() for ch in html):
            continue
        seen.add(id(tag))
        # 子孙也标记掉。不然一句话里的 <b> 会被当成独立片段再吐一遍，
        # 翻译表里出现互相包含的两条，替换时后者会把前者的结果覆盖掉。
        for d in tag.descendants:
            if isinstance(d, Tag):
                seen.add(id(d))
        yield tag, html


def dump(path: str) -> None:
    soup = BeautifulSoup(open(path, encoding="utf-8").read(), "html.parser")
    t = soup.find("title")
    if t:
        print(f"\n[title]\n{t.decode_contents().strip()}")
    for m in soup.find_all("meta"):
        if m.get("name") in ("description", "og:description") or \
           m.get("property") in ("og:title", "og:description"):
            print(f"\n[meta {m.get('name') or m.get('property')}]\n{m.get('content','')}")
    for tag, html in segments(soup):
        print(f"\n[{tag.name}]\n{html}")
    for tag in soup.find_all(True):
        for a in TRANSLATABLE_ATTRS:
            v = tag.get(a)
            if v and any(ch.isalpha() for ch in v):
                print(f"\n[@{a}]\n{v}")


if __name__ == "__main__":
    dump(sys.argv[1])
