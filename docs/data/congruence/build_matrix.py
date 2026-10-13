#!/usr/bin/env python3
"""Turn your own record of the 7 group posts into an incidence matrix that verify_automorphisms.py reads.

Input: a CSV you fill in yourself from Instagram, one row per post:
    shortcode,credited
    DU5tCKGAQDQ,timballard89 latterdaychad someaccount anotherone thirdone
(credited = every account in the post's Collaborators list, space-separated, any order; leave out the uploader).

Output: my_incidence_matrix.csv (accounts x posts, 1 = credited), with YOUR account names, not our letters.
Plain Python 3, no packages. Usage: python3 build_matrix.py my_posts.csv
"""
import csv, sys

src = sys.argv[1] if len(sys.argv) > 1 else "my_posts.csv"
with open(src, newline="") as f:
    rows = [r for r in csv.DictReader(f)]
posts = [r["shortcode"].strip() for r in rows]
cred = [set(r["credited"].split()) for r in rows]
accounts = sorted(set().union(*cred), key=lambda a: (-sum(a in c for c in cred), a))
out = "my_incidence_matrix.csv"
with open(out, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["account"] + posts)
    for a in accounts:
        w.writerow([a] + [1 if a in c else 0 for c in cred])
print(f"{len(accounts)} accounts, {len(posts)} posts, sizes {sorted(len(c) for c in cred)} -> {out}")
print(f"next: python3 verify_automorphisms.py {out}")
