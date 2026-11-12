# MANIFEST — `docs/data/dark-horse-on-instagram/`

The text files a Pages data folder for "The Dark Horse Collaboration on Instagram" would hold. All files sit flat in
that folder. Sizes are bytes. **Text only: no media.** The article's images live elsewhere in the site (as files of
their own), not in this data folder.

| file | bytes | size | what |
|---|---:|---|---|
| `README.md` | 5088 | 5.0 KiB | how each section-6 number is made, the commands, how to check it, limits |
| `after_two_months.py` | 6096 | 6.0 KiB | the method as code; `--check` compares with `numbers.json` |
| `numbers.json` | 2295 | 2.2 KiB | the expected section-6 numbers |
| `posts.csv` | 2582 | 2.5 KiB | the 22 May–June 2025 co-posts (B1–B22) for the earlier sections |
| `timballard89_2026-11-06_reverse_0853.jsonl` | 291111 | 284.3 KiB | our copy of the grid, saved Nov 6, 2026: one post per line |
| `after_two_months_output.txt` | 4911 | 4.8 KiB | the printed output of both commands on this copy |
| `SHA256SUMS` | 000619 | 0.6 KiB | hashes of the files above; `sha256sum -c SHA256SUMS` |
| `MANIFEST.md` | 001772 | 1.7 KiB | this list |

**Size flag:** nothing is near 5 MB. The largest file is the grid copy at **291,111 bytes (284.3 KiB)**; the whole
folder is under 0.35 MB. No file needs special handling for a host limit.

**Not in this folder, by design:** the article pages (`*.html`), their CSS and images, and our private builder
`build_article.py` (it reads paths outside the folder). A readers' copy needs only the files above.

**Hash names:** in this working copy the three files that also exist under `inputs/` are hashed as `inputs/…`;
shipped flat, `sha256sum -c SHA256SUMS` then needs those prefixes removed from `SHA256SUMS`.

Backfire Tracking, 2026-11-10.
