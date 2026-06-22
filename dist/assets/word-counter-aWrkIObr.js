import"./modulepreload-polyfill-B5Qt9EMX.js";const n=document.getElementById("txt"),l=document.getElementById("out");document.getElementById("y").textContent=new Date().getFullYear();function a(){const s=n.value||"",t=s.length,e=(s.trim().match(/\S+/g)||[]).length,p=(s.match(/[.!?]+/g)||[]).length,c=s.trim()?s.trim().split(/\n\s*\n/).length:0,o=s?s.split(/\r?\n/).length:0;l.innerHTML=`<div class='row'><span>Characters</span><span class='amount'>${t}</span></div>
        <div class='row'><span>Words</span><span class='amount'>${e}</span></div>
        <div class='row'><span>Sentences</span><span class='amount'>${p}</span></div>
        <div class='row'><span>Paragraphs</span><span class='amount'>${c}</span></div>
        <div class='row'><span>Lines</span><span class='amount'>${o}</span></div>`}n.addEventListener("input",a);a();
