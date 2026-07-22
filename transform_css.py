#!/usr/bin/env python3
"""Update public/style.css with new design system."""
import re

with open("/Users/pushpanderkumar/websites/uptools/public/style.css", "r") as f:
    css = f.read()

# Replace :root variables
css = re.sub(
    r""":root\{[^}]*--bg:#0c0c14;""",
    """:root{\n  --bg:#080d1a;""",
    css
)
css = css.replace("--surface:#16161f;", "--surface:rgba(17,24,39,0.6);")
css = css.replace("--surface-2:#1c1c28;", "--surface-2:rgba(17,24,39,0.75);")
css = css.replace("--surface-input:#12121a;", "--surface-input:rgba(17,24,39,0.8);")
css = css.replace("--text:#f0f0f5;", "--text:#e2e8f0;")
css = css.replace("--text-2:#9898ac;", "--text-2:#94a3b8;")
css = css.replace("--muted:#686878;", "--muted:#64748b;")
css = css.replace("--faint:#3a3a4a;", "--faint:#334155;")
css = css.replace("--border:rgba(255,255,255,.08);", "--border:rgba(255,255,255,0.06);")
css = css.replace("--border-hover:rgba(255,255,255,.14);", "--border-hover:rgba(255,255,255,0.12);")
css = css.replace("--radius:12px;", "--radius:16px;")
css = css.replace("--radius-sm:8px;", "--radius-sm:12px;")
css = css.replace("--trans:.18s ease;", "--trans:.3s cubic-bezier(0.4,0,0.2,1);")
css = css.replace("--font:-apple-system,BlinkMacSystemFont,'Inter','Segoe UI',Roboto,sans-serif;", "--font:'Inter',system-ui,-apple-system,sans-serif;")
css = css.replace("--accent-bg:rgba(99,102,241,.1);", "--accent-bg:rgba(99,102,241,0.12);")
css = css.replace("--accent-glow:rgba(99,102,241,.15);", "--accent-glow:rgba(99,102,241,0.2);")

# Update body
css = css.replace(
    "body{margin:0;min-height:100dvh;color:var(--text);background:var(--bg);font:400 15px/1.6 var(--font);-webkit-font-smoothing:antialiased;overflow-x:hidden;position:relative}",
    "body{margin:0;min-height:100dvh;color:var(--text);background:var(--bg);font:400 15px/1.6 var(--font);-webkit-font-smoothing:antialiased;overflow-x:hidden;position:relative;font-family:'Inter',system-ui,-apple-system,sans-serif}"
)

# Replace old mesh background with note
old_mesh_pattern = r"body::before\{content:\"\";position:fixed.*?filter:blur\(60px\)\}"
new_mesh = "/* Mesh background is rendered via HTML .mesh-bg in index.html */"
css = re.sub(old_mesh_pattern, new_mesh, css, flags=re.DOTALL)

# Remove @keyframes orbFloat
css = re.sub(r"@keyframes orbFloat\{.*?\}", "", css, flags=re.DOTALL)

# Update card
css = css.replace(
    """  background:var(--surface);\n  border:1px solid var(--border);\n  border-radius:var(--radius);\n  padding:20px;\n  transition:all var(--trans);\n  position:relative;\n  overflow:hidden;""",
    """  background:rgba(17,24,39,0.6);\n  backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);\n  border:1px solid rgba(255,255,255,0.06);\n  border-radius:var(--radius);\n  padding:20px;\n  transition:all var(--trans);\n  position:relative;\n  overflow:hidden;"""
)

# Update card hover
css = css.replace(
    """.card:hover{\n  border-color:var(--border-hover);\n  transform:translateY(-2px);\n  box-shadow:0 8px 30px rgba(0,0,0,.3);\n}""",
    """.card:hover{\n  border-color:rgba(255,255,255,0.12);\n  background:rgba(17,24,39,0.75);\n  transform:translateY(-3px);\n  box-shadow:0 12px 40px rgba(0,0,0,0.3),0 0 0 1px rgba(99,102,241,0.08);\n}"""
)

# Update card::before
css = css.replace(
    "background:linear-gradient(90deg, var(--accent), var(--accent-2));",
    "background:linear-gradient(90deg,transparent,var(--accent),transparent);"
)

# Update header
css = css.replace(
    "background:rgba(12,12,20,.88);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-bottom:1px solid var(--border)}",
    "background:rgba(8,13,26,0.85);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid rgba(255,255,255,0.05)}"
)

# Update nav-games
css = css.replace(
    ".nav-games{color:#fff!important;background:linear-gradient(135deg,#f43f5e,#f97316)!important;font-weight:600;padding:6px 14px!important;border-radius:var(--radius-pill)!important}",
    ".nav-games{color:#fff!important;background:linear-gradient(135deg,#f43f5e,#f97316)!important;font-weight:600;padding:6px 14px!important;border-radius:var(--radius-pill)!important;box-shadow:0 4px 15px rgba(244,63,94,0.2)}"
)

