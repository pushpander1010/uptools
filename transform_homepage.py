#!/usr/bin/env python3
"""Transform uptools homepage with new dark glassmorphism design."""
import re

with open('/Users/pushpanderkumar/websites/uptools/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print(f"Original: {len(html)} chars")

# ========== 1. ADD TAILWIND CDN + INTER FONT ==========
tailwind_block = """<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        navy: { 950:'#080d1a', 900:'#0b1120', 800:'#111827', 700:'#1e293b', 600:'#334155' },
        brand: { DEFAULT:'#6366f1', light:'#818cf8', dark:'#4f46e5', glow:'rgba(99,102,241,0.15)' },
      },
      fontFamily: { sans: ['Inter','system-ui','-apple-system','sans-serif'] },
    },
  },
}
</script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
"""
html = html.replace('<!-- Critical CSS', tailwind_block + '<!-- Critical CSS', 1)
print("Added Tailwind CDN + Inter font")

# ========== 2. REPLACE INLINE CRITICAL CSS ==========
new_css = """<style>
:root{--bg:#080d1a;--surface:rgba(17,24,39,0.6);--surface-2:rgba(17,24,39,0.75);--surface-input:rgba(17,24,39,0.8);--text:#e2e8f0;--text-2:#94a3b8;--muted:#64748b;--faint:#334155;--border:rgba(255,255,255,0.06);--border-hover:rgba(255,255,255,0.12);--radius:16px;--radius-sm:12px;--radius-pill:999px;--accent:#6366f1;--accent-2:#818cf8;--accent-bg:rgba(99,102,241,0.12);--accent-border:rgba(99,102,241,0.3);--accent-glow:rgba(99,102,241,0.2);--cat-finance:#22c55e;--cat-tax:#f59e0b;--cat-banking:#0ea5e9;--cat-crypto:#f97316;--cat-ai:#a855f7;--cat-dev:#06b6d4;--cat-security:#ef4444;--cat-health:#14b8a6;--cat-social:#ec4899;--cat-images:#8b5cf6;--cat-text:#64748b;--cat-fun:#f43f5e;--cat-cricket:#3b82f6;--cat-sports:#3b82f6;--cat-canada:#dc2626;--cat-marketing:#f97316;--cat-networking:#0ea5e9;--cat-education:#8b5cf6;--cat-tools:#6366f1;--cat-whatsapp:#25d366}
*{box-sizing:border-box}
html{color-scheme:dark;-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;font:400 15px/1.6 'Inter',system-ui,-apple-system,sans-serif;background:var(--bg);color:var(--text);-webkit-font-smoothing:antialiased;position:relative;overflow-x:hidden}
.mesh-bg{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}
.mesh-orb{position:absolute;border-radius:50%;filter:blur(80px)}
.mesh-orb-1{width:600px;height:600px;top:-10%;left:-5%;background:radial-gradient(circle,rgba(99,102,241,0.12),transparent 70%);animation:drift1 25s ease-in-out infinite alternate}
.mesh-orb-2{width:500px;height:500px;top:20%;right:-10%;background:radial-gradient(circle,rgba(139,92,246,0.10),transparent 70%);animation:drift2 20s ease-in-out infinite alternate-reverse}
.mesh-orb-3{width:400px;height:400px;bottom:10%;left:30%;background:radial-gradient(circle,rgba(6,182,212,0.08),transparent 70%);animation:drift3 30s ease-in-out infinite alternate}
.mesh-orb-4{width:350px;height:350px;top:60%;right:20%;background:radial-gradient(circle,rgba(244,63,94,0.06),transparent 70%);animation:drift1 22s ease-in-out infinite alternate-reverse}
.mesh-orb-5{width:450px;height:450px;bottom:-5%;right:-5%;background:radial-gradient(circle,rgba(16,185,129,0.07),transparent 70%);animation:drift2 28s ease-in-out infinite alternate}
@keyframes drift1{0%{transform:translate(0,0) scale(1)}33%{transform:translate(40px,-30px) scale(1.05)}66%{transform:translate(-20px,40px) scale(0.95)}100%{transform:translate(30px,20px) scale(1.02)}}
@keyframes drift2{0%{transform:translate(0,0) scale(1)}50%{transform:translate(-30px,20px) scale(1.08)}100%{transform:translate(20px,-30px) scale(0.96)}}
@keyframes drift3{0%{transform:translate(0,0) rotate(0deg)}100%{transform:translate(30px,-20px) rotate(5deg)}}
@media(prefers-reduced-motion:reduce){.mesh-orb{animation:none!important}}
body::before{content:"";position:fixed;inset:0;z-index:1;pointer-events:none;opacity:0.015;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.grid-pattern{background-image:linear-gradient(rgba(255,255,255,0.02) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,0.02) 1px,transparent 1px);background-size:60px 60px}
img,svg,video{max-width:100%;height:auto;display:block}
a{color:inherit;text-decoration:none}
.wrap{width:min(100%-24px,1120px);margin:32px auto;position:relative;z-index:10}
.card{background:rgba(17,24,39,0.6);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,0.06);border-radius:var(--radius);padding:20px;transition:all .3s cubic-bezier(0.4,0,0.2,1);position:relative;overflow:hidden}
.card::before{content:"";position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,var(--accent),transparent);opacity:0;transition:opacity .3s}
.card:hover{border-color:rgba(255,255,255,0.12);background:rgba(17,24,39,0.75);transform:translateY(-3px);box-shadow:0 12px 40px rgba(0,0,0,0.3),0 0 0 1px rgba(99,102,241,0.08)}
.card:hover::before{opacity:1}
.btn{display:inline-flex;align-items:center;gap:6px;min-height:38px;padding:7px 16px;border-radius:var(--radius-sm);background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;border:none;font-weight:600;font-size:14px;text-decoration:none;cursor:pointer;transition:all .3s cubic-bezier(0.4,0,0.2,1);position:relative;overflow:hidden}
.btn::before{content:"";position:absolute;inset:0;background:linear-gradient(135deg,rgba(255,255,255,.15),transparent);opacity:0;transition:opacity .3s}
.btn::after{content:"";position:absolute;inset:-1px;border-radius:inherit;background:linear-gradient(135deg,#6366f1,#8b5cf6);filter:blur(12px);opacity:0;transition:opacity .3s;z-index:-1}
.btn:hover::before{opacity:1}.btn:hover::after{opacity:0.5}.btn:hover{transform:translateY(-2px);filter:brightness(1.1)}.btn:active{transform:scale(.98)}
.btn.secondary{background:rgba(255,255,255,0.05);color:var(--text-2);border:1px solid rgba(255,255,255,0.08)}
.btn.secondary:hover{border-color:rgba(99,102,241,0.3);color:var(--text);filter:none}
.btn.secondary::before{display:none}.btn.secondary::after{display:none}
.btn.sm{padding:4px 10px;font-weight:500;font-size:12px}
.site{position:sticky;top:0;z-index:50;background:rgba(8,13,26,0.85);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid rgba(255,255,255,0.05)}
.header-inner{display:flex;align-items:center;justify-content:space-between;gap:12px;width:min(100%-24px,1120px);margin:0 auto;min-height:56px;padding:0}
.brand{display:inline-flex;align-items:center;gap:10px;color:var(--text);font-weight:700;font-size:16px}
.brand b{transition:opacity .2s,max-width .3s;overflow:hidden;max-width:0;opacity:0;white-space:nowrap}
.brand:hover b{max-width:200px;opacity:1}
.nav-links{position:relative;display:flex;gap:2px;align-items:center}
.nav-links a{color:var(--text-2);text-decoration:none;padding:6px 12px;border-radius:var(--radius-sm);font-size:14px;font-weight:500;transition:all .25s cubic-bezier(0.4,0,0.2,1);white-space:nowrap}
.nav-links a:hover{color:var(--text);background:rgba(255,255,255,.06)}
.nav-links a[aria-current="page"]{color:var(--text);background:rgba(255,255,255,.08)}
.nav-games{color:#fff!important;background:linear-gradient(135deg,#f43f5e,#f97316)!important;font-weight:600;padding:6px 14px!important;border-radius:var(--radius-pill)!important;box-shadow:0 4px 15px rgba(244,63,94,0.2)}
.nav-games:hover{filter:brightness(1.15);transform:translateY(-1px);box-shadow:0 6px 20px rgba(244,63,94,0.3)}
.more-btn{position:relative;display:inline-flex;align-items:center;gap:4px;padding:5px 11px;border-radius:var(--radius-sm);background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08);color:var(--text-2);font-weight:500;font-size:13px;cursor:pointer;transition:all .25s ease}
.more-btn:hover{border-color:rgba(255,255,255,0.15);color:var(--text)}
.more-menu{display:none;position:absolute;top:calc(100%+6px);right:0;min-width:200px;background:rgba(17,24,39,0.9);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,0.08);border-radius:var(--radius);box-shadow:0 12px 40px rgba(0,0,0,0.5);padding:4px 0;z-index:1000}
.more-menu.open{display:block}
.more-menu a{display:block;padding:7px 14px;font-size:13px;font-weight:500;color:var(--text-2)}
.more-menu a:hover{background:rgba(255,255,255,.06);color:var(--text)}
.hero{display:flex;flex-direction:column;gap:12px;padding:28px;position:relative;overflow:hidden;background:linear-gradient(135deg,var(--accent-bg),transparent);border:1px solid var(--accent-border)}
.hero::after{content:"";position:absolute;top:-30%;right:-15%;width:250px;height:250px;border-radius:50%;background:radial-gradient(circle,rgba(99,102,241,0.1),transparent 70%);pointer-events:none}
.hero-logo{width:52px;height:52px;border-radius:16px}
.games-rail{border:1px solid rgba(255,255,255,0.06)}
.games-rail-head{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.game-chips{display:flex;flex-wrap:wrap;gap:6px}
.game-chip{display:inline-flex;align-items:center;gap:4px;padding:6px 14px;border-radius:999px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);color:var(--text-2);font-weight:500;font-size:13px;text-decoration:none;transition:all .25s cubic-bezier(0.4,0,0.2,1)}
.game-chip:hover{border-color:rgba(99,102,241,0.4);color:var(--text);background:rgba(99,102,241,0.1);transform:translateY(-3px) scale(1.03);box-shadow:0 8px 25px rgba(99,102,241,0.15)}
h1{margin:.1rem 0 .25rem;line-height:1.2;font-weight:700;letter-spacing:-0.02em}
.controls{display:grid;grid-template-columns:1fr;gap:10px;margin:14px 0 8px}
.controls .search{display:flex;align-items:center;gap:8px;background:rgba(17,24,39,0.8);border:1px solid rgba(255,255,255,0.06);border-radius:var(--radius);padding:10px 14px;transition:all .3s ease}
.controls .search:focus-within{border-color:#6366f1;box-shadow:0 0 0 3px rgba(99,102,241,0.15),0 4px 20px rgba(0,0,0,0.2)}
.controls .search span{opacity:.4}
.controls .search .input{flex:1;min-width:0;background:transparent;border:0;outline:0;color:var(--text);font-size:15px}
.catbar{display:flex;gap:4px;overflow:auto;padding:4px;border:1px solid rgba(255,255,255,0.06);border-radius:var(--radius);background:rgba(17,24,39,0.6);scrollbar-width:thin}
.cat-pill{display:inline-flex;align-items:center;gap:4px;padding:5px 10px;border-radius:999px;border:1px solid rgba(255,255,255,0.06);background:transparent;color:var(--text-2);white-space:nowrap;font-weight:500;font-size:13px;cursor:pointer;transition:all .2s ease}
.cat-pill:hover{color:var(--text);background:rgba(255,255,255,0.04)}
.cat-pill[aria-current="true"]{color:var(--text);background:rgba(99,102,241,0.15);border-color:rgba(99,102,241,0.4)}
.tools-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.pill,.chip{display:inline-flex;align-items:center;gap:4px;padding:4px 10px;border-radius:999px;font-size:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);color:var(--text-2);font-weight:500;transition:all .2s ease}
.chip{cursor:pointer}.chip:hover{border-color:rgba(99,102,241,0.3);color:var(--text)}
.badge{font-size:11px;background:rgba(99,102,241,0.12);color:#818cf8;border:1px solid rgba(99,102,241,0.3);padding:2px 8px;border-radius:999px;font-weight:500}
.note{color:var(--muted)}.note.small{font-size:13px}
.sr-only{position:absolute;left:-9999px}
.filter-chip{transition:all .2s ease}
.filter-chip:hover{background:rgba(99,102,241,0.1);border-color:rgba(99,102,241,0.3);color:var(--text)}
.filter-chip.active{background:rgba(99,102,241,0.15);border-color:rgba(99,102,241,0.4);color:#fff}
.tool-card{transition:all .3s cubic-bezier(0.4,0,0.2,1)}
.tool-card::before{content:"";position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,var(--accent),transparent);opacity:0;transition:opacity .3s}
.tool-card:hover::before{opacity:1}
.tool-card:hover{transform:translateY(-4px);border-color:rgba(255,255,255,0.12);box-shadow:0 12px 40px rgba(0,0,0,0.3),0 0 0 1px rgba(99,102,241,0.1)}
.gradient-text{background:linear-gradient(135deg,#fff 0%,#818cf8 40%,#c084fc 70%,#f472b6 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.section{margin:16px 0}
.section h2{font-size:19px;font-weight:700;margin-bottom:12px}
</style>"""

style_start = html.find('<style>')
style_end = html.find('</style>') + len('</style>')
if style_start > 0 and style_end > style_start:
    html = html[:style_start] + new_css + html[style_end:]
    print("Replaced inline critical CSS")

# ========== 3. ADD MESH BACKGROUND ==========
mesh_html = """<!-- ===== Animated Mesh Background ===== -->
<div class="mesh-bg">
<div class="mesh-orb mesh-orb-1"></div>
<div class="mesh-orb mesh-orb-2"></div>
<div class="mesh-orb mesh-orb-3"></div>
<div class="mesh-orb mesh-orb-4"></div>
<div class="mesh-orb mesh-orb-5"></div>
</div>
"""
html = html.replace('<body>\n', '<body>\n' + mesh_html, 1)
print("Added mesh background")

# ========== 4. RESTYLE HEADER LOGO ==========
old_logo = '<img alt="UpTools logo" height="28" loading="eager" src="/assets/logo/uptools-logo.svg" width="28"/>'
new_logo = '<div style="width:36px;height:36px;border-radius:10px;background:linear-gradient(135deg,#6366f1,#8b5cf6,#ec4899);display:flex;align-items:center;justify-content:center;box-shadow:0 4px 16px rgba(99,102,241,0.3);flex-shrink:0"><img alt="UpTools logo" height="24" loading="eager" src="/assets/logo/uptools-logo.svg" width="24" style="border-radius:0"/></div>'
html = html.replace(old_logo, new_logo, 1)
print("Restyled header logo")

# ========== 5. RESTYLE HERO ==========
old_hero = '''<section aria-labelledby="hero-title" class="card hero">
<img alt="UpTools compact logo" class="hero-logo" height="48" loading="eager" src="/assets/logo/uptools-logo.svg" width="48"/>
<div>
<h1 id="hero-title">Games &amp; Tools — all in one place.</h1>
<p class="note" style="margin:0">UpTools is your hub for <b style="color:var(--text)">free online games</b> and <b style="color:var(--text)">everyday tools</b> — calculators, converters, AI helpers and 24+ instant mini-games. No sign-ups, no bloat.</p>
<div class="chips" style="margin-top:10px">
<a class="chip" href="/games/" style="border-color:var(--accent);color:var(--text)">🎮 Play Games</a>
<span class="pill">⚡ Loads fast</span>
<span class="pill">🕵️ Privacy-first</span>
<a class="chip" href="/sitemap.xml" title="Explore everything">Sitemap</a>
</div>
</div>
</section>'''

new_hero = '''<section aria-labelledby="hero-title" class="card hero">
<div style="position:relative;z-index:1">
<div style="display:flex;align-items:center;gap:16px;margin-bottom:12px">
<div style="width:56px;height:56px;border-radius:16px;background:linear-gradient(135deg,#6366f1,#8b5cf6,#ec4899);display:flex;align-items:center;justify-content:center;box-shadow:0 8px 32px rgba(99,102,241,0.3);flex-shrink:0"><img alt="UpTools logo" height="36" loading="eager" src="/assets/logo/uptools-logo.svg" width="36" style="border-radius:0"/></div>
<div><h1 id="hero-title" class="gradient-text" style="font-size:26px;font-weight:800;letter-spacing:-0.03em;margin:0">Games &amp; Tools</h1><p style="color:var(--text-2);font-size:13px;margin:2px 0 0">All in one place.</p></div>
</div>
<p style="color:var(--text-2);font-size:14px;line-height:1.6;max-width:600px;margin:0 0 16px">Your hub for <span style="color:#fff;font-weight:600">free online games</span> and <span style="color:#fff;font-weight:600">everyday tools</span> — calculators, converters, AI helpers and 24+ instant mini-games. No sign-ups, no bloat.</p>
<div style="display:flex;flex-wrap:wrap;gap:8px">
<a href="/games/" class="btn" style="padding:8px 20px;border-radius:12px;font-size:14px">🎮 Play Games</a>
<span class="pill" style="border-color:rgba(255,255,255,0.08)">⚡ Loads fast</span>
<span class="pill" style="border-color:rgba(255,255,255,0.08)">🔒 Privacy-first</span>
</div>
</div>
<div style="display:flex;gap:24px;padding-top:8px;flex-shrink:0">
<div style="text-align:center"><div style="font-size:28px;font-weight:800" class="gradient-text">300+</div><div style="font-size:11px;color:var(--muted);margin-top:2px;font-weight:500">Tools</div></div>
<div style="text-align:center"><div style="font-size:28px;font-weight:800" class="gradient-text">24+</div><div style="font-size:11px;color:var(--muted);margin-top:2px;font-weight:500">Games</div></div>
<div style="text-align:center"><div style="font-size:28px;font-weight:800" class="gradient-text">0</div><div style="font-size:11px;color:var(--muted);margin-top:2px;font-weight:500">Sign-ups</div></div>
</div>
</section>'''

html = html.replace(old_hero, new_hero)
print("Restyled hero")

# ========== 6. RESTYLE GAMES RAIL ==========
old_gr = '''<div class="games-rail-head">
<h2 id="games-rail" style="margin:0">🎮 Free Mini Games</h2>
<a class="btn" href="/games/">Play all 24+ games →</a>
</div>
<p class="note small" style="margin:.35rem 0 .75rem">Instant browser games. No download, no sign-up — just click and play.</p>'''

new_gr = '''<div class="games-rail-head">
<div><h2 id="games-rail" style="margin:0;font-size:18px">🎮 Free Mini Games</h2>
<p class="note small" style="margin:2px 0 0">Instant browser games — click and play.</p></div>
<a class="btn" href="/games/" style="padding:6px 16px;font-size:13px">Play all 24+ →</a>
</div>'''

html = html.replace(old_gr, new_gr)
print("Restyled games rail")

# ========== 7. UPDATE CARDHTML ==========
old_card = '''      function cardHTML(t, favs) {
        const isFav = favs.has(t.slug);
        const mainCat = (t.cats || [])[1] || (t.cats || [])[0] || 'tools';
        const catColor = CATEGORIES[mainCat] ? getComputedStyle(document.documentElement).getPropertyValue('--cat-' + mainCat).trim() : '';
        const catStyle = catColor ? `border-left:3px solid ${catColor}` : '';
        const badgeStyle = catColor ? `background:${catColor}20;color:${catColor};border:1px solid ${catColor}40` : '';
        const newBadge = t.new ? `<span class="badge" style="background:#22c55e20;color:#22c55e;border:1px solid #22c55e40">New</span>` : '';
        return `
      <article class="tool-card card" data-tags="${(t.tags || []).join(',')}" data-title="${t.title.toLowerCase()}" data-cats="${(t.cats || []).join(',')}" style="${catStyle}">
        <div style="display:flex;align-items:center;justify-content:space-between;gap:.6rem;margin-bottom:.5rem">
          <span class="badge" style="${badgeStyle}">${badgeFor(t)}</span>${newBadge}
        </div>
        <a class="tool-title" href="${t.href}" aria-label="${t.title}" style="font-size:1rem;font-weight:600;text-decoration:none;color:var(--text);letter-spacing:-0.01em">${t.title}</a>
        <p class="tool-desc note" style="margin:.3rem 0 .5rem;font-size:13px;line-height:1.5">${t.desc}</p>
        <div class="tags" style="display:flex;flex-wrap:wrap;gap:4px;margin-bottom:.5rem">${tagBadges(t)}</div>
        <div style="display:flex;align-items:center;justify-content:space-between;gap:.5rem">
          <a class="btn" href="${t.href}" style="font-size:13px;padding:5px 12px">Open</a>
          <button class="fav btn secondary sm ${isFav ? 'active' : ''}" data-fav="${t.slug}" aria-label="Favourite ${t.title}" title="Favourite">
            ${isFav ? '★' : '☆'}
          </button>
        </div>
      </article>`;'''

new_card = '''      function cardHTML(t, favs) {
        const isFav = favs.has(t.slug);
        const mainCat = (t.cats || [])[1] || (t.cats || [])[0] || 'tools';
        const catColor = CATEGORIES[mainCat] ? getComputedStyle(document.documentElement).getPropertyValue('--cat-' + mainCat).trim() : '';
        const iconBg = catColor ? catColor + '18' : 'rgba(99,102,241,0.1)';
        const badgeStyle = catColor ? `background:${catColor}18;color:${catColor};border:1px solid ${catColor}35` : '';
        const newBadge = t.new ? `<span class="badge" style="background:rgba(34,197,94,0.12);color:#22c55e;border:1px solid rgba(34,197,94,0.3)">New</span>` : '';
        return `
      <article class="tool-card card" data-tags="${(t.tags || []).join(',')}" data-title="${t.title.toLowerCase()}" data-cats="${(t.cats || []).join(',')}">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px">
          <div style="width:40px;height:40px;border-radius:12px;background:${iconBg};display:flex;align-items:center;justify-content:center;font-size:20px;flex-shrink:0">${t.icon}</div>
          <div style="min-width:0;flex:1">
            <span class="badge" style="${badgeStyle}">${badgeFor(t)}</span>${newBadge}
          </div>
        </div>
        <a class="tool-title" href="${t.href}" aria-label="${t.title}" style="font-size:15px;font-weight:600;text-decoration:none;color:var(--text);letter-spacing:-0.01em;display:block;margin-bottom:4px">${t.title}</a>
        <p class="tool-desc note" style="margin:0 0 10px;font-size:13px;line-height:1.5;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden">${t.desc}</p>
        <div class="tags" style="display:flex;flex-wrap:wrap;gap:4px;margin-bottom:10px">${tagBadges(t)}</div>
        <div style="display:flex;align-items:center;justify-content:space-between;gap:8px">
          <a class="btn" href="${t.href}" style="font-size:13px;padding:5px 14px;border-radius:10px">Open</a>
          <button class="fav btn secondary sm ${isFav ? 'active' : ''}" data-fav="${t.slug}" aria-label="Favourite ${t.title}" title="Favourite" style="border-radius:10px">
            ${isFav ? '★' : '☆'}
          </button>
        </div>
      </article>`;'''

html = html.replace(old_card, new_card)
print("Updated cardHTML")

# ========== 8. RESTYLE FOOTER ==========
old_foot = '''<footer class="note small site-footer" role="contentinfo">
        © <span id="y"></span> UpTools . <a href="/about/">About</a> . <a href="/contact/">Contact</a> .
        <a href="/sitemap.xml">Sitemap</a> . <a href="/robots.txt">Robots</a> .
        <a href="/privacy-policy/">Privacy Policy</a>
</footer>'''

new_foot = '''<footer style="text-align:center;padding:32px 0 24px;margin-top:32px;border-top:1px solid rgba(255,255,255,0.05);position:relative;z-index:10">
<div style="display:flex;align-items:center;justify-content:center;gap:10px;margin-bottom:12px">
<div style="width:32px;height:32px;border-radius:8px;background:linear-gradient(135deg,#6366f1,#8b5cf6);display:flex;align-items:center;justify-content:center"><img alt="UpTools" height="20" src="/assets/logo/uptools-logo.svg" width="20" style="border-radius:0"/></div>
<span style="font-size:14px;font-weight:700;color:#fff">UpTools</span>
</div>
<p style="font-size:12px;color:var(--muted);max-width:400px;margin:0 auto 12px;line-height:1.6">300+ free tools and 24+ browser games. No sign-ups, no data collection. Everything runs in your browser.</p>
<div style="display:flex;flex-wrap:wrap;justify-content:center;gap:12px;font-size:12px;color:var(--muted)">
<a href="/about/" style="color:var(--muted)">About</a>
<a href="/contact/" style="color:var(--muted)">Contact</a>
<a href="/sitemap.xml" style="color:var(--muted)">Sitemap</a>
<a href="/robots.txt" style="color:var(--muted)">Robots</a>
<a href="/privacy-policy/" style="color:var(--muted)">Privacy</a>
</div>
<p style="font-size:11px;color:var(--faint);margin:12px 0 0">© <span id="y"></span> UpTools. All rights reserved.</p>
</footer>'''

html = html.replace(old_foot, new_foot)
print("Restyled footer")

# ========== 9. SECTION TITLE SIZES ==========
for old, new in [
    ('<h2 style="margin-top:0">✅ Do\'s and ❌ Don\'ts</h2>', '<h2 style="margin-top:0;font-size:18px">✅ Do\'s and ❌ Don\'ts</h2>'),
    ('<h2 style="margin-top:0">Frequently Asked Questions</h2>', '<h2 style="margin-top:0;font-size:18px">Frequently Asked Questions</h2>'),
    ('<summary style="cursor:pointer;font-weight:700;font-size:1.1rem;padding:4px 0">', '<summary style="cursor:pointer;font-weight:700;font-size:18px;padding:4px 0">'),
    ('<h2 id="video-learn">🎥 Learn: Using calculators smartly</h2>', '<h2 id="video-learn" style="font-size:18px">🎥 Learn: Using calculators smartly</h2>'),
    ('<h2>⭐ Your favourites</h2>', '<h2 style="font-size:18px">⭐ Your favourites</h2>'),
    ('<h2>⏱️ Continue</h2>', '<h2 style="font-size:18px">⏱️ Continue</h2>'),
    ('<h2 id="featured">🔥 Featured</h2>', '<h2 id="featured" style="font-size:18px">🔥 Featured</h2>'),
    ('<h2 id="tools-heading">🧰 All tools</h2>', '<h2 id="tools-heading" style="font-size:18px">🧰 All tools</h2>'),
]:
    html = html.replace(old, new, 1)

print("Restyled section titles")

# ========== WRITE ==========
with open('/Users/pushpanderkumar/websites/uptools/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nFinal: {len(html)} chars")
print("DONE!")
