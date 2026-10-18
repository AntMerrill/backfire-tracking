# Data: every @timballard89 Instagram collab, in time order

The data behind https://antmerrill.github.io/backfire-tracking/tb-collabs.html (October 18, 2026).

**What a collab is here:** an Instagram co-author post: the owner plus its listed collaborators. Caption tags are not collabs and
are not counted. A TB collab post has @timballard89 and at least one other account on it.

**Why the owner matters:** Instagram leaves a post's owner off that post's own collaborator list. A post another account owns, with
TB as its only listed collaborator, looks like a solo TB post unless the owner is read too. Our older tables missed those (618 posts,
295 accounts). With the owner on every post: **1,004 collab posts, 423 accounts, 709 of the posts owned by the other account.**

| File | What it is |
|---|---|
| `timballard89_timeline_with_owners_2026-10-17.jsonl` | TB's whole Instagram grid as captured Oct 17, 2026: 3,684 posts (the profile said 3,732), Oct 2016 to Oct 2026. Fields: shortcode, taken_at, id_time, owner, collaborators, credits (caption @-tags), date_mismatch |
| `tb_collab_posts.csv` | The 1,004 collab posts, oldest first: date, link, owner, the other accounts on it |
| `tb_collab_accounts.csv` | The 423 accounts in order of their first collab with TB: first post, owner or collaborator on it, posts with TB, how many they own, last |
| `replicate.py` | Rebuilds both tables from the jsonl and checks them. Prints REPLICATED. Plain Python 3, no packages |
| `*_plain.png`, `*_spicy_stamped.png` | The cards: month by month, top 20 partners, one co-presence graph per year (2022-2026) |
| `2026-10-18_tb_collabs_sound.mp4` | One piano note per collab post (pitch = accounts on the post), dots light up as they sound; Apr 2022 to Oct 2026 in 100 s |
| `page_walker.js`, `decode_pages.py` | How the grid was captured (in a logged-in browser, one page of 12 posts at a time) and decoded |
| `tb_collab_cards.py`, `tb_copresence_year.py`, `tb_collab_sound_video.py` | The scripts that drew the cards and made the video (as run; they read local paths) |
| `SHA256SUMS` | Every file above |

Coverage: 3,684 of 3,732 posts. A live site gives a slightly different set each time; the raw file, the code and the hashes are here so
anyone can rerun it.
