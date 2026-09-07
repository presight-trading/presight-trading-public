/* ---------- 界面文案：跟随 <html lang> 自动切换 ----------
   原来只分「英文/其它」，日、越、泰三个语种因此全都落进中文分支——
   页面通篇是泰文，指标条却写着「412 天」。加语种时最容易漏的就是这种
   由 JS 注入、不在 HTML 里的字。 */
const LANG = (document.documentElement.lang || 'zh').toLowerCase().slice(0,2);
const TEXTS = {
  zh:{
    tradesUnit:'笔',
    recentWins:'近期盈利成交', buy:'买', sell:'卖',
    loading:'成交记录加载中…',
    locale:'zh-CN', daysUnit:'<small>天</small>',
    now:'刚刚', min:' 分钟前', hour:' 小时前', day:' 天前',
    updated:'更新于 ', demo:'演示数据', copied:'已复制',
    errT:'成交记录暂时取不到', errB:'数据接口没有响应。稍后会自动重试，也可以刷新页面。',
    emptyT:'还没有已平仓的交易', emptyB:'策略正在运行，第一笔成交平仓后会立刻出现在这里。',
    annNote:'预估年化＝近 30 天收益率按月复利外推 (1+r)^12−1，是一种推算而非业绩承诺：一个月的结果会被放大十二次，短期的运气与回撤同样会被放大。不代表未来收益。',
    refNote:'收益率按实盘成交价格与每万美元仓位权重计算，并非策略账户的真实盈亏；仅已平仓，不含浮动盈亏与隔夜利息；实际结果随账户规模、点差与滑点不同。',
  },
  en:{
    tradesUnit:'trades',
    recentWins:'Recent winning trades', buy:'BUY', sell:'SELL',
    loading:'Loading fill history…',
    locale:'en-GB', daysUnit:'<small>days</small>',
    now:'just now', min:'m ago', hour:'h ago', day:'d ago',
    updated:'updated ', demo:'demo data', copied:'Copied',
    errT:'Fill history unavailable', errB:'The data endpoint did not respond. It will retry automatically, or you can reload the page.',
    emptyT:'No closed trades yet', emptyB:'The strategy is running. The first closed trade will appear here immediately.',
    annNote:"The annualised figure extrapolates the last 30 days by monthly compounding, (1+r)^12−1. It is an estimate, not a promise: one month of results gets multiplied twelve times, and so does one month of luck or drawdown. It does not indicate future returns.",
    refNote:"Returns are computed from live fill prices and a position weight per $10,000; they are not the strategy account's actual P&L. Closed trades only; excludes floating P&L and swap. Actual results vary with account size, spread and slippage.",
  },
  ja:{
    tradesUnit:'件',
    recentWins:'直近の利益確定', buy:'買', sell:'売',
    loading:'約定履歴を読み込み中…',
    locale:'ja-JP', daysUnit:'<small>日</small>',
    now:'たった今', min:' 分前', hour:' 時間前', day:' 日前',
    updated:'更新 ', demo:'デモデータ', copied:'コピーしました',
    errT:'約定履歴を取得できません', errB:'データ側から応答がありません。自動で再試行します。ページの再読み込みでもかまいません。',
    emptyT:'決済済みの取引はまだありません', emptyB:'戦略は稼働中です。最初の決済が出たらすぐここに表示されます。',
    annNote:'推定年率は直近 30 日の収益率を月次で複利換算した (1+r)^12−1 の外挿値です。予測でも約束でもありません——1 か月分の結果が 12 回掛け合わされるため、短期の幸運もドローダウンも同じだけ拡大されます。将来の収益を示すものではありません。',
    refNote:'収益率は実際の約定価格と1万ドルあたりのポジション比率をもとに算出したものであり、戦略口座の実際の損益ではありません。決済済み取引のみを対象とし、含み損益とスワップ(オーバーナイト金利)は含みません。実際の結果は口座規模・スプレッド・スリッページによって異なります。',
  },
  vi:{
    tradesUnit:'lệnh',
    recentWins:'Lệnh có lãi gần đây', buy:'MUA', sell:'BÁN',
    loading:'Đang tải lịch sử khớp lệnh…',
    locale:'vi-VN', daysUnit:'<small>ngày</small>',
    now:'vừa xong', min:' phút trước', hour:' giờ trước', day:' ngày trước',
    updated:'cập nhật ', demo:'dữ liệu mẫu', copied:'Đã sao chép',
    errT:'Chưa lấy được lịch sử khớp lệnh', errB:'Máy chủ dữ liệu không phản hồi. Hệ thống sẽ tự thử lại, hoặc bạn có thể tải lại trang.',
    emptyT:'Chưa có lệnh nào đóng', emptyB:'Chiến lược đang chạy. Lệnh đóng đầu tiên sẽ hiện ở đây ngay lập tức.',
    annNote:'Lợi nhuận năm ước tính là phép ngoại suy lợi nhuận 30 ngày gần nhất theo lãi kép hằng tháng, (1+r)^12−1. Đây là ước tính, không phải cam kết: kết quả của một tháng được nhân lên mười hai lần, và may mắn hay sụt giảm trong tháng đó cũng vậy. Không phản ánh lợi nhuận trong tương lai.',
    refNote:'Lợi nhuận (%) được tính từ giá khớp lệnh thực tế và tỷ trọng vị thế trên mỗi 10.000 đô la; đây không phải lãi/lỗ thực tế của tài khoản chiến lược. Chỉ tính các lệnh đã đóng; không bao gồm lãi/lỗ chưa thực hiện và phí qua đêm. Kết quả thực tế sẽ khác nhau tùy theo quy mô tài khoản, spread và trượt giá.',
  },
  th:{
    tradesUnit:'ออเดอร์',
    recentWins:'ออเดอร์ที่ได้กำไรล่าสุด', buy:'ซื้อ', sell:'ขาย',
    loading:'กำลังโหลดประวัติออเดอร์…',
    locale:'th-TH', daysUnit:'<small>วัน</small>',
    now:'เมื่อครู่', min:' นาทีที่แล้ว', hour:' ชั่วโมงที่แล้ว', day:' วันที่แล้ว',
    updated:'อัปเดตเมื่อ ', demo:'ข้อมูลตัวอย่าง', copied:'คัดลอกแล้ว',
    errT:'ยังดึงประวัติออเดอร์ไม่ได้', errB:'เซิร์ฟเวอร์ข้อมูลไม่ตอบสนอง ระบบจะลองใหม่อัตโนมัติ หรือคุณจะรีเฟรชหน้าก็ได้',
    emptyT:'ยังไม่มีออเดอร์ที่ปิดแล้ว', emptyB:'กลยุทธ์กำลังทำงาน ออเดอร์แรกที่ปิดจะขึ้นตรงนี้ทันที',
    annNote:'ผลตอบแทนต่อปีโดยประมาณคือการคาดการณ์จากผลตอบแทน 30 วันล่าสุด ทบต้นรายเดือน (1+r)^12−1 เป็นเพียงการประมาณ ไม่ใช่คำสัญญา: ผลของหนึ่งเดือนถูกคูณสิบสองครั้ง โชคดีหรือการขาดทุนในเดือนนั้นก็ถูกขยายเท่ากัน ไม่ได้บ่งชี้ผลตอบแทนในอนาคต',
    refNote:'อัตราผลตอบแทนคำนวณจากราคาที่ execute จริงและน้ำหนักตำแหน่งต่อทุก 10,000 ดอลลาร์ ไม่ใช่กำไร/ขาดทุนจริงของบัญชีกลยุทธ์ นับเฉพาะออเดอร์ที่ปิดแล้ว ไม่รวมกำไร/ขาดทุนที่ยังไม่เกิดขึ้นจริงและดอกเบี้ยข้ามคืน ผลลัพธ์จริงจะแตกต่างกันไปตามขนาดบัญชี สเปรด และสลิปเพจ',
  },
};
const T = TEXTS[LANG] || TEXTS.zh;

