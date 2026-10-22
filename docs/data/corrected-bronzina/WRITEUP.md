# Sandra ↔ Boner, corrected: the bronzina co-post chain, and what the expofamily blind spot does to it

**In-house only.** Everything below is computed from captures already on disk
(`~/boner_vault/dl_wm_outputs/ig_timelines/`). Nothing was fetched, nothing is quoted
from the outside world, nothing gets posted. Working folder:
`~/Desktop/claude/2026-10-22/opencode/tb_object_expofamily/`.

This is the written-up version of O6 (`o6.py`, `REPORT.md`), putting the two loose
ends — **sandrabronzina** and **expofamily.cl** — into the same picture and asking
whether either of them is load-bearing for the Holland object.

## 1. The question

After the set-1 result, the TB material had two names that never resolved:

- **sandrabronzina** — 16 co-posts with TB, from 2025-11-04 to 2026-10-16. Big edge,
  but her *role* was never pinned down.
- **expofamily.cl** — public account (263 posts, 8,891 followers, verified live
  2026-10-22), but invisible to the headless scraper: header renders, timeline never
  does, `collabnet` returns 0. See `~/Desktop/claude/2026-10-22/opencode/insta_blindspot.md`.

Both sit at the edge of the TB co-poster object, so both could in principle change it.
The test: build the object from disk, compute |Aut|, then re-compute with expofamily's
own blocks hidden and with expofamily dropped as a point.

## 2. The object, as computed

Points = owner ∪ collaborators per captured post. Blocks = posts with ≥ 2 points.
Holland rows = the set of blocks a point sits in. Twin = identical row. |Aut| = product
of factorial(twin class size). Script `o6.py` sha256
`ab7aa923907fb45a7ace4e4f6999ce9e06fee3364afcafe53262949a65c7123d`; log `run.log`
sha256 `841260c3b97c6fa23034ad07ae2cb4148212214830e8444fd22554aea5918b18`.

