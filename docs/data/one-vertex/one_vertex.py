#!/usr/bin/env python3
"""Two worlds, one vertex: where the Chadverse core and Bronzina's Coset meet. Plain Python 3, no packages.

W1 = ../who-went-first/incidence_matrix.csv  (the 7 group posts; rows TB, LDC, A-K) + latterdayavenger, who posted all 7
W2 = ../holland24/matrix_first16.csv         (the first 16 timballard89 x sandrabronzina co-posts, 15 accounts)
Only TB is named across files (TB = timballard89). A link joins two accounts that share at least one post.
Usage: python3 one_vertex.py
"""
import csv, itertools, os
here = os.path.dirname(os.path.abspath(__file__))
def load(p):
    R = list(csv.reader(open(os.path.join(here, p))))
    return R[0][1:], {r[0]: {c for c, v in zip(R[0][1:], r[1:]) if v == "1"} for r in R[1:]}
P1, W1 = load("../who-went-first/incidence_matrix.csv"); W1 = {("timballard89" if a == "TB" else "W1:" + a): s for a, s in W1.items()}
W1["W1:LDA"] = set(P1)
P2, W2 = load("../holland24/matrix_first16.csv")
both = set(W1) & set(W2)
print(f"W1 (Chadverse core): {len(W1)} accounts x {len(P1)} posts;  W2 (Bronzina's Coset): {len(W2)} accounts x {len(P2)} posts")
print("posts in both:", len(set(P1) & set(P2)), "  accounts in both:", sorted(both))
for a in sorted(both):
    print(f"  {a}: on {len(W1[a])} of {len(P1)} W1 posts, {len(W2[a])} of {len(P2)} W2 posts")
posts = {a: W1.get(a, set()) | W2.get(a, set()) for a in set(W1) | set(W2)}
adj = {a: {b for b in posts if b != a and posts[a] & posts[b]} for a in posts}
print("accounts:", len(adj), " links:", sum(map(len, adj.values())) // 2)
def pieces(skip=frozenset()):
    seen, n = set(skip), 0
    for s in adj:
        if s in seen: continue
        n += 1; st = [s]
        while st:
            x = st.pop()
            if x in seen: continue
            seen.add(x); st += [y for y in adj[x] if y not in seen]
    return n
cuts = [a for a in adj if pieces({a}) > pieces()]
print("pieces:", pieces(), "  cut vertices:", cuts, "  pieces without TB:", pieces({"timballard89"}))
cross = [(a, b) for a in W1 for b in W2 if a not in both and b not in both]
print("links between the worlds not through TB:", sum(1 for a, b in cross if b in adj[a]))
# betweenness (Brandes, unweighted, unordered pairs)
bc = dict.fromkeys(adj, 0.0)
for s in adj:
    S, P, sig, d, Q = [], {v: [] for v in adj}, dict.fromkeys(adj, 0), dict.fromkeys(adj, -1), [s]
    sig[s], d[s] = 1, 0
    while Q:
        v = Q.pop(0); S.append(v)
        for w in adj[v]:
            if d[w] < 0: d[w] = d[v] + 1; Q.append(w)
            if d[w] == d[v] + 1: sig[w] += sig[v]; P[w].append(v)
    dl = dict.fromkeys(adj, 0.0)
    while S:
        w = S.pop()
        for v in P[w]: dl[v] += sig[v] / sig[w] * (1 + dl[w])
        if w != s: bc[w] += dl[w]
bc = {a: v / 2 for a, v in bc.items()}
top = sorted(bc.items(), key=lambda kv: -kv[1])[:2]
print(f"betweenness: {top[0][0]} {top[0][1]:.1f}, next {top[1][1]:.1f}")
print(f"cross-world pairs (one account from each side, not TB): {len(W1) - 1} x {len(W2) - 1} = {(len(W1) - 1) * (len(W2) - 1)}, every one through TB")
