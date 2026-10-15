# Test it yourself: do the 7 posts really have this shape?

The page claims that 7 Instagram posts, uploaded by latterdayavenger between Feb 18 and Apr 18, 2026, credit 13 accounts in a pattern whose symmetry group has **order 12**:
- timballard89 and latterdaychad are interchangeable;
- three one-time accounts are interchangeable;
- every other account is unique.

The README's "Check the math" section tests the arithmetic on **our** matrix.
This test checks the **data**: you collect the credits yourself, straight from Instagram, and see whether you get the same answer.
You don't need our letters A–K. The symmetry count doesn't depend on what you call the accounts.

## What you need
- A web browser. Some posts may need you to be logged in to Instagram.
- Python 3 (free), and the two scripts in this folder: `build_matrix.py` and `verify_automorphisms.py`.

## Steps

1. **Open each of the 7 posts.** The links are in `group_posts.csv`:
   - https://www.instagram.com/p/DU5tCKGAQDQ/
   - https://www.instagram.com/p/DU_DpXzgafm/
   - https://www.instagram.com/p/DVC61j0gVvk/
   - https://www.instagram.com/p/DVMDNEjgf3v/
   - https://www.instagram.com/p/DWhOINgDwip/
   - https://www.instagram.com/p/DW99EnrgVYo/
   - https://www.instagram.com/p/DXQTcYlgZ5c/ — **deleted**; see "B7 has been deleted" below.
2. **For each post, write down:**
   - who uploaded it (the first name in the header);
   - every account in its Collaborators list. On the web, click the "and N others" part of the header to see the full list.
3. **Put the credits in a file** called `my_posts.csv`:

       shortcode,credited
       DU5tCKGAQDQ,accountone accounttwo ...

   Use one line per post. Leave the uploader out, as Instagram does.
4. **Run:**

       python3 build_matrix.py my_posts.csv
       python3 verify_automorphisms.py my_incidence_matrix.csv

## B7 has been deleted

The seventh post, `https://www.instagram.com/p/DXQTcYlgZ5c/` (posted 2026-04-18),
was deleted from Instagram between **Oct 5 and Oct 13, 2026**. You will not be able
to open it. The full record of what we hold and what we lost is in
[`evidence/B7_DELETED.md`](evidence/B7_DELETED.md).

Do the test with the **6 posts you can still open**. Leave B7 out of `my_posts.csv`.
You will not get 12 — you will get the number below, and matching it is the point.

### Pass / fail, 6 posts

| Check | Expected |
|---|---|
| Uploader of all 6 posts | latterdayavenger |
| Accounts credited per post | 5 on every post |
| Different accounts in total | **12** (B7's three one-time accounts are absent) |
| On all 6 posts | exactly 2: timballard89 and latterdaychad |
| Pairs that ever share a post | **35 of 66** |
| \|Aut(N)\| printed by the script | **24** |
| Orbits | {timballard89, latterdaychad}, a trio of one-time accounts, **a pair of one-time accounts**, and 6 accounts alone |

If you get 24, you have independently confirmed that **B7 is load-bearing**: one
deleted post is worth a factor of 2, and its row in the matrix cannot be invented
quietly, because removing it visibly changes the answer. With all 7 posts the number
is 12.

### Why this still counts as a test

B7's media is gone, so its credits cannot be re-collected. Everything else about it
can: the post existed (we downloaded it twice on Oct 5, 2026), it was uploaded by
`latterdayavenger`, and its record is preserved hashed and dated in `evidence/`. The
structure's headline claim — order 12, not 24 — rests on that one post, and this page
says so rather than leaving you to find the hole.

## Pass / fail

The test **passes** if all of these hold:

| Check | Expected |
|---|---|
| Uploader of all 7 posts | latterdayavenger |
| Accounts credited per post | 5 on every post |
| Different accounts in total | 13 |
| On all 7 posts | exactly 2: timballard89 and latterdaychad |
| Pairs that ever share a post | 40 of 78 |
| \|Aut(N)\| printed by the script | **12** |
| Orbits | {timballard89, latterdaychad}, one trio of accounts that appear only on the same single post, and 8 accounts alone |

It **fails** if any of these differ.
If yours differs, check first whether a post has been edited, deleted or made private since Oct 5, 2026. Note the date you looked.
Tell us either way. A failure is as useful as a pass.

## What the test can't show
- Who runs any of these accounts, or why they post together.
- B7's credits. We captured them Oct 1–5, 2026, but the response that recorded them
  was not retained, and the post has since been deleted. B7's row is single-sourced.
  Everything else about B7 — that it existed, who uploaded it, that it carried five
  credits — is supported by the dated records in `evidence/`.

## Our own runs
| Date | Who | How | Result |
|---|---|---|---|
| 2026-10-05 | us | Instagram's own post data (our captures) | 12, orbits as above |
| 2026-10-11 | us | re-downloaded the posts through our pipeline after a storage failure | 6 of 7 re-downloaded (B1–B6), uploader latterdayavenger and dates confirmed; files + hashes in `evidence/`. B7 refused by Instagram that day (HTTP 400) — see below |
| 2026-10-13 | us | captured `latterdayavenger`'s own profile timeline (354 posts, back to 2025-04-01) | B7 absent; its neighbours Apr 16 and Apr 20 both present, so the capture is not truncated there. B7 already deleted by this date |
| 2026-10-15 | us | confirmed B7 deleted: HTTP 200, empty shell, **no `og:` tags** — Instagram does not 404 a deleted post, and a live post always serves `og:image`. No Internet Archive snapshot exists. Signed CDN URLs have expired (403) | deletion window pinned to **Oct 5–13, 2026** |
| 2026-10-15 | us | re-ran this test on our own matrix, B7 dropped | 12 accounts, 35/66 pairs, **\|Aut\| = 24**, orbits as in the 6-post table above |
