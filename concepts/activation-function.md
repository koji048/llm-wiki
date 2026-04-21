---
title: Automatic Differentiation
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [autograd, gradients, computation]
sources: []
---

# Automatic Differentiation

**Automatic differentiation** (autograd) is the automatic computation of exact gradients via the chain rule, applied to arbitrary computational graphs.

## Types

- **Forward mode**: Computes gradients in same direction as computation
- **Reverse mode**: Computes gradients in reverse direction (used in deep learning)

## How It Works

1. Build computational graph (forward pass)
2. Traverse graph in reverse, applying chain rule (backward pass)
3. Exact gradients (not approximation like numerical differentiation)

## Implementation: micrograd

[[Building micrograd]] is an educational implementation of reverse-mode autograd in ~300 lines of Python.

## See Also

- [[Building micrograd]]
- [[backpropagation]]
- [[chain-rule]]
- [[PyTorch]]
