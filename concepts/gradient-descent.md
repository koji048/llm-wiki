---
title: SFT (Supervised Fine-Tuning)
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [fine-tuning, alignment, training]
sources: []
---

# SFT (Supervised Fine-Tuning)

**SFT** is the first stage of alignment, where the pre-trained model is fine-tuned on human-written demonstration data.

## Process

1. Collect pairs of (input prompt, ideal response) from human annotators
2. Fine-tune the pre-trained model using these pairs
3. Model learns to follow instructions via standard [[gradient-descent]]

## Characteristics

- Simple, supervised approach
- Relies on high-quality human annotations
- Establishes basic instruction-following capability

## See Also

- [[Deep Dive into LLMs]]
- [[RLHF]]
- [[alignment]]
- [[gradient-descent]]
