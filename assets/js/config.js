/* ============================================================
   配置区 —— 上线前只需要改这里
   ============================================================ */
const CONFIG = {
  // 你的成交记录 API。留空则使用下方的演示数据。
  tradesEndpoint : '',

  // 交易平台注册链接（带你的推广参数）
  brokerSignupUrl: 'https://example-broker.com/register?ref=PRESIGHT',

  // 社区入口
  communityUrl   : 'https://t.me/your_channel',

  // 自动刷新间隔（毫秒）
  refreshMs      : 60000,

  // 表格显示条数
  rowLimit       : 12,
};

/* 期望的 API 返回格式（数组，按平仓时间倒序）：
[
  {
    "closedAt" : "2026-07-28T09:41:00Z",   // ISO 8601
    "symbol"   : "XAUUSD",
    "side"     : "buy",                     // "buy" | "sell"
    "lots"     : 0.40,
    "openPrice": 2412.35,
    "closePrice":2419.80,
    "pips"     : 74.5,
    "pnl"      : 298.00                     // USD，可为负
  }
]
若你的字段名不同，改下面的 normalize() 一个函数即可。 */

function normalize(raw){
  return {
    closedAt  : raw.closedAt  ?? raw.close_time ?? raw.time,
    symbol    : raw.symbol    ?? raw.instrument,
    side      : (raw.side     ?? raw.type ?? '').toLowerCase(),
    lots      : Number(raw.lots ?? raw.volume ?? 0),
    openPrice : Number(raw.openPrice  ?? raw.open_price ?? 0),
    closePrice: Number(raw.closePrice ?? raw.close_price ?? 0),
    pips      : Number(raw.pips ?? 0),
    pnl       : Number(raw.pnl ?? raw.profit ?? 0),
  };
}
