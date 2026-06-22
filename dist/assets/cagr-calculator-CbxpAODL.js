import"./modulepreload-polyfill-B5Qt9EMX.js";import{a as u,$ as e}from"./utils-BBOWJhvt.js";const n=(t,a=2)=>new Intl.NumberFormat(void 0,{maximumFractionDigits:a}).format(t);function l(){const t=Number(e("#startValue").value||0),a=Number(e("#endValue").value||0),r=Number(e("#years").value||0),o=Number(e("#decimals").value||2);if(t<=0||a<0||r<=0){e("#result").textContent="Enter a starting value above zero, a non-negative ending value and a period greater than zero.";return}const s=Math.pow(a/t,1/r)-1,i=(a-t)/t*100;e("#result").innerHTML=`
        <div><strong>CAGR:</strong> ${n(s*100,o)}%</div>
        <div class="note small" style="margin-top:8px">Total growth over ${n(r,2)} years: ${n(i,o)}%</div>
        <div class="note small" style="margin-top:4px">Equivalent multiplier: ${n(a/t,4)}x</div>
      `}u("input, select").forEach(t=>t.addEventListener("input",l));e("#y").textContent=new Date().getFullYear();l();
