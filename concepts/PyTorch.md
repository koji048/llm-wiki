---
title: Next-Token Prediction
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [LLM, training-objective, core-concept]
sources: []
---

# Next-Token Prediction

**Next-token prediction** is the core training objective for language models — predicting the next token given all preceding tokens.

## The Objective

Given tokens `t1, t2, ..., tn`, predict `tn+1`.

The model learns: `P(tn+1 | t1, t2, ..., tn)`

## Why It Works

- Self-supervised: labels come from the data itself
- Forces the model to build internal representations
- Captures language structure, facts, reasoning
- Is the foundation of all capabilities

## Connection to Intelligence

Karpathy argues this simple objective, at scale, produces:
- Language understanding
- Reasoning capabilities
- World knowledge
- Emergent behaviors

## See Also

- [[Deep Dive into LLMs]]
- [[Intro to Large Language Models]]
- [[pre-training]]
