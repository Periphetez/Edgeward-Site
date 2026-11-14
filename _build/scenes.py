"""Animated SVG graphics for the Edgeward site (concept views)."""
import math, random

W = "#F4F4F1"; SAGE = "#9DC183"; LIME = "#C5E86C"; ORG = "#E07B39"
INK = "#0C0E0D"; MUT = "#9AA09C"; RULE = "#333936"; PANEL = "rgba(9,11,10,.93)"
MONO = "'JetBrains Mono',ui-monospace,Menlo,monospace"
SANS = "Inter,system-ui,sans-serif"
GLYPH = "M0,-8 L2,-2 L8,1 L8,3 L2,2 L1.5,6 L4,8 L4,9 L0,8 L-4,9 L-4,8 L-1.5,6 L-2,2 L-8,3 L-8,1 L-2,-2 Z"


def T(x, y, s, size=14, fill=W, mono=True, weight=None, anchor=None, extra=""):
    a = f' text-anchor="{anchor}"' if anchor else ""
    w = f' font-weight="{weight}"' if weight else ""
    ls = 1.2 if mono else -0.3
    fam = MONO if mono else SANS
    return (f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}" fill="{fill}"'
            f' letter-spacing="{ls}"{a}{w}{extra}>{s}</text>')


def P(pts):
    return "M" + " L".join(f"{x},{y}" for x, y in pts)


def vis(frm, to, dur, fade=0.025):
    """Opacity animation: visible between fractions frm..to of a dur-second loop."""
    a, b = min(frm + fade, to), max(to - fade, frm)
    return (f'<animate attributeName="opacity" dur="{dur}s" repeatCount="indefinite" '
            f'values="0;0;1;1;0;0" keyTimes="0;{frm};{a};{b};{to};1"/>')


def route(d, col=W, w=34, dash=None, op=.12, pts=()):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    s = (f'<path d="{d}" fill="none" stroke="{col}" stroke-opacity="{op}" stroke-width="{w}" '
         f'stroke-linejoin="round" stroke-linecap="round"/>'
         f'<path d="{d}" fill="none" stroke="{col}" stroke-width="1.6"{da} stroke-linejoin="round"/>')
    for x, y in pts:
        s += f'<circle cx="{x}" cy="{y}" r="4" fill="{INK}" stroke="{col}" stroke-width="1.5"/>'
    return s


def air(path, dur, label, col=W, begin=0, s=1.0, fs=13):
    mp = f'<animateMotion dur="{dur}s" begin="{begin}s" repeatCount="indefinite" path="{path}"'
    return (f'<g>{mp}/><circle r="{26*s}" fill="{col}" opacity=".10"/>'
            f'<path d="M{-14*s},{8*s} V{-2*s} A{14*s},{14*s} 0 0 1 {14*s},{-2*s} V{8*s} Z" '
            f'fill="{INK}" fill-opacity=".92" stroke="{col}" stroke-width="2"/>'
            f'{T(20*s, -12*s, label, fs*s, col)}</g>'
            f'<g>{mp} rotate="auto"/><path transform="rotate(90) scale({s}) translate(0,1)" d="{GLYPH}" fill="{col}"/></g>')


def hatch(pid):
    return (f'<pattern id="{pid}" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
            f'<rect width="10" height="10" fill="{ORG}" fill-opacity=".06"/>'
            f'<line x1="0" y1="0" x2="0" y2="10" stroke="{ORG}" stroke-opacity=".35" stroke-width="2"/></pattern>')


def nfz(pts, label, pid, fs=13):
    x = sum(p[0] for p in pts) / len(pts); y = sum(p[1] for p in pts) / len(pts)
    return (f'<path d="{P(pts)}Z" fill="url(#{pid})" stroke="{ORG}" stroke-width="1.8" stroke-dasharray="8 5"/>'
            + T(x, y + 4, label, fs, ORG, anchor="middle"))


def team(x, y, label, fs=12):
    return (f'<g transform="translate({x},{y})"><circle r="11" fill="{INK}" fill-opacity=".9" stroke="{SAGE}" stroke-width="2"/>'
            f'<circle r="3.5" fill="{SAGE}"/>{T(17, 5, label, fs, SAGE)}</g>')


