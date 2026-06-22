import"./modulepreload-polyfill-B5Qt9EMX.js";import{a as c,$ as n}from"./utils-BBOWJhvt.js";const e=t=>new Intl.NumberFormat(void 0,{maximumFractionDigits:2}).format(t);function a(){const t=Number(n("#cost").value||0),r=Number(n("#sale").value||0),o=Number(n("#targetMargin").value||0);if(t<0||r<=0){n("#result").textContent="Enter a cost of zero or more and a selling price above zero.";return}const s=r-t,l=t===0?0:s/t*100,m=r===0?0:s/r*100,i=o>=100||1-o/100<=0?1/0:t/(1-o/100);n("#result").innerHTML=`
        <div><strong>Gross profit:</strong> ${e(s)}</div>
        <div class="note small" style="margin-top:6px"><strong>Markup:</strong> ${e(l)}%</div>
        <div class="note small" style="margin-top:4px"><strong>Margin:</strong> ${e(m)}%</div>
        <div class="note small" style="margin-top:8px"><strong>Price needed for ${e(o)}% margin:</strong> ${Number.isFinite(i)?e(i):"Not possible"}</div>
      `}c("input").forEach(t=>t.addEventListener("input",a));n("#y").textContent=new Date().getFullYear();a();
