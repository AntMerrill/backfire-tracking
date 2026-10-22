# Run 1 on THE SET (10-10, 8 posts) — claude, 2026-10-21 18:30. A run, not a verdict.
Set: tb_breaks/2026-10-21_THE_SET.md (John 15:29). Points: tb_oct10_14/set1/points.txt copied unchanged (the regex seed).
Incidence: point in post iff its regex hits the post's Whisper SRT (transcript only; no captions; same C2 command as set1).
Coverage: DeVR5nLBTsB is a photo post (no SRT) -> empty column. DeUWZAaxQDT, DeUbBdGxi3O hit none of the 9 points -> empty.
Isaiah hits no post -> isolated point.

Result (three ways agree): |Aut| = 12 (S3 x C2).
  orbits {Catherine, Backfire, forgive}, {God, children}; Utah, Israel, war, Isaiah fixed.
  V1 verify_automorphisms.py, V2 brute force 9!, V3 computed in Sage (run by claude at John's ask).
Sage note: IncidenceStructure -> bliss aborts ("out of bounds vertex number") on empty blocks and on isolated points.
  aut_v3_183049.out = that crash, kept. aut_v3_183109.out drops the 3 empty blocks + Isaiah first (each is alone of its kind, so the group is unchanged).
Row-equal classes (order kept): only {Catherine, Backfire, forgive} (all three only in DeV2P_UIf8b).
Compare set1/ (Oct 10-11 run, superseded): |Aut| = 2, swap Catherine<->forgive.
Hashes: SHA256SUMS.
