---
title: Deep Dive into LLMs like ChatGPT
created: 2026-04-20
updated: 2026-04-20
type: entity
tags: ["LLM", "pre-training", "alignment", "context window"]
sources: [raw/transcripts/7xTGNNLPyMI]
---

# Deep Dive into LLMs like ChatGPT

This video provides a deep technical exploration of how large language models like ChatGPT are trained and function. Karpathy breaks down the two-stage training process: pre-training on internet-scale text using next-token prediction, which compresses world knowledge into neural network weights; and post-training (alignment) using human feedback to shape the model into a helpful assistant. He explains the context window as the working memory where users and models jointly build token sequences, and discusses the implications of knowledge cutoffs, model sizes, and the lossy probabilistic nature of LLM knowledge. The talk also covers how gradient descent and backpropagation are used to train the model, and how tokenization schemes affect what the model sees.

## Key Concepts
- Next-Token Prediction
- Pre-training vs Post-training
- Context Window
- Alignment
- Knowledge Cutoff

## Related Entities
- [[Andrej Karpathy]]
- [[How I use LLMs]]
- [[OpenAI]]

## Source
[[raw/transcripts/7xTGNNLPyMI]]
