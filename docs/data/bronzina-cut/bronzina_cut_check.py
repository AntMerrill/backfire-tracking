#!/usr/bin/env python3
"""Check "Sixteen links, one block" (docs/bronzina-cut.html). Plain Python 3, no packages.

Rebuilds "two worlds, one vertex" (one-vertex.html) from the already-public matrices, then again as our login saw it on
Nov 6, 2026, and prints accounts, posts, lines, pieces and cut vertices for both.
  W1 = the Chadverse core: ../who-went-first/incidence_matrix.csv (letters A-K for smaller accounts) + the host
       latterdayavenger on all 7 posts (Instagram leaves the owner off its own collaborator list).
  W2 = Bronzina's coset, the first 16 timballard89 x sandrabronzina co-posts: ../holland24/matrix_first16.csv.
  Nov 6: s16_status.csv (this folder) for W2; for W1, B6 and B7 are off every grid we hold, B1-B5 unchanged
       with TB still listed (checked on latterdayavenger's grid, same login).
Run from this folder:  python3 bronzina_cut_check.py
"""
import csv, itertools
from collections import defaultdict

def rows(p):
    r = list(csv.reader(open(p)))
    return r[0][1:], {x[0]: [int(v) for v in x[1:]] for x in r[1:]}

TB = "TB"   # W1 calls him TB; W2 calls him timballard89: same account
w1_codes, w1 = rows("../who-went-first/incidence_matrix.csv")
w2_codes, w2 = rows("../holland24/matrix_first16.csv")
blocks_then = []
for j, c in enumerate(w1_codes):
    blocks_then.append(("W1", c, {a for a, v in w1.items() if v[j]} | {"LDA"}))
for j, c in enumerate(w2_codes):
    blocks_then.append(("W2", c, {("TB" if a == "timballard89" else a) for a, v in w2.items() if v[j]}))

status = list(csv.DictReader(open("s16_status.csv")))
assert [s["shortcode"] for s in status] == w2_codes, "status rows must follow the matrix's post order"
blocks_now = [b for b in blocks_then if b[0] == "W1" and b[1] not in ("DW99EnrgVYo", "DXQTcYlgZ5c")]
for s in status:
    if s["on_tb_grid_nov6"] == "1":
        blocks_now.append(("W2", s["shortcode"], {("TB" if a == "timballard89" else a) for a in s["accounts_nov6_excluding_sb"].split(";")}))

def graph(blocks, points):
    adj = {p: set() for p in points}
    for _, _, acc in blocks:
        for x, y in itertools.combinations(sorted(acc), 2):
            adj[x].add(y); adj[y].add(x)
    return adj

def pieces(adj, drop=None):
    seen, n = set(), 0
    for s in adj:
        if s == drop or s in seen: continue
        n += 1; stack = [s]; seen.add(s)
        while stack:
            for y in adj[stack.pop()]:
                if y != drop and y not in seen: seen.add(y); stack.append(y)
    return n

def report(name, blocks, points):
    adj = graph(blocks, points)
    k = pieces(adj)
    cuts = sorted(p for p in adj if pieces(adj, p) > k - (0 if adj[p] else 1))
    lines = sum(len(v) for v in adj.values()) // 2
    lonely = sorted(p for p in adj if not adj[p])
    print(f"{name}: {len(adj)} accounts, {len(blocks)} posts, {lines} lines, {k} piece(s); "
          f"cut vertices {cuts}; accounts with no line {lonely}")
    return adj

pts_then = set().union(*(b[2] for b in blocks_then))
pts_now = pts_then | set().union(*(b[2] for b in blocks_now))      # keep every Oct 16 account, so the ones left alone show
t = report("Oct 16 (as one-vertex.html)", blocks_then, sorted(pts_then))
n = report("Nov 6, our login", blocks_now, sorted(pts_now))
sb_then = sum("sandrabronzina" in b[2] for b in blocks_then)
sb_now = sum("sandrabronzina" in b[2] for b in blocks_now)
print(f"sandrabronzina on {sb_then} of {sum(b[0]=='W2' for b in blocks_then)} Bronzina-coset posts on Oct 16; "
      f"on {sb_now} of {sum(b[0]=='W2' for b in blocks_now)} still on Tim's grid on Nov 6")
gone = [s["shortcode"] for s in status if s["on_tb_grid_nov6"] == "0"]
print(f"off Tim's grid on Nov 6: {len(gone)} ({', '.join(gone)}), all owned by "
      f"{sorted({s['owner'] for s in status if s['on_tb_grid_nov6'] == '0'})}")
new = sorted(set().union(*(b[2] for b in blocks_now if b[0]=='W2')) - set().union(*(b[2] for b in blocks_then if b[0]=='W2')))
print(f"accounts on the Bronzina-coset posts on Nov 6 that weren't on Oct 16: {new}")
