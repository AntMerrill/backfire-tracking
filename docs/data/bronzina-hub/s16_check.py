#!/usr/bin/env python3
"""S16 (TB x SB, first 16 co-posts): recompute every number the result paper uses, and run the null model.

Reason (AGENTS.md rule 7):
  (1) purpose: one script that (a) rebuilds rows, rooms, |Aut_<| from the matrix and (b) samples the
      fixed-margins null model for the paper's statistics S1-S4.
  (2) checked: holland24/verify_automorphisms.py (unordered |Aut| only; no rooms-by-r, no null model),
      2026-10-23 opencode/join_dates/join_dates.py (dates, not incidence). Neither samples a null.
  (3) lives: one-off in this dated folder.

Usage: python3 -I s16_check.py MATRIX.csv [N_SAMPLES] [SEED]
Stdlib only. Deterministic for a given seed.
"""
import csv
import math
import random
import sys
from itertools import combinations

HOST = ("timballard89", "sandrabronzina")


def load(path):
    with open(path, newline="") as f:
        rows = list(csv.reader(f))
    posts = rows[0][1:]
    inc = {r[0]: frozenset(j for j, v in enumerate(r[1:]) if v.strip() == "1") for r in rows[1:]}
    return posts, inc


def rooms(inc):
    by = {}
    for p, row in inc.items():
        by.setdefault(row, []).append(p)
    return sorted((sorted(v) for v in by.values()), key=lambda v: (-len(v), v))


def stats(inc, guests, nblocks):
    """S1 rooms of >=2 recurring guests; S2 blocks touched by recurring guests;
    S3 those blocks form one interval of the chain; S4 one guest row contains every other recurring row."""
    rec = [g for g in guests if len(inc[g]) >= 2]
    s1 = sum(1 for room in rooms({g: inc[g] for g in rec}) if len(room) >= 2)
    touched = sorted(set().union(*(inc[g] for g in rec))) if rec else []
    s2 = len(touched)
    s3 = bool(touched) and touched[-1] - touched[0] + 1 == len(touched)
    s4 = any(all(inc[g] <= inc[h] for g in rec if g != h) for h in rec) if len(rec) >= 2 else False
    return s1, s2, s3, s4


def swap_chain(inc, guests, rng, steps):
    """Checkerboard swaps on the guest x block 0-1 matrix: keeps every row sum and column sum."""
    m = {g: set(inc[g]) for g in guests}
    for _ in range(steps):
        a, b = rng.sample(guests, 2)
        xa = list(m[a] - m[b])
        xb = list(m[b] - m[a])
        if not xa or not xb:
            continue
        i, j = rng.choice(xa), rng.choice(xb)
        m[a].remove(i); m[a].add(j)
        m[b].remove(j); m[b].add(i)
    return m


def main():
    path = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 20261029
    posts, inc = load(path)
    nb = len(posts)
    guests = sorted(p for p in inc if p not in HOST)

    print(f"matrix {path}: v={len(inc)} b={nb}")
    print("hosts on every block:", all(len(inc[h]) == nb for h in HOST))
    print("r:", {p: len(inc[p]) for p in sorted(inc, key=lambda p: (-len(inc[p]), p))})
    print("guest count per block:", [sum(1 for g in guests if j in inc[g]) for j in range(nb)])
    rm = rooms(inc)
    print("rooms of size>1:", [(r, sorted(inc[r[0]])) for r in rm if len(r) > 1])
    print("|Aut_<| = prod |room|! =", math.prod(math.factorial(len(r)) for r in rm))
    rec = [g for g in guests if len(inc[g]) >= 2]
    print("recurring guests:", {g: sorted(j + 1 for j in inc[g]) for g in rec})
    print("distinct rows among recurring guests:", len({inc[g] for g in rec}) == len(rec))
    for a, b in combinations(rec, 2):
        print(f"  |R({a}) ^ R({b})| = {len(inc[a] & inc[b])}")
    obs = stats(inc, guests, nb)
    print("observed S1,S2,S3,S4 =", obs)

    rng = random.Random(seed)
    m = swap_chain(inc, guests, rng, 20000)  # burn-in
    c1 = c2 = c3 = c4 = call = 0
    for _ in range(n):
        m = swap_chain(m, guests, rng, 200)
        s = stats({g: frozenset(v) for g, v in m.items()}, guests, nb)
        c1 += s[0] <= obs[0]
        c2 += s[1] <= obs[1]
        c3 += s[2] >= obs[2]
        c4 += s[3] >= obs[3]
        call += (s[1] <= obs[1]) and (s[2] >= obs[2]) and (s[3] >= obs[3])
    print(f"null: {n} samples, seed {seed}, 200 swaps apart after 20000 burn-in")
    print(f"  P(S1 <= {obs[0]}) = {c1 / n:.4f}")
    print(f"  P(S2 <= {obs[1]}) = {c2 / n:.4f}")
    print(f"  P(S3 >= {obs[2]}) = {c3 / n:.4f}")
    print(f"  P(S4 >= {obs[3]}) = {c4 / n:.4f}")
    print(f"  P(S2<=obs and S3 and S4) = {call / n:.4f}")


if __name__ == "__main__":
    main()
