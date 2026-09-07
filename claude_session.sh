#!/bin/bash
: '
=============================================================================
claude_session.sh - session relocation + repo verification for the surveys repo
=============================================================================

Repo:   https://github.com/kapilw25/surveys.git
Scope:  MAC ONLY. There is no GPU half, no SSH, and no destructive git command
        anywhere in this script. It cannot delete a file it did not back up.

THE PROBLEM THIS SOLVES
=======================
Claude Code stores every session under a folder named after the ABSOLUTE path
of the project, with each non-alphanumeric character replaced by "-":

    /Users/kapilwanaskar/Downloads/research_projects/surveys
      ->  ~/.claude/projects/-Users-kapilwanaskar-Downloads-research-projects-surveys

Rename or move the repo and that slug changes, so "claude --resume" no longer
sees any of the old transcripts. They are not lost, just filed under the old
slug. Worse, absolute paths are also embedded INSIDE the transcripts and inside
a few repo files, so a plain folder rename leaves stale paths behind.

This script fixes both halves:
  1. transcripts: rewrite the embedded paths, then fast-forward-merge the old
     slug directory into the new one.
  2. repo files: rewrite any absolute path still pointing at the old location
     (for example .claude/audit/audit_ledger.jsonl).

SAFETY MODEL - FAST-FORWARD ONLY, COMPARED IN CANONICAL SPACE
=============================================================
Session JSONLs are append-only, so a merge is safe exactly when the destination
is a byte-for-byte PREFIX of the incoming file, the same test git uses for a
fast-forward push.

That comparison must NOT run on raw bytes. A transcript can literally MENTION
the other path (a conversation about this very rename does). Rewriting changes
those mentions too, so an otherwise untouched file comes back looking modified,
a false "diverged" that would block the merge.

Every comparison therefore runs in CANONICAL space: both the old and the new
repo path collapse to one neutral token before comparing, which makes the test
invariant to whichever direction the file was last rewritten.

  - destination missing            ->  copy
  - canonically identical          ->  skip
  - destination is a canon prefix  ->  fast-forward (old copy saved to backups)
  - anything else                  ->  DIVERGED: destination kept, loud warning

Destination-only files are never deleted. The old slug directory is never
deleted either, so it remains a complete backup.

USAGE
=====
    bash claude_session.sh --relocate <old_absolute_path>
        # The repo was renamed or moved on this Mac, so its slug changed.
        # MAC_REPO auto-derives from the folder THIS script sits in, so the new
        # path is simply wherever it now lives and needs no edit here.
        #
        #   mv .../survery_paper/robot_skills  .../surveys
        #   cd  .../surveys
        #   bash claude_session.sh --relocate \
        #        /Users/kapilwanaskar/Downloads/research_projects/surveys
        #   claude --resume

    bash claude_session.sh --verify-repo [--deep]
        # Read only. No writes, no network mutation. Reports every discrepancy
        # between the working tree and origin/main, flags a misconfigured
        # remote, and lists untracked files that a stray "git clean -fd" would
        # destroy. --deep also runs git fsck --connectivity-only.

    --dry-run   Show every decision, change nothing.
    --force     On divergence, take the incoming copy (old copy is backed up).

NOTES
=====
    - Overwritten files are kept under ~/.claude_session_backups/
    - git_push.sh pushes to an EXPLICIT url and never updates the "origin"
      remote, so "origin" can drift and point at an unrelated repository.
      --verify-repo detects that and prints the one-line fix.
    - This script deliberately has no "git reset --hard" and no "git clean".
      Syncing the repo is what git_push.sh and plain git are for.

=============================================================================
'

set -euo pipefail

# === Configurable ===
# MAC_REPO auto-derives from THIS script own folder, so renaming or moving the
# repo needs NO edit here. After a rename, migrate the sessions with:
#     bash claude_session.sh --relocate <old_absolute_path>
MAC_REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
GIT_BRANCH="main"
EXPECTED_REMOTE="https://github.com/kapilw25/surveys.git"

# Gitignored ON PURPOSE: per-user runtime state and large regenerated artifacts.
# --verify-repo lists these separately so their absence never reads as a failure.
LOCAL_ONLY=(
    ".env"
    ".claude/state"
    ".claude/settings.local.json"
    "overleaf_draft/p1_weights_or_skills/weights_or_skills_arxiv.zip"
)

