# DH22 deep pass, 2026-11-25 — data, method, and how to check it

This folder holds the data behind `../../dh22-deep-2026-11-25.html`. Everything
here comes from the verified haul and the 2026-11-25 deep pass; nothing is typed
by hand. Run `python3 check.py` to rebuild the two headline results from the
files in this folder (standard library only).

## The set, named first

**DH22** is the set of **22 co-posts of `timballard89` posted 2025-05-01 ..
2025-06-30 UTC, and the 28 accounts on them** (`timballard89` is on all 22; the
other 27 are the rest). It is **not** S16 / holland24 and **not** the rigid grid.
Numbers from different sets are not carried between them.

| set | what it is | size |
|---|---|---|
| DH22 member set | participants of the 22 defining co-posts | 28 accounts, 22 posts |
| DH22 clean 28-set capture | archive timelines, one per seed (captured 11-18/19) | 27 files / 27 accounts |
| DH22 haul holland-60 | dated captures incl. deep re-scrapes | 60 files / 42 capture accounts |
| DH22 network object (union) | every account in any captured block, deduped by shortcode | 2,904 accounts x 98,432 posts |

## Headline results

1. **Canonical DH22 object:** 28 accounts x 22 posts, `|Aut| = 768 = 4!·2!⁵`
   (one 4-class + five 2-classes). The 4-class is
   `dignidadyderecho`, `emilia_maldonadojaramillo`, `pabloaproano`,
   `timballardfoundationecuador`. The five pairs are
   `47contadoallan/_revistatimeline`, `americatv/rolando_gps`,
   `biakicis/mareannl`, `gusgayer/jorgeseifjunior`,
   `herzog_foundation/momsforamerica`.
2. **Validation:** the same reused construction reproduces the known answer
   exactly: `sandrabronzina` **282 x 766, |Aut| = 150,994,944**, trio included.
3. **Network (union view):** **2,904 accounts x 98,432 posts, |Aut| ≈ 1.80e103**.
   The 11-20 `holland_keep` baseline **2,898 x 98,420 ≈ 2.99e102** is reproduced;
   the clean 28-set archive view is **1,592 x 27,277 ≈ 7.9958e67**.
4. **Long tail, not one rigid object:** largest class 4; 239 non-trivial classes
   = 186 pairs + 43 triples + 10 quads.
5. **Best twin:** `defeatleftism / jdvance4usa` — 16 co-posts, survives the
   merge. Capture-local: `38contadoallan / allanconta_35` — 24 co-posts in
   `maxcardosobr_2026-11-19`, does not survive.

## How it is made

- **Points** are accounts. **A block** is the set of accounts Instagram credits
  on one post: the owner plus the listed collaborators in the post header.
  Caption @-tags and picture credits do not count.
- **Dedupe** by shortcode, keeping the earliest `taken_at` (the house keep rule).
- **Classes:** two accounts are in the same class when they appear on exactly the
  same set of posts (identical membership rows). Accounts in one class are
  interchangeable.
- **|Aut|** is the product of `(class size)!` over the classes. This is the
  house *time-order* group: blocks stay ordered by time, so only account classes
  contribute. It is the same rule as the 2026-10-20 pass (`scan.py` /
  `jsonl_to_matrix.py`), whose known answers this pass reproduces.
- For the canonical object the blocks are the 22 defining posts; for the network
  object the blocks are every captured post (deduped/merged by shortcode).

## Limits

- **Snapshot to 2026-11-19, not a census.** Coverage is egocentric (60 + 27
  captured grids; block sizes 1-6), not a population sample.
- **One defining post is not in any capture:** `DKYTBMSuTjl` (2025-06-02,
  `cristianosenpolitica`). 21 of 22 are captured.
- **Two captured defining posts are incomplete:** `DKSZ5T6iU3E` misses
  `americatv`; `DLfpqobvgiT` misses `4ludlins`.
- **Owner injection:** the archive timelines carry no `owner` field, so the
  capture account is supplied as the owner (the holland-input convention). This
  is an assumption, documented, not a recorded field; it is required for the
  archive view.
- **Co-posting is all this shows.** It does not establish intent, and says
  nothing about what an account thinks or does off Instagram.
- The canonical 768 is a definition-level, structural result (who is named on
  which of the 22 posts), not a discovery about the wider network.

## Files

| file | what |
|---|---|
| `canonical_object.tsv` | the 28 canonical accounts: class size, class row (which of the 22 posts), posts participated, how many it owns |
| `canonical_posts.tsv` | the 22 defining posts: date, shortcode, owner, canonical accounts, and whether/how the post appears in the haul |
| `known_answer_object.tsv` | compact account-by-block membership of the sandrabronzina known-answer object (282 accounts x 766 blocks), so `check.py` is self-contained |
| `repeats.tsv` | repeated-twin table (per-capture and combined views) |
| `summary.json` | the deep-pass summary the page quotes |
| `check.py` | standard-library check: rebuilds the canonical 768 and the known answer |
| `SHA256SUMS` | hashes of the files here (`sha256sum -c SHA256SUMS`) |

The full deep pass (report, all objects, per-capture scan, source script) is the
2026-11-25 handoff `dh22_deep_out/`; this folder is the self-contained subset the
page needs.

Backfire Tracking, 2026-11-25. Data derived from captures dated 2013-01-02 ..
2026-11-19; canonical posts 2025-05-05 .. 2025-06-30 UTC.
