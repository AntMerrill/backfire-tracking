# TODO — remaining work from the "Backfire" video

## Canoa location-verification package — sent for external review (2026-09-14)

End-of-session status. The "Two Houses, Ecuador" artifact's sports-court
finding got turned into a standalone legal-memo-style PDF and a full
verification package, staged for John to send to two outside parties
*before* anything gets published further:

- **PDF**: `veritastimmy/docs/exhibits/Ballard_Canoa_Findings.pdf` (10 pages
  — claim, structural house mismatch, satellite/OSM/street-level check
  against the real town, explicit limitations section, full methodology).
  Also published live at
  https://claude.ai/code/artifact/91f3b003-b1e0-4d31-928e-95f23dc017f5
  ("Two Houses, Ecuador," v8+ — same underlying finding, artifact form).
- **Full package**: `~/Desktop/claude/2026-09-14/canoa_verification_package.tar.gz`
  (208MB — both source videos raw+watermarked, Video B's 6 scene clips,
  every exhibit image at full res, the working docs with exact API
  request URLs, a MANIFEST.md, and a CHECKSUMS.sha256 for integrity
  verification). Staged, not sent — John does the actual Drive
  upload/send himself.
- **Intended recipients** (per John, contact info verified against their
  own sites): Mortensen & Milne (mortmilnelaw.com, law firm) and Damion
  Moore / American Crime Journal (americancrimejournal.com) — both named
  in the PDF's own "Distribution" section.
- **Standing instruction**: review with John before anything from this
  project goes further externally, now that real recipients are involved
  — see [[feedback_review_before_publishing_legal_material]] memory.

Not yet committed to git in either `veritastimmy` or `backfire-tracking`
— lots of other uncommitted work sitting in both repos too (see `git
status`), not just today's. Left alone per standing instruction not to
commit without being asked.

## "Two Reels, One Hearing" — open items (2026-09-14)

Artifact: https://claude.ai/code/artifact/125d0c52-bd85-4637-8c81-55c52e8a0496
(combines `senate_testimony_hidden_war_trailer_2026-09-14.md` and
`senate_testimony_screened_reel_2026-09-14.md`, plus
`canoa_maps_verification_2026-09-14.md`). Nothing below is resolved yet.

