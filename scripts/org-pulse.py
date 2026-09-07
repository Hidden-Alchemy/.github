#!/usr/bin/env python3
"""
Hidden Alchemy — Org Pulse SVG generator.

Renders assets/svg/org-pulse.svg: a self-contained dark dashboard card with
live counts drawn from the public GitHub API. No secrets, no third-party
services, no vanity metrics.

Run:  python3 scripts/org-pulse.py [output_path]
Env:  PULSE_STAGE (default: concept) — human-maintained lifecycle stage.
"""
import datetime
import json
import os
import sys
import urllib.request

BASE = "https://api.github.com"
OUT = sys.argv[1] if len(sys.argv) > 1 else "assets/svg/org-pulse.svg"
STAGE = os.environ.get("PULSE_STAGE", "concept").lower()
STAGES = ["idea", "concept", "architecture", "system", "automation", "reality"]
STATUS = {  # human-maintained lifecycle status per repo (§24)
    ".github": "active",
    "community": "active",
    "ideas": "active",
    "idea-forge": "concept",
}
ACTIVE = [r for r, s in STATUS.items() if s == "active"]
STAGE_COLORS = {"active": "#3FB950", "concept": "#E3C080", "archived": "#6e7681"}


def get(path):
    req = urllib.request.Request(
        BASE + path,
        headers={"User-Agent": "hidden-alchemy-pulse", "Accept": "application/vnd.github+json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def safe(fn, default):
    try:
        return fn()
    except Exception:
        return default


def main():
    repos = safe(
        lambda: [r for r in get("/orgs/Hidden-Alchemy/repos?per_page=100&type=public")],
        [],
    )
    names = sorted(r["name"] for r in repos)
    ideas = safe(lambda: len(get("/repos/Hidden-Alchemy/ideas/issues?state=open&per_page=100")), 0)
    green = 0
    for n in names:
        def one_repo(n):
            raw = get(f"/repos/Hidden-Alchemy/{n}/commits/main")
            sha = raw["sha"] if isinstance(raw, dict) else raw[0]["sha"]
            runs = get(f"/repos/Hidden-Alchemy/{n}/commits/{sha}/check-runs")["check_runs"]
            return any(x["name"] == "repo-health-check" and x["conclusion"] == "success" for x in runs)
        if safe(lambda: one_repo(n), False):
            green += 1
    now = datetime.datetime.now(datetime.timezone.utc)
    stamp = now.strftime("%Y-%m-%d %H:%M UTC")

    dot = lambda cx, cy, c: f'<circle cx="{cx}" cy="{cy}" r="5" fill="{c}">' \
                            '<animate attributeName="opacity" values="1;0.25;1" dur="1.6s" repeatCount="indefinite"/></circle>'
    tile = lambda x, label, value, accent: (
        f'<rect x="{x}" y="96" width="210" height="62" rx="14" fill="#151b23" stroke="#262d36"/>'
        f'<rect x="{x}" y="96" width="210" height="3" rx="1.5" fill="{accent}"/>'
        f'<text x="{x+14}" y="119" fill="#8b949e" font-size="9.5" letter-spacing="2">{label}</text>'
        f'<text x="{x+14}" y="146" fill="#e6edf3" font-size="24" font-weight="800">{value}</text>'
    )
    stage_chips = []
    for i, s in enumerate(STAGES):
        cur = s == STAGE
        x = 40 + i * 146
        if cur:
            body = f'<rect x="{x}" y="208" width="136" height="30" rx="15" fill="#E3C080"/>' \
                   f'<text x="{x+68}" y="228" text-anchor="middle" fill="#0d1117" font-size="12" font-weight="800" letter-spacing="1">{s.upper()}</text>'
        else:
            body = f'<rect x="{x}" y="208" width="136" height="30" rx="15" fill="#151b23" stroke="#30363d"/>' \
                   f'<text x="{x+68}" y="228" text-anchor="middle" fill="#8b949e" font-size="12" font-weight="700" letter-spacing="1">{s.upper()}</text>'
        stage_chips.append(body)

    repo_chips = []
    for n in names:
        c = STAGE_COLORS.get(STATUS.get(n, "concept"), "#E3C080")
        repo_chips.append(
            f'<circle cx="{58 + len(repo_chips)*130 + 6}" cy="286" r="3.5" fill="{c}"/>'
            f'<text x="{58 + len(repo_chips)*130 + 18}" y="290" font-size="11.5" fill="#e6edf3">{n}</text>'
        )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 320" role="img"
  font-family="'Inter',-apple-system,'Segoe UI',Roboto,sans-serif">
  <title>Hidden Alchemy org pulse — live snapshot of repositories, ideas, active systems and pipeline stage</title>
  <defs>
    <pattern id="g" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0 H0 V40" fill="none" stroke="#16191f" stroke-width="1"/>
    </pattern>
  </defs>
  <rect x="0" y="0" width="980" height="320" fill="#0d1117"/>
  <rect x="0" y="0" width="980" height="320" fill="url(#g)"/>

  <text x="40" y="48" fill="#e6edf3" font-size="21" font-weight="800" letter-spacing="2">ORG PULSE</text>
  {dot(44, 72, "#3FB950")}
  <text x="58" y="76" fill="#8b949e" font-size="12">snapshot · {stamp} · regenerated daily</text>

  {tile(40, "REPOSITORIES", names.__len__(), "#E3C080")}
  {tile(266, "IDEAS IN FLIGHT", ideas, "#6E9E87")}
  {tile(492, "ACTIVE SYSTEMS", len(ACTIVE), "#3FB950")}
  {tile(718, "HEALTH GREEN", str(green) + "/" + str(len(names)), "#3FB950")}

  <text x="40" y="182" fill="#8b949e" font-size="9.5" letter-spacing="2">PIPELINE · LOCKED ON {STAGE.upper()}</text>
  {''.join(stage_chips)}

  <text x="40" y="278" fill="#8b949e" font-size="9.5" letter-spacing="2">REPOSITORIES</text>
  {''.join(repo_chips)}
</svg>'''

    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote {OUT} (repos={len(names)}, ideas={ideas}, active={len(ACTIVE)}, health={green}/{len(names)}, stage={STAGE})")


if __name__ == "__main__":
    main()