---
title: RLHF (Reinforcement Learning from Human Feedback)
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [alignment, training, fine-tuning]
sources: []
---

# RLHF (Reinforcement Learning from Human Feedback)

**RLHF** is an alignment technique that uses human feedback to train a reward model, then optimizes the LLM against that reward.

## The Three Steps

1. **Collect demonstrations**: Humans write ideal responses
2. **[[SFT]]**: Fine-tune model on demonstrations
3. **Reward modeling**: Train a model to predict human preference
4. **[[PPO]]**: Optimize policy against reward model

## Why RLHF?

- Pre-trained models are not naturally helpful
- Humans can signal preference without writing full responses
- Scales better than purely supervised approaches

## Alternatives

- **[[DPO]]** (Direct Preference Optimization): Simpler, no separate reward model
- **Constitutional AI**: Uses principles instead of human feedback

## See Also

- [[Deep Dive into LLMs]]
- [[alignment]]
- [[SFT]]
- [[DPO]]
