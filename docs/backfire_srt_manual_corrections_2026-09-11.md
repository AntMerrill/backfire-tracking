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
