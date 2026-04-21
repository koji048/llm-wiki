---
title: micrograd
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [autograd, educational, backpropagation]
sources: []
---

# micrograd

**micrograd** is an educational automatic differentiation library (~300 lines) by Andrej Karpathy that implements [[backpropagation]] from scratch.

## Purpose

Strip away all abstraction of modern deep learning frameworks to reveal exactly how neural networks learn.

## Core Design

- `Value` class wraps scalars
- Operations build computational graph
- `backward()` propagates gradients via [[chain-rule]]

## Educational Value

Understanding micrograd gives deep intuition for:
- How [[gradient-descent]] works
- How [[backpropagation]] propagates gradients
- How [[PyTorch]]'s autograd works internally

## See Also

- [[Building micrograd]]
- [[automatic-differentiation]]
- [[backpropagation]]
