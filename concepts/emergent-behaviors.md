---
title: Alignment
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [training, safety, helpfulness]
sources: []
---

# Alignment

**Alignment** is the process of shaping a pre-trained LLM into a helpful, safe assistant.

## Why Alignment?

Pre-trained models:
- Are raw next-token predictors
- May generate harmful content
- Don't naturally follow instructions
- Need guidance to be useful

## Techniques

- **[[SFT]]**: Supervised Fine-Tuning on demonstrations
- **[[RLHF]]**: Reinforcement Learning from Human Feedback
- **Constitutional AI**: Rule-based guidance
- **DPO**: Direct Preference Optimization

## What Can Go Wrong Without Alignment

- Harmful content generation
- Refusal to help
- Manipulation or deception
- Lack of safety guardrails

## See Also

- [[Deep Dive into LLMs]]
- [[Intro to Large Language Models]]
- [[RLHF]]
- [[SFT]]
