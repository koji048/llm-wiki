---
title: Loss Function
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [optimization, training, objective]
sources: []
---

# Loss Function

A **loss function** measures how wrong a model's predictions are. During training, we minimize this value via [[gradient-descent]].

## Common Loss Functions

### Cross-Entropy Loss
- Used for classification
- Measures difference between predicted and true distributions
- Steep gradient when model is very wrong → fast learning

### Mean Squared Error (MSE)
- Used for regression
- `L = Σ(prediction - target)²`
- Sensitive to outliers

### Negative Log-Likelihood (NLL)
- Equivalent to cross-entropy for classification
- Often used in language modeling

## See Also

- [[gradient-descent]]
- [[backpropagation]]
- [[Building micrograd]]
- [[pre-training]]