# Never rewritten and never scanned during --relocate.
PRUNE_DIRS=(".git" "node_modules")

# === Args ===
MODE=""
DRY_RUN=0
FORCE=0
DEEP=0
OLD_REPO=""

usage() {
    echo "Usage: bash claude_session.sh --relocate <old_path> | --verify-repo [options]"
    echo "  options: --dry-run  --force  --deep"
    echo "  e.g. bash claude_session.sh --relocate /Users/you/old/path"
}

while [ $# -gt 0 ]; do
    case "$1" in
        --verify-repo) MODE="$1" ;;
        --relocate)
            shift
            [ $# -gt 0 ] || { echo "Error: --relocate requires the OLD absolute repo path"; usage; exit 1; }
            MODE="--relocate"; OLD_REPO="$1" ;;
        --dry-run) DRY_RUN=1 ;;
        --force)   FORCE=1 ;;
        --deep)    DEEP=1 ;;
        -h|--help) usage; exit 0 ;;
        *) echo "Unknown arg: $1"; usage; exit 1 ;;
    esac
    shift
done

[ -n "$MODE" ] || { echo "Error: a mode is required"; usage; exit 1; }

# === Derived ===
# Claude Code slug rule: every non-alphanumeric character becomes "-".
slug() { printf '%s' "$1" | sed 's#[^A-Za-z0-9]#-#g'; }

MAC_SLUG="$(slug "$MAC_REPO")"
MAC_SESSIONS="$HOME/.claude/projects/$MAC_SLUG"   # the LIVE dir claude --resume reads

BACKUP_ROOT="$HOME/.claude_session_backups"
STAGE="$BACKUP_ROOT/.stage"                       # transient, path-rewritten tree
REPO_BACKUP="$BACKUP_ROOT/repo_paths/$(date +%Y%m%d-%H%M%S)"

if [ "$(uname)" != "Darwin" ]; then
    echo "Warning: this script is meant to run on the Mac, not on $(uname). Continuing anyway."
fi

# =============================================================================
# Session helpers
# =============================================================================

fsize() { wc -c < "$1" | tr -d ' '; }

# canon <file> - emit the file with BOTH repo paths collapsed to one neutral
# token. All merge comparisons happen in this space, so a path rewrite (or a
# transcript that literally mentions the other path) can never look like
# divergence. The length guards matter: an empty pattern would match the empty
# string at every position and destroy the file.
canon() {
    CN_A="$MAC_REPO" CN_B="${OLD_REPO:-}" LC_ALL=C perl -pe '
        s!\Q$ENV{CN_A}\E!\x01REPO\x01!g if length $ENV{CN_A};
        s!\Q$ENV{CN_B}\E!\x01REPO\x01!g if length $ENV{CN_B};
    ' < "$1"
}

canon_size() { canon "$1" | wc -c | tr -d ' '; }

canon_equal() { cmp -s <(canon "$1") <(canon "$2"); }

# canon_prefix <src> <dst> - true if canon(dst) is a prefix of canon(src).
# head -c closes the pipe early so perl takes SIGPIPE; pipefail is disabled
# inside the subshell to stop that from reading as a comparison failure.
canon_prefix() {
    local cs
    cs=$(canon_size "$2")
    if [ "$cs" -eq 0 ]; then return 0; fi
    ( set +o pipefail
      canon "$1" | head -c "$cs" | cmp -s - <(canon "$2") )
}

# rewrite_tree <src_dir> <stage_dir> <from_path> <to_path>
rewrite_tree() {
    local src="$1" stage="$2"
    export RW_FROM="$3" RW_TO="$4"

    rm -rf "$stage"; mkdir -p "$stage"
    ( cd "$src" && find . -type d ) | while IFS= read -r rd; do mkdir -p "$stage/$rd"; done
    ( cd "$src" && find . -type f ) | while IFS= read -r rf; do
        case "$rf" in
            *.jsonl|*.json|*.md|*.txt|*.js|*.log)
                LC_ALL=C perl -pe 's!\Q$ENV{RW_FROM}\E!$ENV{RW_TO}!g' < "$src/$rf" > "$stage/$rf" ;;
            *)
                cp -p "$src/$rf" "$stage/$rf" ;;
        esac
    done
}

