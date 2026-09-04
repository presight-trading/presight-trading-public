"""海报上的关键数字，以及「它们必须和官网一致」的校验。

用户的要求是「PDF 要跟着网站的内容更新」。真正危险的不是措辞不同步——
措辞差一点没人受伤——而是**数字**：保护期几个月、门槛多少钱、返现几个
百分点。海报会被下载、转到微信、脱离官网独立流传，改了官网忘了海报，
外面就长期挂着一份旧条款，而且撤不回来。

所以这里把关键数字集中定义，生成海报时逐个回官网页面里核对；对不上就
直接报错、不出图。宁可出不来，也不要出一张和官网不一致的。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# 每一项：(名字, 海报上的写法, 必须能在这些页面里找到的证据)
# 证据用正则，因为官网上同一个数字的排版不尽相同（5,000 / 5000）。
FACTS = [
    ("保护期", "1 个月（30 个自然日）",
     [("protection.html", r"1 个月.{0,4}30 个自然日"),
      ("index.html", r"连续跟单满 1 个月|满 1 个月")]),
    ("赔付上限", "基准资金全额",
     [("protection.html", r"基准资金全额|<b>基准资金全额</b>")]),
    ("到账时限", "10 个工作日",
     [("protection.html", r"10 个工作日"), ("index.html", r"10 个工作日")]),
    ("申请时限", "5 个自然日",
     [("protection.html", r"5 个自然日")]),
    ("跟单参数", "Autoscale / Value by asset / Ratio = 1",
     [("protection.html", r"Autoscale.{0,80}Value by asset.{0,60}Ratio = 1"),
      ("index.html", r"Autoscale")]),
    ("信号源", "PRESIGHT ALPHA-1",
     [("protection.html", r"PRESIGHT ALPHA-1"), ("index.html", r"PRESIGHT ALPHA-1")]),
    ("报备对象", "@PresightAdminBot",
     [("protection.html", r"@PresightAdminBot"), ("index.html", r"@PresightAdminBot")]),
    ("IB 分成", "50%",
     [("index.html", r"50%")]),
    ("IB 门槛", "3 名用户 · 入金合计 ≥ 5,000 美元",
     [("index.html", r"3</span> 名用户.{0,80}5,000|入金合计</b>不低于 5,000")]),
    ("首月保收益", "1%",
     [("index.html", r"首月保收益")]),
]


def check() -> list[str]:
    """返回不一致的项。空列表表示海报与官网对得上。"""
    cache: dict[str, str] = {}
    bad: list[str] = []
    for name, shown, evidence in FACTS:
        for page, pattern in evidence:
            if page not in cache:
                cache[page] = (ROOT / page).read_text(encoding="utf-8")
            if not re.search(pattern, cache[page], re.S):
                bad.append(f"{name}（海报写「{shown}」）在 {page} 里找不到对应内容"
                           f"　正则：{pattern}")
    return bad


if __name__ == "__main__":
    problems = check()
    if problems:
        print("❌ 海报与官网不一致：")
        for p in problems:
            print("   " + p)
        sys.exit(1)
    print(f"✅ 海报的 {len(FACTS)} 项关键内容都能在官网页面里找到对应")
