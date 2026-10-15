# B7 — `DXQTcYlgZ5c` — post deleted

B7 is the seventh block of the seven-post set analysed in
[`automorphism-group.html`](../../../automorphism-group.html). Unlike B1–B6 it has
been **deleted from Instagram**, so it cannot be re-downloaded. This note is the
record of what we hold, what we lost, and what a reader can still check.

## The post, as captured

| | |
|---|---|
| Shortcode | `DXQTcYlgZ5c` |
| URL | https://www.instagram.com/p/DXQTcYlgZ5c/ |
| Posted | 2026-04-18T01:34:57Z |
| Uploader | `latterdayavenger` |
| Media | video, 16.366 s, 720×1280, 2 011 350 bytes |
| At capture | 105 likes, 4 comments |
| Credits (as published in `group_posts.csv`) | `latterdaychad`, `timballard89`, plus 3 one-time accounts |

It is the only post of the seven whose credits list **two** of the accounts that
appear on all seven — which is what makes `timballard89` and `latterdaychad`
interchangeable and gives the structure its order 12.

## Timeline

| Date | Event |
|---|---|
| 2026-04-18 | Posted. |
| 2026-10-01 – 05 | Captured in the profile sweep that produced `group_posts.csv` and `incidence_matrix.csv`. |
| 2026-10-05 07:58 and 09:18 | **Downloaded twice, successfully.** Full mp4 plus watermarked copy written. Logs: `B7_dllink_2026-10-05_*.log`. |
| between Oct 5 and Oct 11 | A storage failure destroyed the downloaded media (disclosed in the paper). |
| 2026-10-11 09:52 | Re-fetch **failed**: HTTP 400 from Instagram's video-info endpoint; carousel fallback found 0 slides; HTML fallback returned HTTP 200 with 0 image candidates; capture saved with `{"status": "no_post_model"}`. Log: `B7_dllink_2026-10-11_095218.log`. |
| 2026-10-13 | **Absent** from `latterdayavenger`'s own timeline capture (354 posts, reaching back to 2025-04-01), while its neighbours 2026-04-16 and 2026-04-20 are both present. The capture is not truncated at that date, so the post was already gone. |
| 2026-10-15 | Confirmed deleted. `GET` on the post URL returns **HTTP 200**, body 591 988 bytes, `<title>Instagram</title>`, and **no `og:` tags at all**. |

### Why "no `og:` tags" is the test

Instagram does not return 404 for a deleted post — it serves the same empty shell
it serves for anything else. A *live* post always populates the `og:title` and
`og:image` metadata that crawlers and link-unfurlers read. HTTP 200 with a bare
shell and no `og:` image means there is no post.

There is also **no Internet Archive snapshot**: the `archive.org` availability API
returns `archived_snapshots: {}` and the CDX index returns nothing for this URL.

## What is in this folder

| File | What it is |
|---|---|
| `B7_instagram__DXQTcYlgZ5c.raw.json.gz` | The raw extractor record from 2026-10-05: uploader, timestamp, duration, formats and 11 thumbnail URLs. 3 654 bytes. |
| `B7_instagram__DXQTcYlgZ5c.metadata.json` | The pipeline's metadata record for the same capture. |
| `B7_dllink_2026-10-05_073832.log` | First successful download, 2026-10-05. |
| `B7_dllink_2026-10-05_091800.log` | Second successful download, 2026-10-05. |
| `B7_dllink_2026-10-11_095218.log` | The failed re-fetch. |
| `B7_DELETED.md` | This note. |

Hashes are in `SHA256SUMS` and `manifest.csv`.

### Redaction

The logs and the metadata record are published as held, with one change: local
filesystem paths (`/home/…`) have been replaced with `~`, and the name of the
browser-cookie file used for the downloads with a generic `instagram.cookies.txt`.
Nothing else was altered — every timestamp, task name, error and the two successful
download records are intact. The raw extractor record is unmodified. `SHA256SUMS`
and `manifest.csv` hash the published (redacted) copies.

### Durable identifiers

The media bytes are gone, but the raw record pins the asset:

- CDN asset key: `670212956_1490923949338077_2825788258852863422`
  (thumbnail path `/v/t51.71878-15/670212956_1490923949338077_2825788258852863422_n.jpg`)
- `ig_cache_key`: `Mzg3NzY4NDc5MjU5NDExMjA5MjE3OTI2MjUwOTk0MjY3NjU5`
  (base64 for `387768479259411209217926250994267659`)

The signed CDN URLs inside the raw record have expired — they return **403** as of
2026-10-15 — so the file cannot be re-fetched from them. We searched by media key,
exact byte count and filename across every capture tree on the machine: no copy of
the media survives anywhere.

## What a reader can still verify

1. **B1–B6 are unchanged** and can be opened and re-collected as described in
   [`TEST.md`](../TEST.md).
2. **B7's effect on the structure can be reproduced without B7's media.** Delete the
   B7 column from `incidence_matrix.csv` and re-run `verify_automorphisms.py`. The
   answer is **|Aut| = 24**, not 12, and a new interchangeable pair appears among the
   one-time accounts. So B7's row is load-bearing: it is not a column that could
   quietly be invented, because removing it visibly changes the result.
3. **B7's own record** is the five files above, hashed and dated.

## Honest limitation

The raw record is an extractor dump — it does **not** contain the collaborators
list. B7's credits therefore rest on the 2026-10-01 – 05 profile capture that
produced `group_posts.csv`, and that particular response was not retained. B7's row
in the incidence matrix is single-sourced. We record that here rather than leave it
to be found by someone else.
