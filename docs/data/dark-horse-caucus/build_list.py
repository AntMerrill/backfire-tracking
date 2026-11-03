#!/usr/bin/env python3
"""Rebuild the Dark Horse Caucus list (the contributors) from posts.csv. Python 3, standard library only.

    python3 build_list.py           # writes contributors.txt and contributors.csv next to this file
    python3 build_list.py --check   # rebuilds in memory and compares with the files here; exit 1 if they differ

Rule (the whole method):
  1. posts.csv = the 22 Instagram posts dated 2025-05-01..2025-06-30 (UTC) on which timballard89 is the owner or a
     listed collaborator together with at least one other account. One row per post, in posting order (B1..B22).
  2. The accounts on a post = its owner + its listed collaborators (the names in the post header, not caption tags).
  3. Contributors = every account on any of the 22 posts except timballard89 (who is on all 22).
  4. Order = the first post an account appears on (B1 first); accounts on the same post in alphabetical order.
"""
import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CENTRE = "timballard89"


def build():
    posts = list(csv.DictReader(open(HERE / "posts.csv", newline="")))
    first, n_posts, n_owned = {}, {}, {}
    for k, p in enumerate(posts):
        accounts = {p["owner"]} | set(p["collaborators"].split())
        n_owned[p["owner"]] = n_owned.get(p["owner"], 0) + 1
        for a in sorted(accounts):
            if a == CENTRE:
                continue
            n_posts[a] = n_posts.get(a, 0) + 1
            first.setdefault(a, k)
    order = sorted(first, key=lambda a: (first[a], a))
    txt = ["# Dark Horse Caucus on Insta: accounts co-posting with timballard89, May-June 2025 (22 posts)",
           "# order = first post they appear on (then alphabetical); timballard89 (on all 22) left out",
           "# built by build_list.py from posts.csv"]
    txt += ["@" + a for a in order]
    rows = [["n", "handle", "first_post", "first_posted_utc", "posts", "owns"]]
    for i, a in enumerate(order, 1):
        p = posts[first[a]]
        rows.append([str(i), a, p["post"], p["posted_utc"], str(n_posts[a]), str(n_owned.get(a, 0))])
    return "\n".join(txt) + "\n", rows


def main():
    txt, rows = build()
    if "--check" in sys.argv:
        same_txt = (HERE / "contributors.txt").read_text() == txt
        same_csv = list(csv.reader(open(HERE / "contributors.csv", newline=""))) == rows
        print(f"contributors.txt {'OK' if same_txt else 'DIFFERS'}; contributors.csv {'OK' if same_csv else 'DIFFERS'};"
              f" {len(rows) - 1} contributors")
        sys.exit(0 if same_txt and same_csv else 1)
    (HERE / "contributors.txt").write_text(txt)
    with open(HERE / "contributors.csv", "w", newline="") as fh:
        csv.writer(fh, lineterminator="\n").writerows(rows)
    print(f"wrote contributors.txt and contributors.csv: {len(rows) - 1} contributors")


if __name__ == "__main__":
    main()
