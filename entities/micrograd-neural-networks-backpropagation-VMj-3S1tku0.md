---
title: The spelled-out intro to neural networks and backpropagation: building micrograd
created: 2026-04-20
updated: 2026-04-21
type: entity
tags: [video, neural-networks, backpropagation, micrograd, karpathy, tutorial, autograd, deep-learning, python]
sources: []
---

# The spelled-out intro to neural networks and backpropagation: building micrograd

## Overview
Andrej Karpathy walks through building **micrograd**, a minimal automatic differentiation (autograd) engine, from scratch in a Jupyter notebook. Starting from the concept of a derivative, he iteratively builds up a `Value` object class that wraps scalars, implements addition and multiplication operations that maintain an expression graph (via `prev`/`children` pointers), adds a `backward()` method that recursively applies the chain rule to compute gradients, then wraps Values into Neurons, Layers, and finally a full MLP (Multi-Layer Perceptron). The lecture culminates in a training loop using Mean Squared Error loss and gradient descent. Karpathy's central claim: **micrograd's ~150 lines of code contain the entire intellectual core of neural network training; everything else in PyTorch is efficiency.**

## Key Concepts

- **Derivative (d/dx)**: Measures how a function's output changes when its input changes by a tiny amount `h`. Intuitively: "if you nudge the input, how does the output change?" Karpathy emphasizes this is the fundamental quantity needed for learning.

- **Chain Rule**: The recursive calculus rule that backpropagation is built on. If `z` depends on `y` which depends on `x`, then `dz/dx = (dz/dy) * (dy/dx)`. Multiplication of local derivatives propagates gradient signals backwards through the expression graph.

- **Expression Graph / Computation Graph**: A directed acyclic graph (DAG) where nodes are `Value` objects and edges (`prev`, `children`) record which values contributed to which. This graph structure is what enables automatic differentiation — traversing it backwards gives all gradients.

- **Forward Pass**: Evaluating the mathematical expression (neural network) on input data to produce an output (or loss). Each operation creates new `Value` objects that remember their parents.

- **Backward Pass (Backpropagation)**: Starting from the output node with gradient 1.0, recursively call `backward()` on each node's children, multiplying local gradients via the chain rule, accumulating gradients on each `Value.data` leaf.

- **Value Object**: The core data structure — wraps a scalar `data` value, stores a `grad` (gradient), and maintains a `prev` set of parent values and an `op` string describing the operation that created it (e.g., `+`, `*`, `tanh`).

- **Neuron**: A single perceptron unit — weights `w`, bias `b`, input `x` → computes `dot(w, x) + b` → passes through a non-linearity (e.g., `tanh`) → outputs a scalar `Value`.

- **Layer**: A list of neurons all sharing the same input. Each neuron produces one output value.

- **MLP (Multi-Layer Perceptron)**: A stack of layers where the output of layer `i` is the input to layer `i+1`. Implemented as a Python list of layers.

- **Mean Squared Error (MSE) Loss**: `L = (1/n) * Σ(y_pred - y_target)²`. The single scalar output that the backward pass originates from. Low loss = predictions match targets.

- **Gradient Descent**: After `backward()`, each learnable parameter `p` is nudged: `p.data -= learning_rate * p.grad`. This causes loss to decrease when the gradient is negative (and vice versa), iteratively improving predictions.

- **Learning Rate**: A small scalar (e.g., 0.01–0.1) controlling the step size of each gradient descent update. Too large = unstable; too small = slow convergence.

## Major Sections

### 1. Introduction & Motivation (~0:00–8:00)
Karpathy introduces micrograd as an autograd engine — the mathematical core of any neural network library like PyTorch or JAX. He shows the two-file micrograd codebase (`engine.py` + `nn.py`) and makes his central claim: ~150 lines is all you need; everything else is engineering efficiency. He notes he wrote micrograd specifically so people can understand how things work at the fundamental level.

### 2. Derivatives Intuitively (~8:00–20:00)
Using a simple scalar function `f(x)` plotted as a parabola, Karpathy walks through the definition of a derivative as `lim(h→0) [f(x+h) - f(x)] / h`. He interprets it as "how does the function respond to a tiny nudge in the input?" He extends this to functions of multiple variables (a, b, c → d), checking gradients numerically by perturbing inputs by a small `h` and seeing the effect on the output.

### 3. Building the `Value` Class (~19:00–30:00)
Karpathy creates a `class Value` that wraps a scalar `data`. It gets `_prev` (set of parent values) and an `op` label. Addition (`__add__`) and multiplication (`__mul__`) are implemented as dunder methods that create new `Value` objects, setting their `_prev` to include both operands. This is the expression graph.

### 4. Forward Pass (~30:00–33:00)
Building a simple expression like `d = (a * b) + c` using Value objects — calling `.data` on any Value gives its scalar. The forward pass evaluates the entire expression graph, producing a final output Value.

