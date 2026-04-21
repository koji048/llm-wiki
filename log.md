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
## [2026-04-20] ingest | Deep Dive into LLMs like ChatGPT
- Created entities/deep-dive-into-llms-7xTGNNLPyMI.md — comprehensive entity page for Karpathy's ~3.5hr deep dive into LLMs
- Covers: tokenization, Transformer architecture, pre-training, SFT, Reward Model, RLHF, tool use, "Thinking" models, hallucination, Swiss cheese capability model
- Cross-referenced: [[how-i-use-llms-EWvNQjAaOHw]], [[intro-to-large-language-models-zjkBMFhNj_g]], [[karpathy-llm-wiki]], [[micrograd-neural-networks-backpropagation-VMj-3S1tku0]]
## [2026-04-20] ingest | How I use LLMs
- Created entities/how-i-use-llms-EWvNQjAaOHw.md — comprehensive entity page for Karpathy's practical guide to using LLMs (~2hr)
- Covers: LLM ecosystem (ChatGPT, Claude, Gemini), context window, search tools, Python execution, custom GPTs, voice I/O, image generation (DALL-E), translation
- Cross-referenced: [[deep-dive-into-llms-7xTGNNLPyMI]], [[intro-to-large-language-models-zjkBMFhNj_g]], [[karpathy-llm-wiki]]
## [2026-04-20] ingest | micrograd neural networks backpropagation video
- Created entities/micrograd-neural-networks-backpropagation-VMj-3S1tku0.md — comprehensive entity page for Karpathy's micrograd lecture
- Covers: derivatives, chain rule, Value class, expression graph, forward/backward pass, Neuron/Layer/MLP classes, MSE loss, training loop, PyTorch internals comparison
- Cross-referenced: [[deep-dive-into-llms-7xTGNNLPyMI]], [[how-i-use-llms-EWvNQjAaOHw]], [[karpathy-llm-wiki]]
- Updated index.md (total pages: 4)
## [2026-04-20] ingest | Intro to Large Language Models video
- Created entities/intro-to-large-language-models-zjkBMFhNj_g.md — comprehensive entity page for Karpathy's ~1hr intro talk
- Covers: LLM as two files, pre-training as lossy compression, fine-tuning (SFT), RLHF, tool use (Python, calculator, DALL-E), multimodality, LLM OS analogy, AlphaGo self-improvement analogy, jailbreaks, prompt injection, data poisoning attacks
- Cross-referenced: [[karpathy-llm-wiki]], [[deep-dive-into-llms-7xTGNNLPyMI]], [[how-i-use-llms-EWvNQjAaOHw]], [[micrograd-neural-networks-backpropagation-VMj-3S1tku0]]
- Updated index.md (total pages: 5)
## [2026-04-20] create | Tum Office runtime fix — OpenRouter migration
- Created concepts/tum-office-runtime-fix.md documenting the port conflict, systemd services, and OpenRouter migration
- Also pushed to github.com/koji048/tum-office (new private repo)
- Related: concepts/tum-office-runtime-fix

## [2026-04-20] ingest | 4 Karpathy video transcripts processed
- Ingested from raw/transcripts/ (4 .txt files, VTT format cleaned)
- Created entities: VMj-3S1tku0, 7xTGNNLPyMI, EWvNQjAaOHw, zjkBMFhNj_g
- Updated index.md with 4 new entity pages
- Source: YouTube auto-generated captions via yt-dlp

## [2026-04-21] lint+dedupe | Entity quality and deduplication pass
- Removed 4 auto-generated .en.md duplicates — kept comprehensive slug-named entity files
- Adopted remote slug-named entities: deep-dive-into-llms, how-i-use-llms, intro-to-large-language-models, micrograd (created by cron pipeline)
- Added 10 stub entities: andrej-karpathy, gpt-4, llama-2, deepseek-r1-reasoning-model, instruct-gpt-paper, rlhf, transformer, fineweb, karpathy-llm-wiki, karpathy-llm-wiki (concept)
- All wikilinks now resolve to existing files; no dangling references
- Obsidian-ready: clean slug filenames, proper frontmatter, [[wikilinks]] between related entities

## [2026-04-21] lint+dedupe | Stub entity quality fix
- Fixed 8 stub files: replaced all dead wikilinks (deleted .en.md files, non-existent stubs)
- FineWeb: removed accidental Chinese mixed-language text
- All wikilinks: bare format (no [[entities/...]] prefix), all resolve to existing files

## [2026-04-21] update | karpathy-llm-wiki concept page expanded
- Rewrote concepts/karpathy-llm-wiki.md: full gist content captured
- Sections: Core Insight, Three Layers, Operations (Ingest/Query/Lint), Index and Log, Why It Works, Optional Tools, Implementation Notes
- Removed broken [[llm-wiki-skill]] and [[obsidian]] wikilinks
- Added valid wikilinks to [[andrej-karpathy]] and [[rlhf]]
- Type: concept (was summary)


## [2026-04-21] create | microgpt entity page
- Created entities/microgpt.md: full gist content as entity page
- ~300-line dependency-free GPT in pure Python; covers Value class autograd, transformer architecture, custom Adam, training loop, inference
- Added to index.md after micrograd entry, bumped page count to 15
- Wikilinks to [[micrograd-neural-networks-backpropagation-VMj-3S1tku0]], [[transformer]], [[andrej-karpathy]]

