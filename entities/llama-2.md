---
title: "Llama 2"
created: 2026-04-21
updated: 2026-04-21
type: entity
tags: [model, open-weight, meta]
sources: []
---

# Llama 2

## Summary
Llama 2 is Meta's open-weight large language model family, released in July 2023 with models ranging from 7B to 70B parameters. The 70B version is used as Karpathy's primary running example in his "Intro to LLMs" talk — demonstrating that an LLM is "just two files": a ~140GB parameters file and a ~500-line C runfile. Training cost ~$2M on 6,000 GPUs over 12 days on ~10TB of text.

## Key Facts
- Released: July 2023
- Developer: Meta AI
- Parameters: 7B, 13B, 34B, 70B
- Training: Pre-training + fine-tuning, optional RLHF
- Context: 4,096 tokens (original)

## Related Entities
- [[entities/[1hr Talk] Intro to Large Language Models [zjkBMFhNj_g].en.md]] — Karpathy's Llama 2 70B case study
- [[entities/Deep Dive into LLMs like ChatGPT [7xTGNNLPyMI].en.md]] — Training pipeline details
- [[Meta AI]] — Developer
- [[Transformer]] — Architecture
