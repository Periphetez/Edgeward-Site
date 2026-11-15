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
    <p class="eyebrow">Work with us</p>
    <h2>Need custom drone software or a TAK integration?</h2>
    <p class="lead">Tell us about your aircraft, your team and the challenges you want to overcome. We'll come back with a clear plan for how our software can be built into a custom solution that works with you, and for you.</p>
    <div class="btns"><a class="btn" href="mailto:{EMAIL}">Email {EMAIL}</a><a class="btn ghost" href="capabilities.html">See capabilities</a></div>
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
     "Every flight is checked against every other aircraft, no-fly zone and the weather before it leaves the ground. If one drifts off plan, the operator gets a fix to approve.",
     ["4D plans checked against every other plan, no-fly volumes, weather and radio needs",
      "Off-plan aircraft get the least disruptive route back, to approve or cancel in TAK",
      "Positions come from the ground station you already use. Nothing added to the aircraft",
      "Runs offline on one Windows laptop"],
     [("sim", "Simulation &amp; hardware-in-the-loop tested"), ("", "Not yet flown")], scenes.decon()),
    ("one-map", "02", "One map", "One map, every aircraft",
     "Positions, plans and alerts for the whole fleet, inside ATAK and WinTAK. No new screens for your operators to learn.",
     ["Live positions, flight plans and alerts sent as standard Cursor-on-Target",
      "Plan, approve and cancel from ATAK or WinTAK chat",
      "ATAK phones and WinTAK laptops share the same picture",
      "Open standards, so other TAK tools see the same data"],
     [("bench", "Proven on ATAK &amp; WinTAK with a simulated aircraft")], scenes.cop()),
    ("detection", "03", "Search &amp; rescue", "Onboard detection for search &amp; rescue",
     "The aircraft spots people and vehicles itself, works out where they are on the ground, and puts them on the map.",
     ["Person and vehicle detection on an onboard NVIDIA Jetson",
      "Each detection geolocated to a position on the ground",
      "Reported to TAK as map markers your teams can act on",
      "Built for area searches where every minute counts"],
     [("flight", "Flight-tested · 3 flights, Sept 2026"), ("bench", "TAK reporting shown with recorded flight data")], scenes.det()),
    ("daa", "04", "Detect &amp; avoid", "Detect, alert &amp; avoid",
     "One onboard camera watches for other aircraft, warns the operator and can steer clear. No LiDAR and no ground link needed.",
     ["Spots nearby aircraft with a single onboard camera",
      "Estimates time to closest approach and alerts the operator",
      "Can command an avoidance manoeuvre through the autopilot",
      "A tested fail-safe returns the aircraft to a safe state if commands are lost"],
     [("bench", "Bench &amp; simulation tested"), ("", "Airborne testing next")], scenes.daa()),
]


# YouTube demos: id, title, length, honest test label
VIDEOS = [
    ("vlFKHVtb1XA", "Off-plan alert and operator-approved reroute in WinTAK", "0:47", "sim", "Simulation"),
    ("DU9ia2neNSw", "Off-plan aircraft flagged in seconds", "1:39", "sim", "ArduPilot simulation"),
    ("owoK8Ph-H1Q", "Drone deconfliction on TAK: walkthrough", "2:13", "sim", "Simulation"),
    ("3qRIRZOXNsI", "Autonomous zone response: draw a zone in ATAK, drone responds", "1:27", "sim", "Simulation · real ATAK"),
    ("4XseMFF_3HM", "First flight test: onboard detection on the ATAK map", "0:34", "flight", "Flight test · TAK from recorded data"),
]
CAP_VIDEO = {"deconfliction": "vlFKHVtb1XA", "one-map": "3qRIRZOXNsI", "detection": "4XseMFF_3HM"}


def watch(yt, label="Watch it work"):
    return f'<button class="watch" type="button" data-yt="{yt}"><span class="play" aria-hidden="true"></span>{label}</button>'


def demo_card(v):
    yt, title, length, cls, tag = v
    return (f'<button class="demo" type="button" data-yt="{yt}"><span class="thumb" style="background-image:url(https://i.ytimg.com/vi/{yt}/hqdefault.jpg)">'
            f'<span class="play" aria-hidden="true"></span><span class="len">{length}</span></span>'
            f'<span class="dbody"><span class="chip {cls}">{tag}</span><span class="dt">{title}</span></span></button>')


