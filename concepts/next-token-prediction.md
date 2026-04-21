---
title: DPO (Direct Preference Optimization)
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [alignment, fine-tuning, alternative-to-RLHF]
sources: []
---

# DPO (Direct Preference Optimization)

**DPO** is a simpler alternative to [[RLHF]] that directly optimizes against a preference oracle without a separate reward model.

## How It Works

Instead of:
1. Train reward model
2. Optimize policy against reward with [[PPO]]

DPO reframes the problem as a classification on preference data:
- Given (prompt, chosen response, rejected response)
- Optimize model to prefer chosen over rejected

## Advantages

- No separate reward model needed
- No PPO training complexity
- Simpler implementation

## See Also

- [[RLHF]]
- [[alignment]]
- [[Deep Dive into LLMs]]
