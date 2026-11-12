#!/usr/bin/env python3
"""Dark Horse article, section 6: timballard89's grid after May-June 2025.

    python3 after_two_months.py           # print the section-6 numbers
    python3 after_two_months.py --check   # compare them with inputs/numbers.json; exit 1 if anything differs

Source: inputs/timballard89_2026-11-06_reverse_0853.jsonl, our copy of the grid saved Nov 6, 2026
(one JSON object per post: shortcode, taken_at, owner, collaborators). Python 3 standard library only.

Method:
  1. A post is on the grid if it has an owner. The span is the first to the last taken_at (UTC).
  2. A co-post is a post whose owner is not timballard89, or whose collaborators list is non-empty.
     (That is the article's "shared with at least one other account".)
  3. A partner of timballard89 is any account in a co-post's header (owner + collaborators) other than
     timballard89 himself; partners are ranked by how many co-posts they are on.
  4. The seven Brazilian politicians are the ones who appeared on the May-June 2025 co-posts.
  5. Months are UTC calendar months of the co-posts: with @timballardfoundationecuador, and all others.
"""
import collections
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE if (HERE / "numbers.json").exists() else HERE / "inputs"  # flat beside the script, or in inputs/
SRC = DATA / "timballard89_2026-11-06_reverse_0853.jsonl"
NUMBERS = DATA / "numbers.json"
CENTRE = "timballard89"
BR7 = ["biakicis", "damaresalvesoficial", "generalgirao", "mariofriasoficial",
       "carlosjordy", "gusgayer", "jorgeseifjunior"]


def utc(t):
    return datetime.fromtimestamp(t, timezone.utc)


def accounts(row):
    return {row["owner"]} | set(row.get("collaborators") or [])


def compute():
    rows = [json.loads(line) for line in open(SRC) if line.strip()]
    tb = [r for r in rows if "owner" in r]
    co = [r for r in tb if r["owner"] != CENTRE or r.get("collaborators")]
    partners = collections.Counter(a for r in co for a in accounts(r) - {CENTRE})
    br_hits = {a: partners[a] for a in BR7}
    br_posts = {a: sorted(r["shortcode"] for r in co if a in accounts(r)) for a in BR7}
    ver = sorted([utc(r["taken_at"]).date().isoformat(), r["shortcode"], r["owner"]]
                 for r in co if "eduardoverastegui" in accounts(r))
    lais = sorted([utc(r["taken_at"]).date().isoformat(), r["shortcode"]]
                  for r in co if "laisjordy" in accounts(r))
    mon = collections.defaultdict(lambda: [0, 0])
    for r in co:
        mon[utc(r["taken_at"]).strftime("%Y-%m")][
            0 if "timballardfoundationecuador" in accounts(r) else 1] += 1
    return {
        "span": [utc(min(r["taken_at"] for r in tb)).date().isoformat(),
                 utc(max(r["taken_at"] for r in tb)).date().isoformat()],
        "posts": len(tb),
        "coposts": len(co),
        "top12": sorted(([a, n] for a, n in partners.most_common(12)),
                        key=lambda p: (-p[1], p[0])),
        "br7": br_hits,
        "br7_posts": br_posts,
        "verastegui": ver,
        "laisjordy": lais,
        "monthly": {m: mon[m] for m in sorted(mon)},
    }


def show(n):
    out = []
    out.append("timballard89's grid, as held: section 6 of the article")
    out.append("source: inputs/timballard89_2026-11-06_reverse_0853.jsonl (our copy, saved Nov 6, 2026)")
    out.append("")
    out.append(f"date span : {n['span'][0]} to {n['span'][1]}")
    out.append(f"posts     : {n['posts']:,}")
    out.append(f"co-posts  : {n['coposts']:,}")
    out.append("")
    out.append("top 12 partners (co-posts Oct 2025 - Nov 2026):")
    for i, (a, c) in enumerate(n["top12"], 1):
        out.append(f"  {i:2d}. @{a:<30s} {c:>4d}")
    out.append("")
    out.append("the seven Brazilian politicians who appear on the May-June 2025 co-posts,")
    out.append("and how many co-posts on this grid put them beside timballard89:")
    for a in BR7:
        sc = n["br7_posts"][a]
        out.append(f"  @{a:<24s} {n['br7'][a]:>3d}   " + (" ".join(sc) if sc else "(no co-posts)"))
    out.append("")
    out.append(f"@eduardoverastegui co-posts ({len(n['verastegui'])}):")
    for date, sc, owner in n["verastegui"]:
        out.append(f"  {date}  {sc}  owner @{owner}")
    out.append("")
    out.append(f"@laisjordy co-posts ({len(n['laisjordy'])}):")
    for date, sc in n["laisjordy"]:
        out.append(f"  {date}  {sc}")
    out.append("")
    out.append("co-posts by month: with @timballardfoundationecuador, and all others")
    for m, (e, o) in n["monthly"].items():
        out.append(f"  {m}  {e:>4d} with   {o:>4d} other   ({e + o:>4d} total)")
    out.append("")
    return "\n".join(out)


def check(n):
    want = json.load(open(NUMBERS))
    tests = [
        ("date span", n["span"], want["tb_span"]),
        ("post count", n["posts"], want["tb_posts"]),
        ("co-post count", n["coposts"], want["tb_coposts"]),
        ("top 12 partners",
         sorted((list(p) for p in n["top12"]), key=lambda p: (-p[1], p[0])),
         sorted((list(p) for p in want["tb_top"][:12]), key=lambda p: (-p[1], p[0]))),
        ("seven Brazilian politicians", n["br7"], want["br7_on_tb_grid"]),
        ("@eduardoverastegui co-posts", n["verastegui"], want["verastegui"]),
        ("@laisjordy co-posts", n["laisjordy"], want["laisjordy"]),
        ("co-posts by month", n["monthly"], want["monthly"]),
    ]
    bad = 0
    for label, got, exp in tests:
        ok = got == exp
        bad += not ok
        print(f"{'OK      ' if ok else 'DIFFERS '} {label}")
        if not ok:
            print(f"   computed: {got}")
            print(f"   numbers.json: {exp}")
    print(f"{len(tests) - bad}/{len(tests)} section-6 numbers match inputs/numbers.json")
    return 0 if bad == 0 else 1


def main():
    n = compute()
    print(show(n), end="")
    if "--check" in sys.argv:
        print()
        rc = check(n)
        print("CHECK PASS" if rc == 0 else "CHECK FAILED")
        return rc
    return 0


if __name__ == "__main__":
    sys.exit(main())
