---
title: "RLHF"
created: 2026-04-21
updated: 2026-04-21
type: entity
tags: [technique, alignment, training]
sources: []
---

# RLHF (Reinforcement Learning from Human Feedback)

## Summary
RLHF is a training technique that aligns language models to human preferences by training a reward model from human comparison labels, then using it to guide RL fine-tuning. Introduced in OpenAI's InstructGPT paper (2022), it enables models to improve in unverifiable domains (creative writing, humor, empathy) where automated scoring is impossible. Karpathy notes it is "gameable" — adversarial examples like "the the the the" score 1.0 — and fundamentally different from verifiable-domain RL.

## Key Distinctions
- **Verifiable domains** (math, code, Go): automated scoring enables unbounded RL scaling → superhuman (AlphaGo Move 37)
- **Unverifiable domains** (jokes, poems): gameable reward models; must stop after ~hundreds of updates

## Related Entities
- [[deep-dive-into-llms-7xTGNNLPyMI]] — RLHF deep dive with examples
- [[instruct-gpt-paper]] — Original RLHF paper
- [[deepseek-r1-reasoning-model]] — Evolution: RL without human feedback
- [[intro-to-large-language-models-zjkBMFhNj_g]] — RLHF in the training pipeline overview
