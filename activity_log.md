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

## 2026-09-11

- Snipped every occurrence of two speech patterns from the source
  video: "state president" (35 instances, "stake" mispronounced as
  "state") and "lukewarm" (13 clustered instances). Built a supercut
  of the 35 "state president" clips (2:58 total,
  `state_president_supercut.mp4`); left "lukewarm" as a text-only
  record per John's call, since the point there is the word itself
  never gets consistently transcribed - found 6 distinct spellings
  across 27 hits, including two non-word "q" renderings
  ("luquormism", "luquormed").
- New doc: `docs/backfire_speech_patterns_2026-09-11.md` (also in
  veritastimmy).

- Compiled the actual claims (not just pronunciation) involving the
  unnamed stake president, and every "deep state" mention (5, all in
  the church-governance sense, not US politics) — new doc:
  `docs/backfire_state_president_deep_state_claims_2026-09-11.md`
  (also in veritastimmy).

- Compiled a truth-claims inventory from the master transcript,
  same [F]/[T]/[S] tagging convention as the earlier Fearless Brothers
  claims doc: financial/box-office figures, court outcomes, media
  conduct claims, and dated events. Flagged one internal inconsistency
  worth checking — two different dates two years apart are both
  called "the Day of Atonement," which shouldn't both be true since
  Yom Kippur's Gregorian date moves yearly. New doc:
  `docs/backfire_truth_claims_inventory_2026-09-11.md` (also in
  veritastimmy).

- Checked the "Wikipedia removed articles promoting Ballard/O.U.R. the
  same day as the Church statement" claim against Wikipedia's own
  public edit history (MediaWiki API, no credentials needed). All
  three most-relevant articles (Tim Ballard, Operation Underground
  Railroad, Sound of Freedom (film)) show zero edits anywhere near
  Nov 6, 2025 — gaps of 4 weeks to 6+ months spanning the claimed
  date, each bracketed by a direct permalink. Different pattern than
  the two earlier-verified claims (real event, spun) — here the
  specific claimed event doesn't appear to have happened at all, on
  the record checked. New doc:
  `docs/backfire_wikipedia_removal_claim_debunk_2026-09-11.md` (also
  in veritastimmy). Two Wikipedia-edit drafts from earlier today
  (Borys dismissal, Abraham Accords claim) both set aside per John's
  call — neither posted.

- Compiled every claim in the video about "Elder Ballard" (M. Russell
  Ballard, real LDS apostle, died Nov 2023 — no stated relation beyond
  shared surname): the "best friend" framing, the core contested claim
  that he was never actually cut off (including an assertion of an
  undocumented/unproduced phone recording at 02:06:55), the "he
  recruited me, not vice versa" claims, institutional-association
  claims (Elder Bednar, security detail, a named son's ordination),
  and a defense against a name-misuse allegation. 15 distinct claim
  points, each with an exact cue-start timestamp. New doc:
  `docs/backfire_elder_ballard_claims_2026-09-11.md` (also in
  veritastimmy).

- Made a TODO.md capturing everything still outstanding from today's
  Backfire work (trickle plan for the remaining 3 Elder Ballard wiki
  edits, unused claim clusters, docs with no wiki action taken yet,
  the incomplete Wikipedia-removal debunk, the un-uploaded full SRT
  tar) before moving on to something else.

## 2026-09-11/12

- Word histogram + non-dictionary-word audit of the master SRT (211
  words, `docs/backfire_non_dictionary_words_2026-09-11.md`) — prep
  work for manual SRT correction going forward.
- "Lukewarm" spelling-variant deep dive: 8 spellings, 20 instances,
  garbling clusters hard in the 02:49–03:32 stretch specifically.
  Published as its own artifact (waveform + frequency meter + exhibit
  cards): https://claude.ai/code/artifact/60693757-cfc0-4714-998b-2ba097e66129
- First real manual SRT correction, direct-listen-confirmed by John:
  00:52:43 "Dagan" → "Dick Andersen" (distinct from "Doug Anderson" in
  the blame index — unresolved whether same person). Built a proper
  correction workflow for this going forward: `docs/srt_corrections.json`
  (machine-readable log) + `bin/apply_srt_corrections.py` (applies to a
  copy of the master SRT, outputs a unified diff, never touches the
  original).
- Wiki edits posted: pinpoint citation on the "best friend" ref (rev
  1374455144); new Talk:Tim Ballard section on "state president" vs
  "stake president" (rev 1374458994); found and fixed a citation issue
  on an unrelated anonymous editor's addition (gave it its own pinpoint
  cite instead of sharing ours).
