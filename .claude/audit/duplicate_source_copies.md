---
id: duplicate-source-copies
tools: Bash, Edit, Write
match: (?i)cp\s+-[a-z]*r[a-z]*\b[^|;&]*\b(main\.tex|refs\.bib|overleaf_upload|p3_do_world_models)\b|rsync\s+-[a-z]*r[a-z]*\b[^|;&]*\b(figures|sections|tables)\b
severity: warn
---
# One canonical source, no parallel copies
Problem: cloning a paper's source into a second tree (a loose-root copy, an `overleaf_upload/`, a per-target export dir) means every future edit must be repeated N times and the copies silently drift -- a fix lands in one while a stale figure ships from another. This repo had 3 near-identical P3 copies, so one edit had to be made 3x.
Fix: keep ONE canonical source dir and GENERATE exports (arXiv zip, Overleaf upload) from it on demand; never hand-maintain a second tree. Edit P3 only in `overleaf_draft/p3_action_bench/p3_do_world_models/`. If you must copy, add it to the build script, not the repo.
