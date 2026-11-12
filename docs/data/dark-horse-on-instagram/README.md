# Dark Horse on Instagram — how the section-6 numbers are made, and how to make them yourself

The article's section 6 ("After the two months") is about **one** account's grid: timballard89's. Every number in it
comes from our copy of the grid, saved Nov 6, 2026, and can be rebuilt from it with `after_two_months.py`.

## What each number means

| on the article | what it is | comes from |
|---|---|---|
| **Oct 1, 2025 – Nov 6, 2026** | first to last post date (UTC) on the held grid | `timballard89_2026-11-06_reverse_0853.jsonl` |
| **1,846 posts** | how many posts the held grid holds | the same file, one row per post |
| **865 co-posts** | posts whose header credits another account as well: owner is someone else, or timballard89 has named collaborators | the same file, `owner` and `collaborators` |
| **top 12 partners** | accounts credited beside timballard89 on those co-posts, ranked by how many co-posts they are on | the same file |
| **seven Brazilian politicians, all 0** | for each of @biakicis, @damaresalvesoficial, @generalgirao, @mariofriasoficial, @carlosjordy, @gusgayer and @jorgeseifjunior (the ones on the May–June 2025 co-posts), how many of the 865 co-posts put them beside timballard89 | the same file |
| **@eduardoverastegui appears 4 times** | every co-post with him: date, shortcode, owner | the same file |
| **@laisjordy appears 2 times** | every co-post with her: date, shortcode | the same file |
| **co-posts by month** | each UTC calendar month: co-posts with @timballardfoundationecuador, and all other co-posts | the same file |

A **co-post**, here as in the rest of the article, is an Instagram post whose header credits two or more accounts: the
owner plus the collaborators named beside the owner. Accounts @-tagged in a caption or a photo do not count.

`posts.csv` is the list of the **22** co-posts from May 1 – June 30, 2025 (B1–B22) — the two months the rest of the
article is about. Section 6 does not read it; it is here so the earlier sections can be followed too.

## The exact commands

```
python3 after_two_months.py           # prints every section-6 number
python3 after_two_months.py --check   # prints the same, then compares it with numbers.json; exit 1 on any mismatch
```

The expected values are in `numbers.json` (keys `tb_span`, `tb_posts`, `tb_coposts`, `tb_top`, `br7_on_tb_grid`,
`verastegui`, `laisjordy`, `monthly`). `--check` ends with `CHECK PASS` and exit 0 when all eight groups match.

## Checking it without our files

You don't need our files to check this. Open timballard89's Instagram grid and scroll back to **Oct 1, 2025**. From
there to the top of the grid, count the posts and open the ones whose header names more than one account. For each,
write down the shortcode, the date, the owner and the collaborators beside the owner's name. That is the same
information as `timballard89_2026-11-06_reverse_0853.jsonl`, one post per line. Two things to watch:

- **The span.** The grid starts at Oct 1, 2025, so the first post is the start of the span, not the start of the
  account. Posts before that date are not in these numbers.
- **Month ends.** Dates and months are UTC. A post made late in the day in the Americas can fall on the next UTC date.

## Limits

- **The held grid starts Oct 1, 2025.** Everything here is "as held on Nov 6, 2026"; posts deleted since, or posts
  older than Oct 1, 2025, are not in it.
- **July – September 2025 isn't held.** The grid picks up on Oct 1, 2025, so for those three months we can't say
  anything: not that there were no co-posts, only that we don't hold them.
- **Only his own grid is counted.** In other accounts' held timelines, Instagram served some of these same posts
  without timballard89 in the header (B1, B9 and B21 among them). Counting from those timelines would therefore
  undercount him, so every number above comes from timballard89's grid alone.
- **Only what Instagram shows as a co-post.** Partners tagged or thanked in a caption, or shown in a photo without a
  collaborator credit, are not counted.
- The numbers say who was credited beside timballard89 and when. They say nothing about what any account thinks,
  knows, or did off Instagram.

## Files

| file | what |
|---|---|
| `after_two_months.py` | the method as code; `--check` re-derives every section-6 number and compares with `numbers.json` |
| `numbers.json` | the expected section-6 numbers |
| `timballard89_2026-11-06_reverse_0853.jsonl` | our copy of the grid, saved Nov 6, 2026: one post per line (shortcode, `taken_at`, owner, collaborators) |
| `posts.csv` | the 22 co-posts of May 1 – Jun 30, 2025 (B1–B22), for the earlier sections |
| `after_two_months_output.txt` | the printed output of both commands on this copy |
| `SHA256SUMS` | hashes of the files above (`sha256sum -c SHA256SUMS`) |

`after_two_months.py` reads these files beside itself, or in an `inputs/` folder beside itself (as in our working
copy). The table uses the flat names, the way the files would sit in `docs/data/dark-horse-on-instagram/`.

Backfire Tracking, 2026-11-10.
