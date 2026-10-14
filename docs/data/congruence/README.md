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
