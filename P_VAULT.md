# P-vault: other people's videos in the Backfire story

**Companion to the TB Backfire Log (V-numbers = Ballard's own posts).** P-numbers cover everything else:
sources he reposts or plays, responses, amplifiers, and Ballard appearing on someone else's channel.

## How it's organized (built to stay flexible)

- **P-numbers are permanent**, same rule as V: next unused number, never reused. Seeded 2026-09-27 in date order; later ones go at the end.
- **Three tables, not one.** Items, people and links live apart, so one thing can be tagged many ways without redesigning columns:
  - `P_VAULT.csv`: one row per video. **person** (who's behind it) is separate from **account** (where it's posted) and **speaker** (who talks in it). They often differ: Preston posts from 3 differently named accounts; Latter Day Chad posts as "Zion Media"; Ballard talks on TV Senado's channel.
  - `VAULT_PEOPLE.csv`: person → all their accounts.
  - `VAULT_LINKS.csv`: the web between items, **any direction, V↔P, P↔P, V↔V, or a screenshot → item**, with an optional timestamp on each end. Relations used so far: `cross_post_of`, `plays_audio_of`, `reposts`, `responds_to`, `same_claim_as`, `screened`, `promotes`, `screenshot_of`. Add new ones freely.
- **tags** (free text, `;`-separated) carry the story threads, e.g. `stake-president-rumor`. One video can be in several threads.
- **Placeholders allowed**: a P-number can exist before the video is found (P011), so a V row's "plays someone's audio" always has a place to point.
- **Scope rule**: in if it's part of the Backfire/Ballard story. The Instagram bot network (sandrabronzina etc.) stays in the private `timbot-network` repo, not here.

## Items

| P | Platform | ID | Person (account) | Speaker | Posted (MT) | Length | Title (verbatim) | What it is | Tags | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| P001 | YouTube | `-F9orJXMvR4` | TV Senado (TV Senado) | Tim Ballard (testifying; + other panelists) | 2025-05-20 12:43 | 2:03:05 | CDH debate enfrentamento ao tráfico humano – 20/5/25 | Ballard's Brazilian Senate testimony; Hidden War promo "Sound of Freedom II" screened 13:24–13:48 | ballard-as-guest; hidden-war; sof-2 | live |
| P002 | YouTube | `XAgNSNMkjik` | Danny Tommo (Danny Tommo) | ? | 2026-07-17 18:07 | 1:10 | See you all tomorrow! 🇬🇧🤝🇺🇸 | teaser for P003 | ballard-as-guest; uk | live |
| P003 | YouTube | `nqwKaDoyY4Q` | Danny Tommo (Danny Tommo) | Tim Ballard (guest) | 2026-07-21 12:33 | 14:37 | Sound of Freedom to Hidden War: Tim Ballard Declares: UK Frontline in the Fight Against Ch… | Ballard interview, UK | ballard-as-guest; hidden-war; uk | live |
| P004 | YouTube | `e6-VRFOvGvU` | Washington National Cathedral (Washington National Cathedral) | Dallin H. Oaks | 2026-09-16 19:01 | 1:40:50 | Faith, Freedom, and the Common Good with Dallin H. Oaks | 9.16.26 | context; why it was pulled (09-18) not recorded | context-unverified; lds-leadership | live |
| P005 | Instagram | `DdaPUY2x8QM` | Jason Preston (wearethepeopleutah) | Jason Preston | 2026-09-17 19:25 | 2:57 | TODAY WAS SIGNIFICANT. After nearly a year of litigation, we questioned Joe and Lee Bennion under oath… | FIRST public telling of the rumor: "our state president has been removed, but I cannot verify yet" | stake-president-rumor; bennion-deposition; origin | live |
| P006 | Facebook | `4613324495655403` | Jason Preston (We ARE the People) | Jason Preston | 2026-09-17 19:25 | 2:57 | TODAY WAS SIGNIFICANT. After nearly a year of litigation, we questioned Joe and Lee Bennion under oath… | = P005 (FB cross-post, same minute) | stake-president-rumor; bennion-deposition | live |
| P007 | YouTube | `4hNRNZFOh1M` | Jason Preston (We Are The People Utah) | Jason Preston | 2026-09-21 07:00 | 26:28 | "He Refused to Excommunicate Us. Then He Paid the Price" | Ballard plays its audio in V019 (same day) | stake-president-rumor | live |
| P008 | YouTube | `9r59wR_0MHk` | Latter-day Chad (Zion Media) | Latter-day Chad | 2026-09-21 22:22 | 1:17:01 | BREAKING: They Excommunicated a Stake President for Refusing to Excommunicate Him-is Chad… | amplifies the rumor | stake-president-rumor | live |
| P009 | YouTube | `ugQiIdaG3Y8` | Watcher Palmer (Watcher Palmer) | Watcher Palmer | 2026-09-23 11:47 | 31:52 | Did A Stake President Really Get Excommunicated?  Quiet Moments For The Non Essential. | questions the rumor | stake-president-rumor | live |
| P010 | YouTube | `TjYtjAzLYsk` | Jason Preston (We Are The People Utah) | Jason Preston | 2026-09-24 07:00 | 12:56 | The Rumors Are Spreading. Here's What He Actually Told Us | Ballard reposts it as V032/V042 "Listen to Jason" | stake-president-rumor | live |
| P011 | ? | `` | Latter Day Chad (?) | Latter Day Chad | ≤ 2026-09-19 | ? | (not identified) | the audio Ballard plays in V009 (09-19); source post not found yet | stake-president-rumor; placeholder | not downloaded |
| P012 | Instagram | `DdcSqnmBnYe` | Tim Ballard Foundation Ecuador (timballardfoundationecuador) | ? (Spanish; interview with young people, not Ballard) | 2026-09-18 14:29 | 2:36 | Tuvimos la oportunidad de compartir con jóvenes sobre una realidad que necesita ser hablada, comprendida y enfrentada: la trata de personas… | Ballard's foundation account, Ecuador | ballard-org; ecuador | live |

## Links

| From | Relation | To | At | Note |
|---|---|---|---|---|
| P006 | cross_post_of | P005 |  | same video, same minute, FB + IG |
| V019 | plays_audio_of | P007 |  | V019 note: plays Jason Preston's audio (4hNRNZFOh1M, 5:49) |
| V032 | reposts | P010 |  | "Listen to Jason" = Preston's 09-24 video |
| V042 | cross_post_of | V032 |  | IG copy |
| V009 | plays_audio_of | P011 |  | Latter Day Chad's audio |
| P008 | same_claim_as | P005 |  | stake president excommunicated for refusing to excommunicate Preston |
| P009 | responds_to | P005 |  | asks whether the rumor is true (relation by title; not checked in audio) |
| P010 | same_claim_as | P005 |  |  |
| P001 | screened | hidden-war-promo | 13:24–13:48 | Hidden War promo "Sound of Freedom II" shown in the hearing (cited on en.wiki Sound of Freedom) |
| P003 | promotes | hidden-war |  |  |
| IMG_1278 | screenshot_of | P005 | ~0:10 | our iPhone screenshot: "our state president has been removed. Uh but I cannot" |
| facebook__14qaYWvbJs7 | local_duplicate_of | V021 |  | same video downloaded via share link (resolves to 1774065160384040) |

## The stake-president rumor, in order (from the links above)

1. **P005/P006** (Sept 17, 19:25) Preston: "our state president has been removed, but I cannot verify yet."
2. **V009** (Sept 19) Ballard plays Latter Day Chad's audio (P011, not found yet).
3. **P007** (Sept 21, 07:00) Preston, "He Refused to Excommunicate Us. Then He Paid the Price" → **V019** (Sept 21, 16:59) Ballard plays it.
4. **P008** (Sept 21, 22:22) Zion Media: "BREAKING: They Excommunicated a Stake President…"
5. **P009** (Sept 23) Watcher Palmer: "Did A Stake President Really Get Excommunicated?"
6. **P010** (Sept 24) Preston: "The Rumors Are Spreading…" → **V032/V042** (Sept 25) Ballard: "Listen to Jason."
