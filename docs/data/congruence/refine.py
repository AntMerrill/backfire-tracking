#!/usr/bin/env python3
"""Second check of the orbits: colour refinement on the account-post incidence graph. Plain Python 3, no packages.
Every account starts with one colour; each round recolours every account by the colours of its posts and every post by the
colours of its accounts. Accounts a symmetry can swap always keep the same colour, so the number of final colour classes is
at most the number of orbits. Usage: python3 refine.py [incidence_matrix.csv]"""
import csv, sys
rows = list(csv.reader(open(sys.argv[1] if len(sys.argv) > 1 else "incidence_matrix.csv")))
P = rows[0][1:]; A = [r[0] for r in rows[1:]]
inc = {r[0]: [P[i] for i, v in enumerate(r[1:]) if v == "1"] for r in rows[1:]}
mem = {p: [a for a in A if p in inc[a]] for p in P}
ca = {a: 0 for a in A}; cp = {p: 0 for p in P}
print("start: 1 account class")
for it in range(1, 50):
    na = {a: (ca[a], tuple(sorted(cp[p] for p in inc[a]))) for a in A}
    npp = {p: (cp[p], tuple(sorted(ca[a] for a in mem[p]))) for p in P}
    ka = {k: i for i, k in enumerate(sorted(set(na.values()), key=repr))}; kp = {k: i for i, k in enumerate(sorted(set(npp.values()), key=repr))}
    na = {a: ka[na[a]] for a in A}; npp = {p: kp[npp[p]] for p in P}
    stable = len(set(na.values())) == len(set(ca.values())) and len(set(npp.values())) == len(set(cp.values()))
    ca, cp = na, npp
    print(f"round {it}: {len(set(ca.values()))} account classes, {len(set(cp.values()))} post classes")
    if stable:
        break
groups = {}
for a in A:
    groups.setdefault(ca[a], []).append(a)
print("classes with more than one account:", sorted(sorted(g) for g in groups.values() if len(g) > 1))
