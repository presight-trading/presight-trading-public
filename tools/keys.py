"""按文档顺序列出英文页里所有需要翻译的片段，供新增语种对照。

用法：uv run --with beautifulsoup4 python tools/keys.py index
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import ROOT, leaf_tags                      # noqa: E402
from bs4 import BeautifulSoup                          # noqa: E402

page = "index.html" if (len(sys.argv) < 2 or sys.argv[1] == "index") \
    else "protection.html"
soup = BeautifulSoup((ROOT / "en" / page).read_text(encoding="utf-8"),
                     "html.parser")
n = 0
for tag in leaf_tags(soup):
    inner = tag.decode_contents().strip()
    if not inner or not any(c.isalpha() for c in inner):
        continue
    n += 1
    one = " ".join(inner.split())
    print(f"{n:3d}. {one}")
print(f"\n共 {n} 条")
