# Rebuild both tables from the raw grid file and check them (backfire-tracking, 2026-10-18).  python3 replicate.py   (no packages)
# Collab = an Instagram co-author post: owner + collaborators (caption tags not counted). A TB collab post has
# @timballard89 and at least one other account on it.
import csv, json, datetime as dt
TB = "timballard89"; P = []
for l in open("timballard89_timeline_with_owners_2026-10-17.jsonl"):
    r = json.loads(l); ppl = {r["owner"]} | set(r["collaborators"])
    if TB in ppl and len(ppl) > 1:
        P.append((dt.datetime.fromtimestamp(r["taken_at"], dt.timezone.utc).strftime("%Y-%m-%d"), r["shortcode"], r["owner"], sorted(ppl - {TB})))
P.sort(key=lambda x: (x[0], x[1]))
pub = [(r["date_utc"], r["shortcode"], r["owner"], r["others_with_tb"].split()) for r in csv.DictReader(open("tb_collab_posts.csv"))]
ok1 = sorted(P) == sorted(pub)
A = {}
for d, c, o, x in P:
    for a in x:
        f = A.setdefault(a, {"first": d, "n": 0, "own": 0}); f["n"] += 1; f["own"] += o == a
acc = {r["account"]: r for r in csv.DictReader(open("tb_collab_accounts.csv"))}
ok2 = set(A) == set(acc) and all(A[a]["first"] == acc[a]["first_collab"] and A[a]["n"] == int(acc[a]["posts_with_tb"]) and A[a]["own"] == int(acc[a]["owned_by_them"]) for a in A)
print(f"collab posts: {len(P)} (owned by the other account: {sum(1 for p in P if p[2] != TB)}), accounts: {len(A)}")
print("tb_collab_posts.csv", "matches" if ok1 else "DIFFERS"); print("tb_collab_accounts.csv", "matches" if ok2 else "DIFFERS")
print("REPLICATED" if ok1 and ok2 else "NOT REPLICATED")