/* ---------- 演示数据（接上 API 后自动弃用） ---------- */
/* 这里不造 suggestedLots/pnlUsd，字段形状对齐 normalize() 的输出——
   两个新字段在 DEMO 里天然缺失，表格/指标卡会按向后兼容逻辑显示 "—"，
   这正好顺带验证了缺字段时的兜底路径。
   加了 durationMin 只是保持数据形状一致，页面目前不展示它。 */
const DEMO = (()=>{
  const spec = [
    ['XAUUSD','buy',2412.35,2419.80,74.5,42],   ['EURUSD','sell',1.08942,1.08761,18.1,17],
    ['GBPJPY','buy',198.412,198.905,49.3,63],   ['USDJPY','sell',157.204,157.388,-18.4,28],
    ['XAUUSD','sell',2431.10,2422.65,84.5,55],  ['AUDUSD','buy',0.66218,0.66341,12.3,19],
    ['NAS100','buy',20114.5,20238.0,123.5,71],  ['EURUSD','buy',1.08510,1.08402,-10.8,22],
    ['USDCAD','sell',1.36720,1.36531,18.9,33],  ['XAUUSD','buy',2398.20,2409.55,113.5,48],
    ['GBPUSD','sell',1.28904,1.28812,9.2,15],   ['US30','buy',41890.0,41762.0,-128.0,84],
    ['EURJPY','buy',170.240,170.712,47.2,39],   ['XAUUSD','sell',2445.90,2451.30,-54.0,26],
    ['USDCHF','buy',0.88410,0.88532,12.2,31],
  ];
  const now = Date.now();
  return spec.map((s,i)=>{
    const [symbol,side,openPrice,closePrice,pips,durationMin] = s;
    const closedAt = new Date(now - (i*3.4+1)*3600*1000).toISOString();
    const openedAt = new Date(new Date(closedAt).getTime() - durationMin*60000).toISOString();
    return { closedAt, openedAt, durationMin, symbol, side, openPrice, closePrice, pips };
  });
})();

/* ---------- 工具 ---------- */
const $ = s => document.querySelector(s);
const fmt = (n,d=2) => n.toLocaleString('en-US',{minimumFractionDigits:d,maximumFractionDigits:d});
const price = (s,v) => v.toFixed(s.includes('JPY')?3 : (s==='NAS100'||s==='US30')?1 : (s.includes('XAU')?2:5));
/* 建议手数 / 建议仓位盈亏(USD)：都是可选字段，缺失（null/undefined，包括
   后端字段还没上线、或旧缓存数据）一律显示 "—"，不当成 0——0 是一个真实的
   盈亏结果，不该跟"没有数据"混在一起。 */
function fmtLots(v){ return v==null ? '—' : Number(v).toFixed(2); }
/* ---------- 相对口径：仓位(手/万美元) + 收益率(%) ----------
   2026-09：页面不再展示任何美元金额，只展示"每万美元仓位权重"对应的收益率——
   pnlUsd 本身仍是后端字段(每万美元参考仓位的盈亏)，但页面上只用来换算成
   pct，从不直接格式化成 $ 数值。referenceBalanceUsd 缺省按 10,000 兜底。 */
let REF_BALANCE_USD = 10000;
function refBalanceOf(summary, summary30d){
  return (summary30d && summary30d.referenceBalanceUsd != null) ? Number(summary30d.referenceBalanceUsd)
       : (summary && summary.referenceBalanceUsd != null) ? Number(summary.referenceBalanceUsd) : 10000;
}
/* 统一的收益率格式化：所有 pnlUsd 换算出的百分比(指标卡/英雄区/成交表/
   按品种拆分)都走这一个函数，避免同一页面里出现两种小数位规则。null/
   非有限数一律显示 "—"，不当成 0——0 是一个真实的盈亏结果。 */
function pct(v){
  if(v==null || !isFinite(Number(v))) return '—';
  const n = Number(v) / REF_BALANCE_USD * 100;
  // 单笔 0.01 手的收益率常在 0.001% 量级,两位小数会显示成 "+0.00%" 像坏了;
  // 小于 0.1% 时给 3 位、小于 0.01% 时给 4 位,汇总数字(≥0.1%)仍是 2 位。
  const a = Math.abs(n); const d = a >= 0.1 ? 2 : (a >= 0.01 ? 3 : 4);
  return (n>=0?'+':'−') + a.toFixed(d) + '%';
}
/* 按窗口求和 pnlUsd：只累加窗口内 pnlUsd 非空的成交；窗口内一笔贡献都没有
   （字段还没上线，或这批全是旧缓存数据）时返回 null，页面显示 "—"——
   不能返回 0，0 是一个真实的盈亏结果，跟"没有数据"含义完全不同。 */
