# PL-vault: politicians' posts with Tim Ballard

**Companion to the V-vault (Ballard's own posts) and the P-vault (other people's videos).** PL-numbers cover posts
by **politicians and officials, current or former**, that feature Ballard or list him as an Instagram Collaborator:
campaign ads, hearings, joint appearances.

## Rules (same as V and P)
- **PL-numbers are permanent**: next unused number, never reused. Later finds go at the end.
- `PL_VAULT.csv` has one row per post. **person** (the politician) is separate from **account** (where it's posted)
  and **speaker** (who talks). **office** records their role *on the post date*, with how it ended.
  What they call themselves in the video goes in `what_it_is`, never in `office`.
- People go in the shared `VAULT_PEOPLE.csv`. Links (PL↔V, PL↔P, PL↔PL) go in the shared `VAULT_LINKS.csv`.
- **Files: look the ID up in the master catalog `/mnt/ubuntu26/boner_vault/BONER_VAULT.csv`** (BV-numbers, folder, which
  files exist). `local` here is only the folder name.
- A person's background, sources and account metadata go in a dossier in the private `timbot-network` repo
  (`accounts/<handle>/DOSSIER.md`). Only the post rows live here.

## Items

| PL | Platform | ID | Person (office) | Account | Speaker | Posted (MT) | Length | Title (verbatim) | What it is | Tags | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PL001 | Instagram | `DdziH28vE_5` | Sílvia Waiãpi (former federal deputy, PL-Amapá; seat revoked) | crisnardesdf / Cris Nardes (collab: silviawaiapi, timballard89) | Sílvia Waiãpi | 2026-09-27 15:17 | ~1:28 | Mulheres ocupando espaços… No dia 4, faça sua escolha de forma consciente. Cris Nardes — 10987 | Election ad for Cris (Cristina) Nardes, no. 10987, Distrito Federal, Oct 4 vote. She calls herself "deputada federal pelo estado do Amapá" (term ended 2025-07-31). Ballard is listed as Collaborator and doesn't speak. | brazil; election-2026; campaign-ad; collab-tb | live |
| PL002 | Instagram | `DN5lyfwDiaQ` | Sílvia Waiãpi | silviawaiapi | ? | 2025-08-28 07:09 | carousel (6) | ✨ Gratidão que move nossa missão ✨ No dia 22 de agosto de 2025, o Instituto @timballard89 acompanhado da deputada @silvi… | Ballard's institute and 'deputada' Silvia hand a vehicle to the Oiapoque Conselho Tutelar (Aug 22 2025). Her term had ended 2025-07-31. | brazil; amapa; donation; collab-tb | queued (carousel tool) |
| PL003 | Instagram | `DRPW7C1DSXQ` | Sílvia Waiãpi | lilipacheco.usa / Lidiane Pacheco (collab: matthewcooper, silviawaiapi, timballard89) | none (music only) | 2025-11-19 07:45 | 0:24 | It’s official: HIDDEN WAR IS OUT! Go check this incredible real footage about Tim latest rescue/investigation crossing d… | Hidden War launch post. Collaborator list includes matthewcooper. | hidden-war; collab-tb; matthewcooper | live |
| PL004 | Instagram | `DReWeZLEZYM` | Sílvia Waiãpi | silviawaiapi | Tim Ballard | 2025-11-25 03:27 | 2:11 | Tim Ballard faz uma reflexão sobre os danos causados ao resgate de crianças no Brasil, ao cerceamento da fé… | Her post of a Ballard reflection on 'damage done to child rescue in Brazil'. No collaborators. Ballard: "They hit my friend, Congressman Sylvia… and they shut down our child rescue efforts" (transcript; audio check). Frames her removal as an attack. | brazil; tb-speaks | live |
| PL005 | Instagram | `DYys2LkI3TE` | Sílvia Waiãpi | timballard89 (collab: claudiodantassequeira, silviawaiapi, tbfrescue, timballardfoundationecuador) | Tim Ballard (Hidden War trailer VO) | 2026-05-26 00:47 | 0:29 | Behind the scene footage at Brazil’s Claudio Dantas Show. Previewing the trailer for Hidden War. Streaming on Angel Stud… | Behind-the-scenes at the Claudio Dantas Show, Hidden War trailer preview. | hidden-war; brazil; media-appearance; collab-tb | live |
| PL006 | Instagram | `DYzGBvmREL1` | Sílvia Waiãpi | silviawaiapi (collab: brasilgrandee, timballard89) | ? (woman, Portuguese; check audio) | 2026-05-26 04:29 | 1:30 | A GRITO DE CRIANÇAS NO MEIO FLORESTA QUE MUITOS SE RECUSARAM A ESCUTAR E CRIAM FORMAS DE PROTEGER ABUSADORES E SILENCIAR… | Tags @damares (Damares Alves, senator) alongside Silvia and Ballard. | brazil; amazon; collab-tb; damares | live |
| PL007 | Instagram | `DY2gfk4oAvZ` | Sílvia Waiãpi | timballard89 (collab: silviawaiapi, tbfrescue, timballardfoundationecuador) | Tim Ballard | 2026-05-27 12:11 | 1:12 | Deputada (“Congresswoman”) Silvia Waipai is my hero. I call her my “Jefa” in Brazil. We rescued many children in the Ama… | Ballard-voice caption calls her 'Congresswoman' and 'my Jefa' in May 2026, ten months after her term ended (2025-07-31). Claims joint Amazon rescues 'last year', 'round two this week'. Ballard: flew into "Oipoke" (Oiapoque), then 3 hours by road into the Amazon. | brazil; amazon; collab-tb; title-claim | live |
| PL008 | Instagram | `DY68VeSRWLh` | Sílvia Waiãpi | silviawaiapi (collab: tbfrescue, timballard89) | Tim Ballard (Portuguese dub/interpreter?; check audio) | 2026-05-29 05:52 | 8:43 | Ex agente da CIA- EUA atuou no Brasil no resgate de crianças abusadas sexualmente na amazônia. Em sua missão descobriu a… | Calls Ballard an 'ex agente da CIA' (he was DHS/HSI, not CIA; cf. the LDS Living 'former CIA' item). "trabalhamos com a minha chefe" (we work with my boss) about Silvia. | brazil; amazon; collab-tb; cia-claim | live |

## People
- **Sílvia Waiãpi** (@silviawaiapi): former federal deputy, Amapá (PL), 2023–2025. TRE-AP revoked her mandate on 2024-06-19
  (campaign funds spent on facial harmonization). The PL blocked her 2026 candidacy on 2026-07-21 (Ficha Limpa).
  Dossier: `timbot-network/accounts/silviawaiapi/DOSSIER.md`.