def pulse(x, y, col, delay=0, r0=12, r1=58, dur=2.4):
    return (f'<circle cx="{x}" cy="{y}" r="{r0}" fill="none" stroke="{col}" stroke-width="2">'
            f'<animate attributeName="r" values="{r0};{r1}" dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values=".9;0" dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/></circle>')


def find(x, y, label, fs=12):
    return (f'<g transform="translate({x},{y})"><circle r="19" fill="none" stroke="{LIME}" stroke-opacity=".5" stroke-width="1.5"/>'
            f'<path d="M0,-11 L11,0 L0,11 L-11,0Z" fill="{INK}" fill-opacity=".92" stroke="{LIME}" stroke-width="2"/>'
            f'<circle r="3" fill="{LIME}"/>{T(30, 5, label, fs, LIME)}</g>')


def lawn(x0, y0, w, h, n):
    pts = [(x0, y0)]
    for i in range(n):
        y = round(y0 + i * h / (n - 1)); x = x0 + w if i % 2 == 0 else x0
        pts.append((x, y))
        if i < n - 1:
            pts.append((x, round(y0 + (i + 1) * h / (n - 1))))
    return pts


def panel(x, y, w, h):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{PANEL}" stroke="{RULE}"/>'


def row(x, y, w, k, v, vcol=W, size=14):
    return (f'<line x1="{x}" y1="{y-21}" x2="{x+w}" y2="{y-21}" stroke="{RULE}"/>'
            + T(x, y, k, size - 2, MUT) + T(x + w, y, v, size, vcol, anchor="end"))


def north(x, y):
    return (f'<g transform="translate({x},{y})"><circle r="20" fill="{INK}" fill-opacity=".7" stroke="{RULE}"/>'
            f'<path d="M0,-13 L6,6 L0,2 L-6,6Z" fill="{W}"/></g>')


def svg(vb, body, label, cls="scene"):
    return (f'<svg class="{cls}" viewBox="0 0 {vb[0]} {vb[1]}" preserveAspectRatio="xMidYMid slice" '
            f'role="img" aria-label="{label}">{body}</svg>')


# ------------------------------------------------------------------ HERO
def hero():
    r1 = [(300, 120), (620, 260), (900, 330), (1240, 420), (1520, 380)]
    r2 = [(1500, 820), (1330, 640), (1180, 500), (980, 420), (820, 120)]
    r3 = [(1580, 560), (1400, 560), (1300, 700), (1080, 820)]
    lw = lawn(640, 520, 300, 200, 6)
    sar = [(380, 820), (560, 640)] + lw
    b = f'<defs>{hatch("hh")}<radialGradient id="hg"><stop offset="0" stop-color="{ORG}" stop-opacity=".45"/><stop offset="1" stop-color="{ORG}" stop-opacity="0"/></radialGradient></defs>'
    b += '<image href="assets/img/terrain-hero.jpg" width="1600" height="900"/>'
    b += nfz([(1010, 120), (1150, 95), (1210, 210), (1120, 290), (1000, 250)], "NO-FLY · HELIPAD", "hh")
    b += (f'<rect x="626" y="506" width="328" height="228" fill="{LIME}" fill-opacity=".05" stroke="{LIME}" stroke-opacity=".5" stroke-dasharray="3 5"/>'
          f'<path d="{P(lw)}" fill="none" stroke="{LIME}" stroke-opacity=".5" stroke-width="1.3"/>')
    b += route(P(sar[:3]), LIME, 26, None, .08, [sar[1]])
    b += route(P(r1), W, 34, None, .12, r1[1:-1])
    b += route(P(r2), W, 34, None, .12, r2[1:-1])
    b += route(P(r3), W, 30, "6 6", .07, r3[1:-1])
    b += f'<circle cx="1110" cy="455" r="70" fill="url(#hg)"/>'
    b += (f'<path d="M1180,500 C1260,520 1290,600 1240,660" fill="none" stroke="{SAGE}" stroke-width="2.2" stroke-dasharray="7 6"/>'
          + T(1262, 606, "REROUTE · +38 S", 12, SAGE))
    b += f'<circle cx="1110" cy="455" r="26" fill="none" stroke="{ORG}" stroke-width="2"/>'
    b += pulse(1110, 455, ORG) + pulse(1110, 455, ORG, 1.2)
    b += pulse(820, 600, LIME, .4) + pulse(905, 690, LIME, 1.6)
    b += find(820, 600, "PERSON · 0.91") + find(905, 690, "VEHICLE · 0.88")
    b += team(470, 760, "GND TEAM A") + team(1360, 780, "GND TEAM B")
    b += air(P(r1), 44, "EW-02 · 140 M")
    b += air(P(r1[::-1]), 52, "EW-01 · 110 M", begin=-20)
    b += air(P(r2), 38, "EW-03 · 120 M", begin=-10)
    b += air(P(r3), 30, "EW-04 · 90 M", begin=-5)
    b += air(P(sar), 60, "SAR-2 · SEARCH", LIME, begin=-8)
    b += north(1545, 60)
    return svg((1600, 900), b, "Concept view of the Edgeward common operating picture: aircraft moving on planned routes, "
               "a predicted conflict with a reroute, a no-fly zone, a search pattern and two detections", "scene hero-map")


