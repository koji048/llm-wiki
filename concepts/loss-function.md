---
title: Gradient Descent
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [optimization, training, learning]
sources: []
---

# Gradient Descent

**Gradient descent** is the optimization algorithm used to train neural networks by iteratively updating weights in the direction that reduces the [[loss-function]].

## The Update Rule

```
weight = weight - learning_rate * gradient
```

## Variants

- **SGD**: Uses individual examples
- **Mini-batch**: Uses batches of examples
- **Adam**: Adaptive learning rates, momentum
- **AdamW**: Adam with proper weight decay

## Learning Rate

- Too high: unstable, diverges
- Too low: slow convergence
- Often schedule: high initially, decay over time

## See Also

- [[loss-function]]
- [[backpropagation]]
- [[Building micrograd]]
- [[chain-rule]]
