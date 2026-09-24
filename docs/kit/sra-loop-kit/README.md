# The SRA Loop — publishing kit

Two reader's-guide pages for Latter-day Saints about how a story of an
excommunicated stake president, and the satanic-ritual-abuse (SRA) claims
around it, circulated between Tim Ballard, Jason Preston, Latter Day Chad and
Justin Riggs in September 2026.

- **The SRA Loop** — the five-day life of one story.
- **Fellow Travelers** (Part 2) — the wider circle, starting with Justin
  Riggs on X.

Live copies: https://antmerrill.github.io/backfire-tracking/

## What's in here

| Folder | Use it if you want to… |
|---|---|
| `site/` | **Host it as-is.** Upload the folder anywhere that serves plain files (any web host, S3, Netlify, a WordPress media folder). Each page is a single self-contained HTML file with its images built in. |
| `template/` | **Host it under your own name / URL, or edit it.** Same pages with the images as separate files in `img/`. Run `python3 build.py https://your.site/path/` to fill in your URL for the social-media preview cards, then upload `out/`. Edit the HTML directly for wording. |
| `cards/` | **Promote it.** 1080×1350 and 1600×900 images sized for X/Facebook posts. |
| `sources/` | **Check it.** `SOURCES.md` lists every video, post and timestamp quoted; `kevin_anthology.md` has every "Kevin" line. |

## Embedding in an existing article

- WordPress / most CMSs: upload `site/sra-loop.html` and link to it, or
  paste the contents of `<main>…</main>` from `template/sra-loop.html` into a
  Custom HTML block (and upload `template/img/` alongside).
- The pages use Google Fonts (Literata, IBM Plex Sans Condensed) and fall
  back to system fonts if those are blocked. No JavaScript, no trackers.

## Ground rules the pages follow

- Every quote is the speaker's own public words, attributed, with a source.
- Claims are labeled **Documented / Claimed / Unclear**.
- Private individuals who are accused of things by these speakers are not
  named.
- The tone is aimed at members of the Church: it doesn't mock anyone's faith.

If you change the text, please keep those rules and the Sources section.

## Reuse

Free to host, republish and adapt, with credit and a link back to
https://github.com/AntMerrill/backfire-tracking.