function sumPnlUsd(trades, sinceMs){
  let sum = 0, has = false;
  for(const t of trades){
    if(t.pnlUsd == null || !t.closedAt) continue;
    if(new Date(t.closedAt).getTime() < sinceMs) continue;
    sum += Number(t.pnlUsd); has = true;
  }
  return has ? sum : null;
}
/* 胜率(30 天)前端兜底：summary30d 没给 winRatePct 时，按 pnlUsd>0 的笔数
   占比自己算——只算 pnlUsd 非空的笔，一笔可用数据都没有就是 null。 */
function winRateFromPnl(trades){
  let wins = 0, total = 0;
  for(const t of trades){
    if(t.pnlUsd == null) continue;
    total++; if(Number(t.pnlUsd) > 0) wins++;
  }
  return total ? (wins/total*100) : null;
}
function timeAgo(iso){
  const m = Math.floor((Date.now()-new Date(iso))/60000);
  if(m<1) return T.now;
  if(m<60) return m+T.min;
  const h = Math.floor(m/60);
  if(h<24) return h+T.hour;
  return Math.floor(h/24)+T.day;
}

/* ---------- 渲染成交表 ---------- */
function renderLoading(){
  // 加载期间不要摆一个 260px 高的空曲线框 + 骨架表(网络差时重试可拖到 20 多秒,
  // 用户看到的就是"一大片空白")。整体先藏起来,只在表格位置留一行提示;数据
  // 到了 renderPayload 再 showHistory()。
  hideHistory();
  const st = $('#tradeState');
  if(st){ st.style.display=''; st.innerHTML = `<div class="state">${T.loading}</div>`; }
}
function renderError(){
  // 取不到数据 → 不展示错误框，直接隐藏整个历史成绩区块(见 hideHistory)
  $('#tradeBody').innerHTML = '';
  $('#tradeState').innerHTML = '';
  hideHistory();
}
function renderEmpty(){
  $('#tradeBody').innerHTML = '';
  $('#tradeState').innerHTML =
    `<div class="state"><b>${T.emptyT}</b>${T.emptyB}</div>`;
}

/* ---------- 兜底：历史成绩区块取数/渲染失败就整体隐藏 ----------
   用户要求(2026-09-03)：这一块出问题不能影响页面其它板块。失败时把指标卡、
   净值曲线、成交表连同表头一起藏起来，策略说明与注册 CTA 照常显示；下一次
   定时重试成功再显示回来。 */
const HISTORY_PARTS = ['#strategy .metrics', '#strategy .metrics-note', '#strategy .curvewrap', '#strategy .tbl-head', '#strategy .tblscroll', '#tradeState'];
function hideHistory(){ HISTORY_PARTS.forEach(sel=>{ const el=document.querySelector(sel); if(el) el.style.display='none'; }); }
function showHistory(){ HISTORY_PARTS.forEach(sel=>{ const el=document.querySelector(sel); if(el) el.style.display=''; }); }

/* #upd（「更新于」）显示的是数据生成时间，不是客户端本地时间——
   否则用户看到的「刚刚更新」其实可能是几小时前抓的旧数据。
   iso 为空（比如接口没给 generatedAt）时留空占位符。 */
function renderUpdated(iso){
  $('#upd').textContent = iso
    ? T.updated + new Date(iso).toLocaleTimeString(T.locale,{hour:'2-digit',minute:'2-digit'})
    : '—';
}

/* trades 覆盖近 30 天（后端 windowDays:30，见 config.js 顶部注释），表格
   现在展示同一个 30 天窗口——rowLimit(600) 是"最多多少行"，不是"多少天"，
   两者叠加：先按 closedAt 过滤 30 天窗口，再截前 rowLimit 行。 */
function renderTrades(trades){
  const thirtyDaysAgo = Date.now() - 30*24*3600*1000;
  const recent = trades.filter(t => t.closedAt && new Date(t.closedAt).getTime() >= thirtyDaysAgo);
  if(!recent.length) return renderEmpty();
  $('#tradeState').innerHTML = '';
  $('#tradeBody').innerHTML = recent.slice(0,CONFIG.rowLimit).map(t=>{
    const win = t.pips > 0;
    const pnlCls = t.pnlUsd==null ? '' : (Number(t.pnlUsd)>=0?'g':'r');
    return `<tr>
      <td style="color:#5B6883">${timeAgo(t.closedAt)}</td>
      <td class="sym">${t.symbol}</td>
      <td><span class="side ${t.side==='buy'?'b':'s'}">${t.side==='buy'?'BUY':'SELL'}</span></td>
      <td>${price(t.symbol,t.openPrice)}</td>
      <td>${price(t.symbol,t.closePrice)}</td>
      <td class="pnl ${win?'g':'r'}" style="text-align:right;font-weight:700">${t.pips>0?'+':''}${t.pips.toFixed(1)}</td>
      <td style="text-align:right">${fmtLots(t.suggestedLots)}</td>
      <td class="pnl ${pnlCls}" style="text-align:right;font-weight:700">${pct(t.pnlUsd)}</td>
    </tr>`;
  }).join('');
}

/* ---------- 由成交记录反推指标 ----------
   2026-09（Task 37）：页面改为相对口径——仓位(手/万美元) + 收益率(%)，不再
   展示任何美元金额，也不展示净点数——回撤/盈亏比/净值曲线全部按 pnlUsd
   换算成收益率后前端算(只用 30 天窗口内、pnlUsd 非空的笔；一笔可用数据都
   没有就是 null，显示 "—"，不退回点数)。点数只保留在成交表的"点数"列。 */