def show(c, detail=False, i=0):
    cid, num, lab, title, text, bullets, ch, svg = c
    flip = " flip" if i % 2 else ""
    if detail:
        body = (f'<span class="num"><b>{num}</b> / 04</span><h2>{title}</h2><p>{text}</p><ul>'
                + "".join(f"<li>{b}</li>" for b in bullets) + "</ul>" + chips(ch) + (watch(CAP_VIDEO[cid]) if cid in CAP_VIDEO else ''))
        return f'<div class="show{flip} rv" id="{cid}" style="scroll-margin-top:90px">{screen(lab, svg)}<div>{body}</div></div>\n'
    body = (f'<span class="num"><b>{num}</b> / 04</span><h3>{title}</h3><p>{text}</p>{chips(ch[:1])}'
            f'<a class="more" href="capabilities.html#{cid}">How it works →</a>')
    return f'<div class="show{flip} rv">{screen(lab, svg)}<div>{body}</div></div>\n'


def card(c):
    cid, num, lab, title, text, bullets, ch, svg = c
    return (f'<a class="capcard" href="capabilities.html#{cid}"><span class="num"><b>{num}</b> / 04</span>'
            f'<h3>{title}</h3><p>{text}</p>{chips(ch[:1])}<span class="more">How it works →</span></a>')


# ------------------------------------------------------------------ HOME
index = head("Edgeward | Autonomous drone operations on the TAK map",
             "See everything. Decide first. Trust the mission. Edgeward builds autonomy for drone teams: missions planned, deconflicted and reported back on the ATAK and WinTAK map they already carry. Canadian, Métis-owned, veteran-founded.",
             "index.html") + f"""<main>
<section class="hero">
  <div class="hero-bg">{scenes.hero()}</div>
  <div class="wrap">
    <div class="tag"><span class="dot"></span><span class="mono">{TAGLINE}</span></div>
    <p class="kicker">See everything. Decide first. Trust the mission.</p>
    <h1>One operator.<br>A fleet of drones.<br><span class="hl">One map.</span></h1>
    <p class="lead">Edgeward is building the autonomy that lets drones plan, fly and report back on their own, tasked and tracked from the ATAK and WinTAK your team already carries. Built by a veteran who has run autonomous operations in the field.</p>
    <div class="btns"><a class="btn" href="capabilities.html">See what we build</a><a class="btn ghost" href="capabilities.html#demos">Watch the demos</a></div>
  </div>
  <div class="hero-foot"><div class="wrap mono"><span>MAVLink in</span><span>Cursor-on-Target out</span><span>Runs offline</span><span class="live">Concept view of the Edgeward operating picture</span></div></div>
</section>

<div class="strip"><div class="wrap"><span class="mono">Works with</span><b>ATAK</b><b>WinTAK</b><b>MAVLink</b><b>ArduPilot</b><b>Cursor-on-Target</b><b>NVIDIA Jetson</b></div></div>

<section>
  <div class="wrap">
    <div class="section-head rv"><p class="eyebrow">What we build</p><h2>Four capabilities for drone teams.</h2><p class="lead">Each one is tagged with exactly how far it has been tested today.</p></div>
    <div class="capgrid rv">{''.join(card(c) for c in CAPS)}</div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head rv"><p class="eyebrow">Where we're headed</p><h2>From one operator per drone to one operator per fleet.</h2><p class="lead">Today most drones need a person flying them at every step. We're building toward missions the aircraft finish on their own, so a small team can do the work of a large one.</p></div>
    <div class="road rv">
      <div><span class="chip flight">Now</span><h3>One map for everything</h3><p>Tasking, positions, alerts and finds from every aircraft in the TAK app your team already carries.</p></div>
      <div><span class="chip sim">Next</span><h3>Missions that run themselves</h3><p>Give the aircraft a task. It plans, flies, searches, keeps clear of other traffic and reports back. The operator approves decisions instead of flying.</p></div>
      <div><span class="chip bench">The goal</span><h3>Mass at scale</h3><p>Many aircraft, and in time ground vehicles too, working one mission together under a handful of operators.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head rv"><p class="eyebrow">Proven so far</p><h2>Real numbers, not promises.</h2></div>
    <div class="stats rv">
      <div class="stat"><b>3</b><span>real flights with onboard detection and geolocation</span></div>
      <div class="stat"><b>203</b><span>automated tests on the deconfliction software</span></div>
      <div class="stat"><b>~20 ms</b><span>median deconfliction decision</span></div>
      <div class="stat"><b>1</b><span>laptop, offline. No cloud needed.</span></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head rv"><p class="eyebrow">Who it's for</p><h2>Built for the people who fly.</h2></div>
    <div class="who rv">
      <div><span class="mono">01</span><h3>Search &amp; rescue and public safety</h3><p>Find people faster and keep every aircraft on one map during busy incidents.</p></div>
      <div><span class="mono">02</span><h3>Defence and security</h3><p>TAK-native planning and awareness on open standards, developed in Canada.</p></div>
      <div><span class="mono">03</span><h3>Drone builders and integrators</h3><p>Add TAK integration and onboard autonomy to your platform without building it in-house.</p></div>
    </div>
  </div>
</section>

{CTA}</main>
""" + FOOT

