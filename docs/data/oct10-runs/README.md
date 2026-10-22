# Oct 10 runs: Aut of Tim Ballard's Instagram posts (2026-10-21) — runs, not verdicts

Two runs on @timballard89's own Instagram posts. Points = 9 regexes (`points.txt`), matched against each post's
Whisper transcript (verbatim, uncorrected). A post contains a point iff the regex hits. Aut = every relabelling of the
points that carries the posts (as a multiset) onto itself. Three independent checks per run:
V1 `../who-went-first/verify_automorphisms.py`, V2 brute force over all 9! relabellings, V3 Sage `IncidenceStructure`.
Every command is in the run's files; hashes in each `SHA256SUMS`.

## theset_run1/ — THE SET: the 8 posts of Oct 10 (chosen by time gaps only, `2026-10-21_THE_SET.md`)
|Aut| = 12 (S3 x C2). Orbits {Catherine, Backfire, forgive}, {God, children}; Utah, Israel, war, Isaiah fixed.
Coverage: 3 of 8 posts hit no point (one is a photo post, no transcript); Isaiah hits no post.

## set1_superseded/ — earlier run: 8 posts Oct 10 19:00 -> Oct 11 20:50 (transcript + caption)
|Aut| = 2: the one swap Catherine <-> forgive. Superseded by THE SET; kept as history.

## The crash (Sage)
Sage's `IncidenceStructure(...).automorphism_group()` aborts the whole process
(`std::out_of_range: out of bounds vertex number`, from bliss) when the structure has an empty block,
and again when it has a point in no block. Recorded in `set1_superseded/aut_v3_182414.out` and
`theset_run1/aut_v3_183049.out`. Workaround used: drop empty blocks and isolated points first (here each is
alone of its kind, so the group is unchanged); with that, Sage agrees with V1 and V2 in both runs.
