import"./modulepreload-polyfill-B5Qt9EMX.js";import"./utils.js_v_1.3-l0sNRNKZ.js";const l={business:[{title:"New Product Launch",text:`🚀 Exciting news!

We're launching something amazing today. Can you guess what it is?

👆 Swipe up to find out!`},{title:"Behind the Scenes",text:`👀 Behind the scenes

This is how we make the magic happen. Hard work pays off!

💪 #TeamWork`},{title:"Customer Testimonial",text:`💬 What our customers say:

"This changed everything for my business!"

⭐ Thank you for trusting us!`},{title:"Team Spotlight",text:`🌟 Team Spotlight

Meet Sarah, our amazing designer! She's the creative genius behind our visuals.

👏 #TeamAppreciation`},{title:"Company Milestone",text:`🎉 Milestone Alert!

We just hit 10K followers! Thank you for being part of our journey.

❤️ #Grateful`}],personal:[{title:"Good Morning",text:`☀️ Good morning!

Starting the day with gratitude and positive vibes. What are you grateful for today?

✨ #GoodVibes`},{title:"Weekend Plans",text:`🎉 Weekend vibes!

Planning to relax, recharge, and spend time with loved ones. What about you?

💕 #WeekendMood`},{title:"Daily Motivation",text:`💪 Daily reminder:

You are stronger than you think. Keep pushing forward!

🌟 #Motivation`},{title:"Favorite Things",text:`❤️ Current favorites:

☕ Morning coffee
📚 Good books
🎵 Chill music

What are yours?`},{title:"Life Update",text:`📱 Life update:

Trying new things, learning every day, and enjoying the journey!

✨ #Growth`}],promotional:[{title:"Flash Sale",text:`⚡ FLASH SALE ALERT!

50% OFF everything for the next 24 hours only!

🛒 Shop now before it's gone!`},{title:"Limited Offer",text:`🔥 LIMITED TIME OFFER

Get 2 for the price of 1! Only 48 hours left.

⏰ Don't miss out!`},{title:"New Collection",text:`✨ NEW COLLECTION DROP

Fresh designs, premium quality, unbeatable prices.

👆 Swipe up to shop!`},{title:"Exclusive Deal",text:`🎁 EXCLUSIVE FOR YOU

Special discount just for our story viewers!

💫 Use code: STORY20`},{title:"Last Chance",text:`⏰ LAST CHANCE!

Sale ends in 6 hours. Don't let this opportunity slip away!

🏃‍♀️ Hurry up!`}],interactive:[{title:"This or That",text:`🤔 This or That?

Coffee ☕ or Tea 🍵
Books 📚 or Movies 🎬
Beach 🏖️ or Mountains 🏔️

Vote in our poll!`},{title:"Ask Me Anything",text:`❓ ASK ME ANYTHING

I'm here to answer your questions! Drop them below.

💬 Let's chat!`},{title:"Rate My Outfit",text:`👗 Rate my outfit!

On a scale of 1-10, how would you rate today's look?

⭐ Use the slider!`},{title:"Guess the Location",text:`📍 Guess where I am!

Hint: It's somewhere tropical and beautiful!

🌴 Drop your guesses below!`},{title:"Would You Rather",text:`🤷‍♀️ Would you rather...

Travel to the past or future?
Have the ability to fly or be invisible?

🗳️ Vote now!`}],quotes:[{title:"Motivational Quote",text:`✨ Monday Motivation

"The only way to do great work is to love what you do."

- Steve Jobs

💪 #Motivation`},{title:"Inspirational Quote",text:`🌟 Daily Inspiration

"Believe you can and you're halfway there."

- Theodore Roosevelt

🚀 #Inspiration`},{title:"Success Quote",text:`🎯 Success Mindset

"Success is not final, failure is not fatal: it is the courage to continue that counts."

- Winston Churchill`},{title:"Life Quote",text:`🌈 Life Wisdom

"Life is 10% what happens to you and 90% how you react to it."

- Charles R. Swindoll`},{title:"Dream Quote",text:`💫 Dream Big

"The future belongs to those who believe in the beauty of their dreams."

- Eleanor Roosevelt`}],"behind-scenes":[{title:"Morning Routine",text:`🌅 Morning routine:

6 AM - Wake up
6:30 AM - Workout
7:30 AM - Healthy breakfast
8 AM - Ready to conquer the day!

💪 #MorningVibes`},{title:"Workspace Tour",text:`🏢 Workspace Wednesday

Take a peek at where the magic happens! Clean desk, good vibes, and lots of coffee.

☕ #WorkspaceGoals`},{title:"Creative Process",text:`🎨 Creative process:

1. Brainstorm ideas
2. Sketch concepts
3. Refine and perfect
4. Share with the world!

✨ #CreativeLife`},{title:"Day in the Life",text:`📱 Day in my life:

Morning coffee → Work sessions → Lunch break → More creativity → Evening wind down

🌙 #DayInTheLife`},{title:"Making Process",text:`👀 How it's made:

From concept to creation, here's the journey of our latest project!

🛠️ #BehindTheScenes`}]},c=document.getElementById("templateGrid"),i=document.getElementById("storyText"),d=document.getElementById("storyPreview");let s="business";function h(){u(s),m(),w(),a()}function m(){i.addEventListener("input",a),document.querySelectorAll(".template-category").forEach(e=>{e.addEventListener("click",t=>{y(t.target),s=t.target.dataset.category,u(s)})}),document.getElementById("copyTextBtn").addEventListener("click",v),document.getElementById("clearTextBtn").addEventListener("click",x),document.getElementById("randomTemplateBtn").addEventListener("click",T),c.addEventListener("click",e=>{const t=e.target.closest(".template-card");t&&g(t)}),document.querySelectorAll(".element-btn").forEach(e=>{e.addEventListener("click",t=>{p(t.currentTarget)})})}function u(e){const t=l[e]||[];c.innerHTML=t.map((n,o)=>`<div class="template-card" data-template="${n.text}" data-title="${n.title}">
          <div class="story-mini">
            <div class="story-mini-content">
              ${n.title}
            </div>
          </div>
          <div style="font-size: 0.8rem; font-weight: 600; margin-top: .5rem">${n.title}</div>
          <div style="font-size: 0.7rem; color: var(--muted); margin-top: .25rem">${n.text.substring(0,50)}...</div>
        </div>`).join("")}function y(e){document.querySelectorAll(".template-category").forEach(t=>{t.classList.remove("active")}),e.classList.add("active")}function g(e){const t=e.dataset.template;i.value=t,a(),document.querySelectorAll(".template-card").forEach(n=>{n.classList.remove("selected")}),e.classList.add("selected")}function p(e){e.classList.toggle("active");const t=e.dataset.element;e.classList.contains("active")&&f(t)}function f(e){const n={poll:`

📊 Add a poll: 'Which do you prefer?'`,question:`

❓ Ask your audience: 'What questions do you have?'`,quiz:`

🧠 Quiz time: 'Can you guess the answer?'`,slider:`

📏 Rate this from 1-10!`,countdown:`

⏰ Countdown to something exciting!`,location:`

📍 Tag your location`,mention:`

@ Mention relevant accounts`,hashtag:`

# Add relevant hashtags`}[e];n&&!i.value.includes(n)&&(i.value+=n,a())}function a(){const e=i.value||"Your story text will appear here...";d.textContent=e}async function v(){const e=i.value;if(!e){alert("Please select a template or write some text first!");return}try{await navigator.clipboard.writeText(e),r()}catch{try{const n=document.createElement("textarea");n.value=e,document.body.appendChild(n),n.select(),document.execCommand("copy"),document.body.removeChild(n),r()}catch{alert("Failed to copy. Please copy manually from the text area.")}}}function r(){const e=document.getElementById("copyTextBtn"),t=e.textContent;e.textContent="✅ Copied!",e.style.background="#4CAF50",setTimeout(()=>{e.textContent=t,e.style.background=""},2e3)}function x(){i.value="",a(),document.querySelectorAll(".template-card").forEach(e=>{e.classList.remove("selected")}),document.querySelectorAll(".element-btn").forEach(e=>{e.classList.remove("active")})}function T(){const e=Object.values(l).flat(),t=e[Math.floor(Math.random()*e.length)];i.value=t.text,a()}function w(){const e=document.querySelector(".mobile-menu-toggle"),t=document.querySelector(".nav-links");e&&t&&(e.addEventListener("click",()=>{const n=t.classList.contains("active");t.classList.toggle("active"),e.setAttribute("aria-expanded",!n);const o=e.querySelector(".menu-icon");o&&(o.textContent=n?"☰":"✕")}),t.querySelectorAll("a").forEach(n=>{n.addEventListener("click",()=>{t.classList.remove("active"),e.setAttribute("aria-expanded","false");const o=e.querySelector(".menu-icon");o&&(o.textContent="☰")})}),document.addEventListener("click",n=>{if(!e.contains(n.target)&&!t.contains(n.target)){t.classList.remove("active"),e.setAttribute("aria-expanded","false");const o=e.querySelector(".menu-icon");o&&(o.textContent="☰")}}))}document.getElementById("y").textContent=new Date().getFullYear();document.addEventListener("DOMContentLoaded",()=>{h()});
