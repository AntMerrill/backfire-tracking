# Data: the group's posts as a four-part choir

The data behind https://antmerrill.github.io/backfire-tracking/group-choir.html (October 18, 2026).

The group is the 14 accounts of "Who went first": latterdayavenger (LDA), latterdaychad (LDC), timballard89 (TB) and the eleven
smaller accounts lettered A-K there (same letters). The key from letters to accounts is not published.

**One note per post with 2 or more of the 14 on it** (758 posts, March 2024 to October 2026), from our captures of the group's own
Instagram grids. Co-present = owner or collaborator on the post, or the post is on that account's grid. Caption tags not counted.

| File | What it is |
|---|---|
| `group_choir_notes.csv` | The 758 notes: date, post link, the voices (letters), how many, which part and pitch |
| `group_choir_rests.csv` | Every rest of 7+ days with no group post (14; two after 2024: Sep 11-19, 2025 and Jan 17-24, 2026) |
| `2026-10-18_group_choir_score.mp4` | The score video: four staves, notes scroll past a playhead, rests shaded |
| `tb_group_choir_video.py` | Makes the sound (and a circular version of the picture) from the captures |
| `tb_group_choir_score.py` | Draws the four-part score and joins it to the sound |
| `SHA256SUMS` | Every file above |

Parts: Bass = 2 voices (one note, C2), Tenor = 3 (E4), Alto = 4 (A4), Soprano = 5 (D5) or 6 (G5). Same instrument and tempo as the
TB collab music (16.6 days a second), so a rest sounds as long as it lasted. The scripts read our local captures and an in-house
letter key; the notes file above is what they read, in published form.
