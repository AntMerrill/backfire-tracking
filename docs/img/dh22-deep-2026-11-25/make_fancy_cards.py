#!/usr/bin/env python3
"""One-off: render the six fancier DH22 cards (1200x630, dark/gold, real faces).

Purpose: visual card set on top of the verified DH22 numbers, using chromie's
28 real 150x150 profile pictures.  Why not an existing tool: chromie's
make_sheets.py renders the 7x4 contact sheet and one card with a fixed layout;
no card-set renderer exists in dl_wm / chrome-harvest / the repo.  PIL is the
house imaging library.  Dated one-off, kept with the deliverable (rule 7).

Numbers are read from the deep pass summary / TSVs, never recomputed here.
Usage: make_fancy_cards.py <outdir>
"""
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

BASE = Path("/srv/agents/swap/2026-11-25/dh22_avatars")
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent

FB_PATH = "/home/perl/repos/dl_wm/fonts/Inter-Bold.otf"
FR_PATH = "/home/perl/repos/dl_wm/fonts/Inter-Regular.otf"

W, H = 1200, 630
BG = "#12151c"
PANEL = "#171b24"
INK = "#e6e8ee"
MUTE = "#98a1b3"
RULE = "#2a3242"
GOLD = "#e0b93a"
DIM = "#6d7688"

DATE = "2026-11-25"
DEF = "22 co-posts of timballard89, 2025-05-01 – 2025-06-30 UTC  ·  28 accounts"

# the 28 canonical accounts, in canonical_object.tsv order
ACCOUNTS = [
    "47contadoallan", "4ludlins", "_revistatimeline", "americatv", "biakicis",
    "carlosjordy", "cristianosenpolitica", "damaresalvesoficial",
    "dignidadyderecho", "eduardoverastegui", "emilia_maldonadojaramillo",
    "freedomcenterlu", "generalgirao", "gusgayer", "herzog_foundation",
    "janethinostrozaok", "jorgeseifjunior", "laisjordy", "lilipacheco.usa",
    "mareannl", "mariofriasoficial", "momsforamerica", "pabloaproano",
    "paolafelixdiaz", "rolando_gps", "timballard89",
    "timballardfoundationecuador", "verosevillaec",
]

FOUR = ["dignidadyderecho", "emilia_maldonadojaramillo", "pabloaproano",
        "timballardfoundationecuador"]
PAIRS = [
    ("47contadoallan", "_revistatimeline"),
    ("americatv", "rolando_gps"),
    ("biakicis", "mareannl"),
    ("gusgayer", "jorgeseifjunior"),
    ("herzog_foundation", "momsforamerica"),
]


def F(path, size):
    return ImageFont.truetype(path, size)


def tb(d, text, f, anchor=None):
    return d.textbbox((0, 0), text, font=f)


def tw(d, text, f):
    b = tb(d, text, f)
    return b[2] - b[0]


def layout(d, text, maxw, path=FB_PATH, size=14, min_size=9, max_lines=2):
    """Return (lines, font): prefer one line, wrap on _ . and space otherwise."""
    f = F(path, size)
    if tw(d, text, f) <= maxw:
        return [text], f
    parts = re.findall(r"[^_. ]+[_. ]?", text)
    while size >= min_size:
        f = F(path, size)
        lines, cur = [], ""
        for p in parts:
            trial = cur + p
            if tw(d, trial.rstrip(), f) <= maxw or not cur:
                cur = trial
            else:
                lines.append(cur.rstrip())
                cur = p
        if cur:
            lines.append(cur.rstrip())
        if len(lines) <= max_lines and all(tw(d, ln, f) <= maxw for ln in lines):
            return lines, f
        size -= 1
    f = F(path, min_size)
    return [text], f


def circle(im, disc):
    im = im.convert("RGB").resize((disc, disc), Image.LANCZOS)
    mask = Image.new("L", (disc, disc), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, disc - 1, disc - 1), fill=255)
    out = Image.new("RGBA", (disc, disc), (0, 0, 0, 0))
    out.paste(im, (0, 0), mask)
    return out


