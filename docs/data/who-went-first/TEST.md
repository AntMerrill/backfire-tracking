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
   - https://www.instagram.com/p/DXQTcYlgZ5c/
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
- Posts that were deleted or had credits removed before you looked. We captured them Oct 1–5, 2026.

## Our own runs
| Date | Who | How | Result |
|---|---|---|---|
| 2026-10-05 | us | Instagram's own post data (our captures) | 12, orbits as above |
| 2026-10-11 | us | re-downloaded the posts through our pipeline after a storage failure | 6 of 7 re-downloaded (B1–B6), uploader latterdayavenger and dates confirmed; files + hashes in `evidence/`. B7 refused by Instagram that day (HTTP 400 during a rate limit), pending |