# Update btn
css = css.replace(
    "font-weight:500;font-size:14px;background:var(--accent);color:#fff;border:none;transition:all var(--trans);position:relative;overflow:hidden}",
    "font-weight:600;font-size:14px;background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;border:none;transition:all var(--trans);position:relative;overflow:hidden}"
)

# Add btn glow ::after
old_btn_after = ".btn:hover{filter:brightness(1.1);transform:translateY(-1px)}\n.btn:active{transform:scale(.98)}"
new_btn_after = ".btn::after{content:\"\";position:absolute;inset:-1px;border-radius:inherit;background:linear-gradient(135deg,#6366f1,#8b5cf6);filter:blur(12px);opacity:0;transition:opacity var(--trans);z-index:-1}\n.btn:hover::before{opacity:1}.btn:hover::after{opacity:0.5}.btn:hover{transform:translateY(-2px);filter:brightness(1.1)}.btn:active{transform:scale(.98)}"
css = css.replace(old_btn_after, new_btn_after)

# Update secondary btn
css = css.replace(
    ".btn.secondary,a.btn.secondary{background:transparent;color:var(--text-2);border:1px solid var(--border)}",
    ".btn.secondary,a.btn.secondary{background:rgba(255,255,255,0.05);color:var(--text-2);border:1px solid rgba(255,255,255,0.08)}"
)

# Update game-chip
css = css.replace(
    ".game-chip{display:inline-flex;align-items:center;gap:4px;padding:5px 12px;border-radius:var(--radius-pill);background:var(--surface);border:1px solid var(--border);color:var(--text-2);font-weight:500;font-size:13px;text-decoration:none;transition:all var(--trans)}",
    ".game-chip{display:inline-flex;align-items:center;gap:4px;padding:6px 14px;border-radius:var(--radius-pill);background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);color:var(--text-2);font-weight:500;font-size:13px;text-decoration:none;transition:all .25s cubic-bezier(0.4,0,0.2,1)}"
)
css = css.replace(
    ".game-chip:hover{border-color:var(--accent);color:var(--text);background:var(--accent-bg)}",
    ".game-chip:hover{border-color:rgba(99,102,241,0.4);color:var(--text);background:rgba(99,102,241,0.1);transform:translateY(-3px) scale(1.03);box-shadow:0 8px 25px rgba(99,102,241,0.15)}"
)

# Update footer
css = css.replace(
    "border-top:1px solid var(--border)}",
    "border-top:1px solid rgba(255,255,255,0.05)}"
)

# Update search focus
css = css.replace(
    ".controls .search:focus-within{border-color:var(--accent)}",
    ".controls .search:focus-within{border-color:#6366f1;box-shadow:0 0 0 3px rgba(99,102,241,0.15),0 4px 20px rgba(0,0,0,0.2)}"
)

# Update cat-pill
css = css.replace(
    ".cat-pill[aria-current=\"true\"]{color:var(--text);background:var(--accent-bg);border-color:var(--accent-border)}",
    ".cat-pill[aria-current=\"true\"]{color:var(--text);background:rgba(99,102,241,0.15);border-color:rgba(99,102,241,0.4)}"
)

# Update chips/pills
css = css.replace(
    ".pill,.chip{display:inline-flex;align-items:center;gap:4px;padding:4px 10px;border-radius:var(--radius-pill);font-size:12px;background:var(--surface);border:1px solid var(--border);color:var(--text-2);font-weight:500}",
    ".pill,.chip{display:inline-flex;align-items:center;gap:4px;padding:4px 10px;border-radius:var(--radius-pill);font-size:12px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.06);color:var(--text-2);font-weight:500;transition:all .2s ease}"
)

# Add tool-card hover and gradient-text
if ".tool-card{" not in css:
    css += """
/* ===== Tool Card Hover ===== */
.tool-card{transition:all .3s cubic-bezier(0.4,0,0.2,1)}
.tool-card::before{content:"";position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,var(--accent),transparent);opacity:0;transition:opacity .3s}
.tool-card:hover::before{opacity:1}
.tool-card:hover{transform:translateY(-4px);border-color:rgba(255,255,255,0.12);box-shadow:0 12px 40px rgba(0,0,0,0.3),0 0 0 1px rgba(99,102,241,0.1)}
/* ===== Gradient Text ===== */
.gradient-text{background:linear-gradient(135deg,#fff 0%,#818cf8 40%,#c084fc 70%,#f472b6 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
"""

# Update reduced motion
css = css.replace(
    "@media(prefers-reduced-motion:reduce){*{animation-duration:.01ms!important;transition-duration:.01ms!important}}",
    "@media(prefers-reduced-motion:reduce){*{animation-duration:.01ms!important;transition-duration:.01ms!important}.mesh-orb{animation:none!important}}"
)

with open("/Users/pushpanderkumar/websites/uptools/public/style.css", "w") as f:
    f.write(css)

print("public/style.css updated!")
