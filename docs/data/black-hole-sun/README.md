# Black hole sun: Latter-Day Avenger's grid with owners (captured 2026-10-17)

`latterdayavenger_timeline_with_owners_2026-10-17.jsonl`: every post Instagram served on @latterdayavenger's grid on
October 17, 2026 (334 posts, from the first, 2025-04-01), oldest first, one JSON object per line, with the post's
**owner** read for every post. Fields: `shortcode`, `taken_at`, `id_time`, `owner`, `collaborators`, `credits`, `date_mismatch`.

Why owners matter: Instagram leaves a post's owner off that post's collaborator list ("the host is never on the guest
list"), so a post another account owns can look like LDA's own. Here: 307 posts are LDA's own; 27 are owned by 20
other accounts, 5 of them timballard89.

Count it: `python3 -c "import json,collections;R=[json.loads(l) for l in open('latterdayavenger_timeline_with_owners_2026-10-17.jsonl')];c=collections.Counter(r['owner'] for r in R);print(len(R),c['latterdayavenger'],len(R)-c['latterdayavenger'],len(c)-1,c['timballard89'])"`
→ `334 307 27 20 5`. Check the files: `sha256sum -c SHA256SUMS`.
