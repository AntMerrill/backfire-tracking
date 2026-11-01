#!/usr/bin/env python3
"""Card (outward, grid-relay-m page): TB x druze.spirit has no m. Twin rows, the two take turns owning, the crew splits by side.
Data: ../owners_tb_x_druze_spirit.tsv; timeline figures checked by ../m_check.py.
Style copied from 2026-10-31 make_card_m_is_owner.py. claude, 2026-11-01."""
import csv
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
H0 = Path(__file__).resolve().parent; FD = Path.home() / "Documents/repos/dl_wm/fonts"
SDS = H0.parent / "owners_tb_x_druze_spirit.tsv"
B = lambda s: ImageFont.truetype(str(FD / "Inter-Bold.otf"), s); R = lambda s: ImageFont.truetype(str(FD / "Inter-Regular.otf"), s)
W, H = 1080, 1100; im = Image.new("RGB", (W, H), (250, 248, 243)); d = ImageDraw.Draw(im)
ink, mute, red, grey, green = (25, 25, 30), (105, 105, 112), (190, 30, 40), (222, 220, 214), (35, 130, 80)
OC = {"timballard89": (40, 90, 170), "druze.spirit": (200, 110, 30), "tbfrescue": (130, 170, 220)}

P = list(csv.DictReader(open(SDS), delimiter="\t"))
assert len(P) == 36
blocks = [(p["owner"], set(p["credits"].split(","))) for p in P]
rows = {}
for j, (o, s) in enumerate(blocks):
    for a in s: rows.setdefault(a, set()).add(j)
own = {}
for j, (o, s) in enumerate(blocks): own.setdefault(o, set()).add(j)
assert {a: len(s) for a, s in own.items()} == {"timballard89": 18, "druze.spirit": 16, "tbfrescue": 2}
reg = [a for a, r in rows.items() if 2 <= len(r) < 36]
held = {o: sum(rows[g] <= s for g in reg if g != o) for o, s in own.items()}
assert held == {"timballard89": 2, "druze.spirit": 2, "tbfrescue": 0}, held

d.text((40, 28), "Twins, no m", font=B(48), fill=ink)
d.text((40, 90), "The 36 co-posts of Tim Ballard and druze.spirit. Each square is one post, coloured by who owns it.", font=R(21), fill=mute)

order = ["timballard89", "druze.spirit"] + sorted(reg, key=lambda a: (min(rows[a]), a))
x0, y0, cw, ch = 280, 170, 21, 34
for j in (0, 9, 19, 29, 35): d.text((x0 + j * cw, y0 - 26), f"{j + 1}", font=R(14), fill=mute)
for i, a in enumerate(order):
    y = y0 + i * ch + (14 if i >= 2 else 0)
    d.text((40, y + 6), a, font=B(19) if i < 2 else R(19), fill=ink)
    for j, (o, s) in enumerate(blocks):
        box = [x0 + j * cw + 2, y + 5, x0 + (j + 1) * cw - 2, y + ch - 5]
        d.rectangle(box, fill=OC[o] if a in s else grey)
yk = y0 + len(order) * ch + 30
kx = 40
for lab, c in [("owned by timballard89 (18)", OC["timballard89"]), ("owned by druze.spirit (16)", OC["druze.spirit"]),
               ("owned by tbfrescue (2)", OC["tbfrescue"]), ("not credited", grey)]:
    d.rectangle([kx, yk + 3, kx + 16, yk + 19], fill=c); d.text((kx + 24, yk), lab, font=R(16), fill=mute)
    kx += 24 + d.textlength(lab, font=R(16)) + 30

y = yk + 50
d.text((40, y), "What the table shows", font=B(26), fill=red)
for k, t in enumerate(["Both are on all 36 posts: one room of two. The only symmetry is swapping them (order 2).",
                       "They take turns owning: 18 Tim, 16 druze.spirit, in runs (Aug 29–31 all Tim; Sep–Oct all druze.spirit).",
                       "The regulars split by side. Tim's posts hold 2 of the 6, druze.spirit's hold 2, tbfrescue's none.",
                       "So no owner holds the whole crew, and the shared-post counts are not equal: no hub, no rotation."]):
    d.text((40, y + 42 + k * 32), t, font=R(20), fill=ink)

y += 190
d.text((40, y), "Compare S16", font=B(26), fill=red)
d.text((40, y + 42), "There Tim and Sandra are twins too, but a third account, expofamily.cl, owns posts 11–15 and seats the", font=R(20), fill=ink)
d.text((40, y + 72), "whole crew (2, 2, 2). That hub-and-rotation shape is what m was defined from. Here it does not occur.", font=R(20), fill=ink)

y += 130
d.text((40, y), "druze.spirit's whole timeline (200 co-posts, 108 accounts)", font=B(22), fill=ink)
d.text((40, y + 36), "druze.spirit is on all 200 and alone in its room. It owns 118 posts but holds only 11 of 47 regulars: no m.", font=R(19), fill=ink)
d.text((40, y + 64), "Symmetry 39,813,120, almost all from one-post guests; the rest (24) is two pairs and one trio.", font=R(19), fill=ink)

y += 120
d.text((40, y), "Computed: everything above.   ", font=B(20), fill=green)
d.text((40 + d.textlength("Computed: everything above.   ", font=B(20)), y), "Not claimed: who or what runs either account.", font=B(20), fill=red)

d.text((40, H - 66), "Captures: TB 2026-10-17, druze.spirit 2026-10-19 and 11-01. B36's Tim credit was gone on 11-01 (TB × druze.spirit now 35).", font=R(15), fill=mute)
d.text((40, H - 42), "Data and checker: github.com/AntMerrill/backfire-tracking, docs/data/grid-relay-m.", font=R(15), fill=mute)
out = H0 / "2026-11-01_card_twins_no_m_public.png"; im.save(out); print(out)
