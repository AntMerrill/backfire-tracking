# Pluto's Mr. Right: the Imagination Podcast thumbnails (captured 2026-10-17)

The YouTube channel @imaginationpodcastofficial (The Imagination Podcast, host Emma Katherine), Videos tab, scrolled
from the newest upload down to Season 1 and screenshotted on October 17, 2026.

| file | what it is |
|---|---|
| `screenshots/f01..f17.png` | the video grid of each screenshot: an exact-pixel cut of the original (box in `grid_cut.json`), nothing altered. The browser's sidebar is left out. The full originals are kept offline; their sha256 is in `screenshots/ORIGINALS.tsv`. |
| `boxes.tsv` | every box, in screenshot pixels: `whole` thumbnail (found by opencode), `guest` and `host` photo panels, the season/episode `badge` and `title` code (claude) |
| `crops/` | the exact pixels inside each guest/host box, cut from `screenshots/`, PNG; `crops/MANIFEST.tsv` lists box, who (riggs / emma) and sha256. Six boxes reach outside the published cut and are left out (`crops/LEFT_OUT.txt`). |
| `fingerprints_vs_S6E89.tsv` | dHash distance of each Riggs/Emma crop to the S6E89 crop, fixed boxes |
| `fingerprints_aligned_wide_vs_S6E89.tsv` | the same with a small alignment search (the boxes cut the photos at different offsets) |
| `episode_order_by_eye.tsv` | each video's season/episode code and YouTube's age label, in Videos-tab order, read by eye from the screenshots |
| `replicate.py` | re-cuts every crop and checks its sha256, recomputes both fingerprint tables, prints REPLICATED or not |
| `cards/` | the cards on the page (stamped = with the WATCH BUTTFIRE sticker) |
| `2026-10-17_pluto_mr_right_boxes.mp4` | the boxes over the grid, frame by frame, ending on the season card |

Fingerprint: dHash, 64 bits (9x8 grayscale, LANCZOS); same image = distance 0-5. Pairs known to differ score 9 or more.

Replicate: `pip install pillow numpy`, then `python replicate.py` (about a minute). Check the files: `sha256sum -c SHA256SUMS`.
Page: [The early provenance of Pluto's Mr. Right](../../pluto-mr-right.html).