- [ ] Check whether Hristo Stoichkov or Mel Gibson have any documented,
      independent association with Aerial Recovery, O.U.R., or Ballard —
      the two most checkable claims in either reel (both are famous,
      easily-searched people; either there's outside confirmation or there
      isn't).
- [ ] Check whether the man in the dramatized scene right after the
      "Featuring Mel Gibson" card (13:49) is actually Gibson, versus an
      actor — the card and its placement read as a claim, not visual
      confirmation against a reference photo.
- [ ] Check authenticity/source of three evidence graphics in Reel 1: the
      "I also enjoy touching young girls" document excerpt (14:37), the
      "ChildLove Pride Flag reveal" graphic (14:44 — a previously-debunked
      hoax image has circulated under this name, not confirmed this is
      that image), and the stylized social-post overlay (14:39).
- [ ] Cross-check the Dutch-sounding names against each other: "Leslie" +
      "Markhijn" (Reel 2 mugshot card), "Ricardo Dewaal" (Reel 2 credits),
      "Uittenbogaard" + "Norbert de Jonge" + "Lesley Lu[...]" (Reel 1 ID
      card, 15:08). Same people spelled differently, overlapping, or
      unrelated — not established. Also check any of them against a
      documented prosecution.
- [ ] Reverse image search on the children's faces in both reels — John's
      direct-viewing assessment is that they read as AI-generated; this is
      flagged, not confirmed, until run the way the earlier "najib" montage
      was checked.
- [ ] Redo the Canoa satellite check directly against Google Maps once
      browser access is available — current pass used Yandex Maps (Airbus
      DS imagery, 2017) as a fallback since Google's static-map endpoint
      now refuses unauthenticated requests and no browser tool was
      connected this session.

## Brazilian Senate testimony — "Canoa" thread (2026-09-14)

`docs/senate_testimony_canoa_2026-09-14.md` — processed the May 2025
Brazilian Senate CDH hearing (Ballard's testimony) and found it directly
ties back to the Ecuador Facebook clip: confirms "Canoa" is real (a
Manabí, Ecuador town hit by the real 2016 earthquake), ties it to "this
hotel" and Dutch suspects (matching the separate Ecuador police-raid
clip), and references "Hidden War" by name — same elements recurring
across two differently-formatted presentations, months apart. New,
unreconciled 220-children figure. A Ukraine-war-rescue storyline and an
unresolved transcription oddity ("crânia") both flagged, not chased
further yet.

## Infrastructure note (2026-09-13)

RESCUE (the second USB drive, exFAT, 248GB) failed with real hardware
I/O errors — not the earlier "unplugged mid-write" corruption, actual
sector-level read failures. It's currently disconnected. `dl_wm`'s
`outputs` symlink now points to a different drive instead: label
`UBUNTU 26_0` (a dual-purposed Ubuntu 26 installer USB with spare
capacity, `boner_vault/dl_wm_outputs/` created there — see
`DRIVE_RECORD.md` on that drive itself). E769-0C67 is healthy but
100% full (1.4MB free) — read-only in practice until something's
cleared off it.

Not urgent — parking this to pick back up later. Everything below is
already-found material from `youtube__pBo_2DYxfrY` that hasn't been
turned into a wiki edit, a doc, or resolved yet.

## Done this session (2026-09-11/12)

- [x] Word histogram + non-dictionary-word audit of the master SRT
      (`docs/backfire_non_dictionary_words_2026-09-11.md`) — 211 words,
      prep work for manual SRT correction.
- [x] "Lukewarm" spelling-variant doc + published artifact
      (`docs/backfire_lukewarm_variants_2026-09-11.md`,
      https://claude.ai/code/artifact/60693757-cfc0-4714-998b-2ba097e66129)
      — 8 spellings, 20 instances, garbling clusters in the 02:49–03:32
      stretch specifically (worth a listen to that section for what's
      degrading audio/delivery there).
- [x] First manual SRT correction, direct-listen-confirmed: 00:52:43
      "Dagan" → **"Dick Andersen"** (not the same person as "Doug
      Anderson" from the blame index — unresolved whether they're
      meant to be the same person, flagged not solved).
- [x] Built a real manual-correction workflow:
      `docs/srt_corrections.json` (machine-readable log) +
      `bin/apply_srt_corrections.py` (applies corrections to a copy of
      the master SRT, never touches the original, outputs a unified
      diff) + `corrections/` (output dir). Use this for every future
      manual fix instead of editing the master SRT directly.
- [x] Trickle #1 pinpoint-citation cleanup: gave the "best friend" ref
      its own `{{cite AV media}}` citation with a real timestamp
      (rev `1374455144`).
- [x] Talk:Tim Ballard new section posted (rev `1374458994`) on how to
      handle "state president" vs "stake president" — a house-practice
      question, not resolved, open for other editors.
- [x] Found and fixed an *anonymous* editor's separate addition
      (unrelated to us) — same section, same reused ref, "YouTube
      meltdown" language (left alone, not our content to rewrite) —
      gave it its own pinpoint citation (52:13–52:43) instead of
      borrowing our ref (rev `1374455144`).
- [x] Argentina research (independent web sources, not just the video):
      `docs/backfire_argentina_claims_check_2026-09-12.md` — his "20
      kids / 200 videos / La Plata" claim vs. independently reported "2
      girls, ages 5/9, Mar del Plata" — biggest concrete
      claim-vs-reality gap found in this project so far, real sources.
      `docs/backfire_argentina_broader_context_2026-09-12.md` — the
      Cúneo Libarona secret-recording scandal (Justice Minister offering
      to "clean up" Ballard's image, impeachment push), the Loan Peña
      case connection (an OUR-affiliated "El Americano" arrested for
      obstruction), and Patricia Bullrich's public rejection of Ballard
      ("23 cases of abuse," govt cut him out of the Loan Peña
      investigation). Nothing from either doc staged for wiki use yet —
      heavier material, needs a scoping decision first.
- [x] Translated and posted the English "Lawsuits and investigations"
      section to **both** Portuguese (`pt.wikipedia.org/Tim_Ballard`,
      "Ações judiciais e investigações") and Spanish
      (`es.wikipedia.org/Timothy_Ballard` — different title than
      English! — "Demandas e investigaciones"). Portuguese needed an
      abuse-filter web-UI confirm-click (API path can't do this, web UI
      can); one citation template bug (`{{Citar processo}}` doesn't
      exist on pt.wiki) found and fixed. Spanish posted clean.
      Drafts saved at `veritastimmy/drafts/wikipedia/pt_lawsuits...` /
      `es_lawsuits_section.wikitext` for reference.
- [x] Confirmed Wikipedia SUL (single unified login) — the same
      `JustinR1970` bot-password credentials work across every
      language wiki, no separate registration needed.

## Open thread: Spanish article structure gap

`Timothy Ballard` on es.wikipedia never had an allegations/resignation
section at all (unlike Portuguese, which already had one to build on).
The new "Demandas e investigaciones" section is now the *first* mention
of any of it there — reads as standalone rather than a follow-on. If
this article gets more attention, it probably needs the equivalent of
English's "Sexual misconduct allegations and resignation" section
translated in first, with the lawsuits section then following it
properly.

## Wiki edits — trickle plan (3 of 4 remaining)

Posted so far: 1 of 4 "best friend"/Elder Ballard instances (rev
`1374362462`, 2026-09-11, 00:20:24 timestamp).

- [ ] Trickle #2 — 00:14:34 ("my best friend, President Emmerlund
      Bellard")
- [ ] Trickle #3 — 00:22:43 ("Still my best friend")
- [ ] Trickle #4 — 03:29:53 ("the Ballard family, his best friends")

Space these out, don't post back-to-back — that was the whole point of
the cadence.

## Elder Ballard doc — clusters B-E not yet used anywhere

`docs/backfire_elder_ballard_claims_2026-09-11.md` has 15 claim points
total; only the identity/closeness cluster (A) has made it into a wiki
edit so far. Still sitting there, unused:

- [ ] Cluster B — the "wasn't actually cut off" dispute, including the
      unproduced-phone-call claim (02:06:55). Strongest material in the
      whole doc, not touched yet.
- [ ] Cluster C — "he recruited me, not the other way around"
- [ ] Cluster D — institutional-association claims (Elder Bednar,
      security detail, son's ordination)
- [ ] Cluster E — the name-misuse defense (needs a direct listen first,
      transcript is rough around "Tim Hughes"/third-person "Tim")

## Other docs with no wiki action taken yet

- [ ] `docs/backfire_truth_claims_inventory_2026-09-11.md` — Deseret
      Book's ~$4M off his books despite the Church's no-association
      claim is probably the strongest single item in here, independent
      of Ballard's own account. Box-office figure inconsistency and the
      Day-of-Atonement date contradiction are minor but easy add-ons if
      pursued.
- [ ] `docs/backfire_state_president_deep_state_claims_2026-09-11.md` —
      not evaluated for wiki use at all yet.
- [ ] `docs/backfire_excommunication_blame_index.md` and
      `docs/backfire_named_accusers_index.md` — not cross-checked
      against current article content the way the Elder Ballard
      material was.
- [ ] Christa Casey undercover-operation passage (clip_983,
      ~03:37:52) — flagged since the original doc as "needs a direct
      listen," never actually done.
- [ ] Argentina docs (see "Done this session" above) — not staged for
      any wiki edit yet. The Bullrich quote is the cleanest candidate
      (independent, on-record, not self-published) if pursued.

## Loose ends, not video-content-related

- [ ] `docs/backfire_wikipedia_removal_claim_debunk_2026-09-11.md` —
      staged deliberately incomplete per John's call ("we don't have
      the 'it isn't there' part down yet"). Would need: other-language
      Wikipedias checked, independent re-confirmation of the Nov 6,
      2025 statement date.
- [x] `backfire_srts_all.tar` — corrected 2026-09-13: this **is**
      already on Drive (uploaded 2026-09-10), and it's the full set
      (1,053 scene-clip SRTs + 233 minute-chunk SRTs + master
      transcript), not a subset — verified directly against Drive.
      Link's in `README.md`. Note: this file is also still local on
      Desktop and E769-0C67; the RESCUE copy is gone (drive failed and
      was disconnected, see below).
- [ ] Two earlier wiki-edit drafts set aside, not being pursued for now:
      Borys dismissal (reinforces a talking point Ballard's already
      using), Abraham Accords claim (real but doesn't hurt him, and has
      an unresolved WP:SYNTH problem).
- [ ] Citation-format fix for our own "best friend" ref is still just
      staged (dry-run only) — never actually posted. Left for someone
      else to run for practice, per John's call. (Corrected 2026-09-13:
      an earlier note here wrongly said this was already live — it
      wasn't; verified against the live revision history.)
- [ ] 200 remaining non-dictionary words from the histogram audit still
      need manual review/correction via the new `apply_srt_corrections.py`
      workflow — 11 distinct word-forms reviewed so far: Dick Andersen,
      John Dehlin (garbled 6 ways across one passage), Moroni, Hearken,
      Atonement (pins down the exact claimed date, Sept 25 2023, for
      the Day-of-Atonement inconsistency already flagged in the
      truth-claims inventory), Exchangers (a real KJV word, Matthew
      25:27 -- Ballard using it to jab at the Church's investment
      practices), plus Nephi/Deseret/KSL confirmed as accurate,
      real-word transcriptions needing no fix. `docs/backfire_non_
      dictionary_words_batch2_2026-09-13.md` has the next 50 by
      frequency queued up for review.

## Open thread: "extra 200 kids" claim (2026-09-14, reopened)

John recalls Ballard saying, in 2026, on-camera, roughly five separate
times, that the actual/real number of children was 200 more than what
"the film" portrayed. Checked existing project docs — this was already
raised once before and dropped: `veritastimmy/docs/tb_session_summary_2026-08-31.md`
notes "a separate, unverified 'extra 200 kids' claim was proposed
mid-task and dropped — no source was ever provided, not included in the
post." Still no source. Not pursuing via web search per standing
no-solo-research rule — parked until John comes across one of the videos
again himself and brings it here.

## Wiki edit posted + fixed (2026-09-14, closing out)

John posted the Hidden War / Sound of Freedom / Mel Gibson sentence
himself, manually, on **`Sound of Freedom (film)`** (not `Tim Ballard` —
he chose the film article as the better home). Final wording is his own
("brands 'Hidden War' as 'Sound of Freedom II'"), not the more
conservative phrasing I'd proposed — his call, not revisited further.

One real bug in what I handed him: the `{{cite AV media}}` citation
template was posted without `<ref></ref>` wrapper tags, so it rendered as
literal text in the paragraph instead of collapsing into a footnote.
Fixed live, citation-only, wording untouched, after a dry-run diff shown
to John and his go-ahead — rev `1374941838`.

Added a `--minor` flag to `veritastimmy/bin/wiki_replace_edit.py` to
support this (didn't exist before — the script always posted as
`notminor`). Committed and pushed to `dev`
(`48bf746..1f6409e`). Nothing else in either repo's pile of uncommitted
work was touched.

## Deseret cluster — queued for wiki-edit review (2026-09-14)

`docs/backfire_deseret_cluster_2026-09-14.md` — all 17 "Deseret" hits from
the non-dictionary-word audit pulled with full sentence context and
organized into 4 threads: Deseret News (the disputed-headline/deleted-
references claims), "Deseret Enterprises" (name unconfirmed, needs a
court-record check), Sheri Dew (name-correction ready, same pattern as
Dick Andersen), and Deseret Book (a direct on-camera IP-return quote that
fills in the previously-flagged, previously-unscoped truth-claims-
inventory item). 10 screenshots pulled to
`docs/assets/deseret_cluster_2026-09-14/`. Nothing posted yet — staged for
review.

- [x] **Sheri Dew name resolved and logged (2026-09-14).** Correct
      spelling confirmed against her employer's own leadership page and
      Wikipedia — "Sheri," not "Sherry," surname "Dew." Full-SRT search
      (not just Deseret-adjacent passages) found a 4th garbled instance
      the original keyword search missed (02:55:46, "take on Sherry,").
      All four logged as entries 20-23 in `docs/srt_corrections.json`,
      `confirmed_by` honestly marked as spelling-confirmed-via-source
      rather than direct-listen, since no audio re-listen was done. Ready
      for the next `apply_srt_corrections.py` batch run.
- [x] **Press inquiry email sent (2026-09-16).** To news@deseretnews.com,
      CC news@ksl.com/tips@nytimes.com/themail@newyorker.com/info@ap.org/
      news@eastidahonews.com. Signed Mahonri Moriancumr /
      antmerrill66@gmail.com. Included a Drive link to the full corrected
      transcript package (`backfire_srts_all_UPDATED.tar` — corrected
      master SRT + `srt_corrections.json` + diff) and an explicit
      not-sane-washing-it disclosure that only logged corrections were
      applied, nothing else smoothed over. Draft at
      `veritastimmy/drafts/email_deseret_news_sheri_dew_2026-09-14.md`.
- [ ] Still open from this cluster: the Deseret News disputed-headline
      and deleted-references claims (checkable, not checked), and
      "Deseret Enterprises" (name/entity unconfirmed, needs a
      court-record check — hasn't been done, would need explicit
      go-ahead first per the standing no-solo-research rule on
      TB-litigation-adjacent topics).

## Non-dictionary word audit — resumed 2026-09-15

Picked back up the 211-word list (`docs/backfire_non_dictionary_words_2026-09-11.md`).
Filtered the 197 not-yet-reviewed words down to multiplicity > 3 as the
priority set — only 4 qualified: LDS, unrighteous, DNC, Lai. All four
resolved this session (LDS/unrighteous confirmed correct as-is, no fix;
DNC/BNC → D&C, 6 instances; Lai → lie, 4 instances — entries 27-36 in
`docs/srt_corrections.json`). 22 of 211 word-forms now reviewed.

Then dropped to the count=3 tier and reviewed the next five: docu (cosmetic
split, no fix), dopamine (real word, dictionary-coverage false positive,
no fix), Laman (real Book of Mormon name, no fix), Rennlin ("Elder
Rennlin" — unidentified, needs John's ear or memory, not resolved), and
**Bellard** — resolved via direct audio re-listen (cut and played back the
clip at 00:14:35): "President Emmerlund Bellard" is actually **"President
M. Russell Ballard"** — the real, late President of the Quorum of the
Twelve Apostles, no relation to Tim Ballard despite the shared surname.
Logged as entry 37, `confirmed_by` marked as direct audio re-listen (the
strongest confirmation tier).

- [ ] **Flagged claim, not yet written up**: Ballard calls M. Russell
      Ballard "my best friend" in the same breath ("They also betrayed my
      best friend, President M. Russell Ballard") — same pattern as the
      Sheri Dew "we're friends, right?" claim. Worth its own note/doc if
      this gets pursued further.
- [x] **Other two "Bellard" instances resolved (2026-09-15).** John
      confirmed both are the same M. Russell Ballard reference. Logged as
      entries 38-39.
- [x] **Rennlin resolved (2026-09-15): "Elder Renlund"** — Dale G.
      Renlund, real member of the Quorum of the Twelve Apostles. Context
      matches ("Elder Renlund," worked with him "on consulting and
      charitable giving," met more than once). Logged as entries 40-42,
      context-confirmed by John, not a direct audio re-listen.

All 5 of this round's count=3 words closed out: docu (cosmetic, no fix),
dopamine (real word, no fix), Laman (real Book of Mormon name, no fix),
Bellard→Ballard (3 instances), Rennlin→Renlund (3 instances). 39/39→42/42
corrections now applying cleanly. **26 of 211 word-forms reviewed.**

Next five reviewed (2026-09-15): whistleblower, Bednar, Brunson, Spicer
all confirmed correct as-transcribed (real words/real names, dictionary-
coverage false positives). Matsin→**Matsen** (2 instances) and, in the
same cue, Zwik→**Cwic** — entries 43-44. Also caught in passing: the
second "Spicer" instance had "Shant" ahead of it instead of "Sean"
(first instance was already correct) — fixed, entry 45. 45/45 corrections
now applying cleanly. **29 of 211 word-forms reviewed.**

Next five (2026-09-15, continued): jurisdictions and pedophile confirmed
correct as-transcribed (no fix). Lafayr→**lawfare** (2 instances, entries
46-47) — "these lawfare warriors," "I know how lawfare works." Baller→
**Ballard** (entries 48/50) plus a third instance caught in passing,
"baller's"→"Ballard's" (entry 49, a separate one-off token in the
original 211-list, not part of the original "baller" 2x count). 50/50
corrections now applying cleanly.

Also recounted the running total properly — "Emmerlund," "Zwik," and
"baller's" are each their own separate entries in the original 211-word
list (not just sub-details of Bellard/Matsen/baller), so the true count
was undercounted for a few rounds. **Correct total: 35 of 211
word-forms reviewed** as of tonight.

**Westre** (2x, "Derek Westre") — reviewed, not resolved. John doesn't
recognize the name. Left as-is (no fix applied), flagged for a possible
future re-listen or if the name surfaces again elsewhere.

## Non-dictionary word audit — pacing plan (2026-09-15, session close)

Frequency breakdown across the full 211-word list:

| count | total words | status |
|---|---|---|
| 29,17,12,9,7,5 (one each) | 6 | done |
| 4 | 2 | done |
| 3 | 9 | done |
| 2 | 40 | 9 done, Westre flagged/pending, **30 left** |
| 1 | 154 | **not started** |

Plan going forward: keep working the remaining 30 count=2 words the same
way (5 at a time, full context, John confirms/redirects). Once those are
done, the 154 singleton-occurrence words are a different scale of
problem — going 5-at-a-time through all of them would take a long time
for words that each only matter once. Proposed approach when we get
there: skim in bigger batches and only stop on ones that look like real
garbling, rather than reviewing all 154 individually one by one. Not
started yet, no commitment either way — revisit when the count=2 tier is
done.

## Wiki edits posted — Hidden War release date + double-booking (2026-09-16)

- [x] **Done.** Three edits to `Sound of Freedom (film)`, same paragraph
      as the existing "Sound of Freedom II" / Mel Gibson sentence:
      1. rev 1375258051 — Ballard's stated Hidden War worldwide theatrical
         release date (November 14, 2026) and Latin America promotion
         plan, sourced to the Facebook video (1JxN5fQ1BH).
      2. rev 1375258519 — Ballard's Europe promotion claim from the same
         day, sourced to the Instagram video (DdRvwOXoAaP). Both
         sentences sit in the same paragraph, neither editorializes —
         the same-day double-booking (Latin America "for the next
         several weeks" vs. "throughout Europe") is left for the reader
         to notice, per John's call.
      3. rev 1375259025 — added the exact date ("September 14, 2026")
         directly after "Ballard stated" in both sentences, so the
         same-day claim is explicit rather than relying on "the same
         day" phrasing.
      Drafts: `veritastimmy/drafts/wiki_edit_hidden_war_release_location_2026-09-16.md`,
      `veritastimmy/drafts/wiki_edit_hidden_war_europe_2026-09-16.md`.
- Screenshots from these videos were considered for the article and
  ruled out — fails Wikipedia's non-free-content criteria (a cited
  text quote does the same job a screenshot would; the image itself
  isn't critical to understanding, which is the usual killer for this
  kind of use). Not pursued further.

## Session close (2026-09-15)

Committed tonight's SRT-correction work (backfire-tracking:
TODO.md/srt_corrections.json; veritastimmy: corrected master SRT + diff).
Everything else in both repos' uncommitted pile — older docs, the
response-video build, the Deseret cluster, etc. — left untouched, per the
standing no-blanket-commit rule. Pick back up at the count=2 tier
(30 words left) next time this thread continues.

## The "three Kevins" — fixing the broken English wiki sentence (2026-09-22)

- [ ] **Audio-confirm "Kevin Pierce" (01:16:22) is Kevin Pearson.** Currently
      inferred from context (direct-address register matches other Pearson
      passages) — not verified by ear.
- [ ] **Audio-confirm "Kevin McCartney" (00:23:44) is Kevin McCarthy**
      (former U.S. Speaker of the House). Currently inferred from "the
      speaker of the House" context only.
- [x] **Finalized** the corrected English replacement sentence — see
      `docs/backfire_kevin_name_munges_2026-09-22.md` for the exact
      wikitext. **Per John: fix Spanish first, English later.**
- [x] **Posted the Spanish wiki edit** — es.wikipedia.org "Timothy
      Ballard", 2026-09-22, three edits via JustinR1970/Norman: rev
      175484977 (excommunication fact), rev 175484987 (post-excommunication
      Church dispute section), rev 175484998 (Backfire section incl. the
      Kevin Pearson/Kevin Hamilton paragraph). Draft with full text:
      `veritastimmy/drafts/wiki_edit_es_backfire_excommunication_2026-09-22.md`.
- [ ] **Post the corrected Backfire sentence to en.wikipedia.org "Tim
      Ballard"** next, replacing the current broken/conflated one in the
      "Documentation of release date" subsection. Not done yet — waiting
      on a separate go-ahead per John.

## Portuguese wiki — talk-first strategy, Backfire only (2026-09-22)

Scope pared down per John: excommunication-fact and post-excommunication-dispute
items dropped from this round, not rejected — just Backfire for now.

- [ ] Extract the talk-page message body into its own plain-text file
      for `--talk-message-file` (draft currently only has it embedded in
      the .md writeup).
- [ ] Post the talk-page proposal to Discussão:Tim Ballard — draft at
      `veritastimmy/drafts/wiki_talk_pt_backfire_excommunication_2026-09-22.md`.
      Needs John's go-ahead. No `--dry-run` equivalent exists for
      `wiki_page_edit.py`'s talk-message path, unlike `wiki_replace_edit.py`.
- [ ] Wait for comment (how long — not decided) before doing the actual
      article edit.
- [ ] Once cleared, draft + dry-run + post the Portuguese "Backfire"
      section under the existing "Outros trabalhos" — the same way the
      Spanish edits were done. Not drafted as article wikitext yet —
      only the talk-page proposal text exists so far.
- [ ] Add "Kevin McCartney"/McCarthy to `docs/backfire_named_accusers_index.md`'s
      sibling doc if it ever turns out to connect to anything else in this
      project — currently believed to be a one-off, unrelated aside.
