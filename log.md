---
title: Wiki Log
created: 2026-04-19
updated: 2026-04-20
type: meta
tags: [meta]
---

# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-04-19] create | Wiki initialized
- Domain: AI/ML research, LLM engineering, agent systems
- Structure: raw/, entities/, concepts/, comparisons/, queries/
- Remote: github.com/koji048/llm-wiki
- Notes: Git-based sync — local vault on Mac via Google Drive, VPS edits push via git
## [2026-04-20] create | Tum Office runtime fix — OpenRouter migration
- Created concepts/tum-office-runtime-fix.md documenting the port conflict, systemd services, and OpenRouter migration
- Also pushed to github.com/koji048/tum-office (new private repo)
- Related: concepts/tum-office-runtime-fix

## [2026-04-20] ingest | 4 Karpathy video transcripts processed
- Ingested from raw/transcripts/ (4 .txt files, VTT format cleaned)
- Created entities: VMj-3S1tku0, 7xTGNNLPyMI, EWvNQjAaOHw, zjkBMFhNj_g
- Updated index.md with 4 new entity pages
- Source: YouTube auto-generated captions via yt-dlp