function renderMetrics(trades, summary, summary30d){
  const thirtyDaysAgo = Date.now() - 30*24*3600*1000;
  const trades30 = trades.filter(t => t.closedAt && new Date(t.closedAt).getTime() >= thirtyDaysAgo);

  // 净值曲线 + 最大回撤 + 盈亏比：全部按 30 天 trades 的收益率(pnlUsd 换算
  // 成 % of referenceBalanceUsd)从旧到新累计，pnlUsd 为 null 的笔跳过
  // （不当 0，也不退回点数）。30 天里一笔可用数据都没有（字段还没上线，
  // 或 DEMO 数据）时 dd/pf 都是 null。盈亏比是比值，换算成 % 不影响结果。
  const chron = [...trades30].reverse();
  let eq=0, peak=0, ddCalc=0, hasAnyPnl=false, winSum=0, lossSum=0;
  const curve=[0];
  // 与 curve 一一对应的时间戳：曲线按「第几笔成交」推进，不是按天，
  // 所以悬停要显示日期就必须把每个点的时间一起留下。首点是窗口起点。
  const curveAt=[trades30.length ? new Date(chron[0].closedAt).getTime() : Date.now()];
  chron.forEach(t=>{
    if(t.pnlUsd==null) return;
    hasAnyPnl = true;
    const v = Number(t.pnlUsd) / REF_BALANCE_USD * 100;
    eq+=v; peak=Math.max(peak,eq); ddCalc=Math.max(ddCalc,peak-eq); curve.push(eq);
    curveAt.push(new Date(t.closedAt).getTime());
    if(v>0) winSum+=v; else if(v<0) lossSum+=Math.abs(v);
  });
  const ddPct = hasAnyPnl ? ddCalc : null;
  const pf = hasAnyPnl ? (lossSum>0 ? (winSum/lossSum) : null) : null;

  // 胜率(30 天)：优先用后端算好的 summary30d.winRatePct，避免前后端算法
  // 口径不一致；没有时前端按 pnlUsd>0 的笔数占比自己算。英雄区 #sWin 与
  // 指标卡 #mWin 是同一个值，同一套口径。
  const winRate30 = (summary30d && summary30d.winRatePct != null)
    ? Number(summary30d.winRatePct)
    : winRateFromPnl(trades30);

  $('#mWin').textContent = winRate30!=null ? winRate30.toFixed(1)+'%' : '—';
  $('#mDD').textContent  = ddPct!=null ? '−'+ddPct.toFixed(2)+'%' : '—';
  $('#mPF').textContent  = pf!=null ? pf.toFixed(2) : '—';
  $('#mN').textContent   = (summary30d && summary30d.trades != null) ? summary30d.trades : trades30.length;

  // 近 7 天 / 近 30 天收益率：优先用后端算好的 summary.pnlUsd / summary30d.pnlUsd
  // (避免前后端口径不一致)，都没有时前端按 trades 里的 pnlUsd 自己求和；
  // 一笔可用数据都没有就是 null，显示 "—"，不是 0。求和用原始 USD，换算成
  // % 放到 pct() 里统一做。
  const pnl30 = (summary30d && summary30d.pnlUsd != null) ? Number(summary30d.pnlUsd) : sumPnlUsd(trades, thirtyDaysAgo);
  const mPnl30El = $('#mPnl30');
  if(mPnl30El){ mPnl30El.textContent = pct(pnl30); mPnl30El.className = 'v' + (pnl30==null ? '' : (pnl30>=0?' g':' r')); }

  // 预估年化：由 30 天收益率按月复利推算，指标卡与首屏用同一个值
  const r30 = (pnl30 == null) ? null : Number(pnl30) / REF_BALANCE_USD * 100;
  const ann = annualise(r30);
  const annTxt = ann==null ? '—' : (ann>=0?'+':'−') + Math.abs(ann).toFixed(1) + '%';
  const annCls = ann==null ? '' : (ann>=0?' g':' r');
  ['#mAnn','#sAnn'].forEach(sel=>{
    const el = document.querySelector(sel);
    if(el){ el.textContent = annTxt; el.className = 'v' + annCls; }
  });

  // 英雄区 #sRet / #sWin：近 30 天收益率 + 胜率(30 天)，跟指标卡的
  // #mPnl30 / #mWin 同一套数值，只是摆在首屏。
  $('#sRet').textContent = pct(pnl30);
  $('#sWin').textContent = winRate30!=null ? winRate30.toFixed(1)+'%' : '—';

  // 小字口径说明：固定文案(见 T.refNote)，不再插入具体金额——页面任何
  // 地方都不再出现美元金额，只说明"每万美元仓位权重"这个换算规则本身。
  const noteEl = $('#mRefNote');
  // 年化那条单独一句、排在前面：它是页面上唯一一个外推出来的数字，
  // 混在口径说明里读者会当成同一类脚注滑过去。
  if(noteEl){
    noteEl.innerHTML = (T.annNote ? '<b>' + T.annNote + '</b> ' : '')
                     + (T.refNote || '');
  }

  drawEquity(curve, curveAt);
}

/* 由 30 天收益率按月复利推算年化：(1+r)^12 − 1。
   这是**推算**不是业绩承诺——用一个月的结果外推一年，一个月的运气会被
   放大十二次。所以页面上始终带「推算」角标，并在小字里写清算法和它
   不代表未来。r ≤ −100% 时无意义，直接返回 null。 */
function annualise(r30Pct){
  if(r30Pct == null || !isFinite(r30Pct)) return null;
  const r = r30Pct / 100;
  if(r <= -1) return null;
  return (Math.pow(1 + r, 12) - 1) * 100;
}

