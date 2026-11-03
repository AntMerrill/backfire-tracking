# Dark Horse Caucus on Insta — how the list is made, and how to make it yourself

The list: `contributors.txt` (27 Instagram handles, `@` in front, ready to paste) and `contributors.csv`
(the same, with each account's first post, its date, how many of the 22 posts it is on, and how many it owns).

## What the list is

Every Instagram account that shared a post with **timballard89** between **May 1 and June 30, 2025** (UTC), as
owner or listed collaborator. There are 22 such posts and 28 accounts on them; timballard89 is on all 22 and is left
out of the list, which leaves 27. We call these accounts and two months the "Dark Horse Caucus"; that name is our label,
not something written on the posts.

## The rule, step by step

1. **Co-post.** An Instagram post whose header credits two or more accounts: the owner plus the collaborators shown
   next to the owner's name ("X and Y"). Accounts @-tagged in a caption or photo do **not** count.
2. **The 22.** Every co-post that has timballard89 among its accounts and was posted May 1 – June 30, 2025 (UTC).
   One row each in `posts.csv`, in posting order, numbered B1–B22, with the link, time, owner and collaborators.
3. **The accounts on a post** = its owner + its listed collaborators.
4. **Contributors** = every account on any of the 22, except timballard89.
5. **Order** = the first of the 22 posts an account appears on; accounts first seen on the same post are alphabetical.

`build_list.py` is that rule as code (Python 3, standard library only):

```
python3 build_list.py --check   # rebuilds the list from posts.csv and compares: "contributors.txt OK; contributors.csv OK; 27 contributors"
python3 build_list.py           # writes contributors.txt and contributors.csv from posts.csv
```

## Rebuilding posts.csv yourself, from Instagram

You don't need our files to check this. Open each link in `posts.csv` and read the post header: the owner, the
collaborators beside the owner's name, and the date. Or start from scratch:

1. Open `https://www.instagram.com/timballard89/` (logged in). Posts where he is a collaborator show on his grid too.
2. Scroll back to June 2025 and open every post from June 30 back to May 1, 2025.
3. Write down each post whose header shows more than one account: shortcode (the part after `/p/`), date, owner,
   collaborators. Ignore single-account posts.
4. Put them in `posts.csv` (same columns) and run `python3 build_list.py`.

What we did: we saved timballard89's grid on **2026-10-17** with a logged-in browser, reading Instagram's own post
data (owner, collaborator list, posting time) for each post; nothing was typed by hand. From that capture we kept the
22 posts the rule picks out. Each post's credits were the same in every capture we hold of it.

## Limits

- **As of the capture date.** Owners can delete posts or remove collaborators later; Instagram can also hide posts
  from some viewers. If you rebuild from Instagram today and get a different list, the posts changed or our capture
  missed one: please tell us which.
- **Only what Instagram shows as a co-post.** Partners who were tagged, thanked, or appear in the picture without a
  collaborator credit are not in the list.
- **Times are UTC.** A post made late on June 30 in the Americas can fall on July 1 UTC, and the reverse on May 1.
- The list says who shared posts with timballard89 in those two months. It says nothing about what any account
  thinks, knows, or did off Instagram.

## Files

| file | what |
|---|---|
| `posts.csv` | the 22 posts: B-number, shortcode, link, posting time UTC, owner, collaborators |
| `contributors.txt` | the 27 handles, in order, `@` in front |
| `contributors.csv` | the same with first post, its time, posts, owns |
| `build_list.py` | the rule as code; `--check` re-derives both lists from `posts.csv` |
| `SHA256SUMS` | hashes of the files above (`sha256sum -c SHA256SUMS`) |

Backfire Tracking, 2026-11-02.