def paste_face(img, account, x, y, disc, ring=True, ring_color=GOLD,
               dash=False):
    path = BASE / f"av_{account}.jpg"
    if path.exists():
        img.paste(circle(Image.open(path), disc), (int(x), int(y)),
                  circle(Image.open(path), disc))
    else:
        d = ImageDraw.Draw(img)
        d.ellipse((x, y, x + disc, y + disc), fill=PANEL)
        f = F(FB_PATH, int(disc * 0.5))
        ch = account.lstrip("_")[:1].upper()
        d.text((x + disc / 2, y + disc / 2), ch, font=f, fill=GOLD, anchor="mm")
    if ring:
        layer = Image.new("RGBA", (disc + 10, disc + 10), (0, 0, 0, 0))
        rd = ImageDraw.Draw(layer)
        col = ring_color
        if dash:
            # dashed ring: short arcs
            import math
            r = disc / 2 + 3
            cx = cy = disc / 2 + 5
            for a in range(0, 360, 12):
                rd.arc((cx - r, cy - r, cx + r, cy + r), a, a + 7,
                       fill=col, width=2)
        else:
            rd.ellipse((3, 3, disc + 6, disc + 6), outline=col, width=2)
        img.paste(layer, (int(x) - 5, int(y) - 5), layer)


def monogram(d, letter, x, y, disc, ring_color=GOLD, dash=False):
    d.ellipse((x, y, x + disc, y + disc), fill=PANEL)
    if dash:
        import math
        r = disc / 2 - 1
        cx = cy = x + disc / 2
        for a in range(0, 360, 12):
            d.arc((cx - r, cy - r, cx + r, cy + r), a, a + 7,
                  fill=ring_color, width=2)
    else:
        d.ellipse((x, y, x + disc, y + disc), outline=ring_color, width=2)
    f = F(FB_PATH, int(disc * 0.52))
    d.text((x + disc / 2, y + disc / 2 + 1), letter, font=f, fill=GOLD,
           anchor="mm")


def eyebrow(d, text, y=30, col=MUTE):
    d.text((44, y), text, font=F(FR_PATH, 20), fill=col)


def h1(d, text, y=58, size=44, col=INK):
    d.text((44, y), text, font=F(FB_PATH, size), fill=col)


def gold_rule(img, y, x0=44, x1=W - 44, alpha=150):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(layer).line((x0, y, x1, y), fill=(224, 185, 58, alpha), width=2)
    img.paste(layer, (0, 0), layer)


def footer(d, left="DH22 deep pass · 2026-11-25", right="Backfire Tracking"):
    d.line((44, 596, W - 44, 596), fill=RULE, width=1)
    d.text((44, 606), left, font=F(FR_PATH, 15), fill=DIM)
    d.text((W - 44, 606), right, font=F(FR_PATH, 15), fill=DIM, anchor="ra")


def centered(d, text, y, font, col, cx=W / 2, anchor="ma"):
    d.text((cx, y), text, font=font, fill=col, anchor=anchor)


# ---------------------------------------------------------------- card 1
def card_1():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    eyebrow(d, "DH22  ·  the canonical set")
    h1(d, "DH22 — the 28 accounts", 54, 46)
    d.text((46, 112), DEF, font=F(FR_PATH, 21), fill="#c9ced6")
    d.text((46, 142), f"real profile pictures · captured {DATE}", font=F(FR_PATH, 16), fill=DIM)
    gold_rule(img, 172)

    cols, rows = 7, 4
    disc = 86
    pitch_x = 156
    pitch_y = 100
    total_w = (cols - 1) * pitch_x + disc
    x0 = (W - total_w) / 2
    y0 = 190
    for n, acct in enumerate(ACCOUNTS):
        r, c = divmod(n, cols)
        x = x0 + c * pitch_x
        y = y0 + r * pitch_y
        paste_face(img, acct, x, y, disc, ring=True)
    footer(d)
    return img


# ---------------------------------------------------------------- card 2
def card_2():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    eyebrow(d, "DH22  ·  the 768 object")
    h1(d, "One class of four, five pairs", 54, 42)
    d.text((44, 106), "|Aut| = 4!·2!⁵ = 768", font=F(FB_PATH, 32), fill=GOLD)
    gold_rule(img, 150)

    # class of four
    d.text((44, 162), "THE CLASS OF FOUR — interchangeable", font=F(FB_PATH, 14), fill=MUTE)
    disc = 96
    colw = 278
    x0 = 44
    y = 188
    for i, acct in enumerate(FOUR):
        cx = x0 + i * colw + colw / 2
        x = cx - disc / 2
        paste_face(img, acct, x, y, disc, ring=True)
        lines, f = layout(d, acct, colw - 20, FR_PATH, 15, 11)
        ly = y + disc + 12
        for j, ln in enumerate(lines):
            d.text((cx, ly + j * (f.size + 2)), ln, font=f, fill=INK, anchor="ma")

    # five pairs: two discs per group, one combined label under the pair
    d.text((44, 336), "THE FIVE PAIRS — each co-occurs on one defining post", font=F(FB_PATH, 14), fill=MUTE)
    pdisc = 62
    group = 220
    pair_gap = 8
    gw = 2 * pdisc + pair_gap
    x0 = 50
    y = 360
    for gi, (a, b) in enumerate(PAIRS):
        gc = x0 + gi * group + group / 2
        gx = gc - gw / 2
        for k, acct in enumerate((a, b)):
            x = gx + k * (pdisc + pair_gap)
            paste_face(img, acct, x, y, pdisc, ring=True)
        lines, f = layout(d, f"{a} / {b}", group - 10, FR_PATH, 11, 8, max_lines=1)
        ly = y + pdisc + 9
        for j, ln in enumerate(lines):
            d.text((gc, ly + j * (f.size + 1)), ln, font=f, fill=INK, anchor="ma")

    centered(d, "the remaining 14 accounts are singletons  ·  |Aut| is the product of (class size)! over the classes",
             500, F(FR_PATH, 14), MUTE)
    footer(d)
    return img


