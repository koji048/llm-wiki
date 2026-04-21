---
title: Pre-training
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [training, LLM, foundation]
sources: []
---

# Pre-training

**Pre-training** is the first phase of LLM training, where the model learns to predict the next token on internet-scale text.

## What Happens

- Model reads trillions of tokens
- Learns language structure, facts, reasoning patterns
- Compresses world knowledge into weights (lossily)
- Next-token prediction objective

## Key Properties

- **Self-supervised**: No human labels needed
- **Unsupervised**: No explicit supervision signal
- **Foundation**: This is where capabilities come from

## Scaling Laws

Capabilities improve predictably with:
- Model size (parameters)
- Data size (tokens)
- Compute (FLOPs)

## See Also

- [[Deep Dive into LLMs]]
- [[Intro to Large Language Models]]
- [[alignment]]
- [[emergent-behaviors]]
