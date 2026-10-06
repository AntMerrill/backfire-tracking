# Data: "Sun, Moon and Starlink"

The data behind https://antmerrill.github.io/backfire-tracking/sun-moon-starlink.html (October 6, 2026).

| File | What it is |
|---|---|
| `posts.csv` | The 492 posts: every Instagram post in our captures where timballard89 shares the credit with at least one other account, with the accounts on it |
| `accounts.csv` | The 172 accounts: fixed point or interchangeable, which orbit, orbit size, how many of the 492 posts it is on |

## Notation
- Named: timballard89, timballardfoundationecuador, tbfrescue, hiddenwarmovie, latterdaychad. Every other account is an ID:
  **F001…F068** = the other fixed points (one-of-a-kind accounts), numbered by how many posts they're on;
  **S001…S099** = interchangeable accounts, grouped into orbits **O01…O28** (largest first).
- A post's accounts = everyone credited on it, plus the account whose grid it came from (Instagram leaves the poster out of the credit list).
- **Fixed point**: an account no relabelling can move without changing the record. **Orbit**: a set of accounts that can be
  relabelled among themselves with nothing changing. Same idea as the seven-post analysis in `../who-went-first/README.md`.

## How it was made
- Posts: the Ballard-tied list from our captures (`ig_tagged_posts.py`, 566 posts), keeping the 492 where Ballard and at least one other
  account are on the same post (74 that only mention him in the caption were left out).
- Math: SageMath 10.9, `IncidenceStructure(blocks).automorphism_group()`, then `.orbits()`.
  Result: 73 fixed points; 99 accounts in 28 orbits (sizes 14, 11, 9, 8, 4, 4, 4, 3, 3, 3 and eighteen pairs); group order about 3.3 × 10^30.
- Cross-check: the three accounts called H, I, J in the seven-post analysis form their own orbit here too,
  found without being told.

## Limits
Only the posts in our captures (Ballard's own grid back to Sept 11, 2025; some accounts capped). "Interchangeable" means the same footprint
in this data, not the same operator. Not yet peer reviewed; corrections welcome.
