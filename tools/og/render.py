"""把模板 + 某语种的文案渲染成一份可截图的 HTML。

渲染完立刻自检：漏一个占位符，图上就留一个 {{token}}，而这张图会被
Telegram、微信抓走并长期缓存，改了也不一定刷得掉。

用法：python3 render.py <lang> <输出.html>
"""
from __future__ import annotations

import io
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from strings import HTML_LANG, L                       # noqa: E402


def render(lang: str) -> str:
    tpl = (HERE / "og.tpl.html").read_text(encoding="utf-8")
    words = dict(L[lang])
    words["lang"] = HTML_LANG[lang]

    out = re.sub(r"\{\{(\w+)\}\}", lambda m: words.get(m.group(1), m.group(0)), tpl)

    leftover = sorted(set(re.findall(r"\{\{(\w+)\}\}", out)))
    if leftover:
        sys.exit(f"❌ {lang}：这些占位符没有对应文案 → {leftover}")

    # 反向自检：除中日外，正文里不该再出现中日韩汉字
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
