"""og:image 上的文案。五个语种各一份。

刻意只放三样：这是什么、最关键的承诺、域名。链接卡片在 Telegram 里实际
宽度约 360px，微信更小——按缩到三分之一还读得清来写，塞细则等于什么都
没写。数字（1:1、1 个月）与官网一致，改条款时这里也要跟着改。
"""
from __future__ import annotations

HTML_LANG = {"zh": "zh-Hans", "en": "en", "ja": "ja", "vi": "vi", "th": "th"}

L: dict[str, dict[str, str]] = {}

L["zh"] = dict(
    brand_sub="先见交易学院 · Presight Trading Institute",
    badge="跟单亏损包赔",
    h1a="量化跟单策略，",
    h1b="亏了我们现金赔。",
    lead="策略以<b>自有资金实盘运行</b>，历史成交逐笔公开，盈亏不做筛选。"
         "按规则跟单满一个月，整段期间若为净亏损，按实际金额现金返还。",
    c1k="STRATEGY", c1v="PRESIGHT ALPHA-1",
    c2k="COPY", c2v="1:1 不放大仓位",
    c3k="COVERAGE", c3v="净亏损 · 现金返还",
    foot="外汇 · 黄金 · 原油",
)

L["en"] = dict(
    brand_sub="Presight Trading Institute",
    badge="LOSS COVERAGE",
    h1a="Quant copy-trading,",
    h1b="losses refunded in cash.",
    lead="The strategy runs on <b>our own capital</b>, with every fill published and no losing "
         "trade filtered out. Copy it by the rules for a month and we refund a net loss in cash.",
    c1k="STRATEGY", c1v="PRESIGHT ALPHA-1",
    c2k="COPY", c2v="1:1, no scaling up",
    c3k="COVERAGE", c3v="Net loss · paid in cash",
    foot="FX · GOLD · OIL",
)

L["ja"] = dict(
    brand_sub="Presight Trading Institute",
    badge="損失補償",
    h1a="クオンツのコピートレード、",
    h1b="負けた分は現金で返します。",
    lead="戦略は<b>自己資金で実運用</b>。約定はすべて公開し、負けトレードも伏せません。"
         "規約どおり 1 か月コピーして期間全体が負けなら、その損失を現金で返金します。",
    c1k="STRATEGY", c1v="PRESIGHT ALPHA-1",
    c2k="COPY", c2v="1:1・拡大なし",
    c3k="COVERAGE", c3v="純損失 · 現金で返金",
    foot="FX · ゴールド · 原油",
)

L["vi"] = dict(
    brand_sub="Presight Trading Institute",
    badge="BẢO HIỂM THUA LỖ",
    h1a="Sao chép định lượng,",
    h1b="lỗ được hoàn tiền mặt.",
    lead="Chiến lược chạy bằng <b>vốn của chính chúng tôi</b>, mọi lệnh khớp đều công khai, "
         "không lọc bỏ lệnh lỗ. Sao chép đúng quy định đủ một tháng, cả kỳ lỗ ròng thì hoàn tiền mặt.",
    c1k="STRATEGY", c1v="PRESIGHT ALPHA-1",
    c2k="COPY", c2v="1:1, không phóng đại",
    c3k="COVERAGE", c3v="Lỗ ròng · hoàn tiền mặt",
    foot="FOREX · VÀNG · DẦU",
)

L["th"] = dict(
    brand_sub="Presight Trading Institute",
    badge="ชดเชยการขาดทุน",
    h1a="ก๊อปปี้เทรดเชิงปริมาณ",
    h1b="ขาดทุนคืนเป็นเงินสด",
    lead="กลยุทธ์รันด้วย<b>เงินทุนของเราเอง</b> เปิดเผยทุกออเดอร์ ไม่คัดทิ้งไม้ที่ขาดทุน "
         "ก๊อปปี้ตามกติกาครบหนึ่งเดือน ถ้าตลอดรอบขาดทุนสุทธิ เราคืนเป็นเงินสด",
    c1k="STRATEGY", c1v="PRESIGHT ALPHA-1",
    c2k="COPY", c2v="1:1 ไม่ขยายสถานะ",
    c3k="COVERAGE", c3v="ขาดทุนสุทธิ · คืนเงินสด",
    foot="ฟอเร็กซ์ · ทองคำ · น้ำมัน",
)
