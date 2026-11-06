# Sixteen links, one block — data (bronzina-cut.html)

**What:** the 16 posts of Bronzina's coset (the first 16 timballard89 × sandrabronzina co-posts, as in
`../holland24/matrix_first16.csv`), checked on Tim Ballard's Instagram grid on 2026-10-16 and 2026-11-06.

**Files**
- `s16_status.csv` — one row per post: shortcode, date posted (UTC), owner, whether sandrabronzina is on it on Oct 16
  (owner or listed collaborator), whether the post is on timballard89's grid on Nov 6, whether she is on it on Nov 6,
  and the other accounts on it on Nov 6.
- `bronzina_cut_check.py` — plain Python 3. Rebuilds "two worlds, one vertex" from the published matrices
  (`../who-went-first/incidence_matrix.csv` + the host latterdayavenger on all 7; `../holland24/matrix_first16.csv`), then the
  Nov 6 version (core: B6 and B7 off, B1–B5 unchanged; coset: from `s16_status.csv`). Prints accounts, posts, lines,
  pieces, cut vertices. Output: `bronzina_cut_check_output.txt`.
- `bronzina_cut_card.py` → `bronzina_cut_card.svg` — the first card, from `s16_status.csv` (plain Python 3); the page inlines the SVG.
- `bronzina_posts_per_year.csv`, `bronzina_timeline.csv` — her posts per year (alone / with other accounts) and the dated steps on the
  history card, from her grid as captured on Oct 16, 2026 (3,202 posts). `bronzina_history_card.py` → `bronzina_history_card.svg`
  drew it (it reads that capture, which isn't published: raw scrapes stay with us).

**How made:** metadata-only captures of timballard89's grid (post codes, dates, owner, collaborators; no captions, no
media), read the same way on both dates; posts dated 2025-10-01 to 2026-10-16 compared. Owners on Oct 16 come from an
Oct 17 capture of the same grid. The core-side Nov 6 state comes from latterdayavenger's grid read the same way.

**Limits:** a live site serves a slightly different set each time. Instagram does not say who removed a post or a name,
and it hides a blocking account from the blocked viewer: from here a block and a removal can look alike. John reports
@sandrabronzina is active and blocks us. Smaller core accounts are letters (A–K) as on who-went-first.html.

Check: `sha256sum -c SHA256SUMS`.
