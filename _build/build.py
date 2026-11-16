"""Builds the Edgeward site pages. Run: python3 _build/build.py  (from the repo root)."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import scenes

ROOT = pathlib.Path(__file__).resolve().parent.parent
EMAIL = "contact@edgeward.ca"
LI = "https://www.linkedin.com/company/edgewardisr/"
IG = "https://www.instagram.com/edgewardisr/"
YT = "https://www.youtube.com/@Edge_Ward_ISR"
NAV = [("index.html", "Home"), ("capabilities.html", "Capabilities"), ("about.html", "About")]
TAGLINE = "Canadian · Métis-owned · Veteran-founded"


def head(title, desc, path):
    cur = lambda h: ' aria-current="page"' if h == path else ""
    links = "".join(f'      <a href="{h}"{cur(h)}>{t}</a>\n' for h, t in NAV)
    url = "" if path == "index.html" else path
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#000000">
<meta property="og:type" content="website">
<meta property="og:url" content="https://edgeward.ca/{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://edgeward.ca/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_CA">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Edgeward home"><img src="assets/img/logo-wordmark.png" alt="Edgeward" width="107" height="46"></a>
    <button class="menu-btn" aria-label="Menu" aria-expanded="false">Menu</button>
    <nav class="nav">
{links}      <a class="btn" href="contact.html"{cur('contact.html')}>Contact</a>
    </nav>
  </div>
</header>
"""


FOOT = f"""<footer class="site-foot">
  <div class="wrap">
    <div><img src="assets/img/logo-wordmark.png" alt="Edgeward" width="88" height="38"><p style="margin:12px 0 0">Edgeward Inc. · {TAGLINE}</p></div>
    <nav><a href="capabilities.html">Capabilities</a><a href="about.html">About</a><a href="mailto:{EMAIL}">{EMAIL}</a><a href="{LI}">LinkedIn</a><a href="{IG}">Instagram</a><a href="{YT}">YouTube</a></nav>
  </div>
</footer>
<script src="assets/site.js"></script>
</body>
</html>
"""

CTA = f"""<section class="cta">
  <div class="wrap rv">
    <h2>Have a drone program in mind?</h2>
    <div class="btns"><a class="btn" href="mailto:{EMAIL}">Email {EMAIL}</a></div>
  </div>
</section>
"""


def screen(label, svg):
    return (f'<figure class="screen"><div class="screen-bar"><span class="mono"><i></i>Edgeward // {label}</span>'
            f'<span class="mono cv">Concept view</span></div>{svg}</figure>')


def chips(items):
    return '<div class="chips">' + "".join(f'<span class="chip {c}">{t}</span>' for c, t in items) + "</div>"


# id, number, screen label, title, short text, bullets, chips, svg
CAPS = [
    ("deconfliction", "01", "Deconfliction", "Mission planning &amp; airspace deconfliction",
     "Every flight checked before takeoff. Off-plan aircraft get a reroute to approve in TAK.",
     ["4D plans checked against every other plan, no-fly volumes, weather and radio needs",
      "Off-plan aircraft get the least disruptive route back, to approve or cancel in TAK",
      "Positions come from the ground station you already use. Nothing added to the aircraft",
      "Runs offline on one Windows laptop"],
     [("sim", "Simulation &amp; hardware-in-the-loop tested"), ("", "Not yet flown")], scenes.decon()),
    ("one-map", "02", "One map", "One map, every aircraft",
     "The whole fleet's positions, plans and alerts in ATAK and WinTAK.",
     ["Live positions, flight plans and alerts sent as standard Cursor-on-Target",
      "Plan, approve and cancel from ATAK or WinTAK chat",
      "ATAK phones and WinTAK laptops share the same picture",
      "Open standards, so other TAK tools see the same data"],
     [("bench", "Proven on ATAK &amp; WinTAK with a simulated aircraft")], scenes.cop()),
    ("detection", "03", "Search &amp; rescue", "Onboard detection for search &amp; rescue",
     "The aircraft finds people and vehicles and puts them on the map.",
     ["Person and vehicle detection on an onboard NVIDIA Jetson",
      "Each detection geolocated to a position on the ground",
      "Reported to TAK as map markers your teams can act on",
      "Built for area searches where every minute counts"],
     [("flight", "Flight-tested · 3 flights, Sept 2026"), ("bench", "TAK reporting shown with recorded flight data")], scenes.det()),
    ("daa", "04", "Detect &amp; avoid", "Detect, alert &amp; avoid",
     "One onboard camera spots other aircraft, alerts, and steers clear.",
     ["Spots nearby aircraft with a single onboard camera",
      "Estimates time to closest approach and alerts the operator",
      "Can command an avoidance manoeuvre through the autopilot",
      "A tested fail-safe returns the aircraft to a safe state if commands are lost"],
     [("bench", "Bench &amp; simulation tested"), ("", "Airborne testing next")], scenes.daa()),
]


