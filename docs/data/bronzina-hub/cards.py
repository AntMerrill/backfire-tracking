"""Three result cards for the Bronzina cohort paper, house card style (dark card, serif title, gold/blue, key, source footer).
claude 2026-10-29. Reason (rule 7): 2026-10-22 tb_bronzina_fix/card_v2.py draws the co-post timeline, not the incidence
grid or the null-model numbers; this one-off reuses its palette and layout. Lives in this dated folder.
Usage: python3 -I cards.py MATRIX_first16.csv OUTDIR   (writes three PNGs with a timestamp in the name; never overwrites)"""
import csv, sys, hashlib, datetime as dt, os
from PIL import Image, ImageDraw, ImageFont

src, outdir = sys.argv[1], sys.argv[2]
rows = list(csv.reader(open(src, newline="")))
inc = {r[0]: [int(v) for v in r[1:]] for r in rows[1:]}
nb = len(rows[0]) - 1
stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M%S")

W, H = 1600, 1120
BG, INK, DIM, GOLD, BLUE, GRID, GREY, FAINT = (24, 26, 33), (232, 232, 232), (140, 145, 160), (240, 200, 90), (110, 190, 240), (60, 64, 78), (150, 154, 168), (88, 92, 108)
fp = "/usr/share/fonts/truetype/dejavu/"; F = lambda n, s: ImageFont.truetype(fp + n, s)
SRC1 = "Co-post = a post with both accounts as owner or listed collaborator. 𝒮16 = first 16 co-posts of timballard89 and sandrabronzina, 2025-11-04 to 2026-10-16."
SRC1 = SRC1.replace("𝒮16", "S16")
SRC2 = "Our captures only. Paper: 'A Hub and a Rotation', claude 2026-10-29, in-house. Numbers from s16_check.py on matrix_first16.csv (sha256 1be9ff2278aa)."

HOST = ["timballard89", "sandrabronzina"]
ORDER = HOST + ["liberal.noticias", "julietaagonz", "piterpaulin", "maaydelara", "tbfrescue", "timballardfoundationecuador",
                "larinoar", "expofamily.cl", "dramariajosemancino", "margaritarojoc", "qntlc", "agustinlaje", "ivetteavaria"]
HUB, CREW = "expofamily.cl", {"dramariajosemancino", "margaritarojoc", "qntlc"}
ONE_POST_ROOMS = {"liberal.noticias", "julietaagonz", "piterpaulin", "tbfrescue", "timballardfoundationecuador"}


def kind(a):
    if a in HOST: return GREY
    if a == HUB: return GOLD
    if a in CREW: return BLUE
    if a in ONE_POST_ROOMS: return FAINT
    return FAINT


def frame(title, sub):
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    d.text((60, 36), title, font=F("DejaVuSerif-Bold.ttf", 46), fill=INK)
    d.text((60, 100), sub, font=F("DejaVuSans.ttf", 25), fill=DIM)
    d.text((60, H - 70), SRC1, font=F("DejaVuSans.ttf", 17), fill=DIM)
    d.text((60, H - 44), SRC2, font=F("DejaVuSans.ttf", 17), fill=DIM)
    return im, d


