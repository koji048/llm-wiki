---
title: Building micrograd from Scratch
created: 2026-04-20
updated: 2026-04-21
type: entity
tags: [neural-networks, backpropagation, autograd, PyTorch, micrograd, deep-learning]
sources: [raw/transcripts/VMj-3S1tku0]
---

# Building micrograd from Scratch

In this tutorial, Andrej Karpathy walks through building **micrograd** — a minimal automatic differentiation (autograd) engine — from scratch in a Jupyter notebook. micrograd implements the core algorithm that underlies [[backpropagation]], stripped of all abstraction, revealing exactly how neural networks learn.

## What is micrograd?

**micrograd** is an educational library (~300 lines of code) that implements [[automatic-differentiation]] — specifically, reverse-mode automatic differentiation, which is what modern deep learning frameworks like [[PyTorch]] use. It allows you to build mathematical expressions and automatically compute their gradients with respect to any inputs.

The core insight: **backpropagation** is just the efficient application of the [[chain-rule]] from calculus, computed in reverse order through a computational graph.

## The Value Class and Computational Graph

The foundation of micrograd is the `Value` object. Every number in your computation is wrapped in a `Value`, which:
1. Stores the actual scalar value
2. Stores a reference to the operation that created it (its "creator")
3. Accumulates gradients during the backward pass

```python
Value(data, children=(...), op='...')
```

When you perform operations on `Value` objects (addition, multiplication, tanh, etc.), micrograd builds a **computational graph** — a directed acyclic graph (DAG) where nodes are `Value` objects and edges represent operations.

### Types of Nodes

- **Leaf nodes**: The base inputs (typically model parameters/weights). Created with `Value(data)` and flagged as leaves with `grad = 0` initially.
- **Internal nodes**: Result of an operation on other `Value` objects. They carry the operation label (e.g., `+`, `*`, `tanh`).

## Forward Pass

In the forward pass, each `Value` computes its output from its children:

1. Take the children's output values
2. Apply the mathematical operation (e.g., if `op = '+'`, add them)
3. Store the result as this node's `data`

Example: computing `(a + b) * c`:
- `v1 = Value(a); v2 = Value(b); v3 = Value(c)`
- `v4 = v1 + v2` (creates internal node with `op='+'`, `children=(v1, v2)`)
- `v5 = v4 * v3` (creates internal node with `op='*'`, `children=(v4, v3)`)

When you call `v5.data`, it recursively computes the result: `v4.data + v3.data` → `(a + b) + c`.

## Backward Pass (Backpropagation)

The backward pass is where the magic happens. Starting from the output node, we propagate gradients backward using the [[chain-rule]].

### The Chain Rule

For a function `f(g(x))`, the derivative is: `f'(g(x)) * g'(x)`.

In the multivariate case (multiple inputs): `∂L/∂x = Σ ∂L/∂z_i * ∂z_i/∂x` for all paths from x to L.

### Gradient Accumulation

Each `Value` object has a `grad` attribute (initially 0). During backward pass:
1. Start at the output node with `grad = 1` (since `dL/dL = 1`)
2. For each node, distribute its gradient to its children proportionally via the chain rule
3. Children accumulate (`+=`) their share of the gradient

**In-place accumulation** is crucial: multiple paths to the same node each add their contribution to `grad`.

### Operation-Specific Gradients

Each operation defines its `backward` method implementing the gradient formula:

| Operation | Forward | Backward |
|-----------|---------|----------|
| `+` | `a + b` | `grad` to both children |
| `*` | `a * b` | `grad * b` to a, `grad * a` to b |
| `tanh` | `tanh(x)` | `grad * (1 - tanh²(x))` |

## Leaf Nodes vs Internal Nodes

- **Leaf nodes** (parameters `a`, `b` above) have no children — they are the inputs to the graph
- During backward pass, only leaf nodes actually accumulate gradients; internal nodes just pass gradients through
- When training a neural network, we iterate over leaf nodes to update weights

## Gradient Descent

