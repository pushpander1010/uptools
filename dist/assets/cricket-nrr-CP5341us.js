import"./modulepreload-polyfill-B5Qt9EMX.js";import"./utils-BBOWJhvt.js";const r=e=>document.getElementById(e),u=r("ourRuns"),R=r("ourOvers"),v=r("oppRuns"),c=r("tableBody"),i=r("summary");r("yr").textContent=new Date().getFullYear();let n=[];function w(e){return Math.floor(e/6)+e%6/10}function h(){const e=parseInt(u.value)||0;let a=parseFloat(R.value)||0;const o=parseInt(v.value)||0;if(e<=0||a<=0||o<0){alert("Enter valid match values");return}const d=e/a,l=o/20,p=d-l;n.push({ourRuns:e,ourOvers:a,oppRuns:o,ourRR:d,oppRR:l,nrr:p}),g()}function g(){if(!n.length){c.innerHTML='<tr><td colspan="5" class="note">Add matches above to calculate NRR</td></tr>',i.innerHTML="";return}let e=n.map((s,t)=>{const O=s.nrr>=0?"pos":"neg";return`<tr>
          <td class="pos">${t+1}</td>
          <td>${s.ourRuns} / ${w(s.ourOvers*6)} ov vs ${s.oppRuns}</td>
          <td>${s.ourRR.toFixed(2)}</td>
          <td>${s.oppRR.toFixed(2)}</td>
          <td class="nrr ${O}">${s.nrr>=0?"+":""}${s.nrr.toFixed(2)}</td>
        </tr>`}).join("");c.innerHTML=e;const a=n.reduce((s,t)=>s+t.nrr,0)/n.length,o=n.reduce((s,t)=>s+t.ourRR,0)/n.length,d=n.reduce((s,t)=>s+t.oppRR,0)/n.length,l=n.reduce((s,t)=>s+t.ourRuns,0),p=n.reduce((s,t)=>s+t.ourOvers,0),$=n.reduce((s,t)=>s+t.oppRuns,0);i.innerHTML=`
        <div class="row"><span>Matches Played</span><span class="highlight">${n.length}</span></div>
        <div class="row"><span>Total Runs Scored</span><span class="highlight">${l}</span></div>
        <div class="row"><span>Overs Used</span><span class="highlight">${p.toFixed(1)}</span></div>
        <div class="row"><span>Runs Conceded</span><span class="highlight">${$}</span></div>
        <div class="row"><span>Average Run Rate</span><span class="highlight">${o.toFixed(2)}</span></div>
        <div class="row"><span>Opposition Avg RR</span><span class="highlight">${d.toFixed(2)}</span></div>
        <div class="row"><span>NET RUN RATE</span><span class="highlight ${a>=0?"pos":"neg"}" style="font-size:1.3rem">${a>=0?"+":""}${a.toFixed(3)}</span></div>
      `}r("addBtn").addEventListener("click",h);r("clearBtn").addEventListener("click",()=>{n=[],g()});[u,R,v].forEach(e=>e.addEventListener("keydown",a=>{a.key==="Enter"&&h()}));