# ------------------------------------------------------------------ DECONFLICTION
def decon():
    D = 14
    r1 = [(60, 640), (330, 470), (560, 385), (800, 350), (1160, 310)]
    r2a = "M150,70 L370,230"
    r2mid = "M370,230 L560,385 L700,540"
    r2c = "M700,540 L880,720"
    rr = "M370,230 C470,200 620,250 650,310 C675,360 655,440 700,540"
    fly2 = "M150,70 L370,230 C470,200 620,250 650,310 C675,360 655,440 700,540 L880,720"
    b = f'<defs>{hatch("dh")}<radialGradient id="dg"><stop offset="0" stop-color="{ORG}" stop-opacity=".5"/><stop offset="1" stop-color="{ORG}" stop-opacity="0"/></radialGradient></defs>'
    b += '<image href="assets/img/terrain-a.jpg" x="0" y="-75" width="1200" height="900"/>'
    b += nfz([(900, 500), (1080, 480), (1140, 640), (1000, 700), (890, 625)], "RESTRICTED", "dh", 14)
    b += route(P(r1), W, 36, None, .12, r1[1:-1])
    b += route(r2a, SAGE, 36, None, .12) + route(r2c, SAGE, 36, None, .12, [(700, 540)])
    b += f'<path d="{r2mid}" fill="none" stroke="{MUT}" stroke-opacity=".55" stroke-width="1.6" stroke-dasharray="3 7"/>'
    b += f'<path d="{rr}" fill="none" stroke="{SAGE}" stroke-opacity=".12" stroke-width="36" stroke-linecap="round"/>'
    b += f'<path d="{rr}" fill="none" stroke="{SAGE}" stroke-width="2.6" stroke-dasharray="9 6"/>'
    b += f'<circle cx="370" cy="230" r="4" fill="{INK}" stroke="{SAGE}" stroke-width="1.5"/>'
    b += f'<g opacity="0">{vis(0, .34, D)}<circle cx="560" cy="385" r="95" fill="url(#dg)"/><circle cx="560" cy="385" r="30" fill="none" stroke="{ORG}" stroke-width="2.4"/>{pulse(560, 385, ORG, 0, 30, 80, 1.8)}</g>'
    b += f'<g opacity="0">{vis(0, .27, D)}{T(596, 222, "PROPOSED · +2 MIN", 15, SAGE)}</g>'
    b += f'<g opacity="0">{vis(.27, 1, D)}{T(596, 222, "APPROVED · REROUTING", 15, LIME)}</g>'
    b += air(P(r1), D, "EW-01", W, begin=-4.5, s=1.25, fs=13)
    b += air(fly2, D, "EW-02", SAGE, s=1.25, fs=13)
    # panel
    x, y, w = 800, 34, 366
    b += panel(x, y, w, 232)
    b += f'<g opacity="0">{vis(0, .27, D)}{T(x+22, y+38, "● CONFLICT PREDICTED", 14, ORG)}</g>'
    b += f'<g opacity="0">{vis(.27, 1, D)}{T(x+22, y+38, "● REROUTE APPROVED", 14, LIME)}</g>'
    b += T(x + 22, y + 78, "EW-01 × EW-02", 30, W, mono=False, weight=700)
    b += f'<g opacity="0">{vis(0, .27, D)}{T(x+22, y+106, "Loss of separation in 2 min 14 s", 16, "#CDD3CD", mono=False)}</g>'
    b += f'<g opacity="0">{vis(.27, 1, D)}{T(x+22, y+106, "Separation holds at 310 m", 16, "#CDD3CD", mono=False)}</g>'
    b += row(x + 22, y + 150, w - 44, "FIX", "Reroute EW-02 · +2 min", SAGE)
    b += f'<line x1="{x+22}" y1="{y+166}" x2="{x+w-22}" y2="{y+166}" stroke="{RULE}"/>'
    b += (f'<rect x="{x+22}" y="{y+180}" width="112" height="36" rx="7" fill="{SAGE}"/>'
          + T(x + 78, y + 204, "Approve", 15, INK, mono=False, weight=600, anchor="middle")
          + f'<rect x="{x+22}" y="{y+180}" width="112" height="36" rx="7" fill="#fff" opacity="0"><animate attributeName="opacity" dur="{D}s" repeatCount="indefinite" values="0;0;.7;0;0" keyTimes="0;.24;.265;.31;1"/></rect>'
          + f'<rect x="{x+146}" y="{y+180}" width="100" height="36" rx="7" fill="none" stroke="#4A524E"/>'
          + T(x + 196, y + 204, "Cancel", 15, W, mono=False, weight=600, anchor="middle"))
    b += north(60, 60)
    return svg((1200, 750), b, "Concept view: two aircraft on conflicting routes; the operator approves a reroute and the second aircraft flies around the conflict")


