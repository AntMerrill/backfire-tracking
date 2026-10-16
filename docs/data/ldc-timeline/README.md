# Latter Day Chad's Instagram grid, oldest first (captured 2026-10-16)

`latterdaychad_timeline_2026-10-16.jsonl` — every post Instagram served on @latterdaychad's grid on October 16, 2026,
from the first post (2023-11-24) to 2026-10-15: 2,394 posts, one JSON object per line, oldest first.
The profile showed 2,506 posts on October 15; the rest did not come through (possibly posts kept off the grid; not checked).

| field | meaning |
|---|---|
| `shortcode` | the post: `https://www.instagram.com/p/<shortcode>/` |
| `taken_at` | the posted time Instagram lists (Unix seconds, UTC) |
| `id_time` | the creation time built into the post's id by Instagram's servers (Unix seconds, UTC) |
| `collaborators` | the accounts Instagram lists as collaborators (the posting account is usually left out) |
| `credits` | the accounts the caption names with @. **In this capture, read from the first 200 characters of the caption only**, so a handle at the cut can be clipped (e.g. `ld`, `latterd`). |
| `date_mismatch` | present (true) only when `taken_at` and `id_time` differ by more than an hour (6 posts) |

Metadata only: no captions, pictures or video are kept. Read with a logged-in browser that replayed Instagram's own
"next page of posts" request, twelve posts at a time, back to the first post.

Check the file: `sha256sum -c SHA256SUMS`. Page: [Latter Day Chad, from the first post](../../ldc-from-the-first-post.html).
