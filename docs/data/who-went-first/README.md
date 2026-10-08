# Data: "Who went first"

The data behind https://antmerrill.github.io/backfire-tracking/who-went-first.html (October 5, 2026).

Smaller accounts are letters A-K, as on the page. Named: timballard89 (TB), latterdaychad (LDC) and the
host account latterdayavenger. The key from letters to accounts, the raw captures and the captions are not published.

| File | What it is |
|---|---|
| `group_posts.csv` | The 7 group posts, Feb 18 - Apr 18, 2026: link, time (UTC), who uploaded it, who was credited |
| `incidence_matrix.csv` | The matrix N: accounts x posts, 1 = credited on that post |
| `pair_counts_before_after.csv` | Every pair of the 13 accounts that ever shared a post: shared posts before Feb 18, 2026 and from Feb 18 on, first shared date |
| `ldc_posts_tied_to_ballard.csv` | Every Latter Day Chad post in our captures tied to Ballard: it credits timballard89, or it also appears in timballard89's grid |
| `transcript_word_counts.txt` | Word counts from the 7 joint videos with speech, common words removed |
| `2026-10-05_DSghot5ET_3_screenshot_cropped.jpg` | The December 20, 2025 post as Instagram showed it on Oct 5, 2026 (cropped; mouse pointer removed) |

## Notation

**Accounts**

| Symbol | Meaning |
|---|---|
| TB | timballard89 (Tim Ballard) |
| LDC | latterdaychad (Latter Day Chad) |
| A-K | the 11 smaller accounts credited on the group posts, lettered in order of first appearance (Feb 18 post: A, B, C; then D, E, ...). Same letter = same account, on the page, the cards and in these files |
| host | latterdayavenger, the account that uploaded all 7 group posts. Not one of the 13, and not counted in the matrix |

**Posts and time**

| Term | Meaning |
|---|---|
| group post | one of the 7 posts uploaded by the host, Feb 18 - Apr 18, 2026, each crediting 5 accounts |
| credited | listed in the post's Collaborators list. Instagram leaves the uploader out of that list |
| tied (to Ballard) | the post credits timballard89, or the same post appears in timballard89's grid |
| before / from Feb 18 | split at the first group post, DU5tCKGAQDQ, 2026-02-18 13:53:35 UTC |
| dates | stored in UTC; Instagram shows the viewer's local date, which can be a day earlier |

**The math** (design theory; plain-text forms in brackets)

| Symbol | Meaning |
|---|---|
| point | an account (13 of them) |
| block | a group post, as the set of 5 accounts credited on it (7 blocks) |
| N | the incidence matrix, 13 x 7: N[p][b] = 1 if account p is credited on post b, else 0 (`incidence_matrix.csv`) |
| r_p | the number of posts account p is on: the row sum of N |
| λ_pq (lambda) | the number of posts accounts p and q share (the "pair multiplicity" of design theory; nothing to do with lambda calculus) |
| N·Nᵀ (N N^T) | the 13 x 13 matrix of pair counts: λ_pq off the diagonal, r_p on it |
| 𝟙_B (1_B) | the 0/1 column for block B. N·Nᵀ = Σ_B 𝟙_B 𝟙_Bᵀ: each post adds 1 to every pair inside it |
| K₅ (K5) | a complete set of pairs on 5 accounts: 10 pairs. One group post makes one K₅ |
| derived triples | each post with TB and LDC removed: 3 accounts left. The 7 triples: ABC, ACD, AED, ABD, FBG, HIJ, KGD |
| Aut(N) | the automorphism group: every relabelling of the 13 accounts that carries the set of 7 blocks onto itself |
| orbit | accounts that some automorphism swaps with each other: interchangeable as far as these 7 posts show |
| fixed point | an account no automorphism moves: its pattern across the posts is unique |
| S₂ × S₃ (S2 x S3) | the group of all swaps of 2 things combined with all rearrangements of 3 things; order 2 x 6 = 12 |
| balanced design | every account on the same number of posts (constant r) and every pair meeting equally often (constant λ). This one is far from balanced |

**Line and colour bands** (maps and pair grid on the page): 1 / 2-4 / 5-19 / 20-99 / 100+ shared posts on the
maps; 1 / 2 / 3-4 / all 7 on the pair grid. Faint to strong on one blue hue.