# ------------------------------------------------------------------ COP TABLET
def cop():
    D = 12
    ra = [(90, 340), (250, 250), (520, 170), (700, 215)]
    rb = [(900, 560), (620, 430), (440, 300)]
    rc = [(130, 110), (250, 250), (320, 540)]
    b = (f'<defs>{hatch("ch")}<radialGradient id="cbg" cx=".5" cy=".4" r=".8"><stop offset="0" stop-color="#1B1F1D"/><stop offset="1" stop-color="#070808"/></radialGradient>'
         f'<linearGradient id="cfr" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#30353A"/><stop offset="1" stop-color="#131516"/></linearGradient>'
         f'<clipPath id="ccl"><rect x="98" y="78" width="1004" height="594" rx="14"/></clipPath></defs>')
    b += '<rect width="1200" height="750" fill="url(#cbg)"/>'
    b += '<rect x="70" y="50" width="1060" height="650" rx="46" fill="url(#cfr)" stroke="#3A4044"/>'
    b += '<rect x="84" y="64" width="1032" height="622" rx="34" fill="#050606"/>'
    b += '<circle cx="600" cy="71" r="3" fill="#1d2225"/>'
    s = '<image href="assets/img/terrain-b.jpg" x="-150" y="-120" width="1300" height="836"/>'
    s += nfz([(60, 430), (190, 420), (210, 530), (80, 545)], "NFZ", "ch", 12)
    s += route(P(rc), LIME, 22, None, .09, rc[1:-1])
    s += route(P(ra), W, 22, None, .11, ra[1:-1])
    s += route(P(rb), W, 22, "6 5", .08, rb[1:-1])
    s += pulse(430, 400, LIME, 0, 10, 46) + find(430, 400, "PERSON")
    s += team(420, 520, "TEAM A") + team(790, 390, "TEAM B") + team(70, 200, "CP")
    s += air(P(ra), 20, "EW-01", W, s=.95)
    s += air(P(ra[::-1]), 24, "EW-02", W, begin=-11, s=.95)
    s += air(P(rb), 16, "EW-03", W, begin=-3, s=.95)
    s += air(P(rc), 18, "SAR-2", LIME, begin=-6, s=.95)
    # status bar
    s += f'<rect width="1004" height="42" fill="{PANEL}"/><line x1="0" y1="42" x2="1004" y2="42" stroke="{RULE}"/>'
    s += T(18, 27, "COP", 13, W) + T(70, 27, "5 AIRCRAFT", 13, MUT) + T(190, 27, "3 TEAMS", 13, MUT) + T(284, 27, "1 FIND", 13, LIME)
    s += T(986, 27, "● LINK OK", 13, SAGE, anchor="end")
    # chat
    x, y, w = 676, 58, 312
    s += panel(x, y, w, 246) + T(x + 16, y + 28, "CHAT · EDGEWARD", 12, MUT)
    s += (f'<g opacity="0">{vis(.08, .97, D)}<rect x="{x+12}" y="{y+42}" width="{w-24}" height="60" rx="10" fill="#1A1D1C"/>'
          + T(x + 24, y + 66, "SAR-2", 14, LIME, mono=False, weight=700) + T(x + 76, y + 66, "person detected · 0.91", 14, W, mono=False)
          + T(x + 24, y + 88, "Marker dropped. Team A 420 m.", 14, "#CDD3CD", mono=False) + '</g>')
    s += (f'<g opacity="0">{vis(.3, .97, D)}<rect x="{x+12}" y="{y+110}" width="{w-24}" height="60" rx="10" fill="#1A1D1C"/>'
          + T(x + 24, y + 134, "EW-03", 14, W, mono=False, weight=700) + T(x + 76, y + 134, "off plan 134 m", 14, W, mono=False)
          + T(x + 24, y + 156, "Reroute proposed.", 14, "#CDD3CD", mono=False) + '</g>')
    s += (f'<g opacity="0">{vis(.55, .97, D)}<rect x="{x+116}" y="{y+180}" width="{w-128}" height="42" rx="10" fill="{SAGE}"/>'
          + T(x + 132, y + 207, "APPROVE EW-03", 14, INK, mono=False, weight=700) + '</g>')
    b += f'<g clip-path="url(#ccl)"><g transform="translate(98,78)">{s}</g></g>'
    return svg((1200, 750), b, "Concept view: a rugged tablet showing every aircraft, ground team and find on one TAK map, with alerts arriving in chat")


