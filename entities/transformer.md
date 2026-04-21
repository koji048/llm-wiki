---
title: "Transformer Architecture"
created: 2026-04-21
updated: 2026-04-21
type: entity
tags: [architecture, neural-network]
sources: []
---

# Transformer Architecture

## Summary
The Transformer (Vaswani et al., 2017) is the neural network architecture underlying all modern LLMs. It replaces recurrence with self-attention, allowing parallelized training over long sequences. Key components: positional encodings, multi-head self-attention, feed-forward MLP layers, layer norm. A model like GPT-4o has ~100 transformer layers with billions of parameters total — each layer applying the same mathematical operations to different data.

## Key Components
- **Self-attention**: queries, keys, values — all learned linear projections
- **Multi-head attention**: parallel attention heads for different representation subspaces
- **Positional encoding**: injects token position information (sinusoidal or learned)
- **FFN/MLP**: two-layer fully-connected network with GELU activation
- **Layer norm**: stabilizes training

## Related Entities
- [[entities/Deep Dive into LLMs like ChatGPT [7xTGNNLPyMI].en.md]] — Transformer in the LLM context
- [[entities/[1hr Talk] Intro to Large Language Models [zjkBMFhNj_g].en.md]] — Transformer as the core LLM component
- [[GPT-4]] — GPT-4's architecture
- [[Andrej Karpathy]] — Primary educator on transformers
