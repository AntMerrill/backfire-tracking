# TODO — remaining work from the "Backfire" video

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
- [ ] `backfire_srts_all.tar` (full scene-clip SRTs + master
      transcript, 4.8MB) — still local only (Desktop + both USB
      drives). Only the smaller minute-chunk-only subset made it to
      Google Drive so far.
- [ ] Two earlier wiki-edit drafts set aside, not being pursued for now:
      Borys dismissal (reinforces a talking point Ballard's already
      using), Abraham Accords claim (real but doesn't hurt him, and has
      an unresolved WP:SYNTH problem).
- [ ] Citation-format fix for our own "best friend" ref is DONE (see
      above) — the earlier note about handing it to someone else to
      practice on is moot now, it's already live.
- [ ] 209 remaining non-dictionary words from the histogram audit still
      need manual review/correction via the new `apply_srt_corrections.py`
      workflow — only 1 of 211 done so far (Dick Andersen).
