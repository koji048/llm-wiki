---
title: Activation Function
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [neural-networks, non-linearity]
sources: []
---

# Activation Function

An **activation function** introduces non-linearity into neural networks, enabling them to learn complex patterns.

## Why Non-Linearity?

Without non-linear activations, stacking layers is equivalent to a single linear transformation — no matter how deep.

## Common Activation Functions

| Function | Formula | Range | Notes |
|----------|---------|-------|-------|
| **ReLU** | `max(0, x)` | [0, ∞) | Most common, simple |
| **tanh** | `(exp(x) - exp(-x)) / (exp(x) + exp(-x))` | [-1, 1] | Popular in RNNs |
| **sigmoid** | `1 / (1 + exp(-x))` | [0, 1] | Historical; saturates |

## ReLU Advantages

- Computationally efficient
- Reduces vanishing gradient problem
- Works well in practice

## See Also

- [[Building micrograd]]
- [[neural-network]]
- [[transformer]]
