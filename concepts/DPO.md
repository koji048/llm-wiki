---
title: PPO (Proximal Policy Optimization)
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [RLHF, reinforcement-learning, alignment]
sources: []
---

# PPO (Proximal Policy Optimization)

**PPO** is a reinforcement learning algorithm used in [[RLHF]] to update the LLM policy based on the reward model.

## Why PPO?

- Stable updates (clipped objective prevents large policy changes)
- Sample efficient
- Well-suited for language models

## In RLHF

1. Collect samples from current policy
2. Score with reward model
3. Update policy via PPO to maximize reward
4. KL penalty prevents drifting too far from SFT model

## See Also

- [[RLHF]]
- [[alignment]]
- [[Deep Dive into LLMs]]
