---
title: ALiBi (Attention with Linear Biases)
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [positional-encoding, transformer, architecture]
sources: []
---

# ALiBi (Attention with Linear Biases)

**ALiBi** is a positional encoding method that adds a linear bias to attention scores based on the distance between tokens.

## How It Works

Instead of adding positional encodings to embeddings, ALiBi modifies attention scores:
```
score(q_i, k_j) = q_i · k_j - λ * |i - j|
```

Where λ is a penalty that increases with distance.

## Advantages

- Naturally encodes relative position
- Works well for extrapolation
- No additional parameters

## See Also

- [[positional-encoding]]
- [[transformer]]
- [[attention]]
