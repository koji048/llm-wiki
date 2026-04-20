#!/bin/bash
# process_transcripts.sh — VPS cron job
# Pulls raw transcripts from GitHub, generates LLM Wiki pages, pushes back.

REPO_DIR="/tmp/llm-wiki-process"
LOG="/tmp/transcript-process.log"
TOKEN_FILE="/root/.llm-wiki-git-token"

log() { echo "[$(date '+%Y-%m-%d %H:%M')] $1" | tee -a "$LOG"; }

if [ ! -f "$TOKEN_FILE" ]; then log "ERROR: No git token at $TOKEN_FILE"; exit 1; fi
GIT_TOKEN=$(cat "$TOKEN_FILE")

if [ -d "$REPO_DIR" ]; then
    log "Pulling latest from GitHub..."
    cd "$REPO_DIR" && git pull --quiet origin main 2>&1 | tee -a "$LOG"
else
    log "Cloning llm-wiki..."
    git clone "https://x-access-token:${GIT_TOKEN}@github.com/koji048/llm-wiki.git" "$REPO_DIR" 2>&1 | tee -a "$LOG"
fi

cd "$REPO_DIR"

PROCESSED_MARKER="$REPO_DIR/.transcript-processed"
touch "$PROCESSED_MARKER"

NEW_TRANSCRIPTS=()
for txt in raw/transcripts/*.txt; do
    [ -f "$txt" ] || continue
    [[ "$(basename "$txt")" == ".gitkeep" ]] && continue
    if ! grep -q "$(basename "$txt")" "$PROCESSED_MARKER" 2>/dev/null; then
        NEW_TRANSCRIPTS+=("$txt")
    fi
done

if [ ${#NEW_TRANSCRIPTS[@]} -eq 0 ]; then
    log "No new transcripts."
    exit 0
fi

log "Found ${#NEW_TRANSCRIPTS[@]} new transcript(s)"

for transcript_path in "${NEW_TRANSCRIPTS[@]}"; do
    BASENAME=$(basename "$transcript_path" .txt)
    VIDEO_TITLE=$(echo "$BASENAME" | sed -E 's/\[.*$//' | xargs)
    VIDEO_ID=$(echo "$BASENAME" | grep -oE '[A-Za-z0-9_-]{11}$' || echo "unknown")
    TRANSCRIPT=$(cat "$transcript_path")
    TRANSCRIPT_PREVIEW=$(echo "$TRANSCRIPT" | head -c 25000)

    log "Processing: $VIDEO_TITLE ($VIDEO_ID)"

    ENTITY_RESPONSE=$(curl -s "https://openrouter.ai/api/v1/chat/completions" \
        -H "Authorization: Bearer $OPENROUTER_API_KEY" \
        -H "Content-Type: application/json" \
        -H "HTTP-Referer: https://llm-wiki" \
        -H "X-Title: LLM Wiki Processor" \
        -d "$(jq -n \
            --arg system "You are a wiki engineer. Output ONLY a JSON object, no markdown, no explanation." \
            --arg user "Create a wiki entity page for this YouTube transcript.

VIDEO TITLE: $VIDEO_TITLE
VIDEO ID: $VIDEO_ID

TRANSCRIPT PREVIEW:
$TRANSCRIPT_PREVIEW

Output JSON with exactly these fields:
{\"title\": \"Page Title\", \"type\": \"entity\", \"tags\": [\"video\",\"llm\",\"ai\"], \"summary\": \"200-word summary\", \"key_concepts\": [\"c1\",\"c2\",\"c3\",\"c4\",\"c5\"], \"related_entities\": [\"e1\",\"e2\",\"e3\"]}" \
            '{
                "model": "google/gemini-2.5-pro-preview-05-27",
                "messages": [
                    {"role": "system", "content": $system},
                    {"role": "user", "content": $user}
                ],
                "max_tokens": 1200,
                "temperature": 0.3
            }')")

    TITLE=$(echo "$ENTITY_RESPONSE" | jq -r '.choices[0].message.content // ""' | jq -r '.title // "Untitled"')
    SUMMARY=$(echo "$ENTITY_RESPONSE" | jq -r '.choices[0].message.content // ""' | jq -r '.summary // ""')
    TAGS=$(echo "$ENTITY_RESPONSE" | jq -r '.choices[0].message.content // ""' | jq -r '.tags // ["video"] | join(",")')
    KEY_CONCEPTS=$(echo "$ENTITY_RESPONSE" | jq -r '.choices[0].message.content // ""' | jq -r '.key_concepts // [] | join("; ")')
    RELATED=$(echo "$ENTITY_RESPONSE" | jq -r '.choices[0].message.content // ""' | jq -r '.related_entities // [] | join("; ")')

    TODAY=$(date '+%Y-%m-%d')

    ENTITY_FILE="entities/$(echo "$VIDEO_ID" | tr '[:upper:]' '[:lower:]').md"
    cat > "$ENTITY_FILE" << EOF
---
title: $TITLE
created: $TODAY
updated: $TODAY
type: entity
tags: [$TAGS]
sources: [raw/transcripts/$(basename "$transcript_path")]
---

# $TITLE

$SUMMARY

## Key Concepts
$(echo "$KEY_CONCEPTS" | tr ';' '\n' | sed 's/^/- /')

## Related Entities
$(echo "$RELATED" | tr ';' '\n' | sed 's/^/- [[/; s/$/]]/')

## Source
[[raw/transcripts/$(basename "$transcript_path")]]
EOF

    echo "$(basename "$transcript_path")" >> "$PROCESSED_MARKER"
    log "Created: $ENTITY_FILE"
done

INDEX_UPDATE="## [$(date '+%Y-%m-%d')] Ingest | ${#NEW_TRANSCRIPTS[@]} transcripts processed"
echo "$INDEX_UPDATE" >> index.md

cd "$REPO_DIR"
git config user.email "vps-cron@llm-wiki" 2>/dev/null || true
git config user.name "VPS Cron" 2>/dev/null || true
git add -A 2>&1 | tee -a "$LOG"
if ! git diff --cached --quiet 2>&1; then
    git commit -m "Process transcripts $(date '+%Y-%m-%d %H:%M')" 2>&1 | tee -a "$LOG"
    git push --quiet origin main 2>&1 | tee -a "$LOG"
    log "Pushed to GitHub."
fi

log "Done. ${#NEW_TRANSCRIPTS[@]} transcript(s) processed."
