import"./modulepreload-polyfill-B5Qt9EMX.js";import{_ as L}from"./preload-helper-BXl3LOEh.js";let y={};try{const e=await L(()=>import("./utils-BBOWJhvt.js").then(t=>t.U),[]);y=e?.default||e||{}}catch{y=window.Utils||{}}const a=e=>document.getElementById(e),o=a("input"),l=a("status"),c=a("output");a("runBtn");const b=a("stopBtn"),k=a("charCount"),E=a("pasteBtn"),T=a("clearBtn"),R=a("fileIn");a("saveCfg");const S=a("permBtn"),O=a("copyBtn"),$=a("downloadBtn"),p=a("task"),D=a("taskOptions");a("y").textContent=new Date().getFullYear();const d=()=>{k.textContent=o.value.length.toLocaleString()};o.addEventListener("input",d);d();E.addEventListener("click",async()=>{try{o.value=await navigator.clipboard.readText(),d()}catch{i("Clipboard blocked by browser")}});T.addEventListener("click",()=>{o.value="",d(),o.focus()});R.addEventListener("change",async e=>{const t=e.target.files?.[0];if(!t)return;const n=await t.text();o.value=n,d()});function w(){const e=p.value;let t="";e==="summarize"?t=`
          <label class="inline"><span class="tiny-note">Style</span>
            <select id="optStyle" class="select">
              <option value="brief">Brief</option>
              <option value="bullets">Bulleted</option>
              <option value="detailed">Detailed</option>
            </select>
          </label>
          <label class="inline"><span class="tiny-note">Max words</span>
            <input aria-label="Style" id="optLen" type="number" class="input small" value="180" min="50" max="1000" style="width:100px">
          </label>`:e==="rewrite"?t=`
          <label class="inline"><span class="tiny-note">Tone</span>
            <select id="optTone" class="select">
              <option>Neutral</option><option>Friendly</option><option>Formal</option>
              <option>Academic</option><option>Sales</option><option>Playful</option>
            </select>
          </label>
          <label class="inline"><span class="tiny-note">Constraints</span>
            <input aria-label="Tone" id="optRules" class="input small" placeholder="e.g. shorter, active voice, no jargon" style="width:240px">
          </label>`:e==="translate"?t=`
          <label class="inline"><span class="tiny-note">Language</span>
            <input aria-label="Constraints" id="optLang" class="input small" value="Hindi" style="width:160px">
          </label>`:e==="keywords"?t=`
          <label class="inline"><span class="tiny-note">Top N</span>
            <input aria-label="Language" id="optTopN" type="number" class="input small" value="15" min="5" max="50" style="width:90px">
          </label>
          <label class="inline"><span class="tiny-note">Include phrases</span>
            <select id="optPhrases" class="select"><option>Yes</option><option>No</option></select>
          </label>`:e==="outline"?t=`
          <label class="inline"><span class="tiny-note">Depth</span>
            <select id="optDepth" class="select"><option value="2">H2 + H3</option><option value="3">H2 + H3 + H4</option></select>
          </label>`:e==="seometa"&&(t=`
          <label class="inline"><span class="tiny-note">Site/Brand</span>
            <input aria-label="Depth" id="optBrand" class="input small" value="UpTools" style="width:160px">
          </label>`),D.innerHTML=t}p.addEventListener("change",w);w();function U(e,t){const n=h=>document.getElementById(h)?.value;return e==="summarize"?`You are a precise summarizer. Style: ${n("optStyle")}. Max words: ${n("optLen")||180}. Use clear language.

---
${t}`:e==="rewrite"?`Rewrite the text in a ${n("optTone")||"Neutral"} tone. Constraints: ${n("optRules")||"keep meaning, increase clarity"}. Return only the rewritten text.

---
${t}`:e==="translate"?`Translate the text into ${n("optLang")||"Hindi"}. Maintain meaning and proper nouns. Return only the translation.

---
${t}`:e==="keywords"?`Extract top ${n("optTopN")||15} keywords from the text${(n("optPhrases")||"Yes")==="Yes"?" including keyphrases":""}. Return a comma-separated list.

---
${t}`:e==="outline"?`Create a blog outline with depth level ${n("optDepth")||2}. Use markdown headings. Include a short intro and conclusion.

---
${t}`:e==="seometa"?`From the text, generate:
- SEO Title (<= 60 chars)
- Meta Description (<= 155 chars)
- 10 Keywords
Brand: ${n("optBrand")||"UpTools"}
Return as:
Title: ...
Description: ...
Keywords: ...

---
${t}`:t}const I="together",N="mistralai/Mistral-Small-24B-Instruct-2501";let s=null;async function P({prompt:e}){const t={provider:I,model:N,stream:!0,temperature:.4,messages:[{role:"system",content:"You are a helpful, concise writing assistant."},{role:"user",content:e}]};s=new AbortController;const n=await fetch("/ai",{method:"POST",signal:s.signal,headers:{"Content-Type":"application/json"},body:JSON.stringify(t)});if(!n.ok)throw new Error(`HTTP ${n.status}`);const h=n.body.getReader(),v=new TextDecoder;let u="";for(;;){const{value:g,done:x}=await h.read();if(x)break;const C=v.decode(g);for(const B of C.split(`
`)){const m=B.trim();if(!m||!m.startsWith("data:"))continue;const r=m.slice(5).trim();if(r==="[DONE]")return s=null,u;try{const f=JSON.parse(r).choices?.[0]?.delta?.content??"";f&&(u+=f,c.textContent+=f)}catch{r&&r!=="[DONE]"&&(u+=r+`
`,c.textContent+=r+`
`)}}}return s=null,u}a("stopBtn").addEventListener("click",()=>{s&&(s.abort(),s=null,b.disabled=!0,l.textContent="Stopped.")});a("runBtn").addEventListener("click",async()=>{const e=o.value.trim(),t=p.value;if(!e){i("Enter some text first"),o.focus();return}c.textContent="",b.disabled=!1,l.textContent="Running…";try{const n=U(t,e);await P({prompt:n}),l.textContent="Done."}catch{l.textContent="Error. Check console & settings.",i("Request failed.")}finally{b.disabled=!0}});O.addEventListener("click",async()=>{try{await navigator.clipboard.writeText(c.textContent||""),i("Copied")}catch{i("Copy blocked by browser")}});$.addEventListener("click",()=>{const e=new Blob([c.textContent||""],{type:"text/plain;charset=utf-8"}),t=document.createElement("a");t.href=URL.createObjectURL(e),t.download="ai-output.txt",t.click(),URL.revokeObjectURL(t.href)});S.addEventListener("click",async()=>{const e={t:p.value},t=new URL(location.href);t.hash=encodeURIComponent(btoa(JSON.stringify(e)));try{await navigator.clipboard.writeText(t.toString()),i("Permalink copied")}catch{i("Permalink ready (open address bar)"),history.replaceState({},"",t)}});function i(e){if(typeof y?.toast=="function")return y.toast(e);l.textContent=e,setTimeout(()=>{l.textContent===e&&(l.textContent="")},1800)}(function(){if(location.hash)try{const t=JSON.parse(atob(decodeURIComponent(location.hash.slice(1))));t?.t&&(p.value=t.t),w()}catch{}})();