# ---------------------------------------------------------------- card 3
def card_3():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    eyebrow(d, "DH22  ·  repeated twins")
    h1(d, "Best twin: survives the merge", 54, 42)
    d.text((44, 108), "16 co-posts  ·  still 16 in the merged union", font=F(FB_PATH, 27), fill=GOLD)
    gold_rule(img, 152)

    # two twin tiles (no captured profile picture: monogram, not substituted)
    disc = 150
    gap = 70
    total = 2 * disc + gap
    x0 = (W - total) / 2
    y = 186
    for k, (acct, letter) in enumerate((("defeatleftism", "D"), ("jdvance4usa", "J"))):
        x = x0 + k * (disc + gap)
        monogram(d, letter, x, y, disc)
        d.text((x + disc / 2, y + disc + 12), acct, font=F(FB_PATH, 22), fill=INK, anchor="ma")
    centered(d, "profile pictures for these network accounts were not in the 28-account capture",
             402, F(FR_PATH, 14), DIM)

    d.line((44, 438, W - 44, 438), fill=RULE, width=1)
    d.text((44, 454), "Capture-local, does not survive:", font=F(FB_PATH, 16), fill=MUTE)
    d.text((44, 480), "38contadoallan / allanconta_35 — 24 co-posts in maxcardosobr_2026-11-19",
           font=F(FR_PATH, 17), fill=INK)
    d.text((44, 506), "Also persistent in the union: andres.fearless / karim.fearless (6) and",
           font=F(FR_PATH, 16), fill=MUTE)
    d.text((44, 530), "horanoticiasbr / horapoliticabr (6).", font=F(FR_PATH, 16), fill=MUTE)
    footer(d)
    return img


# ---------------------------------------------------------------- card 4
def card_4():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    eyebrow(d, "DH22  ·  network, union view")
    h1(d, "The whole captured network", 54, 42)
    d.text((44, 110), "2,904 × 98,432", font=F(FB_PATH, 54), fill=INK)
    d.text((44, 182), "|Aut| ≈ 1.80 × 10¹⁰³", font=F(FB_PATH, 32), fill=GOLD)
    d.text((44, 226), "largest class 4  ·  239 non-trivial classes  ·  186 pairs + 43 triples + 10 quads",
           font=F(FR_PATH, 16), fill=MUTE)
    d.text((44, 260), "A long tail of small look-alike classes, not one rigid object. The 11-20",
           font=F(FR_PATH, 16), fill="#c9ced6")
    d.text((44, 284), "baseline (2,898 × 98,420 ≈ 2.99×10¹⁰²) reproduces exactly.",
           font=F(FR_PATH, 16), fill="#c9ced6")

    d.text((44, 400), "Union of 27 archive + 60 holland captures, deduped by shortcode.",
           font=F(FR_PATH, 16), fill=MUTE)
    d.text((44, 426), "snapshot to 2026-11-19  ·  2,904 accounts = 2,898 baseline + 6 collaborator-only",
           font=F(FR_PATH, 16), fill=MUTE)

    # face strip of the 28 along the bottom
    d.text((44, 508), "the 28 DH22 accounts", font=F(FB_PATH, 13), fill=MUTE)
    disc = 32
    pitch = 40
    total = (len(ACCOUNTS) - 1) * pitch + disc
    x0 = (W - total) / 2
    y = 536
    for i, acct in enumerate(ACCOUNTS):
        paste_face(img, acct, x0 + i * pitch, y, disc, ring=True)
    gold_rule(img, 580, 44, W - 44, 90)
    footer(d)
    return img


