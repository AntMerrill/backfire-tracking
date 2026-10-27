# same-reel: Tim Ballard's Facebook reel vs @mariofriasoficial's Instagram reel

Data behind ../../same-reel.html (2026-10-27).

## Sources (public posts)
- Instagram reel by @mariofriasoficial: https://www.instagram.com/reel/De6mHwFRbAG/ , posted 2026-10-25 11:26:35 UTC
  (post time from Instagram's own feed data; the time encoded in the post id is 60 s earlier).
- Facebook reel by Tim Ballard: https://www.facebook.com/reel/1140352768334907/ , 51.6 s (we downloaded it 2026-10-26/27).

The videos are not in this repo (text only). Downloaded with dl_wm's dllink (yt-dlp). sha256 of the files compared:
- Facebook  c71cfe8063cf8c83731ad787c3e0c8a7bb7702e0675163d6b3a307261059cf06
- Instagram c8e2c675081e0bc814596d5620e05a61812b41b1642333c906d52d7d299cf513
Anyone can re-download both and compare; a re-encode by the platform can change the hash but not the frame comparison.

## Files
- frame_diff.csv: every 1/25 s, mean absolute difference between the two videos' frames (90x160 grayscale, left 2/3 of
  the frame so Instagram's share stamp is ignored), 0-255 scale. differs = 1 when > 20.
- spans.csv: runs of differing frames, plus the part of the Facebook reel after the Instagram reel ends.
- scenes.csv: scene cuts found in each video by dl_wm pipeline2 (scene_split.py), 0.2 s steps.
- check_frames.py: recomputes frame_diff.csv and spans.csv from the two downloads. Needs ffmpeg + Pillow.

## Result
1,190 frames compared (the Instagram reel's full 47.6 s). 1,145 frames match (difference at most 2.5); 45 frames differ
(difference at least 56.1), in two runs: 17.92-18.80 s and 30.68-31.60 s. The Facebook reel then runs 4.0 s longer
(47.6-51.6 s): an end card. Nothing else differs, and nothing is shifted in time.

## Limits
- The comparison covers picture only. Audio was not compared sample by sample; both carry the same song by ear and the
  Facebook frames show Instagram's audio label "SIL · Capitão Levanta-Te".
- It shows that the Facebook reel is this Instagram reel with additions. It does not show who made the additions.
