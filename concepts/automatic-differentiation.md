---
title: Backpropagation
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [training, neural-networks, gradients]
sources: []
---

# Backpropagation

**Backpropagation** is the algorithm for efficiently computing gradients of the loss with respect to all weights in a neural network using the [[chain-rule]].

## Process

1. **Forward pass**: Compute loss
2. **Backward pass**: Propagate gradients from loss back to inputs
3. **Gradient accumulation**: Each parameter accumulates gradients from all paths

## Efficiency

Without backpropagation, computing gradients numerically would be O(n) per parameter. Backpropagation achieves O(1) per parameter by reusing computations.

## See Also

- [[Building micrograd]]
- [[chain-rule]]
- [[automatic-differentiation]]
- [[gradient-descent]]
