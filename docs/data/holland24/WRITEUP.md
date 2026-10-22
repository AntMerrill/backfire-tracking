# The first Holland object of order 24: TB × SB, the first 16 co-posts

claude, 2026-10-22 · in-house · nothing pushed or posted
Notation follows the treatise (`automorphism-group.html`, §0–2) and the rooms paper (`rooms.html`, §1–3).

## 0 Notation

The two accounts on every post come first: **p_1 = TB** (timballard89, as throughout the treatise) and **p_2 = SB**
(sandrabronzina). The other 13 are p_3, …, p_15, numbered by first appearance along the chain; within one post the owner comes
first, then the collaborators in alphabetical order. TB and SB are the plain names; the math uses p_1 and p_2.

| symbol | account | first appears |
|---|---|---|
| p_1 (TB) | timballard89 | α_1 |
| p_2 (SB) | sandrabronzina | α_1 (owner) |
| p_3 | liberal.noticias | α_2 (owner) |
| p_4 | julietaagonz | α_2 |
| p_5 | piterpaulin | α_2 |
| p_6 | maaydelara | α_3 (owner) |
| p_7 | tbfrescue | α_8 |
| p_8 | timballardfoundationecuador | α_8 |
| p_9 | larinoar | α_9 (owner) |
| p_10 | expofamily.cl | α_11 (owner) |
| p_11 | dramariajosemancino | α_11 |
| p_12 | margaritarojoc | α_11 |
| p_13 | qntlc | α_11 |
| p_14 | agustinlaje | α_12 |
| p_15 | ivetteavaria | α_16 (owner) |

The other symbols:
- **Chain.** Ω = {α_1 < … < α_16}, the co-posts in time order (rooms paper §1).
- **Blocks.** B_i = B_{α_i} is the set of points on α_i.
- **The structure.** 𝒮_16 = (P, {B_1, …, B_16}), with incidence matrix N (treatise Def. 1.1).
- **Counts.** r_x is the number of blocks on point x; λ_xy is the number of blocks on both x and y.
- **Rooms.** P = P_1 ⊔ … ⊔ P_r, the classes of equal rows of N, called twins in the treatise (rooms paper Def. 2.1).
- **Groups.** Aut_< (rooms paper §3) is the group of order-preserving symmetries. Aut(𝒮_16) (treatise) is the group that ignores order.

## 1 The object

- **Ω.** The co-posts of p_1 and p_2, meaning posts on which both are owner or listed collaborator, in time order,
  2025-11-04 → 2026-10-16. These are the first 16, all from our captures. The 17th, α_17 (Deu_C7mTage, 2026-10-20), came after
  and was fetched by its own link.
- **Incidence.** A point is on α_i if it is the owner or a listed collaborator of α_i. This is the treatise's
  block rule: Instagram leaves the owner off the credit list, so the owner is added.

| block | date (UTC) | points |
|---|---|---|
| B_1 | 2025-11-04 | p_1, p_2 |
| B_2 | 2025-11-21 | p_1, p_2, p_3, p_4, p_5 |
| B_3 | 2026-05-27 | p_1, p_2, p_6 |
| B_4 | 2026-05-27 | p_1, p_2 |
| B_5 | 2026-05-29 | p_1, p_2 |
| B_6 | 2026-05-29 | p_1, p_2 |
| B_7 | 2026-05-29 | p_1, p_2 |
| B_8 | 2026-05-30 | p_1, p_2, p_7, p_8 |
| B_9 | 2026-05-30 | p_1, p_2, p_9 |
| B_10 | 2026-06-02 | p_1, p_2 |
| B_11 | 2026-08-08 | p_1, p_2, p_10, p_11, p_12, p_13 |
| B_12 | 2026-08-19 | p_1, p_2, p_10, p_12, p_13, p_14 |
| B_13 | 2026-08-27 | p_1, p_2, p_10, p_11, p_12 |
| B_14 | 2026-09-15 | p_1, p_2, p_10, p_11 |
| B_15 | 2026-10-05 | p_1, p_2, p_10, p_11, p_13 |
| B_16 | 2026-10-16 | p_1, p_2, p_15 |

- **Size.** v = 15 points, b = 16 blocks, block sizes 2–6.
- **Replication numbers.**
  - r_{p_1} = r_{p_2} = 16
  - r_{p_10} = 5
  - r_{p_11} = 4
  - r_{p_12} = r_{p_13} = 3
  - r = 1 for p_3–p_9, p_14 and p_15
- **Pairs.** 40 of the C(15,2) = 105 pairs have λ_xy > 0.

## 2 Result

**Theorem.** Aut_<(𝒮_16) = Sym{p_1, p_2} × Sym{p_3, p_4, p_5} × Sym{p_7, p_8} ≅ S_2 × S_3 × S_2 ≅ C_2 × C_2 × S_3,
of order **24**.

The rooms of size > 1 are P_1 = {p_1, p_2}, which is on every block; P_2 = {p_3, p_4, p_5}, on B_2 only; and
P_3 = {p_7, p_8}, on B_8 only. The other eight points are singleton rooms. Theorem 3.1 of the rooms paper gives the
product. The isomorphism type can be read off the product, so no Sage run was needed. ∎

This is the **first Holland object of order 24** (John, 2026-10-22). The Parlor Boner's "24" (10-20) does not count.
It came from the distinct-sets reading, on the input that left druze.spirit out. Re-run today with spirit in the room,
the Parlor's Aut_< on its own grid is 6.

## 3 Side readings

- **Ignoring order.** |Aut(𝒮_16)| = 288 = 24 × 12, from the plain-Python `verify_automorphisms.py`, multiset.
  The extra 12 comes from moves that reorder posts in time, so none of them is in Aut_<:
  - Sym{p_6, p_9, p_15} (3! = 6). These are the three one-guest blocks B_3, B_9 and B_16, each p_1, p_2 plus a single
    guest, the treatise's pendant shape.
  - (p_12 p_13), with B_13 ↔ B_15 (2).
- **Adding α_17.** B_17 = {p_1, p_2, p_10, p_11, p_13} = B_15, and it brings no new point. Proposition 4.1 of the rooms paper
  says the rooms can only split. Here none do, so **Aut_< stays 24**. The order-ignoring group drops to 144, because
  r_{p_13} ≠ r_{p_12} now.
- **Which 16.** p_1 is a listed collaborator on 16 of the 17 co-posts. The exception is α_8, which p_1 owns, and
  Instagram leaves an owner off their own credit list. John's object is the **first 16 by time**, not that 16.
- **Retest.** Before this run, `verify_automorphisms.py` gave 12 on the treatise's 𝒮_7 (Who-went-first), as published.

## 4 Files (in `2026-10-22/claude/opie_takeover/first16/`, hashed in `SHA256SUMS`)

- `matrix_first16.csv`: N, 15 × 16. Its rows are handles; §0 is the translation.
- `rooms_first16.txt`: the rooms and the 24
- `verify_first16.out`: |Aut(𝒮_16)| = 288
- `matrix_17.csv` and `verify_17.out`: with α_17
- `cards/…_first16_aut_v3.png`: the results card (headline 24). It still uses plain names; it will move to p-notation if
  it becomes the math version.
- `../gap_classes_17/2026-10-22_tb_sandra_17_coposts_time_order.md`: all 17 posts in time order

## 5 Next: the avatar canvas

Captured avatars on disk: p_1 only (`2026-10-11/left_right_game/av_p1_TB.png`). The other 14 need one capture of
their profile pictures. These are real pictures from the captured profile URLs, never generated. A point whose picture
can't be got is shown as its handle in text.

— claude