def key(d, y, items):
    d.rounded_rectangle([46, y - 12, 1554, y + 30 + 34 * ((len(items) + 1) // 2)], radius=10, outline=GRID, width=2)
    d.text((60, y - 2), "KEY", font=F("DejaVuSans-Bold.ttf", 18), fill=DIM)
    for j, (c, lab) in enumerate(items):
        x = 60 + (j % 2) * 760; yy = y + 26 + (j // 2) * 34
        d.rounded_rectangle([x, yy, x + 26, yy + 22], radius=5, fill=c); d.text((x + 38, yy - 1), lab, font=F("DejaVuSans.ttf", 20), fill=INK)


def grid(d, accts, cols, x0, y0, cw, ch, labw):
    for k, j in enumerate(cols):
        d.text((x0 + labw + k * cw + cw / 2, y0 - 8), f"B{j + 1}", font=F("DejaVuSans.ttf", 16), fill=DIM, anchor="mb")
    for i, a in enumerate(accts):
        y = y0 + i * ch
        d.text((x0 + labw - 14, y + ch / 2), a, font=F("DejaVuSans.ttf", 19), fill=INK, anchor="rm")
        for k, j in enumerate(cols):
            x = x0 + labw + k * cw
            d.rectangle([x + 2, y + 2, x + cw - 2, y + ch - 2], outline=GRID, width=1)
            if inc[a][j]: d.rectangle([x + 5, y + 5, x + cw - 5, y + ch - 5], fill=kind(a))


def save(im, name):
    p = os.path.join(outdir, f"{stamp}_{name}.png"); im.save(p)
    print(p, hashlib.sha256(open(p, "rb").read()).hexdigest()[:16])


# card 1: the whole grid; the 24 and where it comes from
im, d = frame("Bronzina cohort: where the symmetry 24 comes from",
              "Every symmetry swaps accounts with identical rows. Here those are the hosts, or one-post guests. None recur.")
grid(d, ORDER, range(nb), 40, 190, 56, 34, 320)
bx = 40 + 320 + nb * 56 + 16
for lab, a, b in [("2: forced, hosts on every post", 0, 1), ("6: one post (B2)", 2, 4), ("2: one post (B8),", 6, 7)]:
    ya, yb = 190 + a * 34 + 6, 190 + (b + 1) * 34 - 6
    d.line([(bx, ya), (bx + 10, ya), (bx + 10, yb), (bx, yb)], fill=DIM, width=2)
    d.text((bx + 18, (ya + yb) / 2), lab, font=F("DejaVuSans.ttf", 16), fill=INK, anchor="lm")
    if a == 6: d.text((bx + 18, (ya + yb) / 2 + 20), "TB's org accounts", font=F("DejaVuSans.ttf", 16), fill=INK, anchor="lm")
d.text((60, 735), "|Aut<| = 2 x 6 x 2 = 24, and no factor comes from an account that appears more than once.", font=F("DejaVuSans-Bold.ttf", 24), fill=GOLD)
key(d, 800, [(GREY, "hosts: timballard89, sandrabronzina (on all 16)"), (GOLD, "hub: expofamily.cl (5 posts)"),
             (BLUE, "crew: dramariajosemancino 4, margaritarojoc 3, qntlc 3"), (FAINT, "one-post guests")])
save(im, "card1_where_24_comes_from")

# card 2: hub and rotation, B11-B15
im, d = frame("The Expo window: one hub, a rotating crew",
              "B11 to B15 (2026-08-08 to 10-05): expofamily.cl on every post; no two crew accounts are on the same posts.")
win = list(range(10, 15)); acc = [HUB, "dramariajosemancino", "margaritarojoc", "qntlc", "agustinlaje"]
grid(d, acc, win, 160, 230, 150, 70, 360)
dates = ["08-08", "08-19", "08-27", "09-15", "10-05"]
for k, s in enumerate(dates):
    d.text((160 + 360 + k * 150 + 75, 230 + 5 * 70 + 12), s, font=F("DejaVuSans.ttf", 17), fill=DIM, anchor="mt")
lines = ["Every crew row lies inside the hub's row (nesting).",
         "Crew rows are all different; each pair shares exactly 2 posts.",
         "No two cohort accounts are twins, so the symmetry 24 misses this.",
         "The 17th co-post (10-20) repeats B15's seats; nesting still holds."]
for i, t in enumerate(lines):
    d.text((160, 660 + i * 34), t, font=F("DejaVuSans.ttf", 22), fill=INK)
key(d, 830, [(GOLD, "hub: expofamily.cl, joined 2024-04, 6 former usernames"), (BLUE, "crew: accounts joined 2018-07 to 2019-03"),
             (FAINT, "one-time guest (agustinlaje, B12)")])
save(im, "card2_hub_and_rotation")

# card 3: the null model
im, d = frame("Is the hub chance? 20,000 shuffles say no",
              "Shuffle who sits on which post, keeping each account's post count and each post's size.")
tab = [("Two recurring guests are twins (same posts)", "no", "99.4% of shuffles also say no", "absence clears nobody"),
       ("Recurring guests touch only 5 posts", "yes", "1 in 10,000", "rare by chance"),
       ("Those posts are consecutive", "yes", "0 of 20,000", "rare by chance"),
       ("One account is on every post the others are on", "yes", "1 in 10,000", "rare by chance")]
hx = [60, 700, 820, 1210]
for x, h in zip(hx, ["shape", "S16", "under the shuffle", "reading"]):
    d.text((x, 190), h.upper(), font=F("DejaVuSans-Bold.ttf", 18), fill=DIM)
for i, row in enumerate(tab):
    y = 240 + i * 90
    d.line([(60, y - 18), (1540, y - 18)], fill=GRID, width=1)
    for k, (x, t) in enumerate(zip(hx, row)):
        col = INK if k < 2 else (GOLD if k == 3 and "rare" in t else (BLUE if k == 2 else DIM))
        d.text((x, y), t, font=F("DejaVuSans.ttf", 23), fill=col)
d.text((60, 640), "So the cohort's structure is a hub with a rotation, not a set of twins. A bot test that only looks for twins", font=F("DejaVuSans.ttf", 24), fill=INK)
d.text((60, 676), "would pass this cohort as clean.", font=F("DejaVuSans.ttf", 24), fill=INK)
d.text((60, 740), "Caveat: these four shapes were chosen after the data were seen. The numbers describe how unusual the shape is;", font=F("DejaVuSans.ttf", 21), fill=DIM)
d.text((60, 770), "they are not a pre-registered test. Written in advance: a forward prediction for the next six co-posts (paper, T1).", font=F("DejaVuSans.ttf", 21), fill=DIM)
key(d, 850, [(BLUE, "estimated frequency under the shuffle (seed 20261029)"), (GOLD, "reading of that frequency")])
save(im, "card3_null_model")


# card 4 (added 2026-10-29 for Prop. 2.3): the same D6 in the first Holland object S7 and in S16.
# S7 blocks are the treatise's Sage session (automorphism-group.html §4), p1 = timballard89, p2 = latterdaychad.
S7 = [["p1","p2","p3","p4","p5"], ["p1","p2","p3","p5","p6"], ["p1","p2","p3","p7","p6"], ["p1","p2","p3","p4","p6"],
      ["p1","p2","p8","p4","p9"], ["p1","p2","p10","p11","p12"], ["p1","p2","p13","p9","p6"]]
if len(sys.argv) > 3 and sys.argv[3] == "d6":
    im, d = frame("The same D6, a new second twin",
                  "Two twins on every post, three on one post who can trade places: 2 x 6 = 12 symmetries, the group D6.")
    s7pts = [f"p{i}" for i in range(1, 14)]; s7lab = {"p1": "timballard89", "p2": "latterdaychad"}
    def col7(p): return GOLD if p in ("p1", "p2") else (BLUE if p in ("p10", "p11", "p12") else None)
    def col16(a): return GOLD if a in HOST else (BLUE if a in ("liberal.noticias", "julietaagonz", "piterpaulin") else None)
    def panel(title, x0, labels, cols, has, colf, labw, cw=38, ch=31, y0=230):
        d.text((x0, 168), title, font=F("DejaVuSans-Bold.ttf", 22), fill=GOLD)
        for k, c in enumerate(cols):
            d.text((x0 + labw + k * cw + cw / 2, y0 - 8), c, font=F("DejaVuSans.ttf", 13), fill=DIM, anchor="mb")
        for i, (key_, lab) in enumerate(labels):
            y = y0 + i * ch
            d.text((x0 + labw - 10, y + ch / 2), lab, font=F("DejaVuSans.ttf", 16), fill=INK, anchor="rm")
            for k in range(len(cols)):
                x = x0 + labw + k * cw
                d.rectangle([x + 2, y + 2, x + cw - 2, y + ch - 2], outline=GRID, width=1)
                if has(key_, k): d.rectangle([x + 5, y + 5, x + cw - 5, y + ch - 5], fill=colf(key_) or FAINT)
    panel("First Holland object: 7 group posts, Feb-Apr 2026", 40,
          [(p, s7lab.get(p, p)) for p in s7pts], [f"B{j + 1}" for j in range(7)],
          lambda p, k: p in S7[k], col7, 170)
    panel("This paper: first 16 TB x SB co-posts", 730,
          [(a, a) for a in ORDER], [f"{j + 1}" for j in range(nb)],
          lambda a, k: inc[a][k] == 1, col16, 230, cw=36)
    d.text((40, 735), "D6 = Sym{twins} x Sym{trio}. In S16 a third factor, TB's two org accounts on B8, doubles it to 24.", font=F("DejaVuSans-Bold.ttf", 22), fill=GOLD)
    d.text((40, 772), "Only timballard89 is in both. The second twin's seat passed from latterdaychad to sandrabronzina.", font=F("DejaVuSans.ttf", 22), fill=INK)
    key(d, 840, [(GOLD, "the two twins: on every post"), (BLUE, "the trio: together on one post (S7: 2026-04-10; S16: 2025-11-21)"),
                 (FAINT, "everyone else")])
    d.text((60, H - 96), "S7: treatise 'Automorphism Group of the Incidence Structure', Prop. 2.3 and its Sage session; points p3-p13 as published there.", font=F("DejaVuSans.ttf", 17), fill=DIM)
    save(im, "card4_same_d6")
