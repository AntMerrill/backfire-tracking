// claude 2026-10-17. The exact code used for latterdayavenger_2026-10-17_inchrome (334 posts, 28 pages).
// HOW TO REPLICATE (see REPLICATE.md): open https://www.instagram.com/<user>/ in real Chrome (logged in),
// paste STEP 1 in the console, then STEP 2 once, then call `await __one2(false)` until it says next=0.
// Save each returned text block as pages/pNNN.txt; decode with decode_pages.py.

// STEP 1: capture the page's own timeline request (template), then scroll so it fires.
if(!window.__hooked){window.__hooked=1;const O=XMLHttpRequest.prototype.open,H=XMLHttpRequest.prototype.setRequestHeader,S=XMLHttpRequest.prototype.send;
XMLHttpRequest.prototype.open=function(m,u){this.__u=u;this.__h={};return O.apply(this,arguments)};
XMLHttpRequest.prototype.setRequestHeader=function(k,v){this.__h[k]=v;return H.apply(this,arguments)};
XMLHttpRequest.prototype.send=function(b){try{if(typeof b==='string'&&b.includes('PolarisProfilePostsTabContentQuery_connection')&&!window.__tpl)window.__tpl={url:this.__u,headers:this.__h,body:b}}catch(e){}return S.apply(this,arguments)};}
for(let i=0;i<4;i++){window.scrollBy(0,1500);await new Promise(r=>setTimeout(r,2500));}
// check: !!window.__tpl must be true

// STEP 2: one page per call. Set window.__U = "<account>" first. First call: await __one2(true); then await __one2(false).
window.__D=window.__D||[];window.__DI=window.__DI||{};
window.__ix=function(n,nw){if(n==null)return '-';if(!(n in __DI)){__DI[n]=__D.length;__D.push(n);nw.push(n)}return __DI[n].toString(36)};
window.__one2=async function(first){const U=window.__U||'latterdayavenger',K='__rs_cursor_'+U;
let after=first?null:localStorage.getItem(K); if(!first&&!after)return 'ERR no cursor';
const t=window.__tpl,p=new URLSearchParams(t.body),v=JSON.parse(p.get('variables'));v.after=after;v.first=12;p.set('variables',JSON.stringify(v));
window.__n=(window.__n||0)+1; const pause=(window.__n%13===0)?20000:3000+Math.random()*4000; await new Promise(r=>setTimeout(r,pause));
window.scrollBy(0,200+Math.random()*700);
const r=await fetch(t.url,{method:'POST',headers:t.headers,body:p.toString(),credentials:'include'});let j;try{j=await r.json()}catch(e){return 'ERR status '+r.status+' not json'}
const c=j&&j.data&&j.data.xdt_api__v1__feed__user_timeline_graphql_connection; if(!c)return 'ERR stuck status '+r.status;
const re=/(?<![\w.])@([A-Za-z0-9_.]*[A-Za-z0-9_])/g,nw=[],rows=[];
for(const e of c.edges){const n=e.node;const owner=(n.user||n.owner||{}).username||null;
const col=[...new Set([...(n.coauthor_producers||[]),...(n.invited_coauthor_producers||[])].map(x=>x.username))].sort();
const cap=(n.caption&&n.caption.text)||'';const cr=[...new Set([...cap.matchAll(re)].map(m=>m[1]))].sort();
const idt=Math.round(Number((BigInt(n.pk)>>23n)+1314220021721n)/1000);
rows.push([n.code,n.taken_at,idt-n.taken_at,__ix(owner,nw),col.map(x=>__ix(x,nw)).join('.'),cr.map(x=>__ix(x,nw)).join('.')].join(','));}
const pi=c.page_info;if(pi.end_cursor)localStorage.setItem(K,pi.end_cursor);
const out='P'+window.__n+' next='+(pi.has_next_page?1:0)+'\nN '+nw.map((x,i)=>(__D.length-nw.length+i).toString(36)+'='+x).join(' ')+'\n'+rows.join('\n');
localStorage.setItem('__rs_page_'+U+'_'+window.__n,out);return out;};
// Resume after a hang/restart: redo STEP 1, then STEP 2 with window.__n set to the last saved page number,
// and rebuild __D/__DI from the saved pages' N lines (decode_pages.py --dict prints them). Then __one2(false).
