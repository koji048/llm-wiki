---
title: Tokenizer
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [tokenization, preprocessing, vocabulary]
sources: []
---

# Tokenizer

A **tokenizer** converts raw text into integer tokens that language models can process.

## Tokenization Strategies

- **BPE** (Byte Pair Encoding): Iteratively merges most frequent byte pairs
- **SentencePiece**: Unsupervised tokenization, language-agnostic
- **tiktoken**: Fast BPE tokenizer used by OpenAI

## Vocab Size

- GPT-4: ~100k tokens
- GPT-3: ~50k tokens
- Smaller models: 30k-50k tokens

## Implications

- Common words = 1 token; rare words split into subwords
- ~4/3 tokens per English word
- Code often less efficient than natural language
- Different languages have different token densities

## See Also

- [[Deep Dive into LLMs]]
- [[Intro to Large Language Models]]
- [[transformer]]
