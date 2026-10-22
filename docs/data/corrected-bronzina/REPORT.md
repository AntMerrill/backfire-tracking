# O6 — TB co-poster incidence object: is expofamily.cl load-bearing?

On-disk only (`~/boner_vault/dl_wm_outputs/ig_timelines`), no enumeration, no new fetch.
Points = owner + collaborators per captured post. Blocks = posts with >=2 points (a solo post is no relation).
Holland rows = set of blocks a point sits in; identical rows are twins; |Aut| = product of factorial(twin class size).

Script `o6.py` sha256 `ab7aa923907fb45a7ace4e4f6999ce9e06fee3364afcafe53262949a65c7123d`
Log `run.log` sha256 `841260c3b97c6fa23034ad07ae2cb4148212214830e8444fd22554aea5918b18`

## Results

| variant | blocks | points | sandra posts | expofamily posts | |Aut| |
|---|---|---|---|---|---|
| base (TB grid, all captured) | 1004 | 424 | 16 | 11 | 2.00e34 |
| no_ef_blocks (hide expofamily's own blocks) | 997 | 418 | 11 | 4 | 6.00e34 |
| no_ef_point (drop expofamily as a point) | 1004 | 423 | 16 | — | 2.00e34 |
| TB grid ∪ sandra's own grid | 1347 | 631 | 249 | 26 | 1.68e41 |

## What it says

1. **expofamily is not a twin.** Class size 1 in every variant (posts 16 / 11 / 26 as sandra's and its own
   grids join, all distinct rows). It is not interchangeable with anyone, so it cannot inflate the group.
2. **sandra is not a twin either, and never was.** Class size 1 throughout, 16 posts on TB's grid, 249 with
   her own grid merged. Her edge is large but unique; whatever the 16 co-posts are, she is a distinct point.
3. **Hiding expofamily's blocks makes the object *more* symmetric, not less:** |Aut| 2.00e34 -> 6.00e34.
   Removing one distinct point collapses parts of the twin structure that its unique rows were separating.
   This is the general rule, now demonstrated: a grid-blind account in a Holland object *manufactures*
   symmetry. Coverage gaps bias objects toward higher |Aut|.
4. **Dropping expofamily as a point changes |Aut| by 0** (2.00e34 = 2.00e34) — because its row was unique,
   its presence constrains nothing. So the loose end was never load-bearing for the group order.
5. **What the blind spot actually costs is row quality, not the answer:** with its 11 TB-grid blocks in,
   sandra has 16; blind, 11. The one thing that could have moved it the other way — expofamily's own 263
   posts (26 more blocks visible to a session that renders grids) — cannot be read headless.

## Verdict

The sandra loose end resolves without touching the outside world: she and expofamily are both singleton
rows, the group order does not depend on either, and the expofamily blind spot only adds hidden blocks that
would refine rows (|Aut| can only fall) if it lifted. Consistent with "adding blocks refines rows, so
missing blocks manufacture symmetry". O1–O5 remain untouched; expofamily and sandra are points in none
of them.

— opencode, 2026-10-22