def show(c, i=0):
    cid, num, lab, title, text, bullets, ch, svg = c
    flip = " flip" if i % 2 else ""
    body = f'<span class="num"><b>{num}</b> / 04</span><h2>{title}</h2><p>{text}</p>{chips(ch)}'
    return f'<div class="show{flip} rv" id="{cid}" style="scroll-margin-top:90px">{screen(lab, svg)}<div>{body}</div></div>\n'


# ------------------------------------------------------------------ HOME
index = head("Edgeward | Autonomous drone operations on the TAK map",
             "See everything. Decide first. Trust the mission. Edgeward builds autonomy for drone teams on the ATAK and WinTAK map they already carry. Canadian, Métis-owned, veteran-founded.",
             "index.html") + f"""<main>
<section class="hero hero-full">
  <div class="hero-bg">{scenes.hero()}</div>
  <div class="wrap">
    <div class="tag"><span class="dot"></span><span class="mono">{TAGLINE}</span></div>
    <h1>One operator.<br>A fleet of drones.<br><span class="hl">One map.</span></h1>
    <div class="btns"><a class="btn" href="capabilities.html">See what we build</a><a class="btn ghost" href="about.html">Start a conversation</a></div>
  </div>
</section>
</main>
""" + FOOT

# ------------------------------------------------------------------ CAPABILITIES
caps = head("Capabilities | Edgeward",
            "Mission planning and deconfliction, one map in TAK, onboard detection, and detect and avoid.",
            "capabilities.html") + f"""<main>
<section class="page-head"><div class="wrap"><p class="eyebrow">Capabilities</p><h1>What we build.</h1></div></section>
<section style="padding-top:24px">
  <div class="wrap">
{''.join(show(c, i) for i, c in enumerate(CAPS))}  </div>
</section>
{CTA}</main>
""" + FOOT

# ------------------------------------------------------------------ ABOUT
about = head("About | Edgeward",
             "Edgeward is a Canadian, Métis-owned, veteran-founded drone software company based in Alberta.",
             "about.html") + f"""<main>
<section class="page-head"><div class="wrap"><p class="eyebrow">About</p><h1>Autonomous vehicles are the future. They need one place to work from.</h1></div></section>
<section>
  <div class="wrap about-grid">
    <div class="rv">
      <p class="lead">Instead of building another tool, Edgeward puts tasking and results from autonomous drones on the TAK map teams already use.</p>
      <p>Led by an RCAF veteran who has run autonomous drone operations for wildfire and national security missions.</p>
      <div class="btns"><a class="btn" href="contact.html">Get in touch</a></div>
    </div>
    <aside class="facts rv">
      <dl>
        <dt>Company</dt><dd>Edgeward Inc.</dd>
        <dt>Based in</dt><dd>Alberta, Canada</dd>
        <dt>Ownership</dt><dd>Métis-owned, veteran-founded</dd>
      </dl>
    </aside>
  </div>
</section>
</main>
""" + FOOT

# ------------------------------------------------------------------ CONTACT
contact = head("Contact | Edgeward",
               "Talk to Edgeward about autonomous drone software and TAK integration.",
               "contact.html") + f"""<main>
<section class="page-head"><div class="wrap"><p class="eyebrow">Contact</p><h1>Let's talk.</h1></div></section>
<section>
  <div class="wrap">
    <div class="contact-box rv" style="max-width:560px">
      <p><a class="big" href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p style="margin:18px 0 0"><a href="{LI}">LinkedIn</a> · <a href="{IG}">Instagram</a> · <a href="{YT}">YouTube</a></p>
    </div>
  </div>
</section>
</main>
""" + FOOT

for name, html in [("index.html", index), ("capabilities.html", caps), ("about.html", about), ("contact.html", contact)]:
    (ROOT / name).write_text(html)
    print("wrote", name, len(html))
