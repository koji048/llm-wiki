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