# ------------------------------------------------------------------ CAPABILITIES
caps = head("Capabilities | Edgeward",
            "Mission planning and airspace deconfliction, one common operating picture in TAK, onboard detection for search and rescue, and detect, alert and avoid.",
            "capabilities.html") + f"""<main>
<section class="page-head"><div class="wrap"><p class="eyebrow">Capabilities</p><h1>Software for drone teams that work in TAK.</h1><p class="lead">Four capabilities we've built and tested, plus custom software and TAK integrations built around your aircraft.</p>
<div class="legend"><span class="chip flight">Flight-tested</span><span class="chip sim">Simulation or hardware-in-the-loop</span><span class="chip bench">Bench or recorded data</span><span class="chip">Not yet tested</span></div></div></section>
<section style="padding-top:40px">
  <div class="wrap">
{''.join(show(c, True, i) for i, c in enumerate(CAPS))}  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head rv"><p class="eyebrow">How it fits</p><h2>Plugs into the gear you already fly.</h2></div>
    <div class="flow rv">
      <div class="node"><span class="mono">Aircraft</span><strong>Your drone</strong><ul><li>MAVLink autopilots</li><li>Optional onboard computer for detection</li></ul></div>
      <div class="arrow" aria-hidden="true">→</div>
      <div class="node core"><span class="mono">Edgeward</span><strong>Planning &amp; awareness</strong><ul><li>4D plans and deconfliction</li><li>Detection and geolocation</li><li>Alerts and reroutes</li></ul></div>
      <div class="arrow" aria-hidden="true">→</div>
      <div class="node"><span class="mono">Operator</span><strong>ATAK &amp; WinTAK</strong><ul><li>One map for every aircraft</li><li>Approve or cancel from TAK</li></ul></div>
    </div>
    <p class="flow-note mono">MAVLink in · Cursor-on-Target out · No vendor lock-in</p>
  </div>
</section>


<section>
  <div class="wrap">
    <div class="section-head rv"><p class="eyebrow">From the field</p><h2>Built and tested on real hardware.</h2><p class="lead">The concept views show where we're headed. These show the work behind them.</p></div>
    <div class="field rv">
      <figure><img src="assets/img/detection-flight.jpg" alt="Aerial frame with onboard person and vehicle detection" loading="lazy"><figcaption>Onboard detection on a test flight, Sept 2026.</figcaption></figure>
      <figure><img src="assets/img/hil-field-kit.jpg" alt="Hardware-in-the-loop kit in a vehicle" loading="lazy"><figcaption>Hardware-in-the-loop testing on a moving vehicle, Oct 2026.</figcaption></figure>
      <figure><img src="assets/img/onboard-compute.jpg" alt="NVIDIA Jetson and Pixhawk 6X" loading="lazy"><figcaption>Onboard compute: NVIDIA Jetson with a Pixhawk 6X.</figcaption></figure>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="founder" style="margin-bottom:64px">
      <figure class="media rv"><img src="assets/img/airframe-integration.jpg" alt="Onboard computer and wiring integrated into a fixed-wing airframe" loading="lazy"><figcaption>Integrating onboard compute into a fixed-wing airframe.</figcaption></figure>
      <div class="rv show" style="display:block;padding:0"><p class="eyebrow">Custom work</p><h2>Custom drone software &amp; TAK integrations.</h2><p>Already have a platform? We'll connect it to TAK and add the autonomy your operators need, on your hardware.</p>
      <ul><li>TAK integration for drones, sensors and uncrewed vehicles</li><li>Onboard detection and autonomy on edge compute</li><li>Mission planning and deconfliction for your fleet</li></ul></div>
    </div>
    <div class="steps rv">
      <div class="step"><h3>Scope</h3><p>We learn your aircraft, operators and mission, and agree what success looks like.</p></div>
      <div class="step"><h3>Build</h3><p>Software built on open standards: MAVLink and Cursor-on-Target.</p></div>
      <div class="step"><h3>Test</h3><p>Simulation, then hardware-in-the-loop, then flight. We tell you exactly what's been proven.</p></div>
      <div class="step"><h3>Hand over</h3><p>Documentation and support so your team can run it.</p></div>
    </div>
  </div>
</section>

<section id="demos" style="scroll-margin-top:72px">
  <div class="wrap">
    <div class="section-head rv"><p class="eyebrow">Demos</p><h2>Watch it work.</h2><p class="lead">Short videos of each feature as it was built. Each one says whether it's simulation or flight.</p></div>
    <div class="demos rv">""" + "".join(demo_card(v) for v in VIDEOS) + f"""</div>
    <p class="flow-note mono"><a href="{YT}" style="color:inherit">More on our YouTube channel →</a></p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head rv"><p class="eyebrow">Platforms &amp; standards</p><h2>What it works with.</h2></div>
    <div class="stats three rv">
      <div class="stat"><b>Autopilots</b><span>ArduPilot (flight-tested) · PX4 (MAVLink-compatible, not yet flight-tested)</span></div>
      <div class="stat"><b>TAK</b><span>ATAK · WinTAK · FreeTAKServer · Cursor-on-Target</span></div>
      <div class="stat"><b>Onboard</b><span>NVIDIA Jetson · single-camera perception</span></div>
    </div>
  </div>
</section>
{CTA}</main>
""" + FOOT

