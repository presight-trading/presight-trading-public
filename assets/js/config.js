/* ============================================================
   配置区 —— 上线前只需要改这里
   ============================================================ */
const CONFIG = {
  // 你的成交记录 API。留空则使用下方的演示数据。
  tradesEndpoint : '',

  // 交易平台注册链接（带你的推广参数）
  brokerSignupUrl: 'https://secure.decodefx.com/auth/register/?ref=l-246813157-FS8661P7',

  // ---- 社区入口 ----
  // 信号频道：Presight 的对外总入口，公开可搜索，无需申请。
  //
  // 这个 handle 原来挂在另一个频道上，后来整体搬到了原 VIP 频道——
  // 复用旧 handle 是有意的：它已经印在长图里、编进二维码里、写进各群
  // 置顶。换新名字意味着这些全部要跟着改，而已经转发出去的长图改不了。
  channelUrl     : 'https://t.me/presight_signals',

  // 交易学院社区群：公开可搜索，直接进不需要审批
  communityUrl   : 'https://t.me/presight_institute',

  // 推广合作伙伴（IB）专用注册链接。和上面那条不是同一条：走这条注册
  // 的人在后台才看得到「申请成为 IB」，走用户那条就没有。两条别搞混。
  ibSignupUrl    : 'https://secure.decodefx.com/auth/register/?ref=l-91041627-FS8661P7',

  // 报备用的管理员 bot。开户跟单之后，用户把 MT5 账户 ID 私信给它，
  // 它当场回执并把记录落到内部台账群。包赔的保护期正是从这一刻起算的，
  // 所以这个链接断了不只是少个入口——是用户的保护期根本开始不了。
  adminBotUrl    : 'https://t.me/PresightAdminBot',

  // 联系方式
  contactEmail   : 'hello@presighttrading.com',

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
