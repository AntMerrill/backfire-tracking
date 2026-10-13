# Second source: phone screenshots (held locally)

John took screenshots on his iPhone of latterdayavenger's posts with their Collaborators list open, Oct 12, 2026, 21:54 to Oct 13, 2026, 09:58 (the phone's own
timestamps, Pacific time). We hold 53 of them. The images are not published (they show smaller accounts' names and can show our
own viewing account), but their
SHA-256 fingerprints are, in `screenshots_SHA256SUMS`. Anyone we later show a screenshot to can hash it and check it is the
same file, unchanged. Each line also gives the time the phone recorded for that screenshot.

How they were read: text by OCR (dl_wm `bin/ocr_screenshots.py`, Tesseract 5.5.0, defaults), then each Collaborators panel
split into rows (account, display name) by a script with fixed rules. Rules that changed a name are listed per row.

`screenshot_check.csv`: one row per panel row, 169 rows from the 30 panels that are on LDA's posts.
Accounts as on the page (LDA, LDC, TB named; sNNN labels). `on_lda_grid` = the account is one of the 113 on LDA's grid in our capture.

Result: 161 rows were read as is; 160 of them are accounts on LDA's grid, and the 1 other is an OCR slip of an
account that is on it. 8 rows needed a fixed rule (name cut off on screen, "_" read as a space, I for l); all land on
accounts on the grid. The screenshots show 51 of the grid's 113 accounts.

Limit: a screenshot shows a panel, not the post's link, so this checks accounts, not post by post.
