# Manual corrections to the Whisper master SRT

Log of hand-verified fixes to `youtube__pBo_2DYxfrY_master_stitched_patched.srt`,
found via direct listen against a flagged low-confidence/non-dictionary word.
Format: timestamp, what Whisper had, what's actually said, how it was confirmed.

## 00:52:43 — "Dagan" → "Dick Andersen"

- **Master transcript had:** "...the lie from the tabloid magazine from Dagan and the state president wouldn't even let me address it..."
- **Isolated scene-clip re-transcription (clip_361) had:** "...magazine from Dijk Anderson but this state present..."
- **Confirmed by direct listen (John, 2026-09-11):** he says **"Dick Andersen."**
- Note: this is a different name from **Doug Anderson**, already tracked in
  `backfire_excommunication_blame_index.md` as the person Ballard blames most
  (~31 mentions). Not yet checked whether these are meant to be the same
  person under two different renderings or genuinely two different people —
  flagged here, not resolved.

## 01:46:32–01:47:49 — "Dillen"/"Dillenton"/"Dillent" → "Dehlin"

- **Master transcript had** three different garbled spellings of the same
  name across six occurrences in about 90 seconds: "the John Dillen,"
  "Dillen," "suing John Dillen," "of John Dillenton," "John Dillenton
  takes," "John Dillent."
- **Confirmed by John (Hogan), 2026-09-13:** the real name is **John
  Dehlin** — founder of the Mormon Stories podcast, excommunicated from
  the LDS Church in 2015. Fits the context on both counts: Ballard
  claims the Church is suing him, and separately calls him a habitual
  critic ("takes punches at me all the time").
- Six separate correction entries logged (ids 2–7 in
  `srt_corrections.json`) since each occurrence has its own exact cue
  text and, in three cases, its own distinct garbled spelling.

## Three "false-alarm proper nouns" — real words, not fabrications

Three more non-dictionary words turned out not to be garbled invented
names at all, just Whisper mishearing real, pre-existing words/proper
nouns as if they were surnames. Worth distinguishing from the correction
above: these aren't cases of Ballard saying something and Whisper
inventing a new wrong name — the correct word already exists, Whisper
just picked the wrong (also real) word that sounds similar.

- **"Maroney" → "Moroni"** (03:48:59, 03:49:23, 03:49:29) — Captain
  Moroni is a real Book of Mormon figure (Alma 44), not something
  Ballard made up.
- **"Harkin" → "Hearken"** (01:23:10, 01:23:12) — the archaic word
  "hearken" (to listen), not a surname at all. Scriptural phrasing
  ("hearken not unto the words of the prophets").
- **"Atomans" → "Atonement"** (00:15:10, 00:15:25, 00:15:44) — "the Day
  of Atonement." Directly relevant to the Day-of-Atonement date
  inconsistency already flagged in
  `backfire_truth_claims_inventory_2026-09-11.md` — this passage gives
  the specific claimed date, September 25, 2023.

All three logged as corrections (ids 8–15 in `srt_corrections.json`)
since they still need fixing in the SRT text itself, even though no
identification/listening judgment call was really needed here.
