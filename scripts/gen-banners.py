import xml.etree.ElementTree as ET

def build(p):
    D = p["cube_top"]; Lp = p["cube_left"]; Rp = p["cube_right"]
    GD = p["gold_top"]; GL = p["gold_left"]; GR = p["gold_right"]
    cubes_x = [210, 380, 550, 720, 890, 1060]
    heights = [90, 120, 150, 110, 130, 100]
    BASE = 520

    def cube(cx, h, gold):
        y = BASE - h
        w, d = 44, 26
        t, l, r = (GD, GL, GR) if gold else (D, Lp, Rp)
        lift = 14 if gold else 8
        dur = 5 if gold else 6.5
        return f'''<g><animateTransform attributeName="transform" type="translate" values="0,0;0,-{lift};0,0" dur="{dur}s" repeatCount="indefinite" additive="sum"/>
  <polygon points="{cx-w},{y-d} {cx},{y} {cx+w},{y-d} {cx},{y-2*d}" fill="{t}"/>
  <polygon points="{cx-w},{y-d} {cx},{y} {cx},{y-h} {cx-w},{y-h-d}" fill="{l}"/>
  <polygon points="{cx},{y} {cx+w},{y-d} {cx+w},{y-h-d} {cx},{y-h}" fill="{r}"/>
</g>'''

    path = 'M -40 500 C 150 360, 250 355, 300 370 C 420 330, 470 330, 545 340 C 640 320, 700 320, 790 340 C 890 340, 950 350, 1035 362 C 1120 372, 1230 388, 1460 430'

    parts = []
    parts.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 640" role="img" aria-labelledby="t">
<title id="t">Hidden Alchemy — idea-to-reality pipeline, animated 3D scene</title>
<defs>
  <radialGradient id="aura" cx="50%" cy="42%" r="65%">
    <stop offset="0%" stop-color="{p['aurora1']}"/>
    <stop offset="55%" stop-color="{p['aurora2']}"/>
    <stop offset="100%" stop-color="{p['bg']}" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="titleGrad" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{p['gold1']}"/>
    <stop offset="0.5" stop-color="{p['aqua1']}"/>
    <stop offset="1" stop-color="{p['gold2']}"/>
  </linearGradient>
  <linearGradient id="sheen" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="rgba(255,255,255,0)"/>
    <stop offset="0.5" stop-color="{p['sheen']}"/>
    <stop offset="1" stop-color="rgba(255,255,255,0)"/>
  </linearGradient>
  <filter id="soft" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="14"/></filter>
  <filter id="glow" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="7" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="crypt" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="24"/></filter>
</defs>
<rect width="1400" height="640" fill="{p['bg']}"/>
<rect width="1400" height="640" fill="url(#aura)"><animate attributeName="opacity" values="0.55;0.9;0.55" dur="8s" repeatCount="indefinite"/></rect>
<circle cx="705" cy="320" r="380" fill="none" stroke="{p['halo']}" stroke-width="1.5" opacity="0.35">
  <animate attributeName="r" values="340;430;340" dur="11s" repeatCount="indefinite"/>
  <animate attributeName="opacity" values="0.5;0.08;0.5" dur="11s" repeatCount="indefinite"/>
</circle>
<circle cx="705" cy="320" r="300" fill="none" stroke="{p['halo2']}" stroke-width="1" opacity="0.3" stroke-dasharray="4 14">
  <animate attributeName="r" values="260;340;260" dur="14s" repeatCount="indefinite"/>
  <animateTransform attributeName="transform" type="rotate" from="0 705 320" to="360 705 320" dur="60s" repeatCount="indefinite"/>
