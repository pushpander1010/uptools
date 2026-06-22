import"./modulepreload-polyfill-B5Qt9EMX.js";import{a as u,$ as e}from"./utils-BBOWJhvt.js";let r=null;function p(){return`Create 12 LinkedIn headline options.

Role: ${e("#role").value.trim()||"Professional"}
Tone: ${e("#tone").value}
Keywords: ${e("#keywords").value.trim()||"Not specified"}
Target audience: ${e("#goal").value.trim()||"General recruiters and clients"}
Background: ${e("#about").value.trim()||"No extra background provided"}

Requirements:
- Keep each headline under 220 characters.
- Make them sound credible, modern and useful for search discovery.
- Vary between recruiter-friendly, client-facing and authority-building angles.
- Output as a numbered list only.
- Do not use emoji.
- Avoid generic hype like ninja, guru, rockstar, best-in-class.`}async function f(){if(!e("#role").value.trim()){e("#status").textContent="Add a role first.",e("#role").focus();return}e("#output").textContent="",e("#status").textContent="Generating...",e("#generateBtn").disabled=!0,e("#stopBtn").disabled=!1,r=new AbortController;try{const t=await fetch("/ai",{method:"POST",signal:r.signal,headers:{"Content-Type":"application/json"},body:JSON.stringify({stream:!0,temperature:.7,messages:[{role:"system",content:"You write concise, high-quality LinkedIn profile headlines."},{role:"user",content:p()}]})});if(!t.ok)throw new Error(`HTTP ${t.status}`);const s=t.body.getReader(),i=new TextDecoder;for(;;){const{value:l,done:d}=await s.read();if(d)break;for(const c of i.decode(l).split(`
`)){const n=c.trim();if(!n.startsWith("data:"))continue;const a=n.slice(5).trim();if(a==="[DONE]")break;try{const o=JSON.parse(a).choices?.[0]?.delta?.content||"";o&&(e("#output").textContent+=o)}catch{}}}e("#status").textContent="Done."}catch(t){e("#status").textContent=t.name==="AbortError"?"Stopped.":`Error: ${t.message}`}finally{e("#generateBtn").disabled=!1,e("#stopBtn").disabled=!0,r=null}}u(".preset").forEach(t=>t.addEventListener("click",()=>{e("#role").value=t.dataset.role||"",e("#keywords").value=t.dataset.keywords||"",e("#goal").value=t.dataset.goal||""}));e("#generateBtn").addEventListener("click",f);e("#stopBtn").addEventListener("click",()=>r?.abort());e("#copyBtn").addEventListener("click",async()=>{const t=e("#output").textContent.trim();!t||t==="Your headline options will appear here."||(await navigator.clipboard.writeText(t),e("#status").textContent="Copied.")});e("#y").textContent=new Date().getFullYear();
