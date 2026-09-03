/* ---------- 界面文案：跟随 <html lang> 自动切换 ----------
   原来只分「英文/其它」，日、越、泰三个语种因此全都落进中文分支——
   页面通篇是泰文，指标条却写着「412 天」。加语种时最容易漏的就是这种
   由 JS 注入、不在 HTML 里的字。 */
const LANG = (document.documentElement.lang || 'zh').toLowerCase().slice(0,2);
const TEXTS = {
  zh:{
    loading:'成交记录加载中…',
    locale:'zh-CN', daysUnit:'<small>天</small>',
    now:'刚刚', min:' 分钟前', hour:' 小时前', day:' 天前',
    updated:'更新于 ', demo:'演示数据', copied:'已复制',
    errT:'成交记录暂时取不到', errB:'数据接口没有响应。稍后会自动重试，也可以刷新页面。',
    emptyT:'还没有已平仓的交易', emptyB:'策略正在运行，第一笔成交平仓后会立刻出现在这里。',
  },
  en:{
    loading:'Loading fill history…',
    locale:'en-GB', daysUnit:'<small>days</small>',
    now:'just now', min:'m ago', hour:'h ago', day:'d ago',
    updated:'updated ', demo:'demo data', copied:'Copied',
    errT:'Fill history unavailable', errB:'The data endpoint did not respond. It will retry automatically, or you can reload the page.',
    emptyT:'No closed trades yet', emptyB:'The strategy is running. The first closed trade will appear here immediately.',
  },
  ja:{
    loading:'約定履歴を読み込み中…',
    locale:'ja-JP', daysUnit:'<small>日</small>',
    now:'たった今', min:' 分前', hour:' 時間前', day:' 日前',
    updated:'更新 ', demo:'デモデータ', copied:'コピーしました',
    errT:'約定履歴を取得できません', errB:'データ側から応答がありません。自動で再試行します。ページの再読み込みでもかまいません。',
    emptyT:'決済済みの取引はまだありません', emptyB:'戦略は稼働中です。最初の決済が出たらすぐここに表示されます。',
  },
  vi:{
    loading:'Đang tải lịch sử khớp lệnh…',
    locale:'vi-VN', daysUnit:'<small>ngày</small>',
    now:'vừa xong', min:' phút trước', hour:' giờ trước', day:' ngày trước',
    updated:'cập nhật ', demo:'dữ liệu mẫu', copied:'Đã sao chép',
    errT:'Chưa lấy được lịch sử khớp lệnh', errB:'Máy chủ dữ liệu không phản hồi. Hệ thống sẽ tự thử lại, hoặc bạn có thể tải lại trang.',
    emptyT:'Chưa có lệnh nào đóng', emptyB:'Chiến lược đang chạy. Lệnh đóng đầu tiên sẽ hiện ở đây ngay lập tức.',
  },
  th:{
    loading:'กำลังโหลดประวัติออเดอร์…',
    locale:'th-TH', daysUnit:'<small>วัน</small>',
    now:'เมื่อครู่', min:' นาทีที่แล้ว', hour:' ชั่วโมงที่แล้ว', day:' วันที่แล้ว',
    updated:'อัปเดตเมื่อ ', demo:'ข้อมูลตัวอย่าง', copied:'คัดลอกแล้ว',
    errT:'ยังดึงประวัติออเดอร์ไม่ได้', errB:'เซิร์ฟเวอร์ข้อมูลไม่ตอบสนอง ระบบจะลองใหม่อัตโนมัติ หรือคุณจะรีเฟรชหน้าก็ได้',
    emptyT:'ยังไม่มีออเดอร์ที่ปิดแล้ว', emptyB:'กลยุทธ์กำลังทำงาน ออเดอร์แรกที่ปิดจะขึ้นตรงนี้ทันที',
  },
};
const T = TEXTS[LANG] || TEXTS.zh;

