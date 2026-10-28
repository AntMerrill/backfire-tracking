#!/usr/bin/env python3
"""Recompute every number on ballard-bolsonaro.html from posts.csv. Plain Python 3, no packages.
Run: python3 check.py   (prints the counts; exits 1 if any differs from the page)."""
import csv
from collections import defaultdict

BALLARD = {"timballard89", "tbfrescue", "timballardfoundationecuador"}
FRIAS = "mariofriasoficial"
posts = list(csv.DictReader(open("posts.csv")))
split = lambda s: [x for x in s.split(";") if x]

B, Z = set(), set()
part = defaultdict(lambda: [set(), set()])    # account -> [B posts, Z posts] as owner/collaborator
cred = defaultdict(lambda: [set(), set()])    # account -> [B posts, Z posts] as credited
for p in posts:
    sc = p["shortcode"]
    P = set(split(p["collaborators"])) | ({p["owner"]} if p["owner"] != "(not recorded)" else set())
    C = set(split(p["credits"]))
    if (P | C) & BALLARD: B.add(sc)
    if any("bolsonaro" in a for a in P | C) or FRIAS in P: Z.add(sc)
    for side, S in ((0, B), (1, Z)):
        if sc in S:
            for a in P: part[a][side].add(sc)
            for a in C: cred[a][side].add(sc)

seeds = BALLARD | {FRIAS} | {a for a in set(part) | set(cred) if "bolsonaro" in a}
accts = (set(part) | set(cred)) - seeds
t1 = sorted(a for a in accts if part[a][0] and part[a][1])
t2 = sorted(a for a in accts if (part[a][0] and cred[a][1]) or (cred[a][0] and part[a][1]))
t3 = sorted(a for a in accts if cred[a][0] and cred[a][1])
both = sorted(B & Z)
got = {"posts": len(posts), "B": len(B), "Z": len(Z), "in both": len(both),
       "tier 1": len(t1), "tier 2": len(t2), "tier 3": len(t3), "accounts on both sides": len(set(t1) | set(t2) | set(t3))}
page = {"posts": 4363, "B": 4018, "Z": 353, "in both": 8, "tier 1": 10, "tier 2": 7, "tier 3": 9, "accounts on both sides": 19}
for k in page:
    print(f"{k:24} {got[k]:>6}  {'OK' if got[k] == page[k] else 'DIFFERS from page: ' + str(page[k])}")
print("posts in both:", " ".join(both))
print("tier 1:", ", ".join(t1)); print("tier 2:", ", ".join(t2)); print("tier 3:", ", ".join(t3))
raise SystemExit(0 if got == page else 1)