Once we have gradients (via backpropagation), we perform [[gradient-descent]] to update weights:

```python
learning_rate = 0.01
for p in leaf_nodes:
    p.data -= learning_rate * p.grad
```

The **learning rate** is a hyperparameter that controls how large each update step is. Too high = unstable; too low = slow convergence.

### Weight Update Process

1. Forward pass: compute the loss
2. Backward pass: compute gradients via backpropagation
3. Update: `weight = weight - learning_rate * gradient`

This is repeated for many iterations (epochs) until convergence.

## Loss Functions

The **[[loss-function]]** measures how wrong the network's predictions are. During training, we minimize this.

### Mean Squared Error (MSE)

```python
loss = sum((y_pred - y_true)²) / n
```

Used for regression tasks. The gradient is proportional to the prediction error.

### Cross-Entropy Loss

Used for classification. Better for discrete outputs — the gradient is steeper when the model is very wrong, leading to faster learning early on.

### Why Non-Linearity?

The [[activation-function]] (non-linearity) is what allows neural networks to learn complex, non-linear patterns. Without non-linearities (like `tanh`, `sigmoid`, or `ReLU`), stacking layers would be equivalent to a single linear transformation — no matter how many layers, the network could only learn linear relationships.

**Why it matters:** Real-world data (images, text, speech) has highly non-linear structure. Non-linearities allow the network to approximate any arbitrary function.

### Common Activation Functions

- **tanh**: Maps to [-1, 1]. Popular in older RNNs. `tanh'(x) = 1 - tanh²(x)`
- **sigmoid**: Maps to [0, 1]. Historically popular. Gradient saturates for very large/small inputs.
- **ReLU**: `max(0, x)`. Simple and effective. Widely used in modern networks. Gradient is 0 for negative inputs, 1 for positive.

## How PyTorch Mirrors micrograd

PyTorch's `torch.autograd` is essentially a production-scale version of micrograd's design:

| micrograd | PyTorch |
|-----------|---------|
| `Value` | `torch.Tensor` |
| `Value.data` | `tensor.data` |
| `Value.grad` | `tensor.grad` |
| `Value.children` | Computed graph (via `grad_fn`) |
| `backward()` | `loss.backward()` |
| Manual `backward()` per op | `grad_fn` stored per operation |

PyTorch additionally handles:
- GPU acceleration (CUDA tensors)
- Batched operations (vectorization)
- Sparse gradients
- Higher-order derivatives
- Checkpointing for memory efficiency

But the **core algorithm is identical**: build a graph, compute forward pass, run backward pass, accumulate gradients.

## Neural Network Implementation

A simple neural network in micrograd:

1. **Input layer**: Wrap input data in `Value` objects
2. **Linear transformation**: `y = Wx + b` (weights `W`, bias `b` are `Value` leaf nodes)
3. **Activation**: Apply non-linear function (e.g., `tanh`)
4. **Stack layers**: Repeat for depth
5. **Output layer**: Produce scalar prediction
6. **Loss**: Compare prediction to ground truth
7. **Backpropagate**: Compute gradients
8. **Update weights**: `W.data -= lr * W.grad`

Repeat for many iterations.

## Key Concepts

- [[backpropagation]] — Efficient gradient computation via chain rule
- [[chain-rule]] — Foundation of all differentiation
- [[gradient-descent]] — Weight update algorithm
- [[automatic-differentiation]] — Computing exact gradients automatically
- [[loss-function]] — Measures prediction error (MSE, cross-entropy)
- [[activation-function]] — Non-linearities (tanh, sigmoid, ReLU)
- [[PyTorch]] — Production deep learning framework using autograd
- [[neural-network]] — Composed of layers of weighted transformations
- [[Andrej Karpathy]] — The presenter

## Related Entities
- [[Andrej Karpathy]]
- [[PyTorch]]
- [[Deep Dive into LLMs]]
- [[Intro to Large Language Models]]

## Source
[[raw/transcripts/VMj-3S1tku0]]
