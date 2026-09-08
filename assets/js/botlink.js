/* 报备账号 @PresightAdminBot 的正文链接化。
   单独一个文件而不是塞进 app.js：细则页 protection.html 不加载 app.js
   （那里没有图表、没有行情条，整份 app.js 跑起来只会报错），但同样有
   好几处提到报备账号，同样需要能点。 */
/* ---------- 把正文里的 @PresightAdminBot 变成可点的链接 ----------
   报备账号在五个语种、三个页面、十几处正文里都出现，而且措辞各不相同
   （「私信 X」「message X」「X に送る」…）。逐处手动加 <a> 要改十几个
   地方，以后每加一句还会漏——所以在运行时统一处理：遍历文本节点，把这
   个字符串换成链接。

   跳过已经在 <a> 里的：按钮那几处本来就有 href，再包一层会嵌套。
   JS 没跑起来也不会更糟——文字还在，只是不可点，跟改之前一样。 */
function linkifyBot(){
  const HANDLE = '@PresightAdminBot';
  const URL = 'https://t.me/PresightAdminBot';
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
    acceptNode(n){
      if(!n.nodeValue || n.nodeValue.indexOf(HANDLE) === -1) return NodeFilter.FILTER_REJECT;
      if(n.parentElement && n.parentElement.closest('a')) return NodeFilter.FILTER_REJECT;
      return NodeFilter.FILTER_ACCEPT;
    }
  });
  const targets = [];
  for(let n = walker.nextNode(); n; n = walker.nextNode()) targets.push(n);

  targets.forEach(node=>{
    const frag = document.createDocumentFragment();
    node.nodeValue.split(HANDLE).forEach((part, i)=>{
      if(i){
        const a = document.createElement('a');
        a.className = 'botlink';
        a.href = URL;
        a.target = '_blank';
        a.rel = 'noopener';
        a.textContent = HANDLE;
        frag.appendChild(a);
      }
      if(part) frag.appendChild(document.createTextNode(part));
    });
    node.parentNode.replaceChild(frag, node);
  });
}

linkifyBot();
