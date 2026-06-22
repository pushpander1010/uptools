import"./modulepreload-polyfill-B5Qt9EMX.js";import{s as d,$ as e}from"./utils-BBOWJhvt.js";d(e("#y"),new Date().getFullYear());const l=[{rank:1,name:"Indian Institute of Technology Delhi",location:"Delhi",category:"engineering",state:"delhi"},{rank:2,name:"Indian Institute of Technology Bombay",location:"Mumbai",category:"engineering",state:"maharashtra"},{rank:3,name:"Indian Institute of Technology Madras",location:"Chennai",category:"engineering",state:"tamil-nadu"},{rank:4,name:"All India Institute of Medical Sciences Delhi",location:"Delhi",category:"medical",state:"delhi"},{rank:5,name:"Delhi University",location:"Delhi",category:"arts",state:"delhi"},{rank:6,name:"Mumbai University",location:"Mumbai",category:"commerce",state:"maharashtra"},{rank:7,name:"National Law School of India",location:"Bangalore",category:"law",state:"karnataka"},{rank:8,name:"Indian Institute of Technology Kanpur",location:"Kanpur",category:"engineering",state:"uttar-pradesh"}];function i(t=l){const n=t.map(a=>`
        <div class="college-card">
          <div class="college-header">
            <div class="college-rank">#${a.rank}</div>
            <div>
              <h3 class="college-name">${a.name}</h3>
              <p class="college-location">📍 ${a.location}</p>
            </div>
          </div>
          <div>
            <span class="college-category">${a.category.charAt(0).toUpperCase()+a.category.slice(1)}</span>
          </div>
        </div>
      `).join("");e("#collegesList").innerHTML=n||'<p class="muted">No colleges found matching your filters.</p>'}function h(){const t=e("#categoryFilter").value,n=e("#stateFilter").value,a=e("#searchFilter").value.toLowerCase(),r=l.filter(o=>{const c=!t||o.category===t,s=!n||o.state===n,g=!a||o.name.toLowerCase().includes(a);return c&&s&&g});i(r)}e("#filterBtn").addEventListener("click",h);e("#resetFilterBtn").addEventListener("click",()=>{e("#categoryFilter").value="",e("#stateFilter").value="",e("#searchFilter").value="",i()});i();
