# claude 2026-10-17: decode pages/pNNN.txt (from page_walker.js) into <user>_timeline.jsonl, oldest first.
#   python3 decode_pages.py <capture_dir> <user>
import glob, json, sys
cap, user = sys.argv[1], sys.argv[2]
D, recs = {}, {}
for f in sorted(glob.glob(f"{cap}/pages/p*.txt")):
    L = open(f).read().rstrip("\n").split("\n")
    for kv in L[1][2:].split():
        k, v = kv.split("=", 1); D[k] = v
    for row in L[2:]:
        if not row.strip(): continue
        code, ta, dl, o, c, cr = row.split(","); ta = int(ta); idt = ta + int(dl)
        nm = lambda s: sorted(D[x] for x in s.split(".") if x)
        recs[code] = {"shortcode": code, "taken_at": ta, "id_time": idt, "owner": D.get(o), "collaborators": nm(c),
                      "credits": nm(cr), "date_mismatch": abs(idt - ta) > 3600}
R = sorted(recs.values(), key=lambda r: r["taken_at"])
open(f"{cap}/{user}_timeline.jsonl", "w").write("".join(json.dumps(r) + "\n" for r in R))
print(len(R), "posts ->", f"{cap}/{user}_timeline.jsonl")
