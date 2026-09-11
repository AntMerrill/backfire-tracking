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
