import"./modulepreload-polyfill-B5Qt9EMX.js";import{a as u,$ as e}from"./utils-BBOWJhvt.js";let n=null;function p(){return`Create a realistic ${e("#days").value}-day travel itinerary.

Destination: ${e("#destination").value.trim()}
Budget: ${e("#budget").value}
Pace: ${e("#pace").value}
Interests: ${e("#interests").value.trim()||"General sightseeing"}
Notes: ${e("#notes").value.trim()||"No extra notes"}

Requirements:
- Organize by day with morning, afternoon and evening.
- Keep recommendations practical and geographically sensible.
- Mention one signature food or local experience per day when appropriate.
- Include one short budget tip and one transport tip near the end.
- Avoid claiming live prices or opening hours.
- Output in clean markdown with headings and bullet points.`}async function g(){if(!e("#destination").value.trim()){e("#status").textContent="Add a destination first.",e("#destination").focus();return}e("#output").textContent="",e("#status").textContent="Generating...",e("#generateBtn").disabled=!0,e("#stopBtn").disabled=!1,n=new AbortController;try{const t=await fetch("/ai",{method:"POST",signal:n.signal,headers:{"Content-Type":"application/json"},body:JSON.stringify({stream:!0,temperature:.7,messages:[{role:"system",content:"You are a pragmatic travel planner who creates realistic itineraries."},{role:"user",content:p()}]})});if(!t.ok)throw new Error(`HTTP ${t.status}`);const o=t.body.getReader(),s=new TextDecoder;for(;;){const{value:d,done:l}=await o.read();if(l)break;for(const c of s.decode(d).split(`
`)){const a=c.trim();if(!a.startsWith("data:"))continue;const r=a.slice(5).trim();if(r==="[DONE]")break;try{const i=JSON.parse(r).choices?.[0]?.delta?.content||"";i&&(e("#output").textContent+=i)}catch{}}}e("#status").textContent="Done."}catch(t){e("#status").textContent=t.name==="AbortError"?"Stopped.":`Error: ${t.message}`}finally{e("#generateBtn").disabled=!1,e("#stopBtn").disabled=!0,n=null}}u(".preset").forEach(t=>t.addEventListener("click",()=>{e("#destination").value=t.dataset.destination||"",e("#interests").value=t.dataset.interests||"",e("#notes").value=t.dataset.notes||""}));e("#generateBtn").addEventListener("click",g);e("#stopBtn").addEventListener("click",()=>n?.abort());e("#copyBtn").addEventListener("click",async()=>{const t=e("#output").textContent.trim();!t||t==="Your itinerary will appear here."||(await navigator.clipboard.writeText(t),e("#status").textContent="Copied.")});e("#y").textContent=new Date().getFullYear();
