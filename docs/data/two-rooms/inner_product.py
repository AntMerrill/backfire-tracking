#!/usr/bin/env python3
"""Where two Holland objects meet: the inner product <N1, N2> = sum over shared accounts x of r1(x) * r2(x),
r = number of posts the account is on. Plain Python 3, no packages.

N1 = ../congruence/incidence_matrix.csv   (latterdayavenger's grid, 113 accounts x 354 posts; named rows LDA, LDC, TB, the rest s001-s110)
N2 = ../holland24/matrix_first16.csv      (first 16 timballard89 x sandrabronzina co-posts, 15 named accounts)
The s-labels are private (key not published). We checked the key: none of them is any of N2's accounts.
Usage: python3 inner_product.py
"""
import csv, os
here = os.path.dirname(os.path.abspath(__file__))
def load(p):
    R = list(csv.reader(open(os.path.join(here, p)))); return R[0][1:], {r[0]: [int(v) for v in r[1:]] for r in R[1:]}
named = {"TB": "timballard89", "LDC": "latterdaychad", "LDA": "latterdayavenger"}
P1, N1 = load("../congruence/incidence_matrix.csv"); N1 = {named.get(a, a): v for a, v in N1.items()}
P2, N2 = load("../holland24/matrix_first16.csv")
shared = sorted(set(N1) & set(N2))
print(f"N1: {len(N1)} accounts x {len(P1)} posts;  N2: {len(N2)} accounts x {len(P2)} posts")
print("accounts in both:", shared)
total = 0
for a in shared:
    r1, r2 = sum(N1[a]), sum(N2[a]); total += r1 * r2
    print(f"  {a}: on {r1} of N1's posts, {r2} of N2's posts -> {r1} x {r2} = {r1 * r2}")
print("<N1, N2> =", total)
pairs = sum(1 for i in range(len(P1)) for j in range(len(P2)) if any(N1[a][i] and N2[a][j] for a in shared))
print(f"post pairs (one from each) that share an account: {pairs} of {len(P1) * len(P2)}")
