import"./modulepreload-polyfill-B5Qt9EMX.js";const d=(t,e=document)=>e.querySelector(t),u="https://pokeapi.co/api/v2",w=72,L=d("#search"),y=d("#list"),P=d("#status"),S=d("#count"),C=d("#details"),j=d("#loadMore"),v=d("#exportCsv"),E=d("#y");E&&(E.textContent=new Date().getFullYear());let c=[],h=[],$=w;const m=new Map,_=t=>t.charAt(0).toUpperCase()+t.slice(1),f=t=>t==null?"N/A":String(t);function l(t){P.textContent=t}function k(){y.innerHTML="";const t=h.slice(0,$);t.forEach(e=>{const s=document.createElement("button");s.type="button",s.className="poke-btn",s.textContent=_(e.name),s.addEventListener("click",()=>R(e.name)),y.appendChild(s)}),S.textContent=`Showing ${t.length} of ${h.length} Pokemon`,j.disabled=t.length>=h.length}function M(){const t=L.value.trim().toLowerCase();t?h=c.filter(e=>e.name.includes(t)):h=[...c],$=w,k()}function p(t,e,s=255){const i=Math.min(100,Math.round(e/s*100));return`
        <div class="stat-row">
          <div class="mini">${t}</div>
          <div class="bar"><span style="width:${i}%"></span></div>
          <div class="mini">${e}</div>
        </div>
      `}function x(t){const e=t.types.map(n=>`<span class="chip">${n.type.name}</span>`).join(""),s=t.abilities.map(n=>n.ability.name).join(", "),i={};t.stats.forEach(n=>{i[n.stat.name]=n.base_stat}),C.innerHTML=`
        <div class="poke-card">
          <div class="sprite">
            <img src="${t.sprites?.front_default||""}" alt="${t.name}" width="80" height="80" />
          </div>
          <div>
            <div style="font-weight:700">${_(t.name)} <span class="mini muted">#${t.id}</span></div>
            <div class="mini">Height: ${f(t.height)} | Weight: ${f(t.weight)}</div>
            <div class="mini">Base Exp: ${f(t.base_experience)}</div>
          </div>
        </div>
        <div>
          <div class="mini muted">Types</div>
          <div class="row-inline" style="gap:6px;flex-wrap:wrap">${e}</div>
        </div>
        <div>
          <div class="mini muted">Abilities</div>
          <div class="mini">${s||"N/A"}</div>
        </div>
        <div class="stats">
          ${p("HP",i.hp||0)}
          ${p("Attack",i.attack||0)}
          ${p("Defense",i.defense||0)}
          ${p("Sp. Atk",i["special-attack"]||0)}
          ${p("Sp. Def",i["special-defense"]||0)}
          ${p("Speed",i.speed||0)}
        </div>
      `}async function R(t){if(m.has(t)){x(m.get(t));return}l(`Loading ${t}...`);try{const e=await fetch(`${u}/pokemon/${t}`);if(!e.ok)throw new Error("Failed to fetch");const s=await e.json();m.set(t,s),x(s),l("Ready.")}catch{l("Failed to load Pokemon details.")}}async function T(){l("Fetching Pokemon list..."),c=(await(await fetch(`${u}/pokemon?limit=2000`)).json()).results||[],h=[...c],l(`Loaded ${c.length} Pokemon.`),k()}async function D(){if(!c.length)return;v.disabled=!0,l("Exporting all stats. This can take a few minutes...");const t=[["id","name","type_1","type_2","hp","attack","defense","special_attack","special_defense","speed","height","weight","base_experience","abilities"].join(",")];let e=0;for(const n of c)try{const b=await fetch(`${u}/pokemon/${n.name}`);if(!b.ok)throw new Error("fetch");const a=await b.json(),g=a.types.map(o=>o.type.name),r={};a.stats.forEach(o=>{r[o.stat.name]=o.base_stat});const A=a.abilities.map(o=>o.ability.name).join("|");t.push([a.id,a.name,g[0]||"",g[1]||"",r.hp||0,r.attack||0,r.defense||0,r["special-attack"]||0,r["special-defense"]||0,r.speed||0,a.height||0,a.weight||0,a.base_experience||0,A].join(",")),e+=1,e%25===0&&l(`Exporting... ${e} / ${c.length}`),await new Promise(o=>setTimeout(o,80))}catch{continue}const s=new Blob([t.join(`
`)],{type:"text/csv"}),i=document.createElement("a");i.href=URL.createObjectURL(s),i.download="pokemon-stats.csv",i.click(),URL.revokeObjectURL(i.href),l("Export complete."),v.disabled=!1}L.addEventListener("input",()=>{M()});j.addEventListener("click",()=>{$+=w,k()});v.addEventListener("click",()=>{D()});T();