# backup_file <dst_root> <relpath> - stash the version about to be overwritten
backup_file() {
    local root="$1" rel="$2"
    local bdir="$BACKUP_ROOT/$(basename "$root")/$(dirname "$rel")"
    mkdir -p "$bdir"
    cp -p "$root/$rel" "$bdir/$(basename "$rel")"
}

# merge_tree <src_dir> <dst_dir> - fast-forward-only. Sets DIVERGED.
DIVERGED=0
merge_tree() {
    local src="$1" dst="$2"
    local n_new=0 n_same=0 n_ff=0 n_div=0
    DIVERGED=0

    if [ "$DRY_RUN" -eq 0 ]; then mkdir -p "$dst"; fi
    ( cd "$src" && find . -type d ) | while IFS= read -r rd; do
        if [ "$DRY_RUN" -eq 0 ]; then mkdir -p "$dst/$rd"; fi
    done

    while IFS= read -r rel; do
        rel="${rel#./}"
        local s="$src/$rel" d="$dst/$rel" ss ds
        ss=$(fsize "$s")

        if [ ! -e "$d" ]; then
            printf '    new            %s  (%s B)\n' "$rel" "$ss"
            if [ "$DRY_RUN" -eq 0 ]; then cp -p "$s" "$d"; fi
            n_new=$((n_new + 1)); continue
        fi

        ds=$(fsize "$d")

        # Fast path: byte-identical needs no canonicalisation at all.
        if [ "$ss" -eq "$ds" ] && cmp -s "$s" "$d"; then
            n_same=$((n_same + 1)); continue
        fi

        if canon_equal "$s" "$d"; then
            n_same=$((n_same + 1)); continue
        fi

        if canon_prefix "$s" "$d"; then
            printf '    fast-forward   %s  (+%s B)\n' "$rel" "$((ss - ds))"
            if [ "$DRY_RUN" -eq 0 ]; then backup_file "$dst" "$rel"; cp -p "$s" "$d"; fi
            n_ff=$((n_ff + 1)); continue
        fi

        if [ "$FORCE" -eq 1 ]; then
            printf '    FORCED         %s  (src %s B, dst %s B) : dst overwritten, old copy backed up\n' "$rel" "$ss" "$ds"
            if [ "$DRY_RUN" -eq 0 ]; then backup_file "$dst" "$rel"; cp -p "$s" "$d"; fi
            n_ff=$((n_ff + 1)); continue
        fi

        printf '    DIVERGED       %s  (src %s B, dst %s B) : destination KEPT, nothing written\n' "$rel" "$ss" "$ds"
        n_div=$((n_div + 1))
    done < <( cd "$src" && find . -type f )

    echo "    ==== $n_new new, $n_ff fast-forwarded, $n_same unchanged, $n_div diverged"
    DIVERGED=$n_div
}