# ------------------------------------------------------------------ ABOUT
about = head("About | Edgeward",
             "Edgeward is a Canadian, Métis-owned, veteran-founded drone software company based in Alberta.",
             "about.html") + f"""<main>
<section class="page-head"><div class="wrap"><p class="eyebrow">About</p><h1>One place to task every autonomous vehicle, and see everything they find.</h1></div></section>
<section>
  <div class="wrap about-grid">
    <div class="rv">
      <p class="lead">Edgeward was founded on a simple belief: autonomous vehicles are the future, and the teams using them will need one platform to control them all and one place where all their data comes together.</p>
      <p>We didn't want to build yet another tool for operators to learn. Teams already plan, talk and track each other in TAK. So we asked a simple question: why not use the tool that already exists? Edgeward puts the tasking and the results from autonomous work there, so every aircraft, every plan and every find sits on one map.</p>
      <p>The next step is autonomy that does more of the work. Today a drone needs a person at every step. We're building toward missions the aircraft can complete on their own: plan, fly, search, stay clear of other traffic and report back, with the operator approving decisions instead of flying. That is how a small team delivers mass at scale.</p>
      <p>Edgeward is led by an RCAF veteran who has run long-range autonomous drone operations for wildfire and national security missions, and built autonomy and control systems for ground vehicles and heavy equipment on active work sites. We start from what the operator needs, use open standards so nobody is locked in, and say exactly how far each capability has been tested.</p>
      <div class="btns"><a class="btn" href="contact.html">Get in touch</a><a class="btn ghost" href="capabilities.html">See capabilities</a></div>
    </div>
    <aside class="facts rv">
      <dl>
        <dt>Company</dt><dd>Edgeward Inc., federally incorporated in 2026</dd>
        <dt>Based in</dt><dd>Alberta, Canada</dd>
        <dt>Ownership</dt><dd>Métis-owned</dd>
        <dt>Leadership</dt><dd>RCAF veteran founder</dd>
        <dt>Focus</dt><dd>Custom drone software, TAK integration and mission autonomy</dd>
      </dl>
    </aside>
  </div>
</section>
<section class="alt">
  <div class="wrap">
    <div class="section-head rv"><p class="eyebrow">How we work</p><h2>Three rules we build by.</h2></div>
    <div class="who rv">
      <div><span class="mono">01</span><h3>Start with the operator</h3><p>Software should fit the tools and habits a team already has, starting with the TAK devices they carry.</p></div>
      <div><span class="mono">02</span><h3>Open standards</h3><p>MAVLink in, Cursor-on-Target out. Your aircraft and your data are never locked to us.</p></div>
      <div><span class="mono">03</span><h3>Honest about testing</h3><p>Simulation, hardware-in-the-loop, then flight. We say which stage each capability has reached.</p></div>
    </div>
  </div>
</section>
{CTA}</main>
""" + FOOT

# ------------------------------------------------------------------ CONTACT
contact = head("Contact | Edgeward",
               "Talk to Edgeward about custom drone software and TAK integration.",
               "contact.html") + f"""<main>
<section class="page-head"><div class="wrap"><p class="eyebrow">Contact</p><h1>Let's talk about your drone program.</h1><p class="lead">Tell us what you fly, who flies it and what you want it to do. We'll come back with a plan built around you.</p></div></section>
<section>
  <div class="wrap contact-grid">
    <div class="contact-box rv">
      <p class="mono">Email</p>
      <p><a class="big" href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p class="muted" style="margin-top:24px">Based in Alberta. Working with teams across Canada.</p>
      <p style="margin:0"><a href="{LI}">LinkedIn</a> · <a href="{IG}">Instagram</a> · <a href="{YT}">YouTube</a></p>
    </div>
    <div class="contact-box rv">
      <p class="mono">Helpful to include</p>
      <ul>
        <li>Your aircraft and autopilot</li>
        <li>Whether your team already uses ATAK or WinTAK</li>
        <li>What you need the aircraft or the map to do</li>
        <li>Your timeline</li>
      </ul>
    </div>
  </div>
</section>
</main>
""" + FOOT

for name, html in [("index.html", index), ("capabilities.html", caps), ("about.html", about), ("contact.html", contact)]:
    (ROOT / name).write_text(html)
    print("wrote", name, len(html))
