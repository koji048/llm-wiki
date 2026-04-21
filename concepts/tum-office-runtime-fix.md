---
title: Tum Office Runtime Fix
created: 2026-04-19
updated: 2026-04-21
type: concept
tags: [tum-office, openclaw, openrouter, minimax, runtime, systemd]
sources: []
---

# Tum Office Runtime Fix

## Problem

The `tum-office-3d` service was in a crash loop with a `SyntaxError: Unexpected token ')'` at line 890 in `server.js`. The error was structural — the broken file had 902 lines vs the backup's 1215 lines, meaning ~313 lines of handler code were missing.

Root cause: the broken file was a more advanced version (with OpenRouter support and `SKILL_PROMPTS`) but was truncated mid-implementation, leaving unbalanced braces/parentheses from an unclosed construct upstream.

## Resolution

1. **Restored from backup** (`server.js.bak.1775955268`, 1215 lines) — syntax valid, service immediately restored
2. **Added OpenRouter support** to the backup — `LLM_PROVIDER` detection, baseUrl switching, OpenRouter headers
3. **Switched models** from `gpt-4.1-mini/nano` → `minimax/m2.7` (worker) + `minimax/m2.5` (idle)
4. **Created `skills/` directory** with 8 agent skill files per GStack pattern

## Files Changed

| File | Change |
|------|--------|
| `server.js` | OpenRouter patch (buildLLMWorkerOutput + buildLLMIdleThought), Minimax model env vars |
| `skills/` | New directory: 8 agent `.md` files + `SKILL.md` index |

## Current State

- **Service**: `tum-office-3d` active (running)
- **LLM**: enabled, `minimax/m2.7` worker, `minimax/m2.5` idle
- **API key**: loaded from `/root/.openrouter_api_key`
- **Skills**: loaded from `skills/` directory

## Architecture Notes

The Tum Office runtime uses a **Chief of Staff (Lisa)** model for task orchestration, not flat multi-agent broadcast. Specialist agents (Juno, Mika, Cory, Pip, Finance Bot, Comms Bot, Analyst Bot, Risk Bot) are dispatched by Lisa based on task type.

The gstack-inspired architecture is partially implemented — persistent browser daemon for `/qa` and `/review` commands is still missing. See [[garry-gstack]] for the reference architecture.

## Related

- [[garry-gstack]] — reference architecture (persistent browser daemon, SKILL.md pattern)
- [[hermes-agent]] — our agent framework with Telegram gateway
- [[karpathy-llm-wiki]] — LLM Wiki pattern (compounding knowledge base)
