#!/usr/bin/env python3
"""Recompute the DH22 canonical object and the known-answer object.

Standard library only. Reads the files in this directory (relative to the
script), so it runs from a checkout or from the published data folder:

    python3 check.py

Checks:
  1. canonical DH22 object (22 co-posts, 2025-05-01..2025-06-30 UTC):
     28 accounts x 22 posts, |Aut| = 768 = 4! * 2!^5
  2. known answer (sandrabronzina 2026-10-16 grid, same construction):
     282 accounts x 766 posts, |Aut| = 150,994,944

The construction (house rule): points are accounts; a block is the set of
accounts Instagram credits on one post (owner + listed collaborators, caption
tags excluded); accounts with identical block-membership rows form a class;
|Aut| = product of (class size)! over the classes. This is the same rule as
the 2026-10-20 pass (scan.py / jsonl_to_matrix.py), reproduced here in twenty
lines so there is no dependency.
"""
import csv
import math
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent


def aut_of_rows(rows):
    """rows: iterable of (point, iterable-of-block-indices). Returns (points,
    blocks, classes-desc, |Aut|)."""
    rowv = defaultdict(list)
    allblocks = set()
    for p, blocks in rows:
        bs = list(blocks)
        rowv[p] = bs
        allblocks.update(bs)
    classes = defaultdict(list)
    for p, bs in rowv.items():
        classes[tuple(bs)].append(p)
    sizes = sorted((len(v) for v in classes.values()), reverse=True)
    order = math.prod(math.factorial(k) for k in sizes)
    return len(rowv), len(allblocks), sizes, order


def read_tsv(path):
    with open(path, encoding="utf-8") as f:
        lines = [ln for ln in f if not ln.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


def canonical():
    posts = read_tsv(HERE / "canonical_posts.tsv")
    rows = defaultdict(list)
    for post in posts:
        n = int(post["n"])
        for acct in post["canonical_accounts"].split("/"):
            rows[acct].append(n)
    return aut_of_rows(rows.items())


def known_answer():
    objs = read_tsv(HERE / "known_answer_object.tsv")
    rows = []
    for o in objs:
        row = o["class_row"].strip()
        blocks = [int(x) for x in row.split(",")] if row else []
        rows.append((o["account"], blocks))
    return aut_of_rows(rows)


def main():
    ok = True

    points, blocks, classes, order = canonical()
    have = (points, blocks, order)
    want = (28, 22, 768)
    good = have == want and classes == [4, 2, 2, 2, 2, 2] + [1] * 14
    ok &= good
    print(f"canonical DH22 object: {points} accounts x {blocks} posts, "
          f"|Aut|={order} ({'OK' if good else 'FAIL'})")
    print(f"  classes: {classes}")
    if not good:
        print(f"  expected {want}, 4!*2!^5; got {have}")

    points, blocks, classes, order = known_answer()
    have = (points, blocks, order)
    want = (282, 766, 150994944)
    good = have == want
    ok &= good
    print(f"known answer (sandrabronzina): {points} x {blocks}, "
          f"|Aut|={order} ({'REPRODUCED' if good else 'FAIL'})")
    if not good:
        print(f"  expected {want}; got {have}")

    if not ok:
        return 1
    print("all checks OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
