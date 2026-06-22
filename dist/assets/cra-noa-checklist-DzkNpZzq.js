import"./modulepreload-polyfill-B5Qt9EMX.js";import{$ as c,p as l,r as a}from"./utils-BBOWJhvt.js";const m=c("#list"),h=c("#reset"),s="uptools:cra-noa:checklist",r=["Notice of Assessment (NOA)","T4 / T4A slips","RRSP contribution receipts","Tuition/T2202 slips","Medical expense receipts","Charitable donation receipts","Investment income slips (T5/T3)","Rent or property tax receipts (if applicable)","Business income/expense records (if self-employed)"];function p(){const d=a(s,{});m.innerHTML=r.map((i,n)=>{const e=`chk-${n}`,t=d[e]?"checked":"";return`
          <label class="check" style="display:flex;gap:.5rem;align-items:center;padding:.35rem 0;">
            <input aria-label="Checkbox" type="checkbox" id="${e}" ${t}>
            <span>${i}</span>
          </label>
        `}).join(""),r.forEach((i,n)=>{const e=`chk-${n}`,t=document.getElementById(e);t.addEventListener("change",()=>{const o=a(s,{});o[e]=t.checked,l(s,o)})})}h.addEventListener("click",()=>{l(s,{}),p()});p();c("#y").textContent=new Date().getFullYear();
