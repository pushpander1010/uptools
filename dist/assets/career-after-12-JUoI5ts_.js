import"./modulepreload-polyfill-B5Qt9EMX.js";import{s as n,$ as a}from"./utils-BBOWJhvt.js";n(a("#y"),new Date().getFullYear());const r=[{name:"Engineering",icon:"⚙️",desc:"Build the future with technology and innovation",courses:["B.Tech","B.E.","Diploma"],exams:["JEE Main","JEE Advanced","BITSAT"],careers:["Software Engineer","Civil Engineer","Mechanical Engineer","Electrical Engineer"],duration:"4 years"},{name:"Medical",icon:"🏥",desc:"Pursue a career in healthcare and medicine",courses:["MBBS","BDS","B.Pharma","Nursing"],exams:["NEET","AIIMS","JIPMER"],careers:["Doctor","Surgeon","Dentist","Pharmacist","Nurse"],duration:"5.5 years (MBBS)"},{name:"Commerce",icon:"💰",desc:"Master business, finance, and economics",courses:["B.Com","B.B.A.","CA","CS"],exams:["CA Foundation","CUET UG","college-specific admissions"],careers:["Chartered Accountant","Business Analyst","Entrepreneur","Financial Advisor"],duration:"3-4.5 years"},{name:"Arts/Humanities",icon:"📚",desc:"Explore culture, history, and social sciences",courses:["B.A.","B.A. (Hons)","Journalism","Psychology"],exams:["Various entrance exams","UPSC (for civil services)"],careers:["Journalist","Psychologist","Historian","Civil Servant","Teacher"],duration:"3 years"},{name:"Law",icon:"⚖️",desc:"Study law and pursue a legal career",courses:["B.A. LLB","B.Sc. LLB","B.Com. LLB"],exams:["CLAT","AILET","LSAT"],careers:["Advocate","Judge","Legal Consultant","Corporate Lawyer"],duration:"5 years"},{name:"Science",icon:"🔬",desc:"Pursue research and scientific innovation",courses:["B.Sc.","B.Sc. (Hons)","Integrated M.Sc."],exams:["Various entrance exams","CSIR NET"],careers:["Scientist","Researcher","Professor","Lab Technician"],duration:"3-5 years"}];function t(){const s=r.map((e,i)=>`
        <div class="stream-card" onclick="toggleDetails(${i})">
          <div class="stream-icon">${e.icon}</div>
          <h3 class="stream-title">${e.name}</h3>
          <p class="stream-desc">${e.desc}</p>
          <div class="stream-details" id="details-${i}">
            <div class="detail-item"><strong>Courses:</strong> ${e.courses.join(", ")}</div>
            <div class="detail-item"><strong>Entrance Exams:</strong> ${e.exams.join(", ")}</div>
            <div class="detail-item"><strong>Career Options:</strong> ${e.careers.join(", ")}</div>
            <div class="detail-item"><strong>Duration:</strong> ${e.duration}</div>
          </div>
        </div>
      `).join("");a("#streamsContainer").innerHTML=s}window.toggleDetails=function(s){a(`#details-${s}`).classList.toggle("active")};t();
