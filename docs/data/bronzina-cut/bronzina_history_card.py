# one-off (claude 2026-11-06): John "make card" after Opie's Bronzina history (opencode/bronzina_history/).
# Numbers recomputed here from the held grid (sandrabronzina's grid on Oct 16, 3,202 posts) and Tim's grid captures;
# event dates from that grid. Plain, factual, no login talk (John's rule). Style as docs/data/bronzina-cut card.
# Run: ~/miniforge3/envs/dl_wm/bin/python bronzina_history_card.py
import collections, datetime as dt, hashlib, json
from pathlib import Path
D = Path(__file__).resolve().parent
G_FILE = Path("/srv/agents/swap/2026-11-06/bronzina_history_input/sandrabronzina_2026-10-16_grid.jsonl")
G = [json.loads(l) for l in open(G_FILE)]
day = lambda t: dt.datetime.fromtimestamp(t, dt.timezone.utc).date()
borrowed = lambda g: "sandrabronzina" in g.get("collaborators", [])          # listed => someone else owns it
shared = lambda g: borrowed(g) or bool(g.get("collaborators"))             # with at least one other account
Y = collections.Counter(); YS = collections.Counter()
for g in G:
    y = day(g["taken_at"]).year; Y[y] += 1; YS[y] += shared(g)
first = lambda pred: min((g for g in G if pred(g)), key=lambda g: g["taken_at"])
f_any = first(shared)
f_tbtag = first(lambda g: "timballard89" in g.get("credits", []) or "timballard89" in g.get("collaborators", []))
f_tbco = first(lambda g: "timballard89" in g.get("collaborators", []))
f_lib = first(lambda g: "liberal.noticias" in g.get("collaborators", []) + g.get("credits", []))
EV = [(day(f_any["taken_at"]), "first post with another account"),
      (day(f_lib["taken_at"]), "liberal.noticias first appears (169 shared posts since)"),
      (day(f_tbtag["taken_at"]), "first tags Tim Ballard"),
      (day(f_tbco["taken_at"]), "first post with Tim (B1 of the 16)"),
      (dt.date(2026, 5, 30), "TB Rescue + foundation join (B8)"),
      (dt.date(2026, 8, 8), "expofamily.cl posts with Tim (B11-B15)"),
      (dt.date(2026, 10, 22), "blocks us: between Oct 16 and Oct 28")]
S = dict(posts=len(G), shared=sum(map(shared, G)), years={y: [Y[y], YS[y]] for y in sorted(Y)},
         events=[[str(d), t] for d, t in EV], input_sha256=hashlib.sha256(G_FILE.read_bytes()).hexdigest())
print(json.dumps({k: v for k, v in S.items() if k != "input_sha256"}, indent=0)[:900])

W, H = 1200, 675
BG, INK, MUTED, GOLD, DARK, RED = "#fbfaf6", "#1c1d22", "#5d6070", "#b8860b", "#8a8c96", "#8b1e1e"
o = []
def T(x, y, s, sz=18, c=INK, w=600, a="start"):
    o.append(f'<text x="{x}" y="{y}" font-family="IBM Plex Sans Condensed, DejaVu Sans, sans-serif" font-size="{sz}" font-weight="{w}" fill="{c}" text-anchor="{a}">{s}</text>')
T(48, 66, "Bronzina, from 2014 to the block", 42, INK, 700)
T(48, 100, f"@sandrabronzina's Instagram grid as of Oct 16, 2026: {len(G):,} posts since Oct 23, 2014.", 19, MUTED, 500)
# bars: posts per year, shared part in gold on top of solo part
years = sorted(Y); X0, BW, GAP, BASE, SC = 70, 50, 14, 360, 0.36
for i, y in enumerate(years):
    x = X0 + i * (BW + GAP); solo, sh = Y[y] - YS[y], YS[y]
    o.append(f'<rect x="{x}" y="{BASE - solo*SC:.1f}" width="{BW}" height="{solo*SC:.1f}" fill="{DARK}"/>')
    if sh: o.append(f'<rect x="{x}" y="{BASE - Y[y]*SC:.1f}" width="{BW}" height="{sh*SC:.1f}" fill="{GOLD}"/>')
    T(x + BW / 2, BASE - Y[y] * SC - 6, f"{Y[y]}", 13, INK, 600, "middle")
    T(x + BW / 2, BASE + 20, ("2026*" if y == 2026 else str(y)), 13, MUTED, 600, "middle")
o.append(f'<line x1="{X0-6}" y1="{BASE}" x2="{X0 + len(years)*(BW+GAP) - GAP + 6}" y2="{BASE}" stroke="{INK}" stroke-width="1"/>')
# key (right of the bars, clear of them)
kx = X0 + len(years) * (BW + GAP) + 20
o.append(f'<rect x="{kx}" y="170" width="250" height="96" rx="8" fill="#f2efe6" stroke="#d9d6cc"/>')
T(kx + 14, 194, "Posts per year", 15, INK, 700)
o.append(f'<rect x="{kx+14}" y="206" width="18" height="14" fill="{DARK}"/>'); T(kx + 40, 218, "posted alone", 14, INK, 500)
o.append(f'<rect x="{kx+14}" y="230" width="18" height="14" fill="{GOLD}"/>'); T(kx + 40, 242, "with other accounts", 14, INK, 500)
T(kx + 14, 260, "* 2026 to Oct 16", 12, MUTED, 500)
# timeline 2022-2026
TX0, TX1, TY = 70, 1150, 440
d0, d1 = dt.date(2022, 1, 1), dt.date(2026, 12, 31)
px = lambda d: TX0 + (TX1 - TX0) * (d - d0).days / (d1 - d0).days
o.append(f'<line x1="{TX0}" y1="{TY}" x2="{TX1}" y2="{TY}" stroke="{INK}" stroke-width="2"/>')
for y in range(2022, 2027):
    x = px(dt.date(y, 1, 1)); o.append(f'<line x1="{x:.0f}" y1="{TY-6}" x2="{x:.0f}" y2="{TY+6}" stroke="{INK}"/>'); T(x, TY + 24, str(y), 13, MUTED, 600, "middle")
for k, (d, t) in enumerate(EV):
    x = px(d); last = k == len(EV) - 1
    col = RED if last else (GOLD if "Tim" in t or "B" in t else INK)
    o.append(f'<circle cx="{x:.0f}" cy="{TY}" r="7" fill="{col}" stroke="{INK}" stroke-width="1"/>')
    ly = 488 + 22 * {0: 1, 1: 0}.get(k, k)   # first two swapped so the 2023 leader stays clear of the 2022 label
    o.append(f'<line x1="{x:.0f}" y1="{TY+8}" x2="{x:.0f}" y2="{ly-14}" stroke="{col}" stroke-width="1" stroke-dasharray="2 3"/>')
    lab = f"{d:%b %Y}: {t}" if not last else f"Oct 2026: {t}"
    anchor = "end" if x > 700 else "start"
    T(x + (-6 if anchor == "end" else 6), ly, lab, 14, RED if last else INK, 700 if last else 500, anchor)
T(W - 30, H - 14, "Source: sandrabronzina's grid (Oct 16, 2026) and timballard89's grid (Oct 28 and Nov 6), metadata only. Not to scale.", 12, MUTED, 500, "end")
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" role="img"><rect width="{W}" height="{H}" fill="{BG}"/>{"".join(o)}</svg>'
(D / "bronzina_history_card.svg").write_text(svg)   # inline into the page (no binaries on GitHub)
print("wrote", D / 'bronzina_history_card.svg')
