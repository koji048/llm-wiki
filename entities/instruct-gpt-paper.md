---
title: "InstructGPT"
created: 2026-04-21
updated: 2026-04-21
type: entity
tags: [paper, alignment, openai]
sources: []
---

# InstructGPT

## Summary
InstructGPT (2022) is the OpenAI paper ("Training language models to follow instructions with human feedback") that introduced the SFT + RLHF pipeline that became standard for deployed assistants. It hired Upwork/Scale AI labelers to write ideal "helpful, truthful, harmless" responses, demonstrating that a small dataset of high-quality labeled conversations could dramatically improve alignment at relatively low cost compared to pre-training.

## Key Facts
- Published: 2022
- Authors: OpenAI
- Key innovation: RLHF for instruction-following alignment
- Data: ~100K human-labeled conversations

## Related Entities
- [[entities/Deep Dive into LLMs like ChatGPT [7xTGNNLPyMI].en.md]] — InstructGPT as the SFT/RLHF template
- [[RLHF]] — Core technique it introduced
- [[Scale AI]] — Primary labeling vendor
