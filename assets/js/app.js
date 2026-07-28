/* ---------- 演示数据（接上 API 后自动弃用） ---------- */
const DEMO = (()=>{
  const spec = [
    ['XAUUSD','buy',0.40,2412.35,2419.80,74.5],   ['EURUSD','sell',1.20,1.08942,1.08761,18.1],
    ['GBPJPY','buy',0.60,198.412,198.905,49.3],   ['USDJPY','sell',0.80,157.204,157.388,-18.4],
    ['XAUUSD','sell',0.35,2431.10,2422.65,84.5],  ['AUDUSD','buy',1.50,0.66218,0.66341,12.3],
    ['NAS100','buy',0.25,20114.5,20238.0,123.5],  ['EURUSD','buy',1.00,1.08510,1.08402,-10.8],
    ['USDCAD','sell',0.90,1.36720,1.36531,18.9],  ['XAUUSD','buy',0.50,2398.20,2409.55,113.5],
    ['GBPUSD','sell',0.70,1.28904,1.28812,9.2],   ['US30','buy',0.20,41890.0,41762.0,-128.0],
    ['EURJPY','buy',0.55,170.240,170.712,47.2],   ['XAUUSD','sell',0.45,2445.90,2451.30,-54.0],
    ['USDCHF','buy',1.10,0.88410,0.88532,12.2],
  ];
  const now = Date.now();
  return spec.map((s,i)=>{
    const [symbol,side,lots,openPrice,closePrice,pips] = s;
    const mult = symbol.includes('XAU')?10 : (symbol==='NAS100'||symbol==='US30')?1 : 10;
    return {
      closedAt: new Date(now - (i*3.4+1)*3600*1000).toISOString(),
      symbol, side, lots, openPrice, closePrice, pips,
      pnl: +(pips*lots*mult).toFixed(2)
    };
  });
})();

/* ---------- 工具 ---------- */
const $ = s => document.querySelector(s);
const fmt = (n,d=2) => n.toLocaleString('en-US',{minimumFractionDigits:d,maximumFractionDigits:d});
const price = (s,v) => v.toFixed(s.includes('JPY')?3 : (s==='NAS100'||s==='US30')?1 : (s.includes('XAU')?2:5));
function timeAgo(iso){
  const m = Math.floor((Date.now()-new Date(iso))/60000);
  if(m<1) return '刚刚';
  if(m<60) return m+' 分钟前';
  const h = Math.floor(m/60);
  if(h<24) return h+' 小时前';
  return Math.floor(h/24)+' 天前';
}

/* ---------- 渲染成交表 ---------- */
function renderLoading(){
  $('#tradeBody').innerHTML = Array.from({length:6},()=>
    `<tr>${'<td><div class="skel"></div></td>'.repeat(8)}</tr>`).join('');
  $('#tradeState').innerHTML = '';
}
function renderError(){
  $('#tradeBody').innerHTML = '';
  $('#tradeState').innerHTML =
    '<div class="state"><b>成交记录暂时取不到</b>数据接口没有响应。稍后会自动重试，也可以刷新页面。</div>';
}
function renderEmpty(){
  $('#tradeBody').innerHTML = '';
  $('#tradeState').innerHTML =
    '<div class="state"><b>还没有已平仓的交易</b>策略正在运行，第一笔成交平仓后会立刻出现在这里。</div>';
}

function renderTrades(trades){
  if(!trades.length) return renderEmpty();
  $('#tradeState').innerHTML = '';
  $('#tradeBody').innerHTML = trades.slice(0,CONFIG.rowLimit).map(t=>{
    const win = t.pnl >= 0;
    return `<tr>
      <td style="color:#5B6883">${timeAgo(t.closedAt)}</td>
      <td class="sym">${t.symbol}</td>
      <td><span class="side ${t.side==='buy'?'b':'s'}">${t.side==='buy'?'BUY':'SELL'}</span></td>
      <td>${t.lots.toFixed(2)}</td>
      <td>${price(t.symbol,t.openPrice)}</td>
      <td>${price(t.symbol,t.closePrice)}</td>
      <td class="pnl ${win?'g':'r'}">${t.pips>0?'+':''}${t.pips.toFixed(1)}</td>
      <td class="pnl ${win?'g':'r'}" style="text-align:right;font-weight:700">${win?'+':'−'}${fmt(Math.abs(t.pnl))}</td>
    </tr>`;
  }).join('');
  $('#upd').textContent = '更新于 ' + new Date().toLocaleTimeString('zh-CN',{hour:'2-digit',minute:'2-digit'});
}

/* ---------- 由成交记录反推指标 ---------- */
function renderMetrics(trades){
  const n = trades.length;
  const wins = trades.filter(t=>t.pnl>0);
  const gross= trades.reduce((a,t)=>a+t.pnl,0);
  const gp   = wins.reduce((a,t)=>a+t.pnl,0);
  const gl   = Math.abs(trades.filter(t=>t.pnl<0).reduce((a,t)=>a+t.pnl,0));

  // 从旧到新累计，算净值与最大回撤
  const chron = [...trades].reverse();
  let eq=0, peak=0, dd=0; const curve=[0];
  chron.forEach(t=>{ eq+=t.pnl; peak=Math.max(peak,eq); dd=Math.max(dd,peak-eq); curve.push(eq); });

  $('#mRet').textContent = (gross>=0?'+':'−') + fmt(Math.abs(gross),0);
  $('#mWin').textContent = n ? (wins.length/n*100).toFixed(1)+'%' : '—';
  $('#mDD').textContent  = '−' + fmt(dd,0);
  $('#mPF').textContent  = gl ? (gp/gl).toFixed(2) : '—';
  $('#mN').textContent   = n;

  $('#sRet').textContent = (gross>=0?'+':'−') + fmt(Math.abs(gross),0);
  $('#sWin').textContent = n ? (wins.length/n*100).toFixed(1)+'%' : '—';

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
async function loadTrades(){
  if(!CONFIG.tradesEndpoint){
    renderTrades(DEMO); renderMetrics(DEMO);
    $('#upd').textContent = '演示数据';
    return;
  }
  renderLoading();
  try{
    const r = await fetch(CONFIG.tradesEndpoint,{headers:{'Accept':'application/json'}});
    if(!r.ok) throw new Error(r.status);
    const json = await r.json();
    const list = (Array.isArray(json)?json:(json.data||json.trades||[])).map(normalize);
    renderTrades(list); renderMetrics(list);
  }catch(e){ console.error('[presight] trades fetch failed:',e); renderError(); }
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
drawTicker();
drawHero();
loadTrades();
setInterval(loadTrades, CONFIG.refreshMs);

$('#brokerLink').href    = CONFIG.brokerSignupUrl;
$('#communityLink').href = CONFIG.communityUrl;

const io = new IntersectionObserver((es)=>es.forEach(e=>{
  if(!e.isIntersecting) return;
  e.target.classList.add('in');
  if(e.target.classList.contains('strip')){
    countUp($('#sRun'),412,'<small>天</small>');
    countUp($('#sMem'),8640,'+');
  }
  io.unobserve(e.target);
}),{threshold:.15});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
