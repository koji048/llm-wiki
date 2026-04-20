# The spelled-out intro to neural networks and backpropagation： building micrograd [VMj-3S1tku0].en

---
title: "Micrograd: Building Neural Networks from Scratch"
created: 2025-01-15
type: entity
tags:
  - micrograd
  - neural-networks
  - backpropagation
  - autograd
  - automatic-differentiation
  - pytorch
  - chain-rule
  - gradient-descent
  - karpathy
  - deep-learning
  - mlp
  - tutorial
sources:
  - raw_transcript.txt
---

# Micrograd: Building Neural Networks from Scratch

## Summary

This wiki entry documents Andrej Karpathy's foundational tutorial on **micrograd**, a minimal scalar-valued automatic differentiation engine that demonstrates the core principles of neural network training. The tutorial spans the complete journey from understanding derivatives at the most fundamental level to implementing a working multi-layer perceptron (MLP) with full backpropagation support, and finally comparing the implementation to production-grade frameworks like PyTorch.

The lecture begins by framing neural networks as mathematical expression graphs, where backpropagation efficiently computes gradients of a loss function with respect to network weights. Karpathy emphasizes that micrograd—at roughly 150 lines of Python code—contains everything fundamentally necessary to train neural networks; everything beyond it (tensors, GPU acceleration, optimized kernels) is purely about efficiency. The tutorial walks through manually computing derivatives using the chain rule, then automates the process by building a `Value` class that tracks computation graphs and propagates gradients via topological sorting.

The implementation extends to a complete neural network library mirroring PyTorch's API: individual `Neuron` objects with weights, biases, and tanh activations; `Layer` objects containing multiple neurons; and `MLP` objects chaining layers together. A full training loop is demonstrated on a binary classification problem using mean squared error loss and gradient descent. Common pitfalls—particularly forgetting to zero gradients between iterations—are highlighted as illustrative bugs that beginners frequently encounter.

The tutorial concludes by exploring PyTorch's actual production implementation of operations like tanh, revealing the layers of complexity (CPU/GPU kernels, multiple data types, complex number support) that production frameworks must handle. Karpathy also demonstrates how custom functions can be registered with PyTorch's autograd system, showing that the same principles taught with micrograd extend directly to industrial-scale deep learning frameworks.

## Key Concepts

### Automatic Differentiation (Autograd)
A technique for automatically computing derivatives of functions expressed as code. Micrograd implements reverse-mode autograd, the same approach used in PyTorch, TensorFlow, and JAX.

### Backpropagation
The algorithm that efficiently computes gradients of a scalar loss with respect to all parameters by applying the chain rule in reverse through a computation graph.

### Computation Graph
A directed acyclic graph (DAG) where nodes represent values and edges represent operations. Forward pass evaluates the graph; backward pass propagates gradients in reverse topological order.

### Chain Rule
The fundamental calculus rule enabling backpropagation: if z depends on y, and y depends on x, then `dz/dx = (dz/dy) × (dy/dx)`. Karpathy's intuitive analogy: if a car is twice as fast as a bicycle, and a bicycle is four times as fast as a walker, the car is 8× faster than the walker.

### The Value Class
Core abstraction wrapping a scalar with:
- `data`: the numerical value
- `grad`: gradient with respect to final output
- `_prev`: child nodes that produced this value
- `_op`: operation that created this value
- `_backward`: function to propagate gradients locally

### Gradient Accumulation
Critical detail: gradients must use `+=` (not `=`) when a variable appears multiple times in an expression, otherwise contributions get overwritten.

### Topological Sort
Algorithm used to determine the order of `_backward()` calls, ensuring a node's gradient is fully accumulated before being propagated to its inputs.

### Neuron
Computes `tanh(Σ wᵢxᵢ + b)` where weights represent synaptic strengths and bias represents "trigger happiness."

### Multi-Layer Perceptron (MLP)
A sequence of fully-connected layers where each layer's output feeds into the next layer's input.

## Major Sections

### Part 1: Foundations (Introduction)
- Introduction to micrograd philosophy
- Mathematical definition of derivatives
- Building the Value class
- Manual chain rule application
- Addition as gradient distributor
- Multiplication's local derivatives

### Part 2: Automation and Training (Middle)
- Implementing chain rule for tanh
- The gradient accumulation bug fix
- Topological sort for automatic backpropagation
- Extended operations (exp, power, division, subtraction)
- PyTorch comparison and verification
- Building Neuron, Layer, and MLP classes
- Full training loop on binary classification
- The zero_grad bug

### Part 3: Production Comparison and Conclusion (End)
- Exploring PyTorch's actual tanh kernels
- CPU vs GPU implementation differences
- Extending PyTorch via `torch.autograd.Function`
- Custom functions as composable "lego blocks"
- Course wrap-up and resources

## Key Takeaways

1. **Neural networks are just mathematical expressions**—backpropagation is a general algorithm that doesn't fundamentally care about neural networks at all.
2. **Micrograd's ~150 lines contain everything essential** for training neural networks; production frameworks add efficiency, not new fundamental ideas.
3. **The chain rule is the workhorse** of deep learning—every operation just needs to know its local derivative to participate in backpropagation.
4. **Addition distributes gradients** unchanged to its inputs; **multiplication swaps and scales** gradients by the other input's value.
5. **Always use `+=` when accumulating gradients** to handle variables that appear multiple times in an expression.
6. **Topological sorting** ensures correct gradient flow—a node's backward must run only after all its consumers have processed.
7. **Forgetting to zero gradients** is one of the most common bugs in neural network training and can subtly destabilize learning.
8. **The training loop is universal**: forward → loss → zero_grad → backward → parameter update.
9. **The same principles scale**: from this scalar-valued engine to GPT-scale models with billions of parameters—only the architecture and efficiency change.
10. **PyTorch can be extended** by subclassing `torch.autograd.Function` and providing forward/backward implementations.

## Notable Quotes

> "Micrograd is what you need to train neural networks; everything else is just efficiency."

> "Neural networks are just mathematical expressions... backpropagation is significantly more general—it doesn't actually care about neural networks at all."

> "The chain rule fundamentally is telling you how we chain these derivatives together correctly."

> "As long as you can do the forward pass of this little function piece that you want to add and as long as you know the local derivative, the local gradients which are implemented in the backward, PyTorch will be able to back propagate through your function."

## Notable Examples

- **Chain rule analogy**: Car (2× bicycle speed) × Bicycle (4× walking speed) = Car is 8× walking speed.
- **Single neuron computation**: `output = tanh(w₁x₁ + w₂x₂ + b)` with random weights initialized between -1 and 1.
- **Binary classification training**: Demonstrating gradient descent on a small dataset using mean squared error loss.
- **PyTorch verification**: Showing that micrograd's outputs match PyTorch's autograd exactly on identical computations.

## Related Entities

- **PyTorch** — Production-grade autograd framework with the same conceptual foundation
- **Backpropagation** — The core algorithm implemented by micrograd
- **Andrej Karpathy** — Creator of micrograd and instructor of the tutorial series
- **Neural Networks: Zero to Hero** — The broader course series this lecture introduces
- **Makemore** — Karpathy's follow-up tutorial building on micrograd concepts
- **GPT / Transformers** — Large-scale models that operate on the same fundamental principles
- **Chain Rule** — Foundational calculus concept enabling backpropagation
- **Gradient Descent** — Optimization algorithm used to update parameters using computed gradients
- **Multi-Layer Perceptron (MLP)** — Architecture built in this tutorial
- **TensorFlow / JAX** — Alternative autograd frameworks using similar principles