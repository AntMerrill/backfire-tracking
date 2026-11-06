#!/usr/bin/env python3
"""Card for docs/bronzina-cut.html: the 16 posts of Bronzina's coset, Oct 16 vs Nov 6, 2026 (one login, both dates).
Reads only s16_status.csv (this folder). Writes bronzina_cut_card.svg (1200x630), inlined in the page. Plain Python 3, no packages. claude, 2026-11-06."""
import csv
from pathlib import Path
D = Path(__file__).resolve().parent
S = list(csv.DictReader(open(D / "s16_status.csv")))
W, H = 1200, 630
BG, INK, MUTED, GOLD, RED, GREY = "#fbfaf6", "#1c1d22", "#5d6070", "#b8860b", "#8b1e1e", "#9a9aa3"
o = []
def T(x, y, s, sz=20, c=INK, w=600, a="start", it=False):
    o.append(f'<text x="{x}" y="{y}" font-family="IBM Plex Sans Condensed, DejaVu Sans, sans-serif" font-size="{sz}" font-weight="{w}" '
             f'fill="{c}" text-anchor="{a}"{" font-style=" + chr(34) + "italic" + chr(34) if it else ""}>{s}</text>')
T(48, 70, "Sixteen links, one block", 44, INK, 700)
T(48, 106, "Bronzina's coset: the first 16 posts Tim Ballard and @sandrabronzina shared, on Oct 16 and on Nov 6, 2026.", 19, MUTED, 500)
X0, CW, CH = 236, 54, 54
for r, (lab, sub, y) in enumerate((("Oct 16", "on all 16", 170), ("Nov 6", "on none", 300))):
    T(48, y + 28, lab, 26, INK, 700); T(48, y + 52, f"Bronzina {sub}", 15, MUTED, 500)
    for j, s in enumerate(S):
        x = X0 + j * (CW + 4)
        if r == 0:
            o.append(f'<rect x="{x}" y="{y}" width="{CW}" height="{CH}" rx="6" fill="{GOLD}" stroke="{INK}" stroke-width="1.5"/>')
        elif s["on_tb_grid_nov6"] == "0":
            o.append(f'<rect x="{x}" y="{y}" width="{CW}" height="{CH}" rx="6" fill="none" stroke="{RED}" stroke-width="2.5" stroke-dasharray="7 5"/>')
        else:
            o.append(f'<rect x="{x}" y="{y}" width="{CW}" height="{CH}" rx="6" fill="#e6e3da" stroke="{GREY}" stroke-width="1.5"/>')
            o.append(f'<line x1="{x+12}" y1="{y+12}" x2="{x+CW-12}" y2="{y+CH-12}" stroke="{GREY}" stroke-width="2"/>')
        if r == 0:
            T(x + CW / 2, y + CH + 22, s["posted_utc"][2:7].replace("-", "/"), 12, MUTED, 500, "middle")
gone = sum(s["on_tb_grid_nov6"] == "0" for s in S); kept = len(S) - gone
# key (below the rows, clear of them)
ky = 400
o.append(f'<rect x="48" y="{ky}" width="1104" height="78" rx="8" fill="#f2efe6" stroke="#d9d6cc"/>')
o.append(f'<rect x="66" y="{ky+16}" width="22" height="22" rx="4" fill="{GOLD}" stroke="{INK}"/>'); T(98, ky + 33, "post on Tim's grid, Bronzina listed", 15, INK, 500)
o.append(f'<rect x="410" y="{ky+16}" width="22" height="22" rx="4" fill="none" stroke="{RED}" stroke-width="2.5" stroke-dasharray="5 4"/>'); T(442, ky + 33, f"post off Tim's grid ({gone}, all Bronzina's own)", 15, INK, 500)
o.append(f'<rect x="790" y="{ky+16}" width="22" height="22" rx="4" fill="#e6e3da" stroke="{GREY}"/>'); o.append(f'<line x1="795" y1="{ky+21}" x2="807" y2="{ky+33}" stroke="{GREY}" stroke-width="2"/>')
T(822, ky + 33, f"still on the grid, Bronzina not listed ({kept})", 15, INK, 500)
T(66, ky + 62, "Each square is one post, oldest at left (yy/mm under the top row).", 13, MUTED, 500)
T(48, 530, "@sandrabronzina blocks us.", 24, RED, 700)
T(48, 562, "The account is still active. With us blocked, all 16 of its links to Tim vanish from our view at once.", 17, INK, 500)
T(W - 30, H - 16, "Source: timballard89's grid, metadata only, Oct 16 and Nov 6, 2026. Data: data/bronzina-cut/", 12, MUTED, 500, "end")
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" role="img"><rect width="{W}" height="{H}" fill="{BG}"/>{"".join(o)}</svg>'
(D / "bronzina_cut_card.svg").write_text(svg)   # inline into the page (no binaries on GitHub)
print("wrote", D / 'bronzina_cut_card.svg')
