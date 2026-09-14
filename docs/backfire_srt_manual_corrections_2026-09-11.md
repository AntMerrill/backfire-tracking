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
