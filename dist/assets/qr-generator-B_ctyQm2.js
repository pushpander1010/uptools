import"./modulepreload-polyfill-B5Qt9EMX.js";import"./utils-BBOWJhvt.js";const l=(t,e=document)=>e.querySelector(t),b={get(t,e=null){try{return JSON.parse(localStorage.getItem(t))??e}catch{return e}},set(t,e){try{localStorage.setItem(t,JSON.stringify(e))}catch{}}},P=({pa:t,pn:e,am:a,cu:s="INR",tn:n=""})=>`upi://pay?${new URLSearchParams({pa:t,pn:e,am:a||"",cu:s,tn:n}).toString()}`,I=({ssid:t,pass:e,sec:a="WPA",hidden:s=!1})=>`WIFI:T:${a};S:${t};P:${e};H:${s?"true":"false"};;`,U=({fn:t,org:e,tel:a,email:s,url:n})=>`BEGIN:VCARD
VERSION:3.0
FN:${t||""}
ORG:${e||""}
TEL:${a||""}
EMAIL:${s||""}
URL:${n||""}
END:VCARD`,d=l("#fields"),r=l("#mode");function f(){const t=r.value;t==="text"&&(d.innerHTML=`
          <label class="label" for="txt">Text or URL</label>
          <input id="txt" class="input" placeholder="https://example.com or any text" inputmode="text">
        `),t==="wifi"&&(d.innerHTML=`
          <div class="grid two">
            <label class="label">SSID<input aria-label="Text or URL" id="ssid" class="input" placeholder="Wi-Fi name"></label>
            <label class="label">Password<input aria-label="Text or URL" id="wpass" class="input" placeholder="••••••••"></label>
          </div>
          <div class="grid two">
            <label class="label">Security
              <select id="wsec" class="input">
                <option>WPA</option><option>WEP</option><option>nopass</option>
              </select>
            </label>
            <label class="label">Hidden?
              <select id="whid" class="input"><option value="false">No</option><option value="true">Yes</option></select>
            </label>
          </div>
        `),t==="upi"&&(d.innerHTML=`
          <div class="grid three">
            <label class="label">VPA (pa)<input aria-label="name@bank" id="pa" class="input" placeholder="name@bank"></label>
            <label class="label">Name (pn)<input aria-label="Receiver name" id="pn" class="input" placeholder="Receiver name"></label>
            <label class="label">Amount (am)<input aria-label="199.00" id="am" class="input" inputmode="decimal" placeholder="199.00"></label>
          </div>
          <div class="grid two">
            <label class="label">Currency<input aria-label="Text input" id="cu" class="input" value="INR"></label>
            <label class="label">Note (tn)<input aria-label="Payment for..." id="tn" class="input" placeholder="Payment for..."></label>
          </div>
        `),t==="vcard"&&(d.innerHTML=`
          <div class="grid three">
            <label class="label">Full name<input aria-label="Ada Lovelace" id="fn" class="input" placeholder="Ada Lovelace"></label>
            <label class="label">Org<input aria-label="UpTools" id="org" class="input" placeholder="UpTools"></label>
            <label class="label">Phone<input aria-label="+91 90000 00000" id="vtel" class="input" placeholder="+91 90000 00000"></label>
          </div>
          <div class="grid two">
            <label class="label">Email<input aria-label="you@example.com" id="vemail" class="input" placeholder="you@example.com"></label>
            <label class="label">URL<input aria-label="https://example.com" id="vurl" class="input" placeholder="https://example.com"></label>
          </div>
        `),t==="sms"&&(d.innerHTML=`
          <div class="grid two">
            <label class="label">To<input aria-label="+91 90000 00000" id="smsTo" class="input" placeholder="+91 90000 00000"></label>
            <label class="label">Message<input aria-label="Hello..." id="smsBody" class="input" placeholder="Hello..."></label>
          </div>
        `),t==="mailto"&&(d.innerHTML=`
          <div class="grid three">
            <label class="label">To<input aria-label="you@example.com" id="mto" class="input" placeholder="you@example.com"></label>
            <label class="label">Subject<input aria-label="Subject" id="msub" class="input" placeholder="Subject"></label>
            <label class="label">Body<input aria-label="Message" id="mbody" class="input" placeholder="Message"></label>
          </div>
        `)}f();r.addEventListener("change",()=>{f(),setTimeout(c,0)});function g(){const t=r.value;if(t==="text")return(l("#txt")?.value||"").trim();if(t==="wifi")return I({ssid:l("#ssid")?.value||"",pass:l("#wpass")?.value||"",sec:l("#wsec")?.value||"WPA",hidden:l("#whid")?.value==="true"});if(t==="upi")return P({pa:l("#pa")?.value||"",pn:l("#pn")?.value||"",am:l("#am")?.value||"",cu:l("#cu")?.value||"INR",tn:l("#tn")?.value||""});if(t==="vcard")return U({fn:l("#fn")?.value||"",org:l("#org")?.value||"",tel:l("#vtel")?.value||"",email:l("#vemail")?.value||"",url:l("#vurl")?.value||""});if(t==="sms"){const e=l("#smsTo")?.value||"",a=encodeURIComponent(l("#smsBody")?.value||"");return`sms:${e}?&body=${a}`}if(t==="mailto"){const e=l("#mto")?.value||"",a=encodeURIComponent(l("#msub")?.value||""),s=encodeURIComponent(l("#mbody")?.value||"");return`mailto:${e}?subject=${a}&body=${s}`}return""}const u=l("#qr-img"),m=l("#size"),h=l("#ecc"),y=l("#margin"),x=l("#fg"),L=l("#bg");function w(t,e="png"){const a=`${p(+m.value||280,120,1024)}x${p(+m.value||280,120,1024)}`,s=h.value||"M",n=p(+y.value||2,0,20),i=(x.value||"#000000").replace("#",""),S=(L.value||"#ffffff").replace("#",""),o=new URL("https://api.qrserver.com/v1/create-qr-code/");return o.searchParams.set("data",t),o.searchParams.set("size",a),o.searchParams.set("margin",String(n)),o.searchParams.set("ecc",s),o.searchParams.set("color",i),o.searchParams.set("bgcolor",S),e==="svg"&&(o.pathname="/v1/create-qr-code/"),o.toString()}function p(t,e,a){return Math.max(e,Math.min(a,t))}function c(){const t=g(),e=p(+m.value||280,120,1024);if(u.width=e,u.height=e,!t){u.src="",u.alt="Enter details to generate QR";return}const a=w(t);u.src=a,u.alt="QR code",$(t),C(t)}let T;document.addEventListener("input",t=>{t.target.closest("#qr-form")&&(clearTimeout(T),T=setTimeout(c,200))});l("#gen").addEventListener("click",c);l("#download").addEventListener("click",async()=>{const t=g();if(!t)return;const e=w(t,"png"),a=document.createElement("a");a.href=e,a.download="qrcode.png",document.body.appendChild(a),a.click(),a.remove()});l("#download-svg").addEventListener("click",async()=>{const t=g();if(!t)return;const e=w(t).replace("create-qr-code/","create-qr-code/"),s=await(await fetch(e,{headers:{Accept:"image/svg+xml"}})).blob(),n=URL.createObjectURL(s),i=document.createElement("a");i.href=n,i.download="qrcode.svg",document.body.appendChild(i),i.click(),i.remove(),setTimeout(()=>URL.revokeObjectURL(n),1500)});l("#print").addEventListener("click",()=>window.print());function C(t){const e=new URLSearchParams({m:r.value,d:t,s:String(p(+m.value||280,120,1024)),e:h.value,mg:String(p(+y.value||2,0,20)),fg:x.value,bg:L.value}),a=location.pathname+"?"+e.toString();history.replaceState(null,"",a)}l("#share").addEventListener("click",async()=>{try{await navigator.clipboard.writeText(location.href),E("Link copied")}catch{prompt("Copy link:",location.href)}});const v="qr_history_v1";function $(t){if(!t)return;const e={d:t,ts:Date.now()},a=b.get(v,[]);a.find(s=>s.d===t)||(a.unshift(e),b.set(v,a.slice(0,20)),R())}function R(){const t=l("#history");t.innerHTML="";const e=b.get(v,[]);if(!e.length){t.innerHTML='<div class="note small">No history yet.</div>';return}for(const s of e){const n=document.createElement("button");n.className="chip",n.type="button",n.textContent=s.d.length>40?s.d.slice(0,37)+"…":s.d,n.addEventListener("click",()=>{r.value=k(s.d),f(),r.value==="text"&&(l("#txt").value=s.d),c(),E("Loaded from history")}),t.appendChild(n)}const a=document.createElement("button");a.className="btn danger ghost",a.textContent="Clear history",a.style.marginTop="8px",a.onclick=()=>{b.set(v,[]),R()},t.appendChild(document.createElement("div")).appendChild(a)}function k(t){return t.startsWith("WIFI:")?"wifi":t.startsWith("upi://pay?")?"upi":t.startsWith("BEGIN:VCARD")?"vcard":t.startsWith("sms:")?"sms":t.startsWith("mailto:")?"mailto":"text"}R();(function(){const e=new URLSearchParams(location.search),a=e.get("m");a&&(r.value=a),f();const s=e.get("d");s&&r.value==="text"?setTimeout(()=>{const n=l("#txt");n&&(n.value=s,c())},0):s&&setTimeout(()=>c(),0),e.get("s")&&(m.value=e.get("s")),e.get("e")&&(h.value=e.get("e")),e.get("mg")&&(y.value=e.get("mg")),e.get("fg")&&(x.value=e.get("fg")),e.get("bg")&&(L.value=e.get("bg"))})();function E(t){let e=document.createElement("div");e.textContent=t,e.className="toast",e.style.position="fixed",e.style.bottom="14px",e.style.left="50%",e.style.transform="translateX(-50%)",e.style.padding="8px 12px",e.style.border="1px solid var(--cardBorder,#4a5568)",e.style.background="var(--card,#111)",e.style.color="var(--text,#fff)",e.style.borderRadius="10px",e.style.boxShadow="0 0 18px rgba(255,209,102,.15)",e.style.zIndex="9999",document.body.appendChild(e),setTimeout(()=>e.remove(),1400)}c();