# ---------------------------------------------------------------- card 5
def card_5():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    eyebrow(d, "DH22  ·  validation before new ground")
    h1(d, "The known answer, reproduced", 54, 42)
    d.text((44, 118), "282 × 766", font=F(FB_PATH, 72), fill=INK)
    d.text((44, 206), "|Aut| = 150,994,944 — trio included", font=F(FB_PATH, 32), fill=GOLD)
    gold_rule(img, 268, 44, 460)
    d.text((44, 296), "The same construction, unchanged from the 2026-10-20 pass,",
           font=F(FR_PATH, 18), fill="#c9ced6")
    d.text((44, 322), "reproduces sandrabronzina exactly.", font=F(FR_PATH, 18), fill="#c9ced6")
    d.text((44, 360), "A method that misses a known answer is not trusted on a new set.",
           font=F(FR_PATH, 16), fill=MUTE)

    # faint strip of the 28, very dim, ties the card to the face set
    disc = 30
    pitch = 38
    total = (len(ACCOUNTS) - 1) * pitch + disc
    x0 = (W - total) / 2
    y = 540
    strip = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    for i, acct in enumerate(ACCOUNTS):
        paste_face(strip, acct, x0 + i * pitch, y, disc, ring=False)
    alpha = strip.split()[3].point(lambda a: int(a * 0.16))
    strip.putalpha(alpha)
    img.paste(strip, (0, 0), strip)
    footer(d)
    return img


# ---------------------------------------------------------------- card 6
def card_6():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    eyebrow(d, "DH22  ·  scope and caveat")
    h1(d, "A snapshot to 2026-11-19", 54, 42)
    d.text((44, 108), "coverage has holes, stated", font=F(FB_PATH, 26), fill=GOLD)
    gold_rule(img, 150)

    # 22 defining posts as two rows of 11 tiles; 1 dashed, 2 ringed
    ncols = 11
    ts = 40
    gap = 12
    row_w = ncols * ts + (ncols - 1) * gap
    tx0 = (W - row_w) / 2
    ty0 = 186
    missing = {12}
    incomplete = {11, 20}
    for n in range(1, 23):
        r, c = divmod(n - 1, ncols)
        x = tx0 + c * (ts + gap)
        y = ty0 + r * (ts + gap + 6)
        if n in missing:
            # dashed tile, clearly the post, not the account
            for a in range(0, 360, 12):
                import math
                rr = ts / 2 - 1
                cx, cy = x + ts / 2, y + ts / 2
                d.arc((cx - rr, cy - rr, cx + rr, cy + rr), a, a + 7,
                      fill=DIM, width=2)
            d.text((x + ts / 2, y + ts / 2), "12", font=F(FB_PATH, 15), fill=DIM, anchor="mm")
        elif n in incomplete:
            d.rounded_rectangle((x, y, x + ts, y + ts), radius=7, fill=PANEL,
                                outline=GOLD, width=2)
            d.text((x + ts / 2, y + ts / 2), str(n), font=F(FB_PATH, 14), fill=GOLD, anchor="mm")
        else:
            d.rounded_rectangle((x, y, x + ts, y + ts), radius=7, fill=PANEL,
                                outline=RULE, width=1)
            d.text((x + ts / 2, y + ts / 2), str(n), font=F(FR_PATH, 14), fill=MUTE, anchor="mm")

    # legend + facts
    ly = 330
    d.text((44, ly), "all 28 accounts are present", font=F(FB_PATH, 18), fill=INK)
    d.text((44, ly + 30), "dashed tile = 1 of 22 defining posts in no capture (DKYTBMSuTjl, 2025-06-02)",
           font=F(FR_PATH, 16), fill="#c9ced6")
    d.text((44, ly + 56), "gold ring = captured with an incomplete block (DKSZ5T6iU3E misses americatv;",
           font=F(FR_PATH, 16), fill="#c9ced6")
    d.text((44, ly + 82), "DLfpqobvgiT misses 4ludlins)", font=F(FR_PATH, 16), fill="#c9ced6")
    d.text((44, ly + 114), "archive owner is injected as the capture account (documented).",
           font=F(FR_PATH, 15), fill=MUTE)
    d.text((44, ly + 140), "Co-posting is a header credit, not intent.",
           font=F(FR_PATH, 15), fill=MUTE)
    footer(d)
    return img


CARDS = [card_1, card_2, card_3, card_4, card_5, card_6]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for i, fn in enumerate(CARDS, 1):
        im = fn()
        p = OUT / f"fancy_card_{i}.png"
        im.save(p, optimize=True)
        print(p, im.size, p.stat().st_size)


if __name__ == "__main__":
    main()
