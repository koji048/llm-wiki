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
- Created entities: VMj-3S1tku0, 7xTGNNLPyMI, EWvNQjAaOHw, zjkBMFhNj_g
- Updated index.md with 4 new entity pages
- Source: YouTube auto-generated captions via yt-dlp

## [2026-04-21] update | Enrich 4 entities + create 27 concept stubs
- Enriched all 4 entity files with deep technical content from raw transcripts
- 7xTGNNLPyMI: added transformer, attention, tokenizer, SFT, RLHF, DPO, ChatML, context window, multimodal
- EWvNQjAaOHw: added zero-shot, few-shot, chain-of-thought, custom GPTs, memory, model tiers, practical workflows
- VMj-3S1tku0: added Value class, computational graph, forward/backward pass, gradient descent, loss functions, activations, PyTorch
- zjkBMFhNj_g: added token prediction, tokenization, positional encoding, pre-training, alignment, emergent behaviors, limitations
- Created 27 concept stubs in concepts/: transformer, attention, tokenizer, RLHF, SFT, pre-training, alignment, emergent-behaviors, context-window, prompting, chain-of-thought, custom-gpts, multimodal, reasoning-models, next-token-prediction, positional-encoding, RoPE, ALiBi, PPO, DPO, backpropagation, chain-rule, gradient-descent, loss-function, automatic-differentiation, activation-function, neural-network, micrograd
- Updated index.md (total pages: 35)
