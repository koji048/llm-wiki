---
title: Emergent Behaviors
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [LLM, capabilities, scaling]
sources: []
---

# Emergent Behaviors

**Emergent behaviors** are capabilities that appear non-linearly as models increase in scale — they seem to "suddenly" appear at certain threshold sizes.

## Examples

- Basic reasoning (small scale)
- Complex multi-step reasoning (medium scale)
- Coding, translation, summarization (large scale)
- Mathematical proof writing (very large scale)
- Meta-cognition (largest scale)

## Why Does This Happen?

- Unknown. Several theories:
  - Scale enables more complex internal representations
  - Diversity of training data covers more tasks
  - Larger models can memorize and compose patterns

## Implications

- Small models may lack capabilities entirely, then suddenly gain them
- Capabilities are not taught explicitly
- We can't predict exactly what emerges at what scale

## See Also

- [[Intro to Large Language Models]]
- [[pre-training]]
- [[Deep Dive into LLMs]]
