#!/bin/bash
# SessionEnd hook — Relay session transcript to outbox for agent upload
#
# Non-IT equivalent of IT's session-end-upload.sh. Instead of uploading
# directly via az CLI (which non-IT employees don't have), this copies
# the transcript + metadata to ~/.claude/outbox/{session_id}/ where the
# evermore-agent session_upload command picks it up on next heartbeat.
#
# Input: JSON on stdin from Claude Code SessionEnd event
#   { "session_id": "...", "transcript_path": "...", "cwd": "...", "reason": "..." }
#
# Output: Copies transcript + metadata.json to outbox directory.
#         Always exits 0 (errors are non-fatal).
#
# Prerequisites: Basic shell only — no az CLI, git, jq, or other tools required.
#
# ADR: ADR-0e1f439a (Non-IT employee hook profile)

set -uo pipefail
# Note: no -e — we handle errors explicitly to ensure non-fatal exit

OUTBOX_DIR="$HOME/.claude/outbox"

# ── Read hook input from stdin ────────────────────────────────────────────────
# Use python3 (ships with macOS) for JSON parsing. Fall back to basic parsing
# if python3 is unavailable.

INPUT=$(cat)

parse_json() {
    local field="$1"
    if command -v /usr/bin/python3 &>/dev/null; then
        echo "$INPUT" | /usr/bin/python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    print(data.get('$field', ''))
except:
    print('')
" 2>/dev/null
    elif command -v jq &>/dev/null; then
        echo "$INPUT" | jq -r ".$field // empty" 2>/dev/null
    else
        # Last resort: basic grep extraction (handles simple flat JSON)
        echo "$INPUT" | grep -o "\"$field\"[[:space:]]*:[[:space:]]*\"[^\"]*\"" | \
            sed 's/.*"'$field'"[[:space:]]*:[[:space:]]*"\([^"]*\)"/\1/' 2>/dev/null
    fi
}

SESSION_ID=$(parse_json "session_id")
TRANSCRIPT_PATH=$(parse_json "transcript_path")
CWD=$(parse_json "cwd")
REASON=$(parse_json "reason")

# ── Validate required fields ─────────────────────────────────────────────────

if [ -z "$SESSION_ID" ]; then
    # Can't do anything without a session ID
    exit 0
fi

if [ -z "$TRANSCRIPT_PATH" ] || [ ! -f "$TRANSCRIPT_PATH" ]; then
    # No transcript to relay
    exit 0
fi

# ── Create outbox directory ───────────────────────────────────────────────────

SESSION_OUTBOX="${OUTBOX_DIR}/${SESSION_ID}"
mkdir -p "$SESSION_OUTBOX" 2>/dev/null || exit 0

# ── Build metadata ────────────────────────────────────────────────────────────

TIMESTAMP=$(date -u '+%Y-%m-%dT%H:%M:%SZ' 2>/dev/null || echo "unknown")
HOSTNAME_SHORT=$(hostname -s 2>/dev/null || echo "unknown")

if command -v /usr/bin/python3 &>/dev/null; then
    /usr/bin/python3 -c "
import json, sys

metadata = {
    'session_id': '$SESSION_ID',
    'timestamp': '$TIMESTAMP',
    'cwd': '''$CWD''',
    'exit_reason': '$REASON',
    'hostname': '$HOSTNAME_SHORT'
}

json.dump(metadata, sys.stdout, indent=2)
print()
" > "${SESSION_OUTBOX}/metadata.json" 2>/dev/null
elif command -v jq &>/dev/null; then
    jq -n \
        --arg session_id "$SESSION_ID" \
        --arg timestamp "$TIMESTAMP" \
        --arg cwd "$CWD" \
        --arg exit_reason "$REASON" \
        --arg hostname "$HOSTNAME_SHORT" \
        '{
            session_id: $session_id,
            timestamp: $timestamp,
            cwd: $cwd,
            exit_reason: $exit_reason,
            hostname: $hostname
        }' > "${SESSION_OUTBOX}/metadata.json" 2>/dev/null
else
    # Minimal JSON without a proper encoder
    cat > "${SESSION_OUTBOX}/metadata.json" 2>/dev/null << JSONEOF
{
  "session_id": "${SESSION_ID}",
  "timestamp": "${TIMESTAMP}",
  "cwd": "${CWD}",
  "exit_reason": "${REASON}",
  "hostname": "${HOSTNAME_SHORT}"
}
JSONEOF
fi

# ── Copy transcript ───────────────────────────────────────────────────────────

cp "$TRANSCRIPT_PATH" "${SESSION_OUTBOX}/transcript.jsonl" 2>/dev/null

# Always exit 0 — transcript relay is best-effort
exit 0
