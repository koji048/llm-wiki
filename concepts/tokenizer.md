---
title: Attention
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [mechanism, transformer, key-component]
sources: []
---

# Attention

**Attention** is the core mechanism in transformers that allows models to weigh the importance of different parts of the input when processing each element.

## How It Works

1. **Query (Q)**, **Key (K)**, and **Value (V)** vectors are computed for each token
2. **Attention scores**: `score = Q · K^T / sqrt(d_k)`
3. **Softmax** to get weights: `a = softmax(scores)`
4. **Output**: weighted sum of values: `Σ a_i * V_i`

## Multi-Head Attention

Running multiple attention operations in parallel allows the model to attend to different aspects simultaneously.

## See Also

- [[transformer]]
- [[Deep Dive into LLMs]]
- [[context-window]]
