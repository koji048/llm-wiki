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
The Transformer (Vaswani et al., 2017) is the neural network architecture underlying all modern LLMs. It replaces recurrence with self-attention, enabling parallelized training over long sequences. Key components: positional encodings, multi-head self-attention, feed-forward MLP layers, and layer norm.

## Key Components
- **Self-attention**: queries, keys, values — learned linear projections enabling token-to-token relevance scoring
- **Multi-head attention**: parallel attention heads for different representation subspaces
- **Positional encoding**: injects token position information (sinusoidal or learned)
- **FFN/MLP**: two-layer fully-connected network with GELU activation
- **Layer norm**: stabilizes training

## Related Entities
- [[deep-dive-into-llms-7xTGNNLPyMI]] — Transformer in the LLM context
- [[intro-to-large-language-models-zjkBMFhNj_g]] — Transformer as the core LLM component
- [[gpt-4]] — GPT-4's architecture
