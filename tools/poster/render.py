"""把模板 + 某语种的文案渲染成一份可截图的 HTML。

单独一个脚本而不是塞进 build.sh：占位符有四十来个，漏一个就会在图上留下
一个 `{{token}}`，而那张图会被下载、转进微信、脱离官网独立流传——发现时
已经撤不回来。所以这里渲染完立刻自检，有残留就直接失败。

用法：python3 render.py <lang> <输出.html>
"""
from __future__ import annotations

import io
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from strings import HTML_LANG, L, SITES          # noqa: E402


def render(lang: str) -> str:
    tpl = (HERE / "poster.tpl.html").read_text(encoding="utf-8")
    words = dict(L[lang])
    words["lang"] = HTML_LANG[lang]
    # 二维码文件按语种分开：每种语言的图指向自己那一版落地页
    tpl = tpl.replace('src="qr.svg"', f'src="qr-{lang}.svg"')

    out = re.sub(r"\{\{(\w+)\}\}", lambda m: words.get(m.group(1), m.group(0)), tpl)

    leftover = sorted(set(re.findall(r"\{\{(\w+)\}\}", out)))
    if leftover:
        sys.exit(f"❌ {lang}：这些占位符没有对应文案 → {leftover}")

    # 反向自检：除中文版外，正文里不该再出现中日韩汉字（CSS 注释除外）
    body = out.split("</style>", 1)[-1]
    if lang not in ("zh", "ja"):
        han = re.findall(r"[一-鿿]", body)
        if han:
            sys.exit(f"❌ {lang}：正文里残留中文字符 {''.join(sorted(set(han)))[:40]}")
    return out


if __name__ == "__main__":
    lang, dest = sys.argv[1], sys.argv[2]
    io.open(dest, "w", encoding="utf-8").write(render(lang))
    print(f"  ✓ {lang} → {Path(dest).name}")