### 5. Backward Pass & Chain Rule (~33:00–50:00)
Calling `backward()` on the output Value initiates backpropagation. The chain rule is explained as the multiplication of local derivatives: if `L → ... → y → x`, then `dL/dx = dL/dy * dy/dx`. Karpathy implements `backward()` recursively: each Value node calls `backward()` on its parents, passing `grad * local_grad` (the parent's gradient times the local derivative).

- **Addition** backward: `local_grad = 1.0` (gradient passes through unchanged to both children).
- **Multiplication** backward: `local_grad = other_child.data` (the value of the other operand).

### 6. Visualization with `drawdot` (~26:00–45:00)
Karpathy adds a `drawdot()` utility that renders the expression graph using Graphviz, annotating nodes with their data values and labels. This helps visualize how complex expressions form deep computation graphs.

### 7. Non-linearities: tanh (~50:00–1:05:00)
Adding the `tanh` activation function. He shows how to derive the local gradient: `d/dx tanh(x) = 1 - tanh²(x)`. He explains the chain rule in its "computer science" form as a message-passing API — each node type knows how to send gradient messages to its parents based on its local derivative.

### 8. Building the `Neuron` Class (~1:30:00–1:55:00)
The Neuron class holds a list of weights `self.w` (each a `Value`) and a bias `self.b`. The `__call__(x)` method computes `sum(wi * xi) + b` then applies `tanh`. Weights are initialized randomly. Each Value parameter is tracked via `self.parameters = [self.w, self.b]`.

### 9. Building the `Layer` Class (~1:45:00–1:52:00)
A Layer holds a list of `nin` Neurons and computes their outputs in parallel. It takes a vector input and returns a list of Value outputs (one per neuron).

### 10. Building the MLP (~1:50:00–2:00:00)
An MLP is a list of Layers. The `__call__(x)` method sequentially passes data through each layer, applying non-linearities. The MLP takes an input dimension and a list of layer sizes (e.g., `[4, 4, 1]` = 4-input → 4-neuron hidden → 1-neuron output).

### 11. Loss Function & Training Loop (~1:55:00–2:10:00)
Mean Squared Error loss is computed over all examples: `L = mean((y_pred - y_target)²)`. The training loop:
1. **Forward pass**: `ypred = mlp(x)` → compute loss `L`
2. **Backward pass**: `L.backward()` — fills in `grad` for every parameter
3. **Gradient descent step**: for each parameter `p`: `p.data -= lr * p.grad`
4. **Zero gradients**: Reset grads before next iteration (or re-build the graph)

Karpathy demonstrates loss decreasing from ~4.84 to ~4.36 after one step, confirming the network learned.

### 12. Connecting to PyTorch Internals (~2:22:00–2:25:00)
Karpathy shows PyTorch's actual CUDA kernel for `tanh` (from GitHub), revealing the same `1 - tanh²(x)` derivative formula buried inside a massively optimized GPU kernel. He explains that PyTorch's autograd engine works the same way as micrograd — you just register new ops via `torch.autograd.Function` with `forward` and `backward` methods. Everything is composable Lego blocks.

### 13. Closing (~2:24:00–2:26:00)
Karpathy concludes: "I hope you enjoyed building out micrograd with me. Everything else is just Lego blocks on top of this foundation."

## Notable Quotes

> "You can understand how things work at the fundamental level and then you can speed it up later."

> "Micrograd is what you need to train your networks and everything else is just efficiency."

> "Fundamentally, backpropagation is just the chain rule of calculus."

> "We're going to recursively apply the chain rule from calculus and what that allows us to do then is we're going to evaluate basically the derivative of g with respect to all the internal nodes."

> "This is the only thing you have to tell PyTorch and everything would just work."

> "So I hope you enjoyed building out micrograd with me. I hope you find it interesting, insightful."

## Key Takeaways

1. **Backpropagation is the chain rule**: Every gradient signal flowing backward through a neural network is just `upstream_grad * local_gradient`. This is the entire algorithm — all the machinery of modern DL frameworks is just efficiency on top of this.

2. **Expression graphs enable automatic differentiation**: By having each Value object remember its parents (`_prev`) and operation (`op`), the backward pass can traverse the exact computation path in reverse order, applying the correct local gradient formula for each op type.

3. **A 150-line autograd engine is sufficient to train neural networks**: The core ideas require no tensor operations, no GPUs, no complex framework — just scalar values, a few math operations, and recursion.

4. **Every deep learning framework is composable Lego blocks**: PyTorch's `autograd.Function` lets you register custom forward/backward pairs. Micrograd's Value class with `__add__`, `__mul__`, `tanh` methods is the same pattern — you extend it by implementing the local gradient for each new operation.

5. **The training loop is simple**: forward pass → compute loss → `backward()` → gradient descent step → zero gradients → repeat. The complexity is in the mathematics of the derivatives and the engineering of efficient kernels.

## Related Entities

[[deep-dive-into-llms-7xTGNNLPyMI]] — Same author (Andrej Karpathy); covers transformer architecture, pre-training, RLHF, and the broader LLM lifecycle
[[how-i-use-llms-EWvNQjAaOHw]] — Same author; Karpathy's practical perspective on using LLMs day-to-day
[[karpathy-llm-wiki]] — The LLM Wiki pattern that this wiki implements

## Source

https://www.youtube.com/watch?v=VMj-3S1tku0