</circle>''')

    floor = []
    for i in range(-7, 8):
        x = 705 + i * 130
        floor.append(f'<line x1="{x}" y1="545" x2="{705 + i * 60}" y2="662" stroke="{p["grid"]}" stroke-width="1.5"/>')
    for yy in range(500, 641, 18):
        floor.append(f'<line x1="0" y1="{yy}" x2="1400" y2="{yy}" stroke="{p["grid"]}" stroke-width="1"/>')
    parts.append(''.join(floor))

    parts.append(f'''<g font-family="Segoe UI, system-ui, -apple-system, sans-serif">
<text x="705" y="92" text-anchor="middle" font-size="24" letter-spacing="9" font-weight="600" fill="{p['over']}">OPEN ENGINEERING LABORATORY · EST. 2026</text>
<circle cx="1226" cy="74" r="6" fill="{p['live']}"><animate attributeName="opacity" values="1;0.15;1" dur="1.6s" repeatCount="indefinite"/></circle>
<text x="1242" y="80" text-anchor="start" font-family="Menlo, Consolas, monospace" font-size="17" letter-spacing="2" font-weight="700" fill="{p['live']}">LIVE</text>
<text x="705" y="200" text-anchor="middle" font-size="112" font-weight="800" letter-spacing="-3" fill="url(#titleGrad)">Hidden Alchemy</text>
<text x="705" y="256" text-anchor="middle" font-family="Georgia, 'Times New Roman', serif" font-style="italic" font-size="34" fill="{p['tagline']}">raw ideas, forged into real systems</text>
</g>
<rect x="900" y="120" width="420" height="112" fill="url(#sheen)" filter="url(#soft)" opacity="0.9">
  <animate attributeName="x" values="900;-200;900" dur="8s" repeatCount="indefinite"/>
</rect>''')

    parts.append(f'''<g>
<path id="fly" d="{path}" fill="none" stroke="{p['flow']}" stroke-width="3" stroke-linecap="round" stroke-dasharray="26 30">
  <animate attributeName="stroke-dashoffset" values="0;-440" dur="6s" repeatCount="indefinite"/>
</path>
<path d="{path}" fill="none" stroke="{p['flowSoft']}" stroke-width="8" filter="url(#crypt)" opacity="0.4"/>
<g filter="url(#glow)">
  <circle r="14" fill="{p['orb1']}" opacity="0.3"><animateMotion dur="7s" repeatCount="indefinite" path="{path}"/></circle>
  <circle r="7" fill="{p['orb1']}"><animateMotion dur="7s" repeatCount="indefinite" path="{path}"/></circle>
  <circle r="3" fill="#ffffff" opacity="0.9"><animateMotion dur="7s" repeatCount="indefinite" path="{path}"/></circle>
</g>
<g filter="url(#glow)">
  <circle r="5" fill="{p['orb2']}"><animateMotion dur="12s" begin="-4s" repeatCount="indefinite" path="{path}"/></circle>
</g>
<g filter="url(#glow)">
  <circle r="4" fill="{p['orb3']}"><animateMotion dur="16s" begin="-9s" repeatCount="indefinite" path="{path}"/></circle>
</g>
</g>''')

    cubes = []
    for i, (cx, h) in enumerate(zip(cubes_x, heights)):
        cubes.append(cube(cx, h, gold=(i == 1)))
    parts.append('<g>' + ''.join(cubes) + '</g>')

    labels = '<g font-family="Menlo, Consolas, monospace" text-anchor="middle">' + (
        f'<text x="{cubes_x[1]}" y="{BASE + 34}" font-size="17" font-weight="800" fill="{p["gold1"]}" filter="url(#glow)"><tspan>CONCEPT</tspan><tspan x="{cubes_x[1]}" dy="18" font-size="13" font-weight="600">— current —</tspan></text>')
    for i, cx in enumerate(cubes_x):
        if i == 1:
            continue
        names = ["IDEA", "ARCHITECTURE", "SYSTEM", "AUTOMATION", "REALITY"]
        labels += f'<text x="{cx}" y="{BASE + 40}" font-size="14" fill="{p["lab"]}">{names[i - 1 if i > 1 else 0]}</text>'
    labels += '</g>'
    parts.append(labels)

    cx, cy = cubes_x[1], BASE - heights[1] - 30
    parts.append(f'''<ellipse cx="{cx}" cy="{cy}" rx="92" ry="36" fill="none" stroke="{p['ring']}" stroke-width="2.5" opacity="0.9">
  <animateTransform attributeName="transform" type="rotate" values="0 {cx} {cy};360 {cx} {cy}" dur="10s" repeatCount="indefinite"/>