# ------------------------------------------------------------------ DETECTION
def bbox(x, y, w, h, label, col):
    c = 15
    p = (f"M{x},{y+c} V{y} H{x+c} M{x+w-c},{y} H{x+w} V{y+c} M{x+w},{y+h-c} V{y+h} H{x+w-c} M{x+c},{y+h} H{x} V{y+h-c}")
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{col}" fill-opacity=".10" stroke="{col}" stroke-opacity=".5"/>'
            f'<path d="{p}" fill="none" stroke="{col}" stroke-width="3"/>'
            f'<rect x="{x}" y="{y-28}" width="{len(label)*9.4+18}" height="24" fill="{col}"/>' + T(x + 9, y - 11, label, 14, INK, weight=600))


def det():
    D = 10
    b = (f'<defs><linearGradient id="sl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{LIME}" stop-opacity="0"/>'
         f'<stop offset=".85" stop-color="{LIME}" stop-opacity=".14"/><stop offset="1" stop-color="{LIME}" stop-opacity=".5"/></linearGradient></defs>')
    b += '<image href="assets/img/aerial-sensor.jpg" x="0" y="-75" width="1200" height="900"/>'
    # subjects
    b += '<ellipse cx="747" cy="366" rx="7" ry="5" fill="#000" opacity=".45"/><ellipse cx="742" cy="361" rx="6" ry="9" fill="#E07B39"/><circle cx="742" cy="350" r="4.5" fill="#E9D3BC"/>'
    b += '<g transform="rotate(-25 913 418)"><rect x="903" y="399" width="26" height="46" rx="5" fill="#000" opacity=".4"/><rect x="900" y="395" width="26" height="46" rx="5" fill="#B9BEBA"/><rect x="904" y="407" width="18" height="14" rx="2" fill="#2A2E2C"/></g>'
    b += f'<rect x="0" y="-120" width="1200" height="120" fill="url(#sl)"><animate attributeName="y" values="-120;750" dur="3.4s" repeatCount="indefinite"/></rect>'
    b += f'<g opacity="0">{vis(.14, .97, D)}{bbox(716, 331, 52, 58, "PERSON 0.91", LIME)}</g>'
    b += f'<g opacity="0">{vis(.3, .97, D)}{bbox(880, 384, 66, 70, "VEHICLE 0.88", W)}</g>'
    b += f'<g stroke="{W}" stroke-opacity=".55" stroke-width="1.4"><line x1="600" y1="355" x2="600" y2="395"/><line x1="580" y1="375" x2="620" y2="375"/></g>'
    b += f'<g stroke="{W}" stroke-width="3" fill="none"><path d="M26,76 V26 H76"/><path d="M1124,26 H1174 V76"/><path d="M1174,674 V724 H1124"/><path d="M76,724 H26 V674"/></g>'
    b += T(52, 60, "EW-SAR-2 · EO · 120 M AGL", 15, W)
    b += f'<g>{T(1148, 60, "● REC", 15, ORG, anchor="end")}<animate attributeName="opacity" values="1;.2;1" dur="1.4s" repeatCount="indefinite"/></g>'
    b += T(52, 704, "HDG 274 · GS 14 M/S · SEARCH LEG 4 / 6", 14, W)
    x, y, w = 792, 500, 372
    b += f'<g opacity="0">{vis(.42, .97, D)}<path d="M768,372 L{x+40},{y}" stroke="{LIME}" stroke-opacity=".6" stroke-dasharray="4 5" fill="none"/>'
    b += panel(x, y, w, 196)
    b += T(x + 22, y + 36, "● FIND #04 · SENT TO TAK", 14, LIME)
    b += T(x + 22, y + 72, "Person detected", 27, W, mono=False, weight=700)
    b += row(x + 22, y + 112, w - 44, "POSITION", "53.5412 N 113.9871 W")
    b += row(x + 22, y + 144, w - 44, "CONFIDENCE", "0.91")
    b += row(x + 22, y + 176, w - 44, "NEAREST TEAM", "Team A · 420 m", SAGE)
    b += '</g>'
    return svg((1200, 750), b, "Concept view: the aircraft camera scans a forest clearing, boxes a person and a vehicle, and sends the find with its position to TAK")