# =============================================================================
# Repo-internal path rewriting
#
# --relocate fixes the transcripts, but absolute paths also live INSIDE repo
# files (for example .claude/audit/audit_ledger.jsonl records deliverable paths).
# A folder rename leaves those pointing at a directory that no longer exists.
# Binary files are skipped by grep -I. Every file is backed up before editing.
# =============================================================================
rewrite_repo_paths() {
    local old="$1" new="$2"
    local prune=() d
    for d in "${PRUNE_DIRS[@]}"; do prune+=(--exclude-dir="$d"); done

    local hits n=0
    hits=$(grep -rIl "${prune[@]}" -F -- "$old" "$new" 2>/dev/null || true)

    if [ -z "$hits" ]; then
        echo "    no repo file contains the old path - nothing to rewrite"
        return 0
    fi

    while IFS= read -r f; do
        [ -n "$f" ] || continue
        local c
        c=$(grep -c -F -- "$old" "$f" 2>/dev/null || printf '0')
        if [ "$DRY_RUN" -eq 1 ]; then
            printf '    would rewrite  %-58s (%s occurrence(s))\n' "${f#$new/}" "$c"
        else
            mkdir -p "$REPO_BACKUP/$(dirname "${f#$new/}")"
            cp -p "$f" "$REPO_BACKUP/${f#$new/}"
            OLD_P="$old" NEW_P="$new" LC_ALL=C perl -i -pe \
                's!\Q$ENV{OLD_P}\E!$ENV{NEW_P}!g' "$f"
            printf '    rewrote        %-58s (%s occurrence(s))\n' "${f#$new/}" "$c"
        fi
        n=$((n + 1))
    done <<< "$hits"

    if [ "$DRY_RUN" -eq 0 ]; then
        echo "    $n file(s) rewritten; originals backed up under"
        echo "      $REPO_BACKUP"
    else
        echo "    $n file(s) would be rewritten"
    fi
}

# =============================================================================
# Repo verification (READ ONLY)
#
# Every "git ... | head -N" is written as "| sed -n '1,Np'" on purpose: head
# closes the pipe early, git dies of SIGPIPE, and under pipefail+errexit that
# aborts the script. sed reads its input to completion, so it cannot.
# =============================================================================

REPO_DIRTY=0
REPO_BEHIND=0

# count_lines <captured-output> - "grep -c ." cannot be used here: on empty
# input it prints 0 AND exits 1, so a "|| printf 0" fallback fires as well and
# yields the two-line string "0\n0", which then crashes every [ -gt ] test.
count_lines() {
    if [ -z "$1" ]; then printf '0'; else printf '%s\n' "$1" | wc -l | tr -d ' '; fi
}

verify_repo() {
    cd "$MAC_REPO"
    REPO_DIRTY=0
    REPO_BEHIND=0

    echo "  == remote identity =="
    local actual
    actual=$(git remote get-url origin 2>/dev/null || printf '(none)')
    echo "    expected : $EXPECTED_REMOTE"
    echo "    origin   : $actual"
    if [ "$actual" != "$EXPECTED_REMOTE" ]; then
        echo "    MISCONFIGURED: origin does not point at the surveys repo."
        echo "                   git_push.sh pushes to an explicit url and never"
        echo "                   updates origin, so it can drift. Everything below"
        echo "                   would be compared against the WRONG repository."
        echo "    fix: git remote set-url origin $EXPECTED_REMOTE"
        REPO_DIRTY=1
        return 0
    fi

    echo "  == remote reachability =="
    local remote_sha local_sha
    remote_sha=$(git ls-remote origin "refs/heads/$GIT_BRANCH" 2>/dev/null | cut -f1)
    if [ -z "$remote_sha" ]; then
        echo "    FATAL: origin/$GIT_BRANCH not readable - check network or credentials"
        exit 5
    fi
    if git rev-parse --verify --quiet "origin/$GIT_BRANCH" >/dev/null; then
        local_sha=$(git rev-parse "origin/$GIT_BRANCH")
    else
        local_sha="(never fetched)"
    fi
    echo "    github  origin/$GIT_BRANCH : $remote_sha"
    echo "    local   origin/$GIT_BRANCH : $local_sha"
    if [ "$remote_sha" != "$local_sha" ]; then
        echo "    STALE: the local remote-tracking ref is behind GitHub. Run: git fetch origin"
        REPO_BEHIND=1
    fi

    if [ "$local_sha" = "(never fetched)" ]; then
        echo "    -> nothing else can be compared until: git fetch origin"
        return 0
    fi

    echo "  == commits =="
    local counts ahead behind
    counts=$(git rev-list --left-right --count "HEAD...origin/$GIT_BRANCH")
    ahead=$(printf '%s' "$counts" | awk '{print $1}')
    behind=$(printf '%s' "$counts" | awk '{print $2}')
    echo "    local-only commits: $ahead   origin-only commits: $behind"
    if [ "$behind" -gt 0 ]; then REPO_BEHIND=1; fi

    echo "  == tracked files differing from origin/$GIT_BRANCH =="
    local difflist ndiff
    difflist=$(git diff --name-status "origin/$GIT_BRANCH")
    ndiff=$(count_lines "$difflist")
    echo "    $ndiff file(s)"
    if [ "$ndiff" -gt 0 ]; then
        REPO_DIRTY=1
        printf '%s\n' "$difflist" | sed -n '1,15p' | sed 's/^/      /'
        if [ "$ndiff" -gt 15 ]; then echo "      ... and $((ndiff - 15)) more"; fi
    fi

    echo "  == untracked and NOT ignored (a stray 'git clean -fd' would DELETE these) =="
    local untlist nunt
    untlist=$(git ls-files --others --exclude-standard --directory)
    nunt=$(count_lines "$untlist")
    echo "    $nunt path(s)"
    if [ "$nunt" -gt 0 ]; then
        printf '%s\n' "$untlist" | sed -n '1,10p' | sed 's/^/      /'
        if [ "$nunt" -gt 10 ]; then echo "      ... and $((nunt - 10)) more"; fi
        echo "      -> commit them, or accept that they live only on this Mac."
    fi

    echo "  == local-only BY DESIGN (gitignored: per-user state, secrets, big artifacts) =="
    local p
    for p in "${LOCAL_ONLY[@]}"; do
        if [ -e "$p" ]; then
            printf '    %-56s present  %s\n' "$p" "$(du -sh "$p" 2>/dev/null | cut -f1)"
        else
            printf '    %-56s absent\n' "$p"
        fi
    done
    echo "    -> git will never deliver these; they are intentionally not tracked."

    if [ "$DEEP" -eq 1 ]; then
        echo "  == deep object check (git fsck --connectivity-only) =="
        if git fsck --connectivity-only --no-dangling; then
            echo "    OK: every object reachable from origin/$GIT_BRANCH is present"
        else
            echo "    FATAL: object graph is incomplete or corrupt - reclone required"
            exit 5
        fi
    fi

    echo "  == verdict =="
    if [ "$REPO_DIRTY" -eq 0 ] && [ "$REPO_BEHIND" -eq 0 ]; then
        echo "    IN SYNC: every tracked file matches origin/$GIT_BRANCH."
    else
        echo "    OUT OF SYNC: see above. Push with: bash git_push.sh 'message'"
    fi
}

# =============================================================================
# Modes
# =============================================================================
case "$MODE" in

    --verify-repo)
        echo "=== Verify: $MAC_REPO vs $EXPECTED_REMOTE ($GIT_BRANCH) ==="
        echo
        verify_repo
        echo
        if [ "$REPO_DIRTY" -ne 0 ] || [ "$REPO_BEHIND" -ne 0 ]; then exit 4; fi
        ;;

    --relocate)
        # The repo moved on this Mac, so its slug changed and claude --resume
        # can no longer see the old sessions. Rewrite the embedded paths and
        # fast-forward-merge them into the new slug, then fix any absolute path
        # still baked into the repo itself. Safe to re-run: it is the only way
        # to sweep up a session that was still being written during the move,
        # since Claude Code resolves cwd once at startup.
        OLD_SLUG="$(slug "$OLD_REPO")"
        OLD_SESSIONS="$HOME/.claude/projects/$OLD_SLUG"

        echo "=== Relocate (Mac only, no SSH) ==="
        echo "    from  $OLD_REPO"
        echo "    to    $MAC_REPO"
        [ "$DRY_RUN" -eq 1 ] && echo "    (dry run - nothing will be written)"
        echo

        if [ "$OLD_SESSIONS" = "$MAC_SESSIONS" ]; then
            echo "FATAL: old and new paths give the same slug - nothing to relocate."
            echo "       Did you forget to 'mv' the folder, or pass the wrong old path?"
            exit 1
        fi
        [ -d "$OLD_SESSIONS" ] || { echo "FATAL: no sessions at $OLD_SESSIONS"; exit 1; }

        echo "[1/3] rewrite transcripts  $OLD_REPO  ->  $MAC_REPO"
        rewrite_tree "$OLD_SESSIONS" "$STAGE" "$OLD_REPO" "$MAC_REPO"

        echo "[2/3] merge into $MAC_SESSIONS"
        merge_tree "$STAGE" "$MAC_SESSIONS"
        rm -rf "$STAGE"

        echo "[3/3] rewrite absolute paths baked into the repo"
        rewrite_repo_paths "$OLD_REPO" "$MAC_REPO"

        echo
        if [ "$DIVERGED" -gt 0 ]; then
            echo "WARNING: $DIVERGED session file(s) diverged - nothing was overwritten."
            echo "         Inspect, then re-run with --force to take the incoming copy."
            exit 3
        fi
        echo "Done. On the Mac:  cd $MAC_REPO && claude --resume"
        echo "The old slug dir is left intact as a full backup:"
        echo "    $OLD_SESSIONS"
        echo "Re-run this after ending any session that was live during the move."
        ;;
esac