</ellipse>
<g filter="url(#glow)">
  <circle r="4.5" fill="{p['ringDot']}">
    <animateMotion dur="10s" repeatCount="indefinite" path="M {cx-92} {cy} A 92 36 0 1 1 {cx+92} {cy} A 92 36 0 1 1 {cx-92} {cy}"/>
  </circle>
</g>''')

    parts.append(f'''<line x1="0" y1="0" x2="1400" y2="0" stroke="{p['scan']}" stroke-width="2" opacity="0.5">
  <animate attributeName="y1" values="-8;652;-8" dur="6.5s" repeatCount="indefinite"/>
  <animate attributeName="y2" values="-8;652;-8" dur="6.5s" repeatCount="indefinite"/>
</line>''')

    parts.append('</svg>')
    return ''.join(parts)

light = {
    "bg": "#ffffff", "aurora1": "rgba(189,156,97,0.12)", "aurora2": "rgba(76,107,92,0.10)",
    "grid": "rgba(60,90,75,0.10)", "over": "#6E7781", "tagline": "#57606A",
    "gold1": "#BD9C61", "gold2": "#8A6F3F", "aqua1": "#4C6B5C", "sheen": "rgba(255,255,255,0.85)",
    "halo": "rgba(189,156,97,0.5)", "halo2": "rgba(76,107,92,0.45)", "live": "#1a7f37",
    "flow": "#4C6B5C", "flowSoft": "rgba(76,107,92,0.2)", "orb1": "#BD9C61", "orb2": "#2DA44E", "orb3": "#4C6B5C",
    "ring": "#BD9C61", "ringDot": "#E6C078", "scan": "rgba(189,156,97,0.35)",
    "cube_top": "#7FAE94", "cube_left": "#69A084", "cube_right": "#52876A",
    "gold_top": "#E6C078", "gold_left": "#D3AC62", "gold_right": "#BD9C61",
    "lab": "#6E7781",
}

dark = {
    "bg": "#0B0E14", "aurora1": "rgba(189,156,97,0.14)", "aurora2": "rgba(76,107,92,0.20)",
    "grid": "rgba(148,163,184,0.07)", "over": "#9AA3AE", "tagline": "#B9C2CC",
    "gold1": "#E6C078", "gold2": "#8A6F3F", "aqua1": "#7FB39A", "sheen": "rgba(255,255,255,0.22)",
    "halo": "rgba(189,156,97,0.4)", "halo2": "rgba(76,107,92,0.5)", "live": "#3fb950",
    "flow": "#8FC1A8", "flowSoft": "rgba(143,193,168,0.2)", "orb1": "#E6C078", "orb2": "#3fb950", "orb3": "#7FB39A",
    "ring": "#E6C078", "ringDot": "#E6C078", "scan": "rgba(230,192,120,0.22)",
    "cube_top": "#35503F", "cube_left": "#2C4236", "cube_right": "#1E3027",
    "gold_top": "#E6C078", "gold_left": "#C9A45C", "gold_right": "#A98A4B",
    "lab": "#B9C2CC",
}

d = build(dark)
ET.fromstring(d)
open('assets/svg/banner-3d-dark.svg', 'w').write(d)
l = build(light)
ET.fromstring(l)
open('assets/svg/banner-3d-light.svg', 'w').write(l)
for name, b in (("dark", d), ("light", l)):
    print(f"banner-3d-{name}.svg  {len(b)//1024} KB  XML OK")