/* ---------- 演示数据（接上 API 后自动弃用） ---------- */
/* 只公开点数：这里不再造 lots/pnl，字段形状对齐 normalize() 的输出，
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
const HISTORY_PARTS = ['#strategy .metrics', '#strategy .curvewrap', '#strategy .tbl-head', '#strategy .tblscroll', '#tradeState'];
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

function renderTrades(trades){
  if(!trades.length) return renderEmpty();
  $('#tradeState').innerHTML = '';
  $('#tradeBody').innerHTML = trades.slice(0,CONFIG.rowLimit).map(t=>{
    const win = t.pips > 0;
    return `<tr>
      <td style="color:#5B6883">${timeAgo(t.closedAt)}</td>
      <td class="sym">${t.symbol}</td>
      <td><span class="side ${t.side==='buy'?'b':'s'}">${t.side==='buy'?'BUY':'SELL'}</span></td>
      <td>${price(t.symbol,t.openPrice)}</td>
      <td>${price(t.symbol,t.closePrice)}</td>
      <td class="pnl ${win?'g':'r'}" style="text-align:right;font-weight:700">${t.pips>0?'+':''}${t.pips.toFixed(1)}</td>
    </tr>`;
  }).join('');
}

/* ---------- 由成交记录反推指标（只按点数口径：不涉及手数/美元盈亏） ---------- */
function renderMetrics(trades, summary){
  const n = trades.length;
  const wins   = trades.filter(t=>t.pips>0);
  const losses = trades.filter(t=>t.pips<0);

  // 从旧到新累计，算净值曲线（图表用；summary 只给汇总数字，不给逐笔
  // 曲线，所以曲线始终在前端按 trades 现算）
  const chron = [...trades].reverse();
  let eq=0, peak=0, ddCalc=0; const curve=[0];
  chron.forEach(t=>{ eq+=t.pips; peak=Math.max(peak,eq); ddCalc=Math.max(ddCalc,peak-eq); curve.push(eq); });

  // 优先用后端算好的 summary，避免前后端算法口径不一致；
  // 没有 summary（比如 DEMO 数据、或接口暂时没给）时前端自算。
  let netPips, winRatePct, ddPips, pf;
  if(summary){
    // 后端(vip-history.json)的键名是 totalPips / winRatePct / pfPips / maxDrawdownPips；
    // 同时兼容早期草案的 netPips / winRate / profitFactor，任一存在即用。
    netPips    = Number(summary.totalPips ?? summary.netPips);
    winRatePct = Number(summary.winRatePct ?? summary.winRate);
    ddPips     = Number(summary.maxDrawdownPips);
    const pfRaw = summary.pfPips ?? summary.profitFactor;
    pf         = pfRaw != null ? Number(pfRaw) : null;
  }

  $('#mRet').textContent = (netPips>=0?'+':'−') + Math.abs(netPips).toFixed(1);
  $('#mWin').textContent = winRatePct!=null ? winRatePct.toFixed(1)+'%' : '—';
  $('#mDD').textContent  = '−' + Math.abs(ddPips).toFixed(1);
  $('#mPF').textContent  = pf!=null ? pf.toFixed(2) : '—';
  $('#mN').textContent   = n;

  // 英雄区 #sRet 的标签是「近 7 天净点数」，按 closedAt 单独过滤 7 天
  // 窗口——不能直接复用上面的 netPips（那是全量/summary 口径）。
  const sevenDaysAgo = Date.now() - 7*24*3600*1000;
  const net7 = trades
    .filter(t=>t.closedAt && new Date(t.closedAt).getTime() >= sevenDaysAgo)
    .reduce((a,t)=>a+t.pips,0);
  $('#sRet').textContent = (net7>=0?'+':'−') + Math.abs(net7).toFixed(1) + ' pips';
  $('#sWin').textContent = winRatePct!=null ? winRatePct.toFixed(1)+'%' : '—';

  drawEquity(curve);
}

/* ---------- 净值曲线 ---------- */
function drawEquity(curve){
  const W=1080,H=260,P=14;
  const max=Math.max(...curve), min=Math.min(...curve,0), span=(max-min)||1;
  const x=i=>P+i*(W-P*2)/(curve.length-1||1);
  const y=v=>H-P-((v-min)/span)*(H-P*2);
  const line=curve.map((v,i)=>`${i?'L':'M'}${x(i).toFixed(1)} ${y(v).toFixed(1)}`).join(' ');
  const area=`${line} L${x(curve.length-1).toFixed(1)} ${H-P} L${x(0).toFixed(1)} ${H-P} Z`;
  const grid=[0,.25,.5,.75,1].map(f=>{
    const yy=P+f*(H-P*2);
    return `<line x1="${P}" y1="${yy}" x2="${W-P}" y2="${yy}" stroke="#24304A" stroke-width="1" ${f===1?'':'stroke-dasharray="2 6"'}/>`;
  }).join('');
  $('#equityChart').innerHTML = `
    <defs><linearGradient id="eg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#4A66F0" stop-opacity=".30"/>
      <stop offset="100%" stop-color="#4A66F0" stop-opacity="0"/>
    </linearGradient></defs>
    ${grid}
    <path d="${area}" fill="url(#eg)"/>
    <path d="${line}" fill="none" stroke="#4A66F0" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/>
    <circle cx="${x(curve.length-1).toFixed(1)}" cy="${y(curve[curve.length-1]).toFixed(1)}" r="4" fill="#4A66F0"/>
  `;
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
function drawTicker(){
  const rows=[['EURUSD','1.08742',.12],['XAUUSD','2418.65',.48],['GBPUSD','1.28901',-.09],
    ['USDJPY','157.284',.21],['NAS100','20238.5',.87],['BTCUSD','68,412',-1.24],
    ['US30','41,762',-.31],['AUDUSD','0.66341',.18],['USOIL','78.42',.64]];
  const html = rows.map(([s,p,c])=>
    `<span><i>${s}</i>${p} <b class="${c>=0?'up':'dn'}">${c>=0?'▲':'▼'} ${Math.abs(c).toFixed(2)}%</b></span>`).join('');
  $('#ticker').innerHTML = html+html;
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
  const generatedAt = Array.isArray(json) ? null : json.generatedAt;
  showHistory();
  renderTrades(list);
  renderMetrics(list, summary);
  renderUpdated(generatedAt);
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
safe('ticker', drawTicker);
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
    // 吸顶栏的高度现量现用：手机上它排两行，写死一个数就会盖住标题
    const bar = document.querySelector('header');
    const off = (bar ? bar.getBoundingClientRect().height : 0) + 12;
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
}),{threshold:.15});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
});
