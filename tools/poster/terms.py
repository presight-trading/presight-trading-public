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
    ("赔付上限", "投入合计（基准资金＋期间入金）全额",
     [("protection.html", r"等于投入合计</b>，即基准资金加上期间的累计入金")]),
    # 出金规则改过一次（原为「保护期内不出金」）。海报上写的是「首月不出金、
    # 满月后利润随时可取」，这两条必须都能在官网找到——只对上一半的话，
    # 海报会变成一份自相矛盾的摘要，而它是脱离官网独立流传的。
    ("首月出金限制", "跟单首月内不出金",
     [("protection.html", r"跟单首月（自报备起 30 个自然日）内不出金"),
      ("index.html", r"首月内不手动干预、不出金")]),
    ("满月后可出金", "满 1 个月后利润随时可取",
     [("protection.html", r"满一个月之后可以随时出金"),
      ("index.html", r"满一个月后利润随时可以取走")]),
    ("赔付口径", "整段跟单期间的净盈亏",
     [("protection.html", r"净盈亏 = 取回合计 − 投入合计"),
      ("index.html", r"整段跟单期间（出入金全部计入）")]),
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