# ------------------------------------------------------------------ DETECT AND AVOID
def daa():
    D = 12
    rnd = random.Random(4)
    ridges = ""
    for i, (base, amp, col) in enumerate([(540, 44, "#1E2325"), (590, 32, "#141819"), (640, 26, "#0A0C0C")]):
        pts = [(x, round(base - amp * abs(math.sin(x / (150 + i * 55) + i * 1.3)) - rnd.random() * 9)) for x in range(-400, 1640, 24)]
        ridges += f'<path d="M-400,1300 L' + " L".join(f"{x},{y}" for x, y in pts) + f' L1640,1300Z" fill="{col}"/>'
    b = ('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0A0F12"/><stop offset=".42" stop-color="#1A2429"/>'
         '<stop offset=".6" stop-color="#4B5554"/><stop offset=".68" stop-color="#8C7B5F"/><stop offset="1" stop-color="#8C7B5F"/></linearGradient>'
         f'<radialGradient id="sun"><stop offset="0" stop-color="#E9A568" stop-opacity=".6"/><stop offset="1" stop-color="#E9A568" stop-opacity="0"/></radialGradient></defs>')
    world = ('<rect x="-400" y="-500" width="2040" height="1500" fill="url(#sky)"/>'
             '<ellipse cx="860" cy="545" rx="420" ry="150" fill="url(#sun)"/>' + ridges)
    b += (f'<g>{world}<animateTransform attributeName="transform" type="rotate" dur="{D}s" repeatCount="indefinite" '
          f'values="0 600 400;0 600 400;9 600 400;9 600 400;0 600 400" keyTimes="0;.5;.6;.86;1" calcMode="spline" '
          f'keySplines="0 0 1 1;.4 0 .2 1;0 0 1 1;.4 0 .2 1"/></g>')
    # intruder: constant bearing, growing; then slides away as we turn
    plane = ('<g fill="#07090A"><rect x="-62" y="-13" width="124" height="5" rx="2"/><ellipse cx="0" cy="0" rx="9" ry="11"/>'
             '<rect x="-1.6" y="-34" width="3.2" height="24"/><rect x="-23" y="-24" width="46" height="2.6" rx="1"/>'
             '<path d="M-30,-9 L-7,5 L-5,3 L-28,-10Z M30,-9 L7,5 L5,3 L28,-10Z"/>'
             '<path d="M-6,8 L-15,21 L-13,22 L-4,9Z M6,8 L15,21 L13,22 L4,9Z"/><circle cx="-15" cy="22" r="3.2"/><circle cx="15" cy="22" r="3.2"/></g>'
             '<circle r="13" fill="none" stroke="#07090A" stroke-opacity=".35" stroke-width="1.5"/>')
    box = (f'<rect x="-84" y="-56" width="168" height="100" fill="none" stroke="{ORG}" stroke-width="2.5" vector-effect="non-scaling-stroke"/>')
    lab = lambda txt, a, z: f'<g opacity="0">{vis(a, z, D, .01)}<rect x="-106" y="-112" width="250" height="28" fill="{ORG}"/>{T(-94, -92, txt, 15, INK, weight=600)}</g>'
    b += (f'<g opacity="0">{vis(.01, .84, D)}<g><animateTransform attributeName="transform" type="translate" dur="{D}s" repeatCount="indefinite" '
          f'values="800,300;800,300;1520,410;1520,410" keyTimes="0;.5;.8;1" calcMode="spline" keySplines="0 0 1 1;.4 0 .6 1;0 0 1 1"/>'
          f'<g><animateTransform attributeName="transform" type="scale" dur="{D}s" repeatCount="indefinite" values=".4;1.25;1.25" keyTimes="0;.5;1"/>{plane}{box}</g>'
          + lab("INTRUDER · TCPA 18 S", 0, .17) + lab("INTRUDER · TCPA 12 S", .17, .34) + lab("INTRUDER · TCPA 7 S", .34, .5) + lab("AVOIDING · TURN LEFT", .5, .84)
          + '</g></g>')
    # reticle + tape (fixed to our aircraft)
    b += f'<g transform="translate(600,400)" stroke="{W}" stroke-width="2" fill="none" opacity=".9"><path d="M-70,0 H-22 M22,0 H70 M0,-9 V9"/><circle r="4"/></g>'
    tape = ""
    for i in range(21):
        x = 100 + i * 50
        tape += f'<line x1="{x}" y1="64" x2="{x}" y2="{76 if i % 2 else 84}" stroke="{W}" stroke-opacity=".7"/>'
        if i % 2 == 0:
            tape += T(x, 52, f"{(10*i) % 360:03d}", 12, W, anchor="middle", extra=' opacity=".8"')
    b += tape + f'<path d="M600,88 l-8,12 h16z" fill="{LIME}"/>'
    b += (f'<g opacity="0">{vis(.42, .84, D)}<path d="M600,440 C540,462 430,462 330,424" fill="none" stroke="{SAGE}" stroke-width="3" stroke-dasharray="10 8"/>'
          f'<path d="M322,420 l20,-6 l-6,16z" fill="{SAGE}"/>{T(330, 396, "AVOID · TURN LEFT 30°", 15, SAGE)}</g>')
    x, y, w = 40, 128, 336
    b += panel(x, y, w, 196)
    b += f'<g opacity="0">{vis(0, .84, D)}{T(x+22, y+36, "● TRAFFIC ALERT", 14, ORG)}{T(x+22, y+72, "Collision course", 27, W, mono=False, weight=700)}</g>'
    b += f'<g opacity="0">{vis(.84, 1, D)}{T(x+22, y+36, "● CLEAR OF TRAFFIC", 14, LIME)}{T(x+22, y+72, "Traffic avoided", 27, W, mono=False, weight=700)}</g>'
    b += row(x + 22, y + 112, w - 44, "BEARING", "038° R · steady")
    b += row(x + 22, y + 144, w - 44, "SENSOR", "1 camera · onboard")
    b += row(x + 22, y + 176, w - 44, "ACTION", "Alert, then avoid", SAGE)
    return svg((1200, 750), b, "Concept view: the onboard camera tracks an approaching aircraft on a constant bearing, alerts, then turns away")
