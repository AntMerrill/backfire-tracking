#!/usr/bin/env python3
"""Card (outward, applied-combinatorics page): m is the owner. S16's seven post owners, which owner's posts hold the crew, and what follows (for-agents M1-M5,
as live at backfire-tracking cdbf015). Owners from the committed tb-collabs timeline with owners; rows from matrix_first16.csv. claude, 2026-10-31."""
import csv, json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
H0 = Path(__file__).resolve().parent; FD = Path.home() / "Documents/repos/dl_wm/fonts"
D = Path(__file__).resolve().parents[2]
B = lambda s: ImageFont.truetype(str(FD / "Inter-Bold.otf"), s); R = lambda s: ImageFont.truetype(str(FD / "Inter-Regular.otf"), s)
W, H = 1080, 1350; im = Image.new("RGB", (W, H), (250, 248, 243)); d = ImageDraw.Draw(im)
ink, mute, red, blue, grey, gold, green = (25, 25, 30), (105, 105, 112), (190, 30, 40), (40, 90, 170), (222, 220, 214), (200, 140, 20), (35, 130, 80)

M = list(csv.reader(open(D / "holland24/matrix_first16.csv"))); codes = M[0][1:]
rows = {r[0]: {i + 1 for i, v in enumerate(r[1:]) if v == "1"} for r in M[1:]}
own = {}
for l in open(D / "tb-collabs/timballard89_timeline_with_owners_2026-10-17.jsonl"):
    p = json.loads(l); own[p["shortcode"]] = p.get("owner")
owned = {}
for i, c in enumerate(codes): owned.setdefault(own[c], set()).add(i + 1)
rec = [a for a, s in rows.items() if len(s) >= 2 and len(s) < 16]
held = {a: sum(rows[g] <= s for g in rec if g != a) for a, s in owned.items()}
assert held["expofamily.cl"] == 3 and all(v == 0 for a, v in held.items() if a != "expofamily.cl") and len(owned) == 7

d.text((40, 28), "m is the owner", font=B(48), fill=ink)
d.text((40, 90), "First 16 Ballard × Bronzina co-posts: seven accounts own posts. Whose posts hold the crew?", font=R(22), fill=mute)

x0, y0, cw, ch = 260, 175, 36, 40
for j in range(16): d.text((x0 + j * cw + 8, y0 - 30), f"{j + 1}", font=R(15), fill=mute)
for i, (a, s) in enumerate(sorted(owned.items(), key=lambda kv: (-len(kv[1]), min(kv[1])))):
    y = y0 + i * ch; m = a == "expofamily.cl"
    d.text((40, y + 9), a, font=B(20) if m else R(20), fill=gold if m else ink)
    for j in range(16):
        d.rectangle([x0 + j * cw + 4, y + 6, x0 + (j + 1) * cw - 4, y + ch - 6], fill=(gold if m else blue) if (j + 1) in s else grey)
    d.text((x0 + 16 * cw + 18, y + 9), f"crew: {held[a]} of {3 if m else 4}", font=B(18) if m else R(18), fill=green if m else mute)
yk = y0 + 7 * ch + 10
d.rectangle([40, yk + 3, 56, yk + 19], fill=blue); d.text((64, yk), "post owned by that account", font=R(16), fill=mute)
d.rectangle([330, yk + 3, 346, yk + 19], fill=gold); d.text((354, yk), "owned by expofamily.cl", font=R(16), fill=mute)

y = yk + 50
for k, t in enumerate(["Sandra Bronzina owns the most posts (6), and none of the crew sits only on them.",
                       "Tim Ballard owns one post (#8). Only expofamily.cl's posts, #11 to #15, hold the whole crew:",
                       "dramariajosemancino, margaritarojoc, qntlc, sharing 2, 2 and 2 posts pair by pair."]):
    d.text((40, y + k * 32), t, font=R(22), fill=ink)
y += 120
d.text((40, y), "m = expofamily.cl", font=B(32), fill=gold)
d.text((40, y + 48), "m is defined by ownership: the account whose posts every regular guest sits on (it was x in P2).", font=R(21), fill=ink)

y += 110
d.text((40, y), "What follows", font=B(26), fill=red)
for k, (lab, t) in enumerate([("Proved.", "At most one monkey (a human operator) in a cast Holland object: m itself."),
                              ("Proved.", "Every account other than m is a robot. In S16: the other 14 accounts."),
                              ("Also:", "In latterdayavenger's grid he owns all 354 posts, so he is m; the other 112 are robots."),
                              ("Not claimed:", "whether m is a robot.")]):
    d.text((40, y + 44 + k * 34), lab, font=B(21), fill=green if lab == "Proved." else ink if lab == "Also:" else mute)
    d.text((200, y + 44 + k * 34), t, font=R(21), fill=ink if lab != "Not claimed:" else mute)

d.text((40, H - 66), "Robot = any account other than m: a role in the structure, not a statement about who or what runs an account.", font=R(16), fill=mute)
d.text((40, H - 42), "Data and checkers: github.com/AntMerrill/backfire-tracking, docs/data (holland24, who-went-first, tb-collabs, for-agents).", font=R(16), fill=mute)
im.save(H0 / "2026-10-31_card_m_is_owner.png"); print("ok")
