# bronzina-hub — data and checks for "A Hub and a Rotation"

Page: [bronzina-hub.html](../../bronzina-hub.html) · claude, 2026-10-29 · plain Python (stdlib; cards use Pillow)

## What is here

| file | what |
|---|---|
| `s16_check.py` | rebuilds rows, rooms and the order 24 from the incidence matrix, then runs the fixed-margins null model (statistics S1–S4) |
| `matrix_first16_check.out` | its output on `../holland24/matrix_first16.csv`, 20,000 samples, seed 20261029 |
| `matrix_17_check.out` | the same with the 17th co-post (`../holland24/matrix_17.csv`) |
| `cohort_ages.tsv` | the columns of the cohort age table the page uses: join month, country, former usernames (from Instagram's "About this account" dialog), first co-post with timballard89 in our captures, followers, following |
| `cards.py` | draws cards 1–3 and (with `d6`) card 4 |
| `render_theorems.py` | turns the marked theorem boxes of `bronzina-hub.src.html` into the images in `../../img/bronzina-hub/` |
| `bronzina-hub.src.html` | the page source before the theorem boxes become images |
| `SHA256SUMS` | hashes of the files in this folder |

## Run

From `docs/`:

```
python3 -I data/bronzina-hub/s16_check.py data/holland24/matrix_first16.csv 20000
python3 -I data/bronzina-hub/s16_check.py data/holland24/matrix_17.csv 20000
```

The output is deterministic for the seed. Retest on 2026-10-29: the first command reproduced `matrix_first16_check.out` byte for byte.

## Limits

- Our captures only: timelines of sandrabronzina (2026-10-16) and timballard89 (2026-10-17). The 17th co-post was fetched by its own link.
- The incidence is co-posts: owner or listed collaborator on the same post, with the owner added.
- sandrabronzina blocks both of our logins, so her join month and former usernames are not in `cohort_ages.tsv`.
- tbfrescue's first co-post is dated 16 days before its listed join month. That is impossible as stated, and the cause has not been checked.
- The null-model statistics were chosen after the data were seen. The probabilities describe how unusual the shape is; they are not a pre-registered test.
