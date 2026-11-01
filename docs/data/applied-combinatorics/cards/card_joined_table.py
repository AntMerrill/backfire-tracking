#!/usr/bin/env python3
"""Card (outward, applied-combinatorics page): the joined table J = Chadverse core (7 posts) + Bronzina's Coset (first 16 TB x sandrabronzina co-posts), as one
incidence structure. Built the same way as backfire-tracking docs/data/one-vertex/one_vertex.py (TB shared; latterdayavenger on all 7 W1 posts).
Numbers match Opie's one_monkey_verify_v3 report (28 points, 23 posts, 22 rooms, |Aut_<=| = 144). claude, 2026-10-31."""
import csv, math
from collections import defaultdict
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
H0 = Path(__file__).resolve().parent; FD = Path.home() / "Documents/repos/dl_wm/fonts"
D = Path(__file__).resolve().parents[2]
B = lambda s: ImageFont.truetype(str(FD / "Inter-Bold.otf"), s); R = lambda s: ImageFont.truetype(str(FD / "Inter-Regular.otf"), s)
W, H = 1080, 1350; im = Image.new("RGB", (W, H), (250, 248, 243)); d = ImageDraw.Draw(im)
ink, mute, red, blue, green, grey, gold = (25, 25, 30), (105, 105, 112), (190, 30, 40), (40, 90, 170), (40, 130, 90), (218, 216, 210), (200, 140, 20)

def load(p):
    r = list(csv.reader(open(p))); return [x[0] for x in r[1:]], {x[0]: {i for i, v in enumerate(x[1:]) if v == "1"} for x in r[1:]}
n1, w1 = load(D / "who-went-first/incidence_matrix.csv"); n2, w2 = load(D / "holland24/matrix_first16.csv")
J, side = {}, {}
for a in n1:
    k = "timballard89" if a == "TB" else ("latterdaychad" if a == "LDC" else a); J[k] = set(w1[a]); side[k] = 1
J["latterdayavenger"] = set(range(7)); side["latterdayavenger"] = 1
for a in n2:
    J.setdefault(a, set()); J[a] |= {i + 7 for i in w2[a]}; side[a] = 3 if a == "timballard89" else 2
rooms = defaultdict(list)
for a, s in J.items(): rooms[frozenset(s)].append(a)
aut = math.prod(math.factorial(len(v)) for v in rooms.values())
assert (len(J), len(rooms), aut) == (28, 22, 144)
tag = {}; letters = iter(["R1", "R2", "R3", "R4", "R5", "R6"])
for v in sorted(rooms.values(), key=lambda v: (-len(v), min(J[v[0]]))):
    if len(v) > 1:
        t = next(letters)
        for a in v: tag[a] = t
order = ["timballard89"] + sorted([a for a in J if side[a] == 1], key=lambda a: (-len(J[a]), tag.get(a, "Z"), a)) \
        + sorted([a for a in J if side[a] == 2], key=lambda a: (-len(J[a]), tag.get(a, "Z"), min(J[a]), a))

d.text((40, 26), "The joined table: two worlds, one structure", font=B(36), fill=ink)
d.text((40, 72), "Chadverse core (7 group posts) + Bronzina's Coset (first 16 TB × sandrabronzina co-posts). Rows = accounts.", font=R(19), fill=mute)
x0, y0, cw, ch = 300, 150, 27, 30
d.text((x0, y0 - 44), "Chadverse core", font=B(16), fill=green); d.text((x0 + 7 * cw + 14, y0 - 44), "Bronzina's Coset", font=B(16), fill=blue)
for j in range(23):
    xj = x0 + j * cw + (14 if j >= 7 else 0)
    d.text((xj + 4, y0 - 22), str(j + 1 if j < 7 else j - 6), font=R(12), fill=mute)
for i, a in enumerate(order):
    y = y0 + i * ch
    special = a in ("timballard89", "expofamily.cl", "latterdayavenger")
    is_m = a in ("expofamily.cl", "latterdayavenger")
    name = {"timballard89": "timballard89 (TB)"}.get(a, a)
    d.text((40, y + 5), name[:28], font=B(16) if special else R(16), fill=red if a == "timballard89" else gold if is_m else ink)
    for j in range(23):
        xj = x0 + j * cw + (14 if j >= 7 else 0)
        on = j in J[a]
        col = (red if a == "timballard89" else gold if is_m else green if j < 7 else blue) if on else grey
        d.rectangle([xj + 3, y + 5, xj + cw - 3, y + ch - 5], fill=col)
    if a == "latterdayavenger":   # its gold cells are on the left (Chadverse side): mark m there, keep its room tag on the right
        d.text((x0 - 26, y + 3), "m", font=B(18), fill=gold)
        if a in tag: d.text((x0 + 23 * cw + 26, y + 5), tag[a], font=B(16), fill=mute)
    elif is_m: d.text((x0 + 23 * cw + 26, y + 5), "m", font=B(18), fill=gold)
    elif a == "timballard89": d.text((x0 + 23 * cw + 26, y + 5), "not m", font=B(16), fill=red)
    elif a in tag: d.text((x0 + 23 * cw + 26, y + 5), tag[a], font=B(16), fill=mute)
d.line([x0 + 7 * cw + 7, y0 - 4, x0 + 7 * cw + 7, y0 + len(order) * ch], fill=ink, width=2)
yk = y0 + len(order) * ch + 14
d.rectangle([40, yk + 3, 56, yk + 19], fill=red); d.text((64, yk), "TB: in both worlds, the cut vertex; not m", font=R(16), fill=mute)
d.rectangle([520, yk + 3, 536, yk + 19], fill=gold); d.text((544, yk), "m: the owner whose posts hold the regulars", font=R(16), fill=mute)
d.rectangle([40, yk + 29, 56, yk + 45], fill=green); d.text((64, yk + 26), "on a Chadverse post", font=R(16), fill=mute)
d.rectangle([260, yk + 29, 276, yk + 45], fill=blue); d.text((284, yk + 26), "on a Coset post", font=R(16), fill=mute)
d.text((440, yk + 26), "R1, R2, … = shared rooms (identical rows); unmarked = room of one", font=R(16), fill=mute)

y = yk + 70
for k, t in enumerate(["m in each world is the owner of the posts the regulars sit on, in the same gold:",
                       "  Chadverse core: latterdayavenger (owns all 7).   Bronzina's Coset: expofamily.cl (owns #11–#15).",
                       "Not TB. He is the one account in both worlds, the cut vertex where they touch: most central, not m.",
                       "Proved: at most one monkey per object, m; every account other than m is a robot."]):
    d.text((40, y + k * 30), t, font=B(19) if k in (0, 2) else R(19), fill=red if k == 2 else ink)
d.text((40, H - 66), "Robot = any account other than m: a role in the structure, not a statement about who or what runs an account.", font=R(16), fill=mute)
d.text((40, H - 42), "Data and checkers: github.com/AntMerrill/backfire-tracking, docs/data (holland24, who-went-first, tb-collabs, for-agents).", font=R(16), fill=mute)
im.save(H0 / "2026-10-31_card_joined_table.png"); print("ok", len(order))