/* ---------- 净值曲线 ---------- */
function drawEquity(curve, curveAt){
  const W=1080, H=260, L=52, R=16, T_=18, B=30;   // 左侧留给 Y 轴刻度，底部留给日期
  const max=Math.max(...curve), min=Math.min(...curve,0), span=(max-min)||1;
  const x=i=>L+i*(W-L-R)/(curve.length-1||1);
  const y=v=>H-B-((v-min)/span)*(H-B-T_);
  const line=curve.map((v,i)=>`${i?'L':'M'}${x(i).toFixed(1)} ${y(v).toFixed(1)}`).join(' ');
  const area=`${line} L${x(curve.length-1).toFixed(1)} ${H-B} L${x(0).toFixed(1)} ${H-B} Z`;

  /* Y 轴只放三档刻度：最低、中间、最高。刻度越多越像报表，这里要的是
     一眼看出量级，具体数字交给悬停。 */
  const ticks=[min, min+span/2, max];
  const grid=ticks.map(v=>{
    const yy=y(v);
    const dash = Math.abs(v)<1e-9 ? '' : 'stroke-dasharray="2 6"';
    return `<line x1="${L}" y1="${yy.toFixed(1)}" x2="${W-R}" y2="${yy.toFixed(1)}" `
         + `stroke="#24304A" stroke-width="1" ${dash}/>`
         + `<text x="${L-9}" y="${(yy+3.5).toFixed(1)}" text-anchor="end" `
         + `font-family="var(--mono)" font-size="11" fill="#7C89A4">`
         + `${v>=0?'+':'−'}${Math.abs(v).toFixed(1)}%</text>`;
  }).join('');

  /* X 轴只标首、中、末三个日期——30 天逐日标注会把图变成一堵字墙，
     而读者在这里想知道的只是「这段是哪一段时间」。 */
  const fmt = ts => new Date(ts).toLocaleDateString(T.locale,{month:'2-digit',day:'2-digit'});
  const at = curveAt && curveAt.length===curve.length ? curveAt : null;
  const xlab = !at ? '' : [0, Math.floor((curve.length-1)/2), curve.length-1].map((i,k)=>{
    const anchor = k===0 ? 'start' : (k===2 ? 'end' : 'middle');
    return `<text x="${x(i).toFixed(1)}" y="${H-9}" text-anchor="${anchor}" `
         + `font-family="var(--mono)" font-size="11" fill="#7C89A4">${fmt(at[i])}</text>`;
  }).join('');

  $('#equityChart').innerHTML = `
    <defs><linearGradient id="eg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#4A66F0" stop-opacity=".30"/>
      <stop offset="100%" stop-color="#4A66F0" stop-opacity="0"/>
    </linearGradient></defs>
    ${grid}${xlab}
    <path d="${area}" fill="url(#eg)"/>
    <path d="${line}" fill="none" stroke="#4A66F0" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/>
    <circle cx="${x(curve.length-1).toFixed(1)}" cy="${y(curve[curve.length-1]).toFixed(1)}" r="4" fill="#4A66F0"/>
    <g id="eqHover" style="display:none">
      <line y1="${T_}" y2="${H-B}" stroke="#8592AB" stroke-width="1" stroke-dasharray="3 4"/>
      <circle r="4.5" fill="#fff" stroke="#4A66F0" stroke-width="2"/>
    </g>
  `;
  attachEquityHover(curve, curveAt, {W,H,L,R,T_,B,x,y});
}

/* 悬停：竖线 + 圆点 + 一个跟手的小浮层，显示该点的累计收益率和日期。
   SVG 是等比缩放的，所以命中检测在像素坐标里做——用 viewBox 宽度去除
   实际宽度得到比例，再反推索引。 */
function attachEquityHover(curve, curveAt, geo){
  const svg = $('#equityChart');
  const wrap = svg && svg.closest('.curvewrap');
  if(!svg || !wrap) return;
  let tip = wrap.querySelector('.eqtip');
  if(!tip){ tip = document.createElement('div'); tip.className='eqtip'; wrap.appendChild(tip); }
  const g = svg.querySelector('#eqHover');
  const at = curveAt && curveAt.length===curve.length ? curveAt : null;

  const hide = ()=>{ if(g) g.style.display='none'; tip.classList.remove('on'); };
  const move = ev=>{
    const r = svg.getBoundingClientRect();
    if(!r.width) return;
    const scale = geo.W / r.width;
    const px = (ev.clientX - r.left) * scale;              // 换到 viewBox 坐标
    const usable = geo.W - geo.L - geo.R;
    let i = Math.round((px - geo.L) / usable * (curve.length-1));
    i = Math.max(0, Math.min(curve.length-1, i));
    const cx = geo.x(i), cy = geo.y(curve[i]);
    if(g){
      g.style.display='';
      g.querySelector('line').setAttribute('x1', cx.toFixed(1));
      g.querySelector('line').setAttribute('x2', cx.toFixed(1));
      g.querySelector('circle').setAttribute('cx', cx.toFixed(1));
      g.querySelector('circle').setAttribute('cy', cy.toFixed(1));
    }
    const v = curve[i];
    const d = at ? new Date(at[i]).toLocaleDateString(T.locale,
                    {month:'2-digit', day:'2-digit'}) : '';
    tip.innerHTML = `<b class="${v>=0?'up':'dn'}">${v>=0?'+':'−'}${Math.abs(v).toFixed(2)}%</b>`
                  + (d ? `<i>${d}</i>` : '');
    tip.classList.add('on');
    // 贴着光标放，靠右时翻到左边，免得被容器裁掉
    const leftPx = cx / scale;
    const flip = leftPx > r.width - 96;
    tip.style.left = (flip ? leftPx - 12 : leftPx + 12) + 'px';
    tip.style.transform = flip ? 'translateX(-100%)' : '';
    tip.style.top = (cy / scale - 10) + 'px';
  };
  svg.onmousemove = move;
  svg.onmouseleave = hide;
  svg.ontouchmove = e=>{ if(e.touches[0]) move(e.touches[0]); };
  svg.ontouchend = hide;
}

