# PLAN: set 1 (TB IG, Oct 10 19:00 -> Oct 11 20:50, 8 posts) is a Holland object
claude, 2026-10-21. Light: grep + one plain-Python verifier we already have. No Opie, no Sage, no OCR, no web.

## Object (plain words — John approves before C2)
- POSTS (the chain): the 8 posts of set 1 in posting order -> set1/posts.txt.
- POINTS: the things the story speaks of -> set1/points.txt (label + regex). Seed is mine; John edits it.
- INCIDENCE: point p is in post j iff p's regex hits post j's transcript (Whisper SRT, verbatim, uncorrected).
- Aut(N): every relabelling of the points that carries the set of posts onto itself (multiset view) —
  computed by backfire-tracking's own verify_automorphisms.py, unchanged (the "Who went first" verifier, 7 posts there).
- HOLLAND VIEW (order kept): the posts stay in time order, so the only symmetries left swap points whose rows
  are identical across the 8 posts (row-equal classes). The class table is the Holland object's shape.
- PASS (John approves wording): [to fill with John — the exact Holland condition from
  2026-10-18/claude/formal_paper/rigid-grid-owner-section.html §§0-4, and which coset "the whole coset" is].

## Commands (bottom of today's morning list; copy from there)
C1 John edits points.txt -> C2 matrix -> C3 Aut (multiset) -> C4 Holland row classes -> C5 hashes.
Re-run C2-C5 after any edit to points.txt; every run keeps a dated copy.

## Then
Write up by hand (statement, tables, proof) from C3/C4 output. Pages first; FB/X cards later (plain, then sticker).
Catherine at position 4 in both sets is already on record (2026-10-21_catherine_grep.md).