- Argentina research, independent of the video (real news sources, not
  just Ballard's own claims): the Feb 2025 rescue claim ("20 kids/200
  videos/La Plata") doesn't match any independently reported account
  (all say 2 girls, Mar del Plata) — biggest concrete claim-vs-reality
  gap found in this project. Also found: a Justice Minister
  secretly-recorded offering to help "clean up" Ballard's image
  (real institutional scandal, impeachment push), an OUR-affiliated
  operative arrested for obstructing the active Loan Peña missing-child
  case, and Security Minister Patricia Bullrich's on-record rejection
  of Ballard. Two new docs, nothing staged for wiki use yet.
- Translated and posted the English "Lawsuits and investigations"
  section to both Portuguese and Spanish Wikipedia (different article
  titles — "Tim Ballard" vs "Timothy Ballard"). Confirmed Wikipedia's
  SUL means the same bot credentials work on every language wiki.
  Portuguese needed a web-UI abuse-filter confirm-click (API path
  can't do that); found and fixed one broken citation template
  (`{{Citar processo}}` doesn't exist on pt.wiki). Spanish posted
  clean on the first try, but that article never had an allegations
  section to begin with — flagged as a structural gap for later.
- Updated TODO.md with everything above plus what's still open.

## 2026-09-22

- Traced the broken, unattributed sentence at the end of en.wikipedia.org
  "Tim Ballard"'s Backfire subsection ("...like the 'hit job he got from
  his state president Kevin.") back to the corrected master transcript.
  Found it conflates two separate things: Kevin Pearson (LDS Area
  President) allegedly ordering Kevin Hamilton (a Genealogy Department
  employee) to carry out the excommunication "hit job" — and a wholly
  separate, unrelated aside naming "Kevin McCartney" [sic, almost
  certainly Kevin McCarthy, former U.S. Speaker of the House] in a
  political anecdote. Drafted a corrected, properly-attributed
  replacement sentence for the English article (not yet posted).
- New doc: `docs/backfire_kevin_name_munges_2026-09-22.md` (also in
  veritastimmy) — full writeup of all three "Kevin"s, counts, timestamps,
  and what's actually quotable.
- Updated `docs/backfire_excommunication_blame_index.md` (also in
  veritastimmy): resolved the previously-"unnamed" genealogy-department
  person as Kevin Hamilton, added a new Kevin Hamilton section, added a
  new Kevin McCartney/McCarthy section, logged the "Kevin Pierce" name
  munge (probable mishearing of Pearson, not yet audio-confirmed).
- Added a short cross-reference note (not substantive content — out of
  that doc's scope) to `docs/backfire_named_accusers_index.md` (also in
  veritastimmy) pointing to the blame index and the new Kevin doc.
- Separately drafted the Spanish-language wiki edit bringing
  es.wikipedia.org "Timothy Ballard" in line with the English article's
  excommunication/post-excommunication/Backfire content:
  `veritastimmy/drafts/wiki_edit_es_backfire_excommunication_2026-09-22.md`
  (Spanish wikitext + English translation + edit summary, not posted).
- Both audio-confirmations (Pierce=Pearson, McCartney=McCarthy) still
  open — see TODO.md.
- **Finalized** the corrected English replacement sentence (logged in
  `docs/backfire_kevin_name_munges_2026-09-22.md`, also in veritastimmy):
  "Separately in the video, Ballard alleges that Kevin Pearson, an LDS
  area president, ordered a Church employee, Kevin Hamilton, to carry
  out what Ballard calls 'the hit job' leading to his excommunication."
  reusing the article's existing `ref name=":2"` citation. Per John:
  **Spanish gets this content first, English gets fixed later** — added
  the translated paragraph (with its own Spanish citation to the
  Backfire video) to
  `veritastimmy/drafts/wiki_edit_es_backfire_excommunication_2026-09-22.md`,
  which had previously left this material out entirely while it was
  still broken/unresolved.
- **Posted all three Spanish edits** to es.wikipedia.org "Timothy Ballard"
  via JustinR1970/Norman, each dry-run-verified first: rev 175484977
  (excommunication fact, extends the existing lead sentence, reusing the
  article's own already-cited FOX 13 source rather than duplicating it —
  corrected from the original draft, which wrongly targeted "Fundación
  O.U.R" based on an earlier AI-summarized read instead of the raw
  wikitext), rev 175484987 (new "Disputas posteriores a su excomunión
  con la Iglesia" section), rev 175484998 (new "Backfire" section,
  includes the Kevin Pearson/Kevin Hamilton "hit job" paragraph with its
  own citation to the source video). English article's own fix still not
  posted — deliberately held per John.