| variant | blocks | points | sandra posts | expofamily posts | \|Aut\| |
|---|---|---|---|---|---|
| base (TB grid, all captured) | 1004 | 424 | 16 | 11 | 2.00 × 10³⁴ |
| no_ef_blocks (hide expofamily's own blocks) | 997 | 418 | 11 | 4 | 6.00 × 10³⁴ |
| no_ef_point (drop expofamily as a point) | 1004 | 423 | 16 | — | 2.00 × 10³⁴ |
| TB grid ∪ sandra's own grid | 1347 | 631 | 249 | 26 | 1.68 × 10⁴¹ |

## 3. What the numbers say

1. **expofamily is never a twin.** Class size 1 in all four variants — 11, 4, 26 posts
   as different captures join. Its row is unique, so it cannot be swapped with anyone.
2. **sandra is never a twin.** Class size 1 throughout — 16 posts on TB's grid, 249 once
   her own complete grid is unioned in. Her edge is large but unique.
3. **Hiding expofamily's blocks makes the object *more* symmetric** (2.00e34 → 6.00e34).
   Removing a *distinct* point destroys twin structure its unique rows were holding
   apart, so the surviving accounts fall into more equal pairs. This is the general
   rule, demonstrated: **missing blocks manufacture symmetry.** Every grid-incomplete
   account in a Holland object biases that object toward a *higher* |Aut| than the truth.
4. **Dropping expofamily as a point changes |Aut| by exactly 0.** Because its row is
   unique, its presence constrains nothing. The loose end never touched the group order.
5. **What the blind spot actually costs is row quality, not the answer.** With its
   TB-grid blocks counted, sandra has 16 rows; blind, 11. The 263 unreadable posts are
   the only thing that could refine further — and refinement can only *lower* |Aut|.

## 4. The corrected bronzina chain

The 16 co-posts (from `tb_bronzina/joint_posts.tsv`, deduped by shortcode) are not 16
mysteries. Reading down the owner column:

| # | date (UTC) | shortcode | owner | owner side | sandra | TB |
|---|---|---|---|---|---|---|
| 1 | 2025-11-04 | DQncoDDkalv | sandrabronzina | sandra | owner | collab |
| 2 | 2025-11-21 | DRVhr48CbZu | liberal.noticias | third party | collab | collab |
| 3 | 2026-05-27 | DY2kqteiQqQ | maaydelara | third party | collab | collab |
| 4 | 2026-05-27 | DY2_vclhVd5 | sandrabronzina | sandra | owner | collab |
| 5 | 2026-05-29 | DY6Nuq0OU5z | sandrabronzina | sandra | owner | collab |
| 6 | 2026-05-29 | DY7LGsdIKg7 | sandrabronzina | sandra | owner | collab |
| 7 | 2026-05-29 | DY7wTMOoN5U | sandrabronzina | sandra | owner | collab |
| 8 | 2026-05-30 | DY8pKXqN1zq | timballard89 | **TB** | collab | owner |
| 9 | 2026-05-30 | DY9-SxElLGl | larinoar | third party | collab | collab |
| 10 | 2026-06-02 | DZFy1F3h0uh | sandrabronzina | sandra | owner | collab |
| 11 | 2026-08-08 | Dby-pWRzbyU | expofamily.cl | third party | collab | collab |
| 12 | 2026-08-19 | DcPIUYrTUF8 | expofamily.cl | third party | collab | collab |
| 13 | 2026-08-27 | DcjB396IGFD | expofamily.cl | third party | collab | collab |
| 14 | 2026-09-15 | DdUuBCCT0-d | expofamily.cl | third party | collab | collab |
| 15 | 2026-10-05 | DeHiaurTAQI | expofamily.cl | third party | collab | collab |
| 16 | 2026-10-16 | DeifzUMOxmD | ivetteavaria | third party | collab | collab |

The shape: **2 pilot → 6-month pause → burst of 7 in 9 days → a monthly
expofamily-series of 5 → one ivetteavaria close.** TB owns exactly one of the 16
(#8). Sandra owns six. Five are owned by expofamily.cl (#11–15), all of them the
same event-circuit cast (`dramariajosemancino`, `margaritarojoc`, `qntlc`, and on
#13 the whole Chilean promoter list). The harness that introduced the rest:
`liberal.noticias`, `maaydelara`, `larinoar`, `ivetteavaria`.

So the loose end resolves cleanly: **sandra's edge to TB is half ordinary — six of
her own posts with TB as collaborator — and half mediated by a Chilean event
circuit, with expofamily.cl as the hub of the second half.** That is the whole
finding, and it changes nothing about the group.

## 5. The same thing, drawn

- `o6_network.png` — the 27-node neighbourhood around sandra and expofamily.
  Gold nodes = the two focus accounts; red nodes = accounts with an identical row
  (swappable); edge colour/width = number of shared posts. No red on either focus
  node: hidden in colour, that they are singletons. sha256
  `2163de63a77b22e87ec3cfaa490859de6032ae5a312b23d12ea707747eb7a670`.
- `o6_focus_chains.png` — the corrected bronzina chain: one row per co-post,
  owner colour-coded (sandra / TB / expofamily / other), with the collaborator
  column and the 2025 → 2026 gap visible as whitespace.
- Cards: `cards/` — one per finding, 1600×900 @ dpi 100, house render constants.

## 6. Limits

- Nothing outside our captures enters. A post no local capture saw cannot be a block.
- expofamily.cl's own 263 posts are unknown to us (blind spot, not privacy — it is
  public). If they lifted, they would only add blocks, and adding blocks can only
  refine rows, i.e. lower or hold |Aut|. They cannot raise it.
- The `credits` reading used in the chain table is the caption @-tag channel;
  house rule excludes credits from co-presence, so they are reported, not summed.
- All figures are from disk. No Chrome, no fetch, no enumeration.

— opencode, 2026-10-22