## How it was made
- Post data: Instagram's own post records for each account's grid, captured Oct 1, Oct 4 and Oct 5, 2026.
  Latter Day Chad: two captures merged, 1,888 posts back to June 20, 2024. Ballard: back to Sept 11, 2025.
- A post ties two accounts if either credits the other, or the same post appears in both grids. Instagram's
  collaborator list leaves out the account that posted it, which is how we missed Dec 20 on Oct 4.
- "Uploaded by" comes from the downloaded posts' own metadata.
- Times are UTC. Instagram shows local dates, so DSghot5ET_3 (02:12 UTC Dec 21) shows as December 20, 2025.

## Check the math
Everything on the page's algebra section can be recomputed from `incidence_matrix.csv`. Our result:
|Aut(N)| = 12, orbits {TB, LDC} and {H, I, J}, every other account fixed. The math on the page has not
been peer reviewed. Corrections welcome.

### Prediction (made October 5, 2026), now confirmed in Sage
# Type into SageMath (free, https://www.sagemath.org), with the seven posts from `group_posts.csv`:

    B = [["TB","LDC","A","B","C"], ["TB","LDC","A","C","D"], ["TB","LDC","A","E","D"],
         ["TB","LDC","A","B","D"], ["TB","LDC","F","B","G"], ["TB","LDC","H","I","J"],
         ["TB","LDC","K","G","D"]]
    D = IncidenceStructure(B)
    G = D.automorphism_group()
    G.order(), G.orbits()

We predict Sage prints **12** for the order, and orbits **[TB, LDC]** and **[H, I, J]**, with each of
A, B, C, D, E, F, G and K alone in its own orbit. GAP or nauty, run on the account-post incidence graph,
should give the same group. If anyone gets a different answer, tell us.

**Result:** confirmed October 5, 2026 in SageMath 10.9, which printed
`12 (('F',), ('C',), ('A',), ('G',), ('H', 'I', 'J'), ('K',), ('LDC', 'TB'), ('E',), ('B',), ('D',))`.
The same result came from networkx 3.4.2 and from our own count. Our first version of the snippet
used `designs.IncidenceStructure`, which Sage 10.9 does not have; it is corrected above.
Software agreeing is not peer review: the reading of what the symmetry means is still ours to defend.

### Three ways it was checked (all agree)

1. **Our own count, plain Python, no packages:** `verify_automorphisms.py` in this folder.

       python3 verify_automorphisms.py incidence_matrix.csv

   It prints r for every account, the number of pairs that ever meet (40 of 78), |Aut(N)| = 12, and the orbits.
   How it works: it builds each relabelling σ one account at a time (backtracking). Two numbers every symmetry
   must keep the same prune the search:
   - **r:** σ(p) must be on as many posts as p;
   - **λ:** for every account x already placed, λ(p, x) = λ(σ(p), σ(x)).

   Pruning only throws candidates away. Each complete σ is then tested directly: the 7 blocks, relabelled, must be
   exactly the 7 blocks again. So the count is exact, not an estimate.
2. **networkx 3.4.2 (a free graph library):** turn the design into its incidence graph (13 account nodes, 7 post
   nodes, an edge when an account is on a post) and count the graph's symmetries that keep accounts on the account
   side. They are exactly Aut(N).
3. **SageMath 10.9:** the snippet above.

**About the λ.** λ here is design theory's standard letter for how many blocks contain a given pair. It comes from
"2-(v, k, λ) designs", where every pair meets exactly λ times. The other standard letters are v = 13 accounts,
b = 7 posts, k = 5 per post and r = posts per account. It is **not** the λ of lambda calculus (Church's notation for
functions). The script calls it `lam` because `lambda` is a reserved word in Python, which borrowed it from lambda
calculus.

**Why 12.** TB and LDC are on all 7 posts, so they can swap: S₂. H, I and J are each on exactly one post, the same
one, so they can be put in any order: S₃. Every other account's row of N is unique, so it stays put.
Aut(N) ≅ S₂ × S₃, which has order 2 × 6 = 12 (the same group as D₆, the symmetries of a hexagon).

"Watch Buttfire"
