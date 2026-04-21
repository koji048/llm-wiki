---
title: Positional Encoding
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [transformer, position, architecture]
sources: []
---

# Positional Encoding

**Positional encoding** injects position information into transformers, which have no inherent notion of token order.

## Why Needed

Transformers process tokens as a set, not a sequence. Without positional information, "dog bites man" and "man bites dog" would be identical.

## Methods

### Original (Sin/Cosine)
Fixed encodings added to token embeddings:
```
PE(pos, 2i) = sin(pos / 10000^(2i/d))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d))
```

### [[RoPE]] (Rotary Position Embedding)
Rotates query and key vectors to encode relative position. Allows generalization to longer sequences than trained on.

### [[ALiBi]] (Attention with Linear Biases)
Adds linear bias to attention scores based on token distance.

## See Also

- [[transformer]]
- [[attention]]
- [[Deep Dive into LLMs]]
