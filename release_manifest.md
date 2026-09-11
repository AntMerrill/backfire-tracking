# Release manifest — Backfire (youtube__pBo_2DYxfrY)

Physical staging location: `RESCUE` USB drive (248.8GB, label `RESCUE`,
mounted at `/run/media/hogan/RESCUE`), under `backfire_release_staging/`.
Nothing here is pushed to any git remote — this manifest just records
what's on the drive and why, so the drive's contents are legible without
having to re-derive the structure later.

## tier1_preview (~35MB)

Smallest, first-release tier — intentionally not the full archive.

- `highlights/` — curated snip clips (Matthew 18 / "heathens and
  publicans" passage, both cuts), burned captions.
- `docs/` — copies of the three investigative docs (blame index, named
  accusers index, methodology).
- `youtube__pBo_2DYxfrY_master_stitched_patched.srt` — full-video
  transcript, one file, boundary word-cuts already corrected.

## tier2_editor_pack (~7.3GB)

- `scene_clips/` — all 1053 scene clips, **burned** (captions + scene
  number overlay baked in), each with a same-named `.srt` sidecar.
- `compilation_parts/` — the 4 reverse-chronological, hour-ish-length
  compilation videos (everything burned in, ready to watch straight
  through).

## tier3_full_archive (~5.5GB)

- `dev_package/` — the 1053 **plain** (unburned) original scene clips,
  plus the full-length original watermarked source video
  (`_full_source_watermarked.mp4`).
- `minute_chunks/` — the 233 ~1-minute chunks (`hour_N/minute_NN/`),
  each with its own `.srt`, plus:
  - `_edge_checks/` (930 files) — the 232 boundary-verification clips +
    SRTs + whisper.json, the mid-word-cut detection report, and the
    153-row word-fixes reference.
  - both master SRT variants (raw stitch and patched).

## Known issues / caveats carried into the release

- 12 scene clips (`clip_02, 03, 115, 415, 486, 719, 921-926`) have empty
  SRTs — verified by direct watch to be genuinely silent, not a gap. See
  `docs/backfire_minute_chunk_methodology_2026-09-09.md`, "Verified
  no-speech clips" section.
- Some passages in `docs/backfire_named_accusers_index.md` are flagged
  "needs a direct listen" — the Whisper transcript is too garbled there
  to trust as-is, particularly around the Christa Casey / undercover-
  operation passage. Don't treat those as settled quotes.