/* ---------- 主签名图：实线 → 虚线前瞻 ---------- */
function drawHero(){
  const W=520,H=340,P=26, N=44, SPLIT=30;
  let v=100; const pts=[];
  const seed=[3,-1,4,2,-2,5,1,-3,6,2,3,-1,4,5,-2,3,6,1,-1,4,2,5,-3,4,3,6,-1,2,5,3,4,2,6,-1,5,3,7,2,4,6,3,5,4,8];
  for(let i=0;i<N;i++){ v+=seed[i%seed.length]*.9; pts.push(v); }
  const max=Math.max(...pts), min=Math.min(...pts), span=max-min||1;
  const x=i=>P+i*(W-P*2)/(N-1);
  const y=val=>H-P-((val-min)/span)*(H-P*2);

  const seg=(a,b)=>pts.slice(a,b).map((val,k)=>`${k?'L':'M'}${x(a+k).toFixed(1)} ${y(val).toFixed(1)}`).join(' ');
  const solid=seg(0,SPLIT);
  const dash =`M${x(SPLIT-1).toFixed(1)} ${y(pts[SPLIT-1]).toFixed(1)} `+seg(SPLIT,N).slice(1);

  // 前瞻置信带
  const band=[];
  for(let i=SPLIT-1;i<N;i++){ const w=(i-SPLIT+1)*1.9; band.push(`${i===SPLIT-1?'M':'L'}${x(i).toFixed(1)} ${(y(pts[i])-w).toFixed(1)}`); }
  for(let i=N-1;i>=SPLIT-1;i--){ const w=(i-SPLIT+1)*1.9; band.push(`L${x(i).toFixed(1)} ${(y(pts[i])+w).toFixed(1)}`); }

  const ticks=[0,.2,.4,.6,.8,1].map(f=>{
    const yy=P+f*(H-P*2);
    return `<line x1="${P}" y1="${yy}" x2="${W-P}" y2="${yy}" stroke="#C9D3DE" stroke-width="1" stroke-dasharray="1 7"/>`;
  }).join('');

  $('#heroChart').innerHTML = `
    ${ticks}
    <line x1="${x(SPLIT-1).toFixed(1)}" y1="${P-6}" x2="${x(SPLIT-1).toFixed(1)}" y2="${H-P}" stroke="#D6188A" stroke-width="1" stroke-dasharray="3 4" opacity=".55"/>
    <text x="${(x(SPLIT-1)+7).toFixed(1)}" y="${P+2}" font-family="JetBrains Mono, monospace" font-size="9" fill="#D6188A" letter-spacing="1.4">NOW</text>
    <path d="${band.join(' ')} Z" fill="#D6188A" opacity=".09"/>
    <path id="hSolid" d="${solid}" fill="none" stroke="#1B3BD8" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/>
    <path id="hDash"  d="${dash}"  fill="none" stroke="#D6188A" stroke-width="2.4" stroke-dasharray="6 5" stroke-linejoin="round" stroke-linecap="round"/>
    <circle cx="${x(SPLIT-1).toFixed(1)}" cy="${y(pts[SPLIT-1]).toFixed(1)}" r="4.5" fill="#EDF0F4" stroke="#1B3BD8" stroke-width="2.4"/>
  `;

  if(matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  ['hSolid','hDash'].forEach((id,i)=>{
    const p=document.getElementById(id), L=p.getTotalLength();
    p.style.strokeDasharray = id==='hDash' ? `${L}` : `${L}`;
    p.style.strokeDashoffset = L;
    p.style.transition = `stroke-dashoffset 1.5s cubic-bezier(.35,.75,.35,1) ${i*1.15+.25}s`;
    requestAnimationFrame(()=>{
      p.style.strokeDashoffset = 0;
      if(id==='hDash') setTimeout(()=>{ p.style.transition='none'; p.style.strokeDasharray='6 5'; }, 1400+i*1150+250);
    });
  });
}

/* ---------- 顶部行情条 ---------- */
/* ---------- 按品种拆分净点数 ----------
   汇总的净点数是一个数，看不出它从哪来。摊开之后一眼能看到哪个品种在
   贡献、哪个在拖累——对一个把"亏损单同样列出"写在首页的站点来说，这是
   该给的信息，不是可选的装饰。

   条形长度按各品种净点数的绝对值占最大值的比例，盈亏从中线分别向两侧
   展开，所以正负两栏的量级可以直接比。 */
function renderBySymbol(trades){
  // 2026-09:按品种拆分改为收益率(pnlUsd 换算成 % of referenceBalanceUsd、
  // 仅已平仓、不含浮动盈亏与隔夜利息),与页面其它指标同口径;点数只保留
  // 在成交表列里,页面任何地方不再出现美元金额。
  const box = document.getElementById('bySym');
  if(!box) return;
  const g = new Map();
  for(const t of trades || []){
    if(!t.symbol || t.pnlUsd == null || !isFinite(Number(t.pnlUsd))) continue;
    const e = g.get(t.symbol) || {n:0, w:0, p:0};
    e.n++; e.p += Number(t.pnlUsd);
    if(Number(t.pnlUsd) > 0) e.w++;
    g.set(t.symbol, e);
  }
  const rows = [...g.entries()].map(([s,e])=>({s, ...e}))
                               .sort((a,b)=> b.p - a.p);
  if(!rows.length){ box.innerHTML = ''; return; }
  const max = Math.max(...rows.map(r=>Math.abs(r.p))) || 1;

  box.innerHTML = rows.map(r=>{
    const up = r.p >= 0;
    const w = Math.abs(r.p) / max * 50;          // 半幅，从中线向两侧
    const bar = up
      ? `<i class="up" style="left:50%;width:${w}%"></i>`
      : `<i class="dn" style="right:50%;width:${w}%"></i>`;
    return `<div class="bsrow">`
         + `<span class="s">${r.s}</span>`
         + `<span class="bsbar">${bar}</span>`
         + `<span class="n">${r.n} ${T.tradesUnit}</span>`
         + `<span class="p ${up?'up':'dn'}">${pct(r.p)}</span>`
         + `</div>`;
  }).join('');
}

/* ---------- 顶部滚动条：近期盈利成交 ----------
   原来这里滚的是一组**写死的假报价**（EURUSD 1.08742 …）。在一个交易站
   上摆假价格，比空着更糟：它看起来像实时行情，实际永远不动。

   改成滚真实成交，用的是策略面板同一份数据，不额外发请求。按要求优先
   展示盈利单，所以左端加了固定标签写明「近期盈利成交」——完整记录（含
   亏损单）就在下面的面板里，两者不冲突；不写清楚才会变成误导。

   取不到数据就整条隐藏，不再退回假数据。 */
function tickerAgo(iso){
  const diff = (Date.now() - new Date(iso)) / 6e4;
  if(!isFinite(diff) || diff < 0) return '';
  if(diff < 60)   return Math.max(1, Math.round(diff)) + T.min;
  if(diff < 1440) return Math.round(diff / 60) + T.hour;
  return Math.round(diff / 1440) + T.day;
}

function drawTicker(trades){
  const bar = document.querySelector('.tick');
  if(!bar) return;
  const wins = (trades || [])
    .filter(t => Number(t.pips) > 0 && t.symbol && t.closedAt)
    .sort((a, b) => new Date(b.closedAt) - new Date(a.closedAt))
    .slice(0, 16);
  // 少于 4 条不值当滚一条横幅，宁可不显示
  if(wins.length < 4){ bar.hidden = true; return; }

  const html = wins.map(t => {
    const side = (t.side || '').toLowerCase() === 'sell' ? T.sell : T.buy;
    return '<span><i class="sym">' + t.symbol + '</i>'
         + '<i class="sd">' + side + '</i>'
         + '<b class="up">+' + Number(t.pips).toFixed(1) + ' pips</b>'
         + '<i class="ago">' + tickerAgo(t.closedAt) + '</i></span>';
  }).join('');
  $('#ticker').innerHTML = html + html;      // 两份首尾相接，滚动才无缝

  if(!bar.querySelector('.tick-tag')){
    // 轨道套一层 .tick-vp（overflow 归它），标签作为兄弟节点占住左侧，
    // 这样第一条成交不会被标签压住
    const track = $('#ticker');
    const vp = document.createElement('div');
    vp.className = 'tick-vp';
    track.parentNode.insertBefore(vp, track);
    vp.appendChild(track);
    const tag = document.createElement('div');
    tag.className = 'tick-tag';
    tag.textContent = T.recentWins;
    bar.insertBefore(tag, vp);
  }
  bar.hidden = false;
}

/* ---------- 拉数据 ---------- */
/* ---------- 取数：带重试 + 本地缓存 ----------
   2026-09-03 用户反馈：首次打开空白、刷新时好时坏。原因是到数据域名的请求
   在部分网络下**间歇性**失败(连接被重置/超时),失败一次就走了"隐藏区块"的
   兜底。对策：
   1) 每次取数最多试 3 次(0s/1.5s/4s 后重试)，单次 8 秒超时，别让一次抖动定生死；
   2) 成功的数据存 localStorage；下次打开先用缓存立刻渲染，再后台取新数据——
      回访用户永远不会看到空白；
   3) 三次都失败且没有缓存，才隐藏区块(首次访问且网络完全不通)。 */
const CACHE_KEY = 'presight.vipHistory.v1';
function readCache(){ try{ const s=localStorage.getItem(CACHE_KEY); return s ? JSON.parse(s) : null; }catch(e){ return null; } }
function writeCache(json){ try{ localStorage.setItem(CACHE_KEY, JSON.stringify(json)); }catch(e){} }
async function fetchWithRetry(url, delays=[0,1500,4000], timeoutMs=6000){
  let lastErr;
  for(const d of delays){
    if(d) await new Promise(r=>setTimeout(r,d));
    const ctrl = new AbortController(); const timer = setTimeout(()=>ctrl.abort(), timeoutMs);
    try{
      // 简单 GET、不带自定义头：免预检，少一趟往返也少一个失败点。
      // cache:'no-store' 让每次都真正去拿，不被浏览器 HTTP 缓存里的旧文件糊弄。
      const r = await fetch(url, {signal: ctrl.signal, cache: 'no-store'});
      if(!r.ok) throw new Error('HTTP '+r.status);
      return await r.json();
    }catch(e){ lastErr = e; }
    finally{ clearTimeout(timer); }
  }
  throw lastErr;
}
function renderPayload(json){
  const rawTrades = Array.isArray(json) ? json : (json.data || json.trades || []);
  const list = rawTrades.map(normalize);
  const summary = Array.isArray(json) ? null : json.summary;
  const summary30d = Array.isArray(json) ? null : json.summary30d;
  const generatedAt = Array.isArray(json) ? null : json.generatedAt;
  // 先定好参考账户余额，再渲染依赖 pct() 的各个板块，避免按品种拆分/成交表
  // 用旧的 REF_BALANCE_USD 换算，跟同一批数据的指标卡口径对不上。
  REF_BALANCE_USD = refBalanceOf(summary, summary30d);
  showHistory();
  drawTicker(list);
  renderBySymbol(list);
  renderTrades(list);
  renderMetrics(list, summary, summary30d);
  renderUpdated(generatedAt);
  // 数据到位后主动把面板标记为已显示:不依赖滚动淡入的观察时机(面板变高之前
  // 观察器可能已经错过;见 IntersectionObserver 处注释)。
  const box = document.querySelector('#strategy .panelbox'); if(box) box.classList.add('in');
  // 175 行别把面板撑成 9000px:表格区限高、内部滚动,页面其它板块仍在一屏之内可达。
  const tbl = document.querySelector('#strategy .tblscroll'); if(tbl){ tbl.style.maxHeight='62vh'; tbl.style.overflowY='auto'; }
}
let historyPainted = false;
async function loadTrades(){
  if(!CONFIG.tradesEndpoint){
    renderTrades(DEMO); renderMetrics(DEMO);
    $('#upd').textContent = T.demo;
    return;
  }
  if(!historyPainted){
    const cached = readCache();
    if(cached){ try{ renderPayload(cached); historyPainted = true; }catch(e){ console.error('[presight] cached render failed:', e); } }
    else renderLoading();
  }
  try{
    const json = await fetchWithRetry(CONFIG.tradesEndpoint);
    renderPayload(json);
    historyPainted = true;
    writeCache(json);
  }catch(e){
    console.error('[presight] trades fetch failed after retries:', e);
    if(!historyPainted) renderError();   // 有缓存画面就保留，不为一次失败清空
  }
}

/* ---------- 计数动画 ---------- */
function countUp(el,target,suffix='',dur=1100){
  if(matchMedia('(prefers-reduced-motion: reduce)').matches){ el.innerHTML=target.toLocaleString()+suffix; return; }
  const t0=performance.now();
  (function step(t){
    const k=Math.min(1,(t-t0)/dur), e=1-Math.pow(1-k,3);
    el.innerHTML = Math.round(target*e).toLocaleString()+suffix;
    if(k<1) requestAnimationFrame(step);
  })(t0);
}

/* ---------- init ---------- */
/* 每个初始化步骤各自 try/catch：任何一步抛错都不能拖垮后面的步骤
   (2026-09-03：成交表先于首图动画启动，首图/跑马灯出错也不影响成交表)。 */
function safe(label, fn){ try{ return fn(); }catch(e){ console.error('[presight] init step failed: '+label, e); } }
safe('trades', ()=>{ loadTrades(); setInterval(loadTrades, CONFIG.refreshMs); });
// 横幅先藏起来：有真实成交再显示，绝不先摆一条空的或假的
safe('ticker', ()=>{ const b=document.querySelector('.tick'); if(b) b.hidden=true; });
safe('hero', drawHero);

safe('links & ui', ()=>{
$('#brokerLink').href    = CONFIG.brokerSignupUrl;

/* 链接统一由 config.js 注入：把同一 data-link 的元素全部填上，
   页面里加几个入口都不用再改 JS。 */
const LINKS = {
  broker   : CONFIG.brokerSignupUrl,
  ib       : CONFIG.ibSignupUrl,
  bot      : CONFIG.adminBotUrl,
  channel  : CONFIG.channelUrl,
  community: CONFIG.communityUrl,
  email    : 'mailto:' + CONFIG.contactEmail,
};
document.querySelectorAll('[data-link]').forEach(el=>{
  const url = LINKS[el.dataset.link];
  if(url) el.href = url;
});

/* ---------- 带 #hash 进来时把定位补一次 ----------
   两个毛病叠在一起，表现是「点了链接不跳到板块」，手机上尤其明显。

   一是浏览器在文档还没长完时就执行了片段跳转：成交表由 JS 填充、
   图表要等字体，这些都排在 #partner 前面，填进去之后目标被往下推。

   二是——量了才发现这才是主因——页面上有 html{scroll-behavior:smooth}，
   而 scrollIntoView 的默认 behavior:'auto' 会继承它。于是每次都变成
   一段跨越一万多像素的平滑滚动，中途被下一次调用打断，实测停在半路
   （Y 从 10 → 1915 → 5349 就不动了，目标还在下方 4000px）。手机上
   随便碰一下屏幕也会打断它。

   所以这里临时关掉平滑滚动、直接落位。页面内点击锚点仍然是平滑的，
   那时候文档早已长完，也没人会去打断。 */
if(location.hash){
  const settle = ()=>{
    let el;
    try{ el = document.querySelector(location.hash); }catch(_){ return; }
    if(!el) return;
    // 只有真的吸顶时才需要让开它的高度。手机上顶栏是 static，会跟着
    // 滚走，再减一次高度就会把目标顶到屏幕上方之外。
    const bar = document.querySelector('header');
    const pinned = bar && ['sticky','fixed'].includes(getComputedStyle(bar).position);
    const off = (pinned ? bar.getBoundingClientRect().height : 0) + 12;
    const root = document.documentElement;
    const prev = root.style.scrollBehavior;
    root.style.scrollBehavior = 'auto';
    window.scrollTo(0, el.getBoundingClientRect().top + window.scrollY - off);
    root.style.scrollBehavior = prev;
  };
  let done = false;
  // 用户自己滚了就撒手，否则页面还在长、人往下翻却被硬拽回来
  ['wheel','touchmove','keydown'].forEach(e=>
    addEventListener(e, ()=>{ done = true; }, {passive:true, once:true}));

  settle();
  addEventListener('load', ()=>{ if(!done) settle(); });
  if(window.ResizeObserver){
    const ro = new ResizeObserver(()=>{ if(!done) settle(); });
    ro.observe(document.body);
    setTimeout(()=>{ ro.disconnect(); done = true; }, 5000);
  }
}

/* ---------- 一键复制（IB 分享链接） ----------
   剪贴板 API 只在 https 和 localhost 下可用。取不到时不要静默失败——
   退回「把文字选中」，用户按 Cmd+C 仍然拿得走。 */
document.querySelectorAll('[data-copy]').forEach(btn=>{
  btn.addEventListener('click', async ()=>{
    const el = document.querySelector(btn.dataset.copy);
    if(!el) return;
    const text = el.textContent.trim();
    try{
      await navigator.clipboard.writeText(text);
    }catch(_){
      const r = document.createRange(); r.selectNodeContents(el);
      const sel = getSelection(); sel.removeAllRanges(); sel.addRange(r);
      return;
    }
    const was = btn.textContent;
    btn.textContent = T.copied;
    setTimeout(()=>{ btn.textContent = was; }, 1600);
  });
});

/* ---------- 「开始跟单」弹窗 ----------
   顶栏按钮原来锚到 #strategy——那里讲的是策略是什么，不是怎么开始，
   用户点完还得自己把注册、订阅、报备三件事从页面各处拼起来。弹窗把
   这三步连着链接摆在一屏里。

   href 保留着：JS 没加载出来时点击仍然滚到策略区，不会变成死按钮。 */
const mask = $('#startMask');
if(mask){
  const openStart = (e)=>{
    if(e) e.preventDefault();
    mask.hidden = false;
    mask.classList.add('on');
    document.body.style.overflow = 'hidden';   // 背景不要跟着滚
    const first = mask.querySelector('[data-close]');
    if(first) first.focus();
  };
  const closeStart = ()=>{
    mask.classList.remove('on');
    mask.hidden = true;
    document.body.style.overflow = '';
  };
  document.querySelectorAll('[data-open="start"]')
          .forEach(el=>el.addEventListener('click', openStart));

  /* 深链接：#start-copy 直接弹出「三步开始跟单」。
     海报上的二维码指向它——扫码的人手里没有页面上下文，落在首页顶部还得
     自己找入口，一步都不该多。
     不用 #start：那是「四步开始跟单」那一节已经占用的锚点，重名会让浏览器
     先滚过去再弹窗，观感很乱。 */
  if(location.hash === '#start-copy'){
    // 等版式稳定再弹，否则弹窗背后的页面还在长，关掉之后位置是乱的
    addEventListener('load', ()=>setTimeout(()=>openStart(), 300));
  }
  mask.addEventListener('click', e=>{
    // 点遮罩本身或叉号都关；点面板内部不关
    if(e.target === mask || e.target.closest('[data-close]')) closeStart();
  });
  document.addEventListener('keydown', e=>{
    if(e.key === 'Escape' && !mask.hidden) closeStart();
  });
}

const io = new IntersectionObserver((es)=>es.forEach(e=>{
  if(!e.isIntersecting) return;
  e.target.classList.add('in');
  if(e.target.classList.contains('strip')){
    countUp($('#sRun'),412,T.daysUnit);
    countUp($('#sMem'),8640,'+');
  }
  io.unobserve(e.target);
}),{threshold:0});
/* threshold 由 .15 改为 0(2026-09-03 根因):成交面板放 7 天 175 行后高达 9000px,
   手机/桌面视口只能露出 5–10%,永远达不到 15% → .in 永不加 → 面板 opacity 0,
   用户滚到 #strategy 看到"一大片空白";只有数据还没加载完(面板还矮)时先滚到才正常,
   所以"刷新时好时坏"。露出任意 1px 即淡入。 */
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
});
