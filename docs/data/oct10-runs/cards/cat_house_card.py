# One-off (John 10-21): cartoon of THE SET run as a house of cats, drawn with plain shapes (no gen-AI).
# v4 (John): Isaiah outside (hits only DeXgRo8Sb9b, DeYSftAI_6-, the Oct 11 posts). v3 (John): set1 run. Parlor = {Catherine, forgive} (identical rows; one is an outside cat passing through); kitchen = the other 7.
import sys, hashlib
from PIL import Image, ImageDraw, ImageFont
out = sys.argv[1]
W, H = 1600, 900
c = Image.new("RGB", (W, H), "#cfe8ff"); d = ImageDraw.Draw(c)
F = lambda s, b=True: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if b else ""), s)
d.rectangle([0, 760, W, H], fill="#7cc36a")                                   # grass
d.polygon([(160, 300), (750, 70), (1340, 300)], fill="#b5523b", outline="black", width=4)   # roof
d.rectangle([200, 300, 1300, 780], fill="#fff4dc", outline="black", width=4)  # house
d.line([(640, 300), (640, 780)], fill="black", width=4)                       # wall between rooms
d.rectangle([660, 640, 760, 780], fill="#8a5a2b", outline="black", width=3)   # door (to kitchen side)
sign = "BONER-IS-THE-OWNER"
tw = d.textlength(sign, font=F(40)); d.rounded_rectangle([750 - tw/2 - 20, 160, 750 + tw/2 + 20, 220], 10, fill="white", outline="black", width=3)
d.text((750 - tw/2, 166), sign, font=F(40), fill="black")
for x, t in [(420, "PARLOR"), (970, "KITCHEN")]:
    d.text((x - d.textlength(t, font=F(34))/2, 315), t, font=F(34), fill="#555")

def cat(x, y, fur, name, s=1.0):
    r = 34 * s
    d.ellipse([x - 1.3*r, y, x + 1.3*r, y + 1.9*r], fill=fur, outline="black", width=3)            # body
    d.arc([x + 0.8*r, y + 0.2*r, x + 2.2*r, y + 1.7*r], 270, 80, fill="black", width=6)           # tail
    d.ellipse([x - r, y - 1.6*r, x + r, y + 0.3*r], fill=fur, outline="black", width=3)            # head
    for sx in (-1, 1):
        d.polygon([(x + sx*0.95*r, y - 0.9*r), (x + sx*0.85*r, y - 2.1*r), (x + sx*0.2*r, y - 1.5*r)], fill=fur, outline="black")
        d.ellipse([x + sx*0.4*r - 6, y - 0.95*r - 7, x + sx*0.4*r + 6, y - 0.95*r + 7], fill="black")   # eyes
        for dy in (-6, 4):
            d.line([(x + sx*0.25*r, y - 0.45*r), (x + sx*1.3*r, y - 0.45*r + dy*1.6)], fill="black", width=2)  # whiskers
    d.polygon([(x - 6, y - 0.6*r), (x + 6, y - 0.6*r), (x, y - 0.45*r)], fill="#e86a8a")              # nose
    tw = d.textlength(name, font=F(24)); d.text((x - tw/2, y + 2.0*r + 4), name, font=F(24), fill="black")

for i, n in enumerate(["Catherine", "forgive"]):
    cat(330 + i*180, 520, "#f2a03d", n)
d.text((420 - d.textlength("one of these two is", font=F(24, False))/2, 380), "one of these two is", font=F(24, False), fill="#333")
d.text((420 - d.textlength("an outside cat passing through", font=F(24, False))/2, 410), "an outside cat passing through", font=F(24, False), fill="#333")
K = ["God", "Utah", "Israel", "Backfire", "war", "children"]
for i, n in enumerate(K):
    cat(800 + (i % 3)*180 + (60 if i >= 3 else 0), 430 + (i // 3)*190, "#a9a9a9", n, 0.8)
cat(1460, 690, "#333333", "Isaiah", 0.9)
for k, t in enumerate(["outside: never in an", "Oct 10 post"]):
    d.text((1460 - d.textlength(t, font=F(22, False))/2, 560 + k*28), t, font=F(22, False), fill="black")
d.text((40, 810), "Tim Ballard's Instagram, Oct 10 19:00 -> Oct 11 20:50: 8 posts, 9 words: 8 cats in the house, Isaiah outside.", font=F(24, False), fill="black")
d.text((40, 845), "Catherine and forgive sit in exactly the same post, so nobody can tell them apart: |Aut| = 2.   antmerrill.github.io/backfire-tracking/data/oct10-runs/", font=F(20, False), fill="black")
if "--fb" in sys.argv:   # v5 (John): FB jazz headline; sticker goes on after with dl_wm stamp_sticker.py
    for k, t in enumerate(["3rd HOLLAND OBJECT", "FOUND TODAY: ORDER 2"]):
        d.text((30, 14 + k*50), t, font=F(44), fill="#d62828", stroke_width=4, stroke_fill="#ffd60a")
    for sx, sy in [(240, 470), (600, 470), (420, 455)]:
        d.text((sx, sy), "\u2605", font=F(30), fill="#ffb703", stroke_width=1, stroke_fill="black")
c.save(out); print(out, hashlib.sha256(open(out, "rb").read()).hexdigest())
