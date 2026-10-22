#!/usr/bin/env python3
"""Check the symmetry claim on the 'Who went first' page: |Aut(N)| = 12, orbits {TB, LDC} and {H, I, J}.

Reads incidence_matrix.csv (rows = accounts, columns = the 7 group posts, 1 = credited).
Aut(N) = every relabelling of the accounts that carries the set of posts onto itself.
Plain Python 3, no packages. Usage: python3 verify_automorphisms.py [incidence_matrix.csv]
"""
import csv, itertools, sys

path = sys.argv[1] if len(sys.argv) > 1 else "incidence_matrix.csv"
with open(path, newline="") as f:
    rows = list(csv.reader(f))
posts = rows[0][1:]
pts = [r[0] for r in rows[1:]]
blocks = [frozenset(r[0] for r in rows[1:] if r[1 + j] == "1") for j in range(len(posts))]
block_set = sorted(blocks, key=sorted)
r = {p: sum(p in b for b in blocks) for p in pts}
lam = {frozenset(e): sum(set(e) <= b for b in blocks) for e in itertools.combinations(pts, 2)}

auts = []
def extend(m):
    if len(m) == len(pts):
        img = sorted((frozenset(m[p] for p in b) for b in blocks), key=sorted)
        if img == block_set:
            auts.append(dict(m))
        return
    p = pts[len(m)]
    for q in pts:
        if q in m.values() or r[q] != r[p]:
            continue
        if all(lam[frozenset((p, x))] == lam[frozenset((q, m[x]))] for x in m):
            m[p] = q; extend(m); del m[p]
extend({})

orbits = {frozenset(a[p] for a in auts) for p in pts}
print(f"{len(pts)} accounts, {len(blocks)} posts, block sizes {sorted({len(b) for b in blocks})}")
print("r (posts per account):", r)
print("pairs that ever meet:", sum(1 for v in lam.values() if v), "of", len(lam))
print("|Aut(N)| =", len(auts))
print("orbits:", sorted((sorted(o) for o in orbits), key=lambda o: (-len(o), o)))
