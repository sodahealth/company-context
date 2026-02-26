#!/bin/bash
# PreToolUse hook — Safety guard (company-wide employee hook profile)
#
# Four safety patterns for all employees:
#   S-1: Force-push deny — hard block git push --force/-f/--force-with-lease
#   S-2: Credential detection — warn on API key patterns in Write/Edit content
#   S-3: PHI/PII transmission guard — warn on HTTP to non-approved domains
#   S-4: Data classification reminder — inject reminder for shared/public paths
#
# Input: JSON on stdin from Claude Code PreToolUse event
#   { "tool_name": "Bash", "tool_input": { "command": "..." } }
#   { "tool_name": "Write", "tool_input": { "file_path": "...", "content": "..." } }
#   { "tool_name": "Edit", "tool_input": { "file_path": "...", "new_string": "..." } }
#
# Output: JSON deny for S-1; plain text warnings for S-2, S-3, S-4.
#         Exits silently (no output) when no pattern matches.
#
# ADR: ADR-0e1f439a (Non-IT employee hook profile)

set -euo pipefail

# ── Read hook input ───────────────────────────────────────────────────────────

INPUT=$(cat)

# Requires jq — exit silently if not available
if ! command -v jq &>/dev/null; then
    exit 0
fi

TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // empty' 2>/dev/null)
[ -z "$TOOL_NAME" ] && exit 0

# ── Locate approved services list (used by S-3) ──────────────────────────────

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
APPROVED_FILE="$REPO_ROOT/knowledge/approved-services.md"

if [ ! -f "$APPROVED_FILE" ]; then
    APPROVED_FILE="$HOME/.claude/knowledge/approved-services.md"
fi

# ── Helper: check if a domain is on the approved list ─────────────────────────

domain_is_approved() {
    local domain="$1"

    # Always approve localhost / loopback
    case "$domain" in
        localhost|127.0.0.1|0.0.0.0|::1) return 0 ;;
    esac

    # If no approved file exists, skip the check (don't warn)
    [ ! -f "$APPROVED_FILE" ] && return 0

    # Read approved domains (skip comments and blank lines)
    while IFS= read -r line; do
        local pattern
        pattern=$(echo "$line" | sed 's/#.*//' | xargs 2>/dev/null)
        [ -z "$pattern" ] && continue

        # Wildcard: *.example.com matches sub.example.com and example.com
        if [[ "$pattern" == \*.* ]]; then
            local suffix="${pattern#\*.}"
            if [[ "$domain" == "$suffix" ]] || [[ "$domain" == *".$suffix" ]]; then
                return 0
            fi
        else
            if [[ "$domain" == "$pattern" ]]; then
                return 0
            fi
        fi
    done < "$APPROVED_FILE"

    return 1
}

# ══════════════════════════════════════════════════════════════════════════════
# Bash tool patterns (S-1: force-push, S-3: PHI/PII guard)
# ══════════════════════════════════════════════════════════════════════════════

if [ "$TOOL_NAME" = "Bash" ]; then
    COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // empty' 2>/dev/null)
    [ -z "$COMMAND" ] && exit 0

    # ── S-1: Force-push deny (hard deny) ──────────────────────────────────────

    if echo "$COMMAND" | grep -q 'git push' && \
       echo "$COMMAND" | grep -qE '(^|[[:space:]])(-f([[:space:]]|$)|--force)'; then
        REASON="Force-pushing is not allowed. This protects shared branch history from accidental overwrites. Use a regular git push or create a new branch instead."
        REASON_JSON=$(echo "$REASON" | jq -Rs '.')
        echo "{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"permissionDecision\":\"deny\",\"permissionDecisionReason\":${REASON_JSON}}}"
        exit 0
    fi

    # ── S-3: PHI/PII transmission guard (warn, don't block) ──────────────────

    if echo "$COMMAND" | grep -qE '(curl |wget |requests\.(post|put|patch|get))'; then
        # Extract URLs from the command
        URLS=$(echo "$COMMAND" | grep -oE "https?://[^\"'[:space:]>)]+" 2>/dev/null || true)

        if [ -n "$URLS" ]; then
            FLAGGED=""
            while IFS= read -r url; do
                # Extract domain from URL
                domain=$(echo "$url" | sed 's|https\{0,1\}://||' | cut -d'/' -f1 | cut -d':' -f1)
                [ -z "$domain" ] && continue

                if ! domain_is_approved "$domain"; then
                    FLAGGED="${FLAGGED}  - ${domain}
"
                fi
            done <<< "$URLS"

            if [ -n "$FLAGGED" ]; then
                echo ""
                echo "[Safety guard — PHI/PII transmission warning]"
                echo ""
                echo "This command sends data to a domain not on the approved services list:"
                printf "%s" "$FLAGGED"
                echo ""
                echo "Before proceeding, verify:"
                echo "  1. No PHI/PII is included in the request body"
                echo "  2. The destination is an approved vendor for this data type"
                echo "  3. The data classification allows external transmission"
                echo ""
            fi
        fi
    fi

    exit 0
fi

# ══════════════════════════════════════════════════════════════════════════════
# Write/Edit tool patterns (S-2: credentials, S-4: classification reminder)
# ══════════════════════════════════════════════════════════════════════════════

if [ "$TOOL_NAME" = "Write" ] || [ "$TOOL_NAME" = "Edit" ]; then
    OUTPUT=""

    # ── S-2: Credential detection (warn, don't block) ─────────────────────────

    CONTENT=""
    if [ "$TOOL_NAME" = "Write" ]; then
        CONTENT=$(echo "$INPUT" | jq -r '.tool_input.content // empty' 2>/dev/null)
    else
        CONTENT=$(echo "$INPUT" | jq -r '.tool_input.new_string // empty' 2>/dev/null)
    fi

    if [ -n "$CONTENT" ]; then
        CRED_PATTERN='(sk-[a-zA-Z0-9_-]{20,}|xoxb-[a-zA-Z0-9-]+|xoxp-[a-zA-Z0-9-]+|ghp_[a-zA-Z0-9]{36}|gho_[a-zA-Z0-9]{36}|AKIA[A-Z0-9]{16}|Server=.*Password=|postgres://[^[:space:]:]+:[^@]+@|mongodb(\+srv)?://[^[:space:]:]+:[^@]+@|mysql://[^[:space:]:]+:[^@]+@|-----BEGIN (RSA |EC )?PRIVATE KEY-----)'

        if echo "$CONTENT" | grep -qE "$CRED_PATTERN"; then
            OUTPUT="[Safety guard — Credential warning]

The content you are about to write appears to contain an API key, token, or secret.
Review the content carefully. Never commit credentials to version control.
If this is a false positive (e.g., a pattern example or documentation), you may proceed.
"
        fi
    fi

    # ── S-4: Data classification reminder (Write only) ────────────────────────

    if [ "$TOOL_NAME" = "Write" ]; then
        FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty' 2>/dev/null)

        if [ -n "$FILE_PATH" ] && echo "$FILE_PATH" | grep -qiE '(^|/)(public|shared|external|export)(/|$)'; then
            OUTPUT="${OUTPUT}[Safety guard — Data classification reminder]

You are writing to a shared or public location.
Before proceeding, confirm:
  - The content is classified appropriately for this location
  - No internal-only, confidential, or restricted data is included
  - PHI/PII has been removed or is authorized for this destination
"
        fi
    fi

    if [ -n "$OUTPUT" ]; then
        echo ""
        echo "$OUTPUT"
    fi

    exit 0
fi

# No matching pattern — exit silently
exit 0
