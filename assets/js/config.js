/* ============================================================
   配置区 —— 上线前只需要改这里
   ============================================================ */
const CONFIG = {
  // 成交记录 JSON 的地址。留空则使用下方的演示数据。
  //
  // 数据放在独立的公开仓库 presight-trading/strategy-history，后端每
  // 5 分钟自动提交刷新一次 vip-history.json；这里直接指向它在 GitHub
  // 上的 raw 地址（跨域，raw.githubusercontent.com 自带
  // Access-Control-Allow-Origin: *，浏览器 fetch 不需要额外配置）。
  // raw.githubusercontent.com 前端有 CDN，缓存约 5 分钟，所以页面看到
  // 的数据比后端生成时间晚一点是正常的，不代表接口坏了。
  // 走的是这个独立仓库、不是本仓库根目录，所以不存在语言子目录
  // （en/ja/th/vi）相对路径解析错位的问题，不需要写成 /data/... 这种
  // 站内绝对路径。
  tradesEndpoint : 'https://data.presighttrading.com/vip-history.json',
  // 为什么走自有子域 data.presighttrading.com:raw/github.io 两个域在部分地区(尤其中国大陆)
  // 经常解析失败或被拦,而 github.io 与本站(GitHub Pages)解析到同一组 CDN 节点——
  // 能打开本站就能取到数据。数据仓库已开启 Pages,每次推送后自动重新发布(约 1 分钟)。

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
  ibSignupUrl    : 'https://secure.decodefx.com/auth/register/?ref=l-292412201-FS8661P7',

  // 报备用的管理员 bot。开户跟单之后，用户把 MT5 账户 ID 私信给它，
  // 它当场回执并把记录落到内部台账群。包赔的保护期正是从这一刻起算的，
  // 所以这个链接断了不只是少个入口——是用户的保护期根本开始不了。
  adminBotUrl    : 'https://t.me/PresightAdminBot',

  // 联系方式
  contactEmail   : 'hello@presighttrading.com',

  // 自动刷新间隔（毫秒）
  refreshMs      : 60000,

  // 表格显示条数（现为 30 天窗口，行数上限相应从 200 调到 600，见 app.js renderTrades）
  rowLimit       : 600,
};

/* 期望的 API 返回格式（对象；trades 数组按平仓时间倒序）：
{
  "generatedAt": "2026-09-03T00:10:00Z",   // ISO 8601，数据生成时间，页面「更新于」用这个，不用客户端本地时间
  "windowDays" : 30,                        // 可选：trades 覆盖的天数（现为近 30 天；表格同样展示近 30 天，见 app.js）
  "summary": {                              // 可选：后端预算好的汇总指标（近 7 天口径），存在时前端直接用，避免前后端算法口径不一致
    "totalPips"          : 812.4,           // 净点数，带正负号（兼容旧名 netPips）——页面已不展示，只留在接口契约里
    "winRatePct"         : 61.3,            // 胜率，百分比数字（0-100，兼容旧名 winRate）——页面胜率格已改用 summary30d.winRatePct，这个字段目前不用
    "maxDrawdownPips"    : 96.0,            // 最大回撤，累计 pips 峰值回撤，正数——页面已不展示（回撤格改按 pnlUsd 前端算，USD 口径）
    "pfPips"             : 1.82,            // 盈亏比 = 盈利点数之和 / 亏损点数绝对值之和——页面已不展示（盈亏比格改按 pnlUsd 前端算，USD 口径）
    "pnlUsd"             : 214.30,          // 可选：按建议手数折算的美元盈亏（近 7 天），不含隔夜利息，缺省前端按 trades 现算
    "referenceBalanceUsd": 10000            // 可选：suggestedLots/pnlUsd 假设的参考账户余额，缺省 10000
  },
  "summary30d": {                           // 可选：同 summary 结构，口径为近 30 天；pnlUsd/winRatePct/trades/referenceBalanceUsd 会被用到，
                                             // 缺省时前端分别按 30 天 trades 现算（winRatePct 按 pnlUsd>0 笔数占比，trades 按过滤后的笔数）
    "pnlUsd"    : 640.10,
    "winRatePct": 58.7,
    "trades"    : 46
  },
  "trades": [
    {
      "closedAt"     : "2026-07-28T09:41:00Z",  // ISO 8601
      "openedAt"     : "2026-07-28T08:59:00Z",  // ISO 8601，可选；缺失时若同时有 closedAt 会用来换算 durationMin
      "symbol"       : "XAUUSD",
      "side"         : "buy",                    // "buy" | "sell"
      "openPrice"    : 2412.35,
      "closePrice"   : 2419.80,
      "pips"         : 74.5,                     // 必填
      "suggestedLots": 0.12,                     // 可选：按参考账户折算的建议手数，缺失显示 "—"
      "pnlUsd"       : 148.2,                     // 可选：按 suggestedLots、不含隔夜利息折算的美元盈亏，缺失显示 "—"
      "durationMin"  : 42                        // 持仓分钟数，可选（缺失且有 openedAt/closedAt 时自动换算）
    }
  ]
}
suggestedLots / pnlUsd 都是可选字段：后端没给（或还没上线）时 normalize() 落 null，
页面对应列显示 "—"，不报错。若你的字段名不同，改下面的 normalize() 一个函数即可。 */

function normalize(raw){
  const closedAt = raw.closedAt ?? raw.close_time ?? raw.time;
  const openedAt = raw.openedAt ?? raw.open_time  ?? null;
  let durationMin = raw.durationMin ?? raw.duration_min;
  if(durationMin == null && openedAt && closedAt){
    durationMin = Math.round((new Date(closedAt) - new Date(openedAt)) / 60000);
  }
  return {
    closedAt,
    openedAt,
    durationMin: Number(durationMin ?? 0),
    symbol    : raw.symbol    ?? raw.instrument,
    side      : (raw.side     ?? raw.type ?? '').toLowerCase(),
    openPrice : Number(raw.openPrice  ?? raw.open_price ?? 0),
    closePrice: Number(raw.closePrice ?? raw.close_price ?? 0),
    pips      : Number(raw.pips ?? 0),
    // 参考账户（$10,000，见 summary.referenceBalanceUsd）建议手数与对应美元盈亏，
    // 后端字段还没上线或这一笔算不出来时都是 null，前端一律显示 "—"，不报错。
    suggestedLots: raw.suggestedLots ?? null,
    pnlUsd       : raw.pnlUsd ?? null,
  };
}
