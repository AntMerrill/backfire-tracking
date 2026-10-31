#!/usr/bin/env python3
"""m by ownership in S16 (for-agents registry M2). Plain Python 3, stdlib only.
For each account that owns posts among the first 16 timballard89 x sandrabronzina co-posts, take the set of posts it owns, and check
whether every recurring guest (r >= 2, not on every post) is credited only on those posts. Then the pairwise overlaps of those guests.
Owners: ../tb-collabs/timballard89_timeline_with_owners_2026-10-17.jsonl (owner field, as captured). Rows: ../holland24/matrix_first16.csv.
Usage (from docs/data/for-agents):  python3 m_by_ownership.py        claude, for John, 2026-10-31."""
import csv, json, os
from collections import Counter
from itertools import combinations
here = os.path.dirname(os.path.abspath(__file__))
R = list(csv.reader(open(os.path.join(here, "../holland24/matrix_first16.csv"))))
codes = R[0][1:]
rows = {r[0]: {i + 1 for i, v in enumerate(r[1:]) if v == "1"} for r in R[1:]}
owner = {}
for line in open(os.path.join(here, "../tb-collabs/timballard89_timeline_with_owners_2026-10-17.jsonl")):
    p = json.loads(line); owner[p["shortcode"]] = p.get("owner")
own = {i + 1: owner[c] for i, c in enumerate(codes)}
owned = {}
for b, a in own.items(): owned.setdefault(a, set()).add(b)
frame = [a for a, s in rows.items() if len(s) == 16]
recurring = sorted(a for a, s in rows.items() if len(s) >= 2 and a not in frame)
print("owners (posts owned):", ", ".join(f"{a} {len(s)}" for a, s in sorted(owned.items(), key=lambda kv: -len(kv[1]))))
print("frame (on all 16):", frame)
print("recurring guests:", recurring)
for a, s in sorted(owned.items(), key=lambda kv: -len(kv[1])):
    inside = [g for g in recurring if g != a and rows[g] <= s]
    print(f"  owner {a:18s} owns {sorted(s)}  guests seated only on its posts: {len(inside)} of {len([g for g in recurring if g != a])}")
m = [a for a, s in owned.items() if all(rows[g] <= s for g in recurring if g != a)]
crew = [g for g in recurring if g not in m]
lam = {f"{x}+{y}": len(rows[x] & rows[y]) for x, y in combinations(crew, 2)}
print("m by ownership:", m)
print("pairwise posts shared by the other recurring guests:", lam)
assert m == ["expofamily.cl"] and sorted(owned["expofamily.cl"]) == [11, 12, 13, 14, 15] and set(lam.values()) == {2}
assert Counter(own.values()) == Counter({"sandrabronzina": 6, "expofamily.cl": 5, "liberal.noticias": 1, "maaydelara": 1,
                                        "timballard89": 1, "larinoar": 1, "ivetteavaria": 1})
print("ok")
