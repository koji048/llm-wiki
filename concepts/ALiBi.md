---
title: RoPE (Rotary Position Embedding)
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [positional-encoding, transformer, architecture]
sources: []
---

# RoPE (Rotary Position Embedding)

**RoPE** is a positional encoding method that rotates query and key vectors to encode absolute and relative position information.

## Key Advantage

Unlike fixed positional encodings, RoPE allows models to generalize to longer context lengths than they were trained on.

## How It Works

1. Split Q and K vectors into pairs
2. Apply rotary rotation based on position
3. Compute attention using rotated vectors

## Used In

- Llama
- GPT-NeoX
- Many modern open-source models

## See Also

- [[positional-encoding]]
- [[transformer]]
- [[attention]]
