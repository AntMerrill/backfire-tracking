# Ballard and the Bolsonaro accounts: where they meet (data)

Page: [ballard-bolsonaro.html](../../ballard-bolsonaro.html). Oct 28, 2026.

## Files
- `posts.csv`: every post in either set, one row per post (4,363): shortcode, date (UTC), owner, collaborators, credits.
  Lists are `;`-separated. `credits` = accounts @-tagged in the caption. 25 posts have no owner in our capture:
  `(not recorded)`. No captions or images are kept.
- `graph_edges.csv`: the links drawn in `graph.svg` (40 co-post, 89 credit) with the posts behind each.
  `co-post` = both accounts owner or collaborator on the post; `credit` = one is owner or collaborator, the other is in
  its credits.
- `graph.svg`: the graph on the page.
- `check.py`: plain Python 3. Recomputes every number on the page from `posts.csv`: `python3 check.py`.
- `SHA256SUMS`: `sha256sum -c SHA256SUMS`.

## Definitions
- **B (Ballard)**: timballard89, tbfrescue or timballardfoundationecuador is owner, collaborator or credited.
- **Z (Bolsonaro / Frias)**: an account with `bolsonaro` in its name is owner, collaborator or credited, or
  mariofriasoficial is owner or collaborator.
- **Accounts on both sides** (the B and Z accounts themselves left out): tier 1 owner/collaborator on both sides;
  tier 2 owner/collaborator on one side, credited on the other; tier 3 credited on both. Tiers overlap.

## How it was made, and limits
Read from 101 Instagram profile-timeline captures made Oct 7-28, 2026 (metadata only), built around Ballard's, Frias's
and related accounts' grids. It is what those grids hold, not a sample of Instagram. Where a post was captured more
than once, its records were pooled. Counted by Opie (opencode), recounted with separate code by claude (Claude Code).
A shared post or a credit says two accounts appear on one post; nothing about who runs them or why.
