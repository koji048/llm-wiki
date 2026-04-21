---
title: Transformer
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [architecture, neural-network, attention]
sources: []
---

# Transformer

The **Transformer** is a neural network architecture introduced in "Attention Is All You Need" (2017) by Vaswani et al. It is the foundation of modern large language models.

## Core Components

- **[[attention]]** mechanism (self-attention)
- **Feed-forward networks** (MLP layers)
- **Layer normalization**
- **Residual connections**

## Key Innovation

Unlike RNNs, transformers process sequences in parallel by attending to all positions simultaneously via [[attention]], enabling:
- Parallel training (faster)
- No vanishing gradients for long sequences
- Direct connections between any two positions

## Variants

- **Decoder-only** (GPT-style): Used for language modeling
- **Encoder-only** (BERT-style): Used for classification
- **Encoder-decoder** (T5, GPT-4): Used for seq2seq tasks

## See Also

- [[Deep Dive into LLMs]]
- [[Intro to Large Language Models]]
- [[attention]]
- [[positional-encoding]]
