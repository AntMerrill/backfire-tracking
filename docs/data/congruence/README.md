# Data: "Two names, one grid"

The data behind https://antmerrill.github.io/backfire-tracking/congruence.html (October 13, 2026).

Named: latterdayavenger (LDA, the host), latterdaychad (LDC), timballard89 (TB). Every other account is a label s001-s110, numbered
in order of first appearance on LDA's grid. These labels are this page's own (not the A-K of "Who went first"). The key from labels
to accounts, the raw captures and the captions are not published.

| File | What it is |
|---|---|
| `posts_with_dates.csv` | All 354 posts on LDA's grid, Apr 1, 2025 - Oct 13, 2026: link, time (UTC), who was credited |
| `posts.csv` | The same, in the two-column form `build_matrix.py` reads |
| `incidence_matrix.csv` | 113 accounts x 354 posts, 1 = credited. Built by `build_matrix.py` from `posts.csv` |
| `verify_automorphisms.py`, `verify_output.txt` | Lists every symmetry of the matrix (full search). Output: |Aut(N)| = 16, 4 swapping pairs |
| `refine.py`, `refine_output.txt` | A second, independent check (colour refinement). Same 109 orbits, same 4 pairs |
| `ldc_on_lda_grid_by_month.csv` | LDA's posts per month, and how many credit LDC |
| `ldc_posts_crediting_lda.csv` | Every post in LDC's own capture (Apr 29 - Oct 7, 2026) that credits LDA, and whether it is on LDA's grid |
| `build_matrix.py` | Same file as in data/who-went-first, unchanged |

## How it was made
- LDA's grid: our collabnet capture of latterdayavenger, Oct 13, 2026, complete (354 posts). A post's accounts = its Collaborators
  list, plus LDA on every post (it is LDA's grid; Instagram lists the host in only 26 of the 354 lists).
- LDC's posts: our capture of latterdaychad, Oct 7, 2026 (240 posts, Apr 29 - Oct 7, 2026).
- Left out: one post (DX2QReKGCI5, May 2, 2026) that credits LDA in LDC's capture but is not on LDA's grid.

## Limits
- This is LDA's view. Credits are not two-way: a post can credit an account and still not be on that account's grid.
  2 posts by LDC after Jun 11, 2026 credit LDA and are not on LDA's grid (in `ldc_posts_crediting_lda.csv`).
- A symmetry here is a relabelling of accounts that keeps every post's set of accounts. It says nothing about who runs an account.

## Check it
```
python3 build_matrix.py posts.csv            # writes my_incidence_matrix.csv; compare with incidence_matrix.csv
python3 verify_automorphisms.py incidence_matrix.csv
python3 refine.py incidence_matrix.csv
```
Swapping pairs (identical rows; the only points a symmetry moves): τ1 = s038 ↔ s039; τ2 = s044 ↔ s046; τ3 = s048 ↔ s049; τ4 = s103 ↔ s104.

**Scaling.** `verify_automorphisms.py` is an exact *full enumeration*: it builds every relabelling
σ one account at a time, so its cost tracks the number of interchangeable accounts, not just the
matrix size. That is fine here (this matrix is 113 accounts and the search finishes in under a
second) and at the 13-account "Who went first" size. It does **not** scale. Run on a 282-account
matrix it **timed out after 900 s with no output** (152 of those accounts sit on a single post, and
every such leaf is freely swappable, which multiplies the search). For any matrix much bigger or
looser than this one, use a symmetry library instead (Sage/GAP or nauty) by handing it the
account–post incidence and asking for the group:

```
# Save as e.g. aut.sage and run:  sage aut.sage      (SageMath, free: https://www.sagemath.org)
import csv
rows = list(csv.reader(open("incidence_matrix.csv")))
posts = rows[0][1:]
blocks = [sorted(r[0] for r in rows[1:] if r[1+j] == "1") for j in range(len(posts))]
G = IncidenceStructure(blocks).automorphism_group()   # nauty under the hood
G.order(), G.orbits()
```

On `incidence_matrix.csv` this prints **16**, orbits `['s038','s039'] ['s044','s046']
['s048','s049'] ['s103','s104']`, the same answer the enumerator gives here. Use the `sage`
launcher (a bare `python` import can fail if GAP is not on the path). The two methods agree wherever
the enumerator can finish; for larger structures, only the library route does.
