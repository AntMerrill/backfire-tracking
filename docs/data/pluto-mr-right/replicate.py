# Replicate the Pluto's Mr. Right fingerprint test from the files in this folder (backfire-tracking, 2026-10-17).
#   pip install pillow numpy      then      python replicate.py
# 1. Re-cuts every crop from screenshots/ at the boxes in crops/MANIFEST.tsv and checks each one's sha256.
# 2. Recomputes both fingerprint tables and checks them against the published ones:
#    - fingerprints_vs_S6E89.tsv          plain dHash of each fixed-box crop vs the S6E89 crop
#    - fingerprints_aligned_wide_vs_S6E89.tsv   the same with a small alignment search (the boxes cut the photos at
#      different offsets): the reference's face window, slid over each crop at zoom .55-1.80 in 2 px steps, minimum kept
# Fingerprint = dHash (64 bits: 9x8 grayscale, LANCZOS, left<right per row); same image = distance 0-5.
import csv, hashlib, io, sys
from pathlib import Path
import numpy as np
from PIL import Image

D = Path(__file__).parent
def dhash(img):
    g = np.asarray(img.convert("L").resize((9, 8), Image.LANCZOS), dtype=np.int16)
    return int("".join("1" if b else "0" for b in (g[:, 1:] > g[:, :-1]).flatten()), 2)
def ham(a, b): return bin(a ^ b).count("1")
def png_sha(img):
    b = io.BytesIO(); img.save(b, "PNG"); return hashlib.sha256(b.getvalue()).hexdigest()

ok = True
M = list(csv.DictReader(open(D / "crops/MANIFEST.tsv"), delimiter="\t"))
bad = [m["crop"] for m in M if png_sha(Image.open(D / "screenshots" / f"{m['frame']}.png").crop(tuple(int(m[k]) for k in ("x0", "y0", "x1", "y1")))) != m["sha256"]]
print(f"1. crops re-cut from the screenshots: {len(M) - len(bad)}/{len(M)} byte-identical" + (f"  MISMATCH: {bad}" if bad else ""))
ok &= not bad

crop = lambda name: Image.open(D / "crops" / name)
REF = {"emma": "f04_c2r1_designed_host.png", "riggs": "f04_c2r1_designed_guest.png"}   # S6E89
def face(name, fx, fy):
    im = crop(name); w, h = im.size; return im.crop((int(w * fx[0]), int(h * fy[0]), int(w * fx[1]), int(h * fy[1])))
FACE = {"emma": face(REF["emma"], (.15, .95), (.08, .70)), "riggs": face(REF["riggs"], (.05, .95), (.05, .80))}
def aligned(ref, name):
    rh = dhash(ref); rw, rhh = ref.size; c = crop(name); W, H = c.size; best = 64
    for s in np.arange(.55, 1.81, .05):
        w, h = int(rw * s), int(rhh * s)
        if w > W or h > H: continue
        for x in range(0, W - w + 1, 2):
            for y in range(0, H - h + 1, 2):
                best = min(best, ham(rh, dhash(c.crop((x, y, x + w, y + h)))))
    return best

for fname, col, fn in (("fingerprints_vs_S6E89.tsv", "dhash_distance", lambda who, n: ham(dhash(crop(n)), dhash(crop(REF[who])))),
                       ("fingerprints_aligned_wide_vs_S6E89.tsv", "min_dhash_aligned", lambda who, n: aligned(FACE[who], n))):
    rows = list(csv.DictReader(open(D / fname), delimiter="\t")); diff = []
    for r in rows:
        d = fn(r["who"], r["crop"])
        if d != int(r[col]): diff.append((r["crop"], r[col], d))
    print(f"2. {fname}: {len(rows) - len(diff)}/{len(rows)} distances reproduced" + (f"  DIFFERENT: {diff}" if diff else ""))
    ok &= not diff

same = lambda who: sum(1 for r in csv.DictReader(open(D / "fingerprints_aligned_wide_vs_S6E89.tsv"), delimiter="\t") if r["who"] == who and int(r["min_dhash_aligned"]) <= 5)
print(f"   Riggs: {same('riggs')} of 3 crops the same image as S6E89; Emma: {same('emma')} of 63 host crops (incl. video-call stills)")
print("REPLICATED" if ok else "NOT REPLICATED"); sys.exit(0 if ok else 1)
