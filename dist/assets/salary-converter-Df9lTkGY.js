import"./modulepreload-polyfill-B5Qt9EMX.js";import{a as k,$ as t}from"./utils-BBOWJhvt.js";const p=e=>new Intl.NumberFormat(void 0,{maximumFractionDigits:2}).format(e);function c(){const e=Number(t("#amount").value||0),n=t("#period").value,s=Number(t("#hoursPerDay").value||0),r=Number(t("#daysPerWeek").value||0),o=Number(t("#weeksPerYear").value||0);if(e<0||s<=0||r<=0||o<=0){t("#results").innerHTML='<div class="result-box">Enter positive working schedule values.</div>';return}const a=s*r*o,u=n==="hourly"?e*a:n==="daily"?e*r*o:n==="weekly"?e*o:n==="monthly"?e*12:e,l=a>0?u/a:0,i=l*s,m=i*r,y=u/12,d=[["Hourly",l],["Daily",i],["Weekly",m],["Monthly",y],["Annual",u]];t("#results").innerHTML=d.map(([v,h])=>`
        <div class="result-box">
          <strong>${v}</strong>
          <div style="margin-top:8px; font-size:1.2rem">${p(h)}</div>
        </div>
      `).join("")}k("input, select").forEach(e=>e.addEventListener("input",c));t("#y").textContent=new Date().getFullYear();c();
