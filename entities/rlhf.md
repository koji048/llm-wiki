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
RLHF is a training technique that aligns language models to human preferences by training a reward model from human comparison labels, then using that reward model to guide RL fine-tuning. Introduced in OpenAI's InstructGPT paper (2022), it enables models to improve in unverifiable domains (creative writing, humor, empathy) where automated scoring is impossible. Karpathy notes it is "gameable" (adversarial examples like "the the the the" score 1.0) and fundamentally different from verifiable-domain RL.

## Key Distinctions
- **Verifiable domains** (math, code, Go): automated scoring enables unbounded RL scaling → superhuman (AlphaGo Move 37)
- **Unverifiable domains** (jokes, poems): gameable reward models; must stop after ~hundreds of updates

## Related Entities
- [[entities/Deep Dive into LLMs like ChatGPT [7xTGNNLPyMI].en.md]] — RLHF deep dive with examples
- [[InstructGPT]] — Original RLHF paper
- [[DeepSeek R1]] — Next evolution: RL without human feedback
- [[AlphaGo]] — Verifiable-domain RL analogue
- [[Reinforcement Learning]] — Parent technique
