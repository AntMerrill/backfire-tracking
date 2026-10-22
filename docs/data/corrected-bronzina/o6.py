#!/usr/bin/env python3
"""O6: TB co-poster incidence object, on disk only.

Points = accounts (owner + collaborators) seen on TB's captured grids.
Blocks = posts. Holland rows = set of blocks a point appears in.
|Aut| = product of factorial(twin class size).

Variants test whether expofamily.cl (public, grid invisible headless) is load-bearing:
  base        all captured blocks
  no_ef_blocks  drop blocks owned by expofamily.cl (what a blind spot would hide)
  no_ef_point   drop expofamily.cl as a point, keep its blocks
Also reports the same classes when sandra's own grid is unioned in.
"""
import glob, json, math, os
from collections import defaultdict

ROOT = os.path.expanduser("~/boner_vault/dl_wm_outputs/ig_timelines")

def load(patterns):
    posts = {}
    for pat in patterns:
        for f in glob.glob(os.path.join(ROOT, pat)):
            for line in open(f):
                line = line.strip()
                if not line:
                    continue
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                sc = d.get("shortcode")
                if not sc:
                    continue
                cols = {c.lower() for c in (d.get("collaborators") or []) if c}
                own = (d.get("owner") or "").lower() or None
                cur = posts.setdefault(sc, {"owner": None, "cols": set(), "taken_at": None})
                if own and not cur["owner"]:
                    cur["owner"] = own
                cur["cols"] |= cols
                if d.get("taken_at") and not cur["taken_at"]:
                    cur["taken_at"] = d.get("taken_at")
    return posts

def blocks(posts):
    out = {}
    for sc, p in posts.items():
        pts = set(p["cols"])
        if p["owner"]:
            pts.add(p["owner"])
        if len(pts) >= 2:
            out[sc] = (frozenset(pts), p["owner"])
    return out

def aut(points, bl):
    rows = {pt: frozenset(i for i, (s, _) in enumerate(bl.values()) if pt in s) for pt in points}
    cls = defaultdict(list)
    for pt, r in rows.items():
        cls[r].append(pt)
    classes = sorted((sorted(v) for v in cls.values()), key=lambda c: (-len(c), c[0]))
    n = 1
    for c in classes:
        n *= math.factorial(len(c))
    return n, classes, rows

def report(tag, points, bl, focus=("sandrabronzina", "expofamily.cl")):
    n, classes, rows = aut(points, bl)
    twins = [c for c in classes if len(c) > 1]
    print(f"[{tag}] posts={len(bl)} points={len(points)} |Aut|={n} twin_classes={len(twins)}")
    for f in focus:
        if f in rows:
            c = next(c for c in classes if f in c)
            print(f"   {f}: posts={len(rows[f])} class_size={len(c)} class={c[:8]}{'...' if len(c) > 8 else ''}")
        else:
            print(f"   {f}: absent")
    big = [c for c in twins if any(x in c for x in focus) or len(c) > 2]
    for c in big[:6]:
        print(f"   twin>2/touching: {c}")
    return n, classes, rows

tb_patterns = [
    "timballard89.jsonl",
    "timballard89_2026-10-12/*.jsonl",
    "timballard89_2026-10-16_reverse/*.jsonl",
    "timballard89_2026-10-17_inchrome/*.jsonl",
    "timballard89_2026-10-21/*.jsonl",
    "timballard89_2026-10-22/*.jsonl",
]
tb = load(tb_patterns)
bl = blocks(tb)
pts = set().union(*(s for s, _ in bl.values()))
print(f"TB grid: {len(tb)} posts, {len(bl)} blocks with >=2 points, {len(pts)} points")

base = report("base", pts, bl)

ef_blocks = [i for i, (s, own) in enumerate(bl.values()) if own == "expofamily.cl"]
bl2 = {sc: v for i, (sc, v) in enumerate(bl.items()) if i not in ef_blocks}
report("no_ef_blocks", set().union(*(s for s, _ in bl2.values())), bl2)

pts3 = pts - {"expofamily.cl"}
report("no_ef_point", pts3, bl)

print("\n== union with sandra's grid ==")
sb = load(["sandrabronzina_2026-10-16_reverse/*.jsonl"])
merged = dict(tb)
for sc, p in sb.items():
    if sc in merged:
        merged[sc]["cols"] |= p["cols"]
        merged[sc]["owner"] = merged[sc]["owner"] or p["owner"]
    else:
        merged[sc] = p
bl4 = blocks(merged)
pts4 = set().union(*(s for s, _ in bl4.values()))
print(f"merged: {len(merged)} posts, {len(bl4)} blocks, {len(pts4)} points")
report("tb+sandra", pts4, bl4)
