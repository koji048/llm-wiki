# Log

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
- Created entities: deep-dive-into-llms-7xTGNNLPyMI, how-i-use-llms-EWvNQjAaOHw, intro-to-large-language-models-zjkBMFhNj_g, micrograd-neural-networks-backpropagation-VMj-3S1tku0
- Updated index.md with 4 new entity pages
- Source: YouTube auto-generated captions via yt-dlp

## [2026-04-21] lint+dedupe | Entity quality and deduplication pass
- Removed 4 auto-generated .en.md duplicates — kept comprehensive slug-named entity files
- Adopted remote slug-named entities: deep-dive-into-llms, how-i-use-llms, intro-to-large-language-models, micrograd (created by cron pipeline)
- Added 10 stub entities: andrej-karpathy, gpt-4, llama-2, deepseek-r1-reasoning-model, instruct-gpt-paper, rlhf, transformer, fineweb, karpathy-llm-wiki
- All wikilinks now resolve to existing files; no dangling references
- Obsidian-ready: clean slug filenames, proper frontmatter, wikilinks between related entities

## [2026-04-21] lint+dedupe | Stub entity quality fix
- Fixed 8 stub files: replaced all dead wikilinks (deleted .en.md files, non-existent stubs)
- FineWeb: removed accidental Chinese mixed-language text
- All wikilinks: bare format (no [[entities/...]] prefix), all resolve to existing files

## [2026-04-21] update | karpathy-llm-wiki concept page expanded
- Rewrote concepts/karpathy-llm-wiki.md: full gist content captured
- Sections: Core Insight, Three Layers, Operations (Ingest/Query/Lint), Index and Log, Why It Works, Optional Tools, Implementation Notes
- Removed broken wikilinks, added valid links to andrej-karpathy and rlhf
- Type: concept (was summary)

## [2026-04-21] create | microgpt entity page
- Created entities/microgpt.md: ~300-line dependency-free GPT in pure Python
- Covers Value class autograd, transformer architecture, custom Adam, training loop, inference
- Wikilinks to micrograd, transformer, andrej-karpathy
- Added to index.md after micrograd entry

## [2026-04-21] create | llm-automation-modes comparison page
- Created comparisons/llm-automation-modes.md: automated cron pipeline vs. interactive gcm-style
- Dimensions: human in loop, latency, risk, best for, trust model, automation level
- Shared philosophy: LLM does grunt work, human handles decisions

## [2026-04-21] restructure | wiki structure gaps fixed
- Removed duplicate entities/karpathy-llm-wiki.md (kept concepts/ version)
- Moved obsidian-local-vault-setup.md to raw/articles/ (setup docs belong there)
- Renamed queries/ -> analyses/ (matching Astro-Han implementation)
- Created overview.md: top-level synthesis of wiki domains, key themes, structure
- Created glossary.md: living terminology with 30+ defined terms
- Updated index.md: added overview+glossary to Meta, removed obsolete entries
- Page count: 16 -> 20

## [2026-04-21] update | Enrich 4 entities + create 29 concept stubs
- Enriched all 4 entity files with deep technical content from raw transcripts
- deep-dive-into-llms: added transformer, attention, tokenizer, SFT, RLHF, DPO, ChatML, context window, multimodal
- how-i-use-llms: added zero-shot, few-shot, chain-of-thought, custom GPTs, memory, model tiers, practical workflows
- micrograd: added Value class, computational graph, forward/backward pass, gradient descent, loss functions, activations, PyTorch
- intro-to-large-language-models: added token prediction, tokenization, positional encoding, pre-training, alignment, emergent behaviors, limitations
- Created 29 concept stubs: transformer, attention, tokenizer, RLHF, SFT, pre-training, alignment, emergent-behaviors, context-window, prompting, chain-of-thought, custom-gpts, multimodal, reasoning-models, next-token-prediction, positional-encoding, RoPE, ALiBi, PPO, DPO, backpropagation, chain-rule, gradient-descent, loss-function, automatic-differentiation, activation-function, neural-network, micrograd, PyTorch
- Updated index.md (total pages: 49)

## [2026-04-23] create | karpathy-guidelines concept
- Created concepts/karpathy-guidelines.md — four behavioral principles for LLM coding (Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution)
- Source: forrestchang/andrej-karpathy-skills repo (karpathy-inspired guidelines, 76.7k stars)
- Linked to karpathy-llm-wiki, anthropic-agent-skills, tum-office
- Added to index.md (Meta/Pattern Concepts section)
- Also filed: entities/pixel-agents.md (from previous session 20260423)
- Updated total pages: 51
