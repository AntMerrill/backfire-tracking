#!/usr/bin/env python3
"""Card (outward, grid-relay-m page): only the rigid grid with relays has an m. Nine objects, m by ownership.
Data: ../summary_7_lattices_2026-10-31.tsv (7 lattices) and ../m_check.py figures for the two Druze objects. claude, for John, 2026-11-01."""
import csv
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
H0 = Path(__file__).resolve().parent; FD = Path.home() / "Documents/repos/dl_wm/fonts"
TSV = H0.parent / "summary_7_lattices_2026-10-31.tsv"
B = lambda s: ImageFont.truetype(str(FD / "Inter-Bold.otf"), s); R = lambda s: ImageFont.truetype(str(FD / "Inter-Regular.otf"), s)
W, H = 1080, 1180; im = Image.new("RGB", (W, H), (250, 248, 243)); d = ImageDraw.Draw(im)
ink, mute, red, grey, green, band = (25, 25, 30), (105, 105, 112), (190, 30, 40), (222, 220, 214), (35, 130, 80), (232, 242, 234)

T = {r["lattice"]: r for r in csv.DictReader(open(TSV), delimiter="\t")}
assert T["s16_retest"]["m"] == "expofamily.cl" and T["s16_retest"]["lambda_constant"] == "y"
assert [k for k, r in T.items() if r["m"] != "none"] == ["s16_retest", "S_h", "chadverse_core"]

# (label, shape, v, b, m, nested, lambda)
has = [("S_h, LDA's grid", "P1 rigid grid", T["S_h"], "LDA", "79/79", "not equal"),
       ("Chadverse core", "P1 relay p1→h→p2", T["chadverse_core"], "latterdayavenger", "5/5", "not equal"),
       ("S16, Holland 24", "same shape (P2)", T["s16_retest"], "expofamily.cl", "3/3", "2, 2, 2")]
none = [("TB × druze.spirit", "twin frame", {"v": "10", "b": "36"}, "none", "best 2/6", ""),
        ("druze.spirit timeline", "frame + guests", {"v": "108", "b": "200"}, "none", "best 11/47", ""),
        ("mario co-posters", "frame", T["mario_coposters"], "none", "", ""),
        ("Ballard × Bolsonaro", "frame", T["ballard_bolsonaro"], "none", "", ""),
        ("name_tag", "owner not in table", T["name_tag"], "none", "", ""),
        ("Holland order 2", "owner not in table", T["holland_order2"], "none", "", "")]

d.text((40, 28), "Only the rigid grid with relays has an m", font=B(44), fill=ink)
d.text((40, 88), "Nine Holland objects. m by ownership = the owner whose own posts hold every recurring guest's whole row.", font=R(20), fill=mute)

cols = [40, 290, 520, 640, 845, 965]
y = 150
for x, h in zip(cols, ["object", "shape", "v × b", "m", "guests held", "λ"]):
    d.text((x, y), h, font=B(18), fill=mute)
y += 34

def rows(lst, yes):
    global y
    if yes: d.rectangle([30, y - 6, W - 30, y + len(lst) * 46 - 8], fill=band)
    for lab, shp, r, m, nest, lam in lst:
        vals = [lab, shp, f'{r["v"]} × {r["b"]}', m, nest, lam]
        for k, (x, t) in enumerate(zip(cols, vals)):
            f = B(20) if k in (0, 3) and yes else R(20)
            c = green if (k == 3 and yes) else (mute if t == "none" else ink)
            if k == 5 and t == "2, 2, 2": c, f = red, B(20)
            d.text((x, y + 6), t, font=f, fill=c)
        y += 46

d.text((40, y), "Has an m", font=B(22), fill=green); y += 36
rows(has, True); y += 18
d.text((40, y), "No m", font=B(22), fill=mute); y += 36
rows(none, False)

y += 24
kx = 40
for lab, c in [("has an m", band), ("no m", (250, 248, 243))]:
    d.rectangle([kx, y + 3, kx + 18, y + 21], fill=c, outline=mute); d.text((kx + 28, y), lab, font=R(17), fill=mute)
    kx += 28 + d.textlength(lab, font=R(17)) + 40
d.text((kx, y), "λ = how often the other guests meet, on m's posts", font=R(17), fill=mute)

y += 56
d.text((40, y), "What the table shows", font=B(26), fill=red)
for k, t in enumerate(["The three with an m share one shape: a point nothing else can stand in for, a rigid recurring part,",
                       "and every leftover symmetry from forced or weight-one rooms (P1 rigid grid and relay; P2, same shape).",
                       "The six without one are frames or co-host pairs whose ownership splits: no single owner holds the crew.",
                       "In the grid and the relay, m owns every post, so holding every guest comes free. Only S16 also",
                       "seats the crew evenly (2, 2, 2): expofamily.cl, not Sandra, the raw ownership leader with 6."]):
    d.text((40, y + 42 + k * 31), t, font=R(20), fill=ink)

y += 42 + 5 * 31 + 26
d.text((40, y), "Computed: the table.   Shapes: P1 (rigid grid, relay), P2.   Proved: at most one monkey.", font=B(19), fill=green)
d.text((40, y + 32), "Not claimed: ", font=B(19), fill=red)
d.text((40 + d.textlength("Not claimed: ", font=B(19)), y + 32), "whether m is a robot.", font=R(19), fill=ink)

d.text((40, H - 66), "Robot = any account other than m: a role in the structure, not a statement about who or what runs an account.", font=R(15), fill=mute)
d.text((40, H - 42), "Data and checker: github.com/AntMerrill/backfire-tracking, docs/data/grid-relay-m (python3 -I m_check.py).", font=R(15), fill=mute)
out = H0 / "2026-11-01_card_grid_relay_m_public.png"; im.save(out); print(out)
