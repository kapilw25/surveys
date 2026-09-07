---
id: zsh-glob-nomatch
tools: Bash
match: \brm\s+-[a-zA-Z]*\b[^|;&]*\s\*\.[A-Za-z]
severity: warn
---
# zsh aborts the whole command on an unmatched glob
Problem: in zsh a glob with no match (e.g. `*.bcf`) makes the ENTIRE command fail with "no matches found" BEFORE it runs, so a mixed `rm -f a b *.bcf` deletes NOTHING when `*.bcf` has no match. This session leaked ~15MB of build artifacts (main.pdf/aux/log) into an arXiv zip exactly that way.
Fix: never mix explicit filenames with a may-not-match glob in one destructive command. Delete explicit files by name in one command, globs separately with the null-glob qualifier (`rm -f *.bcf(N)`), or `setopt nonomatch`. Always verify with a file/byte count afterwards.
