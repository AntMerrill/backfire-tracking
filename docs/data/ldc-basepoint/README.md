# ldc-basepoint: latterdaychad's car video on Tim Ballard's Facebook

Data behind ../../ldc-basepoint.html (2026-10-29).

## Sources (public posts)
- Instagram, latterdaychad: https://www.instagram.com/p/Decca9IB4mM/ , 2026-10-13 18:24:29 UTC, 32.55 s.
- Facebook, Tim Ballard (officialtimballard): https://www.facebook.com/reel/1653357746398669/ , 2026-10-14 07:23:08 UTC, 69.03 s.

The videos are not in this repo (text only). sha256 of the files compared:
- Instagram e6c12c26a3e8998ab92d08bdc4d477447b52e1c2461d49a33ab757b30882e642
- Facebook  c3717ce1c47672175ea1374387c8d09088f844a35b18ae92b953f65a0cb6d03e

## Method
`../same-reel/check_frames.py`, unchanged: every 1/25 s, 90x160 grayscale, left 2/3 of the frame (Instagram's share stamp ignored),
mean absolute difference 0-255; a frame differs when it is over 20.

## Files
- frame_diff.csv: the b0 comparison, frame by frame. spans.csv: the differing run and the Facebook-only tail.
- elements.tsv: every pair in the multiset M (b0, Tim Ballard's six own cross-posts, the Mario Frias control), with times, gaps, file hashes.
- multiset.tsv: M by source account. frame_checks.tsv: the frame check for each pair.

## Result
812 frames compared; 811 the same (2.7-5.8); 1 differs (76.2), the Instagram video's last frame at 32.44 s. The Facebook reel then
runs 36.56 s longer: more footage of the damaged car with a GoFundMe link on screen (checked by eye at 33-66 s; the work-up's
"screen recording of the GoFundMe page" was an OCR guess and is corrected here). |M| = 8 over 3 accounts.

## Limits
- Only Facebook reels held as video could be compared; most of the 57 Facebook posts captured on 2026-10-29 are metadata only.
- The record shows which video went where and when, not who uploaded it.
