# Activity log — Backfire project (internal tracking)

Appended to as work happens, not written after the fact.

## 2026-09-10

- Set up 3-tier release staging on the `RESCUE` USB drive
  (`backfire_release_staging/tier1_preview`, `tier2_editor_pack`,
  `tier3_full_archive`) — see `release_manifest.md` for full contents.
  Deliberately staged tier1 as a small preview, not the whole archive,
  per John's call.
- Two copy mistakes made and caught/fixed during staging: an rsync
  include-pattern (`clip_*.mp4`) matched `.burned.mp4` files too both
  times it was used (tier2 primary attempt, then again in
  tier3/dev_package) — cleaned up both times by deleting the
  wrongly-included burned copies. Filter pattern needs a real fix if
  this gets scripted/reused rather than run ad hoc again.
- Created this private repo (`AntMerrill/backfire-tracking`) for
  internal tracking — text/docs only, no video binaries. Copied in the
  3 existing investigative docs from `veritastimmy/docs/` (not moved,
  not removed from there).
- John's direction: keep this private, internal-use only, and keep a
  real running log of what's done here — he wants distance from
  handling the underlying material directly.
- **RESCUE drive corruption incident**: both `RESCUE` and `E769-0C67`
  got physically unplugged while mounted and actively being written to.
  Kernel logged unclean-unmount warnings on both; `tier2_editor_pack`
  and then `tier3_full_archive` on `RESCUE` were found empty/scrambled
  afterward (exFAT directory-table corruption, not a simple delete —
  files appeared misfiled into the wrong folder). Verified the actual
  original production data on `E769-0C67` and in the repos was untouched
  — only the staged *copy* on RESCUE was lost. Queued `sudo fsck.exfat`
  for John to run before RESCUE is trusted again; full copy redo is on
  hold pending that.
- Pivoted away from the big multi-tier copy given disk-space limits
  (root disk only 5.5GB free, not enough for tier2 (7.3GB) or tier3
  (5.5GB)). Built a much smaller, dedicated **SRT-only package**
  instead (`backfire_srts_all.tar`, ~4.8MB on Desktop, also copied to
  both USB drives): 1,053 scene-clip SRTs, 233 minute-chunk SRTs, and
  the patched master full-video transcript, plus a README with the
  extraction command and accuracy caveats. Dropped the raw (unpatched)
  master SRT and the 232 edge-check SRTs per John's call — those are
  internal QA material, not needed by a recipient.
- Uploaded (John, via drag-and-drop — no direct-upload path exists for
  Google Drive's UI, no discoverable file-input element in the DOM) a
  copy of the minute-chunk SRTs + README to Google Drive, shared
  "Anyone with the link" (Viewer): see README.md "Downloads" section
  for the link. Note this Drive upload covers the minute-chunk SRTs
  only, not the full `backfire_srts_all.tar` (scene-clip SRTs +
  master transcript) — that hasn't been uploaded anywhere yet, still
  local-only (Desktop + both USB drives).
