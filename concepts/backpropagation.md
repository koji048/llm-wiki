---
title: Chain Rule
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [calculus, backpropagation, gradients]
sources: []
---

# Chain Rule

The **chain rule** from calculus is the mathematical foundation of [[backpropagation]], allowing efficient computation of gradients in deep networks.

## Mathematical Formulation

For `f(g(x))`:
```
d/dx f(g(x)) = f'(g(x)) * g'(x)
```

For multiple variables:
```
∂L/∂x = Σ ∂L/∂z_i * ∂z_i/∂x
```

## In Neural Networks

During backpropagation, gradients flow backward through the computational graph:
1. Start at the loss
2. For each operation, compute how each input affected the output
3. Multiply by the incoming gradient (chain rule)
4. Accumulate gradients at each parameter

## See Also

- [[backpropagation]]
- [[Building micrograd]]
- [[gradient-descent]]
