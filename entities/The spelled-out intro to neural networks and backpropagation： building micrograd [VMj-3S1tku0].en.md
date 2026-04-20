# The spelled-out intro to neural networks and backpropagation： building micrograd

---
title: "The spelled-out intro to neural networks and backpropagation: building micrograd"
created: 2026-04-20
type: entity
tags: [neural-networks, backpropagation, autograd, micrograd, pytorch]
sources: [raw/transcripts/The spelled-out intro to neural networks and backpropagation： building micrograd [VMj-3S1tku0].en.txt]
---

# The spelled-out intro to neural networks and backpropagation: building micrograd

## Summary
Andrej Karpathy delivers a from-scratch lecture building **micrograd**, his ~150-line autograd library (engine.py ~100 lines, nn.py the small neural net library). Starting in a blank Jupyter notebook, he constructs a scalar-valued `Value` class that records a computational DAG via `_prev` (children), `_op` (operation label), `data`, `grad`, and a `_backward` closure. He derives backpropagation as "a recursive application of chain rule backwards through the computation graph," first manually through expressions like `L = d*f` where `d = a*b + c`, then automates it via topological sort and a `.backward()` method.

The lecture develops operations incrementally — addition, multiplication, `tanh` (as a single op), then `exp`, `__pow__` (using the power rule), division (as `x**-1`), subtraction, and `__rmul__` — and demonstrates that **granularity is arbitrary**: any operation works as long as you can express the local derivative. A critical bug is fixed by replacing `=` with `+=` in `_backward` (justified by the multivariate chain rule) so gradients accumulate when variables are reused. Karpathy then builds `Neuron`, `Layer`, and `MLP` classes mirroring PyTorch's API, trains a 41-parameter MLP on 4 examples using mean squared error loss, exhibits the classic "forgot to zero_grad" bug, and concludes by comparing micrograd line-for-line with PyTorch's tanh backward (buried in a `BinaryOpsKernel` after 2,800 search hits) and showing how to extend PyTorch with custom `autograd.Function` subclasses.

Throughout, Karpathy emphasizes that neural nets — even at GPT scale with hundreds of billions of parameters — are "just mathematical expressions" taking data and weights as input, producing a loss, and trained by gradient descent. The same principles scale; production frameworks (PyTorch, JAX) differ only by using n-dimensional tensors for parallelism and accumulating engineering complexity for device/type support.

## Key Concepts
- **Autograd engine**: Short for "automatic gradient"; a system that builds a computational graph during forward computation and automatically computes gradients via backpropagation. Micrograd implements this at scalar granularity for pedagogy; PyTorch and JAX do the same over tensors.
- **Backpropagation**: A recursive application of the chain rule backward through the computational graph that efficiently evaluates the gradient of a loss with respect to all weights. Karpathy calls it "the mathematical core of any modern deep neural network library."
- **Value class**: Micrograd's wrapper around a scalar holding `.data`, `.grad`, `_prev` (set of children), `_op` (operation string), `label`, and `_backward` (closure implementing local chain rule). Supports `+`, `*`, `tanh`, `exp`, `**k`, `/`, `-`, and reverse ops.
- **Chain rule**: If `z` depends on `y` depends on `x`, then `dz/dx = (dz/dy)·(dy/dx)`. Intuition given via the car/bicycle/walker analogy — 2×4 = 8× faster. Local derivatives at each node are multiplied by the upstream gradient.
- **Local derivative & operation behaviors**: A `+` node routes gradients unchanged to all children (local derivative = 1); a `*` node routes the *other* operand's data; `tanh` local derivative is `1 - t²`; `exp` local derivative equals the output itself; `x^k` uses the power rule `k·x^(k-1)`.
- **Topological sort**: A DAG ordering such that every node appears after its dependencies. Built recursively with a `visited` set; backward pass iterates this list in reverse, calling each node's `_backward`.
- **Gradient accumulation (+=)**: When a variable is used in multiple paths, gradients from each path must *sum* (multivariate chain rule). Using `=` instead of `+=` in `_backward` silently overwrites contributions — the bug surfaces in expressions like `a + a`.
- **Neuron / Layer / MLP**: A `Neuron` computes `tanh(Σ w_i·x_i + b)` with random weights in [-1, 1] and a bias controlling "overall trigger happiness." A `Layer` is independent neurons sharing inputs. An `MLP` chains layers. The lecture's demo network has 41 parameters.
- **Gradient descent update**: `p.data += -lr * p.grad` — the negative sign is essential because gradients point toward *increasing* loss. Learning rate tuning is described as "a subtle art": too small is slow, too large causes the loss to explode.
- **zero_grad bug**: Because `_backward` uses `+=`, gradients persist across iterations unless explicitly reset to 0.0 before each backward pass. Karpathy cites this as mistake #3 in his "most common neural net mistakes" tweet.
- **Scalar vs. tensor**: Micrograd operates on single scalars for clarity; PyTorch uses n-dimensional tensors (arrays of scalars) for parallelism and GPU efficiency. The underlying math is identical.
- **Granularity is arbitrary**: You can implement `tanh` as one atomic op or decompose it into `exp`, `+`, `-`, `/`. Both produce identical forward values and leaf gradients, proving the abstraction level is a design choice.

## Major Sections

### Introduction and Motivation (Section 1)
Karpathy introduces micrograd, shows an example expression with inputs `a=-4, b=2` producing `g.data = 24.7`, calls `g.backward()` yielding `a.grad = 138, b.grad = 645`, and frames neural nets as just mathematical expressions from data+weights to a loss.

### Numerical Derivatives (Section 2)
Using `f(x) = 3x² - 4x + 5`, he demonstrates derivatives via the limit definition with `h = 0.001`: slope is 14 at x=3, negative at x=-3, ~0 at the parabola's minimum. Extends to multivariable `d = a*b + c`.

### Building the Value Class (Section 3)
Implements `__add__`, `__mul__`, `__repr__`, and adds `_prev` (as a set), `_op`, and `label` attributes. Introduces a Graphviz-based `draw_dot` visualization with fake "op nodes" as circles between value rectangles.

### Manual Backpropagation (Sections 4–6)
With `L = d*f, d = e+c, e = a*b`, derives gradients by hand: `L.grad=1`, `f.grad=d.data=4`, `d.grad=f.data=-2`, `c.grad=e.grad=-2` (plus routes), `a.grad=6, b.grad=-4`. Verifies each via perturbation ("gradient check"). Demonstrates one optimization step moving L from -8 to -7.

### Building a Neuron with tanh (Sections 6–7)
Constructs a 2-input neuron `tanh(x1·w1 + x2·w2 + b)`, implements `.tanh()` on Value. With bias set to **6.8813735870...** for clean numbers, manually backpropagates: `o.grad=1`, `n.grad = 1-o² = 0.5`, and with `x1=2, x2=0, w1=-3, w2=1`: `w1.grad=1.0, w2.grad=0, x1.grad=-1.5, x2.grad=0.5`.

### Automating Backward (Sections 8–9)
Adds `_backward` closures to each operation, implements topological sort with a `visited` set, consolidates into a `.backward()` method on Value. Surfaces the `a + a` bug (produces grad=1 instead of 2) and fixes it by switching all `_backward` assignments to `+=`. Adds operand coercion for scalars and `__rmul__`.

### Extending Operations (Section 10)
Implements `exp`, `__pow__` (with int/float assertion and power rule), `__truediv__` as `self * other**-1`, and subtraction. Decomposes `tanh(n)` as `(e^(2n) - 1) / (e^(2n) + 1)` and verifies identical gradients.

### PyTorch Parallel and NN Modules (Section 11)
Reproduces the neuron in PyTorch using double-precision single-element tensors with `requires_grad=True`, confirming forward = **0.707** and gradients **0.5, 0, -1.5, 1.0**. Builds `Neuron`, `Layer`, `MLP` classes.

### Training (Sections 12–14)
Defines loss as `sum((yout - ygt)**2 for ygt, yout in zip(ys, ypred))`. Implements `parameters()` on all modules (41 params total). Manual gradient descent drops loss from 4.84 → 4.36 → ... → 7e-9. Builds training loop, discovers and fixes the zero_grad bug, summarizes neural nets as scaled-up versions of the same mechanism (noting GPT uses cross-entropy loss).

### Micrograd Codebase and PyTorch Comparison (Section 15)
Tours `engine.py` (Value with ReLU instead of tanh), `nn.py` (Neuron/Layer/MLP with Module parent class), and `demo.ipynb` (binary classification with batching, max-margin loss, L2 regularization, learning rate decay). Finds PyTorch's tanh backward in a `BinaryOpsKernel` (2,800 results, 406 files) with formula `a * (1 - b*b)` — identical math. Shows custom `torch.autograd.Function` extension.

## Key Takeaways
- Backpropagation is just the chain rule applied recursively backward through a DAG; understanding the gradient through a single node (especially `+`) is understanding all of backprop.
- A `+` node routes gradients unchanged to all children; a `*` node swaps operands when propagating gradients.
- Gradients must *accumulate* (`+=`, never `=`) to correctly handle variables used multiple times — a direct consequence of the multivariate chain rule.
- Operation granularity is a free parameter: implement `tanh` atomically or decompose into `exp/+/−/÷` — results are identical as long as local derivatives are correct.
- Always call `zero_grad` before `.backward()`; forgetting is one of the most common neural net bugs and only hides itself on trivially easy problems.
- The gradient descent update is `p.data += -lr * p.grad`; the negative sign matters because the gradient points toward increasing loss.
- Learning rate tuning is "a subtle art" — too small is slow, too large causes divergence because local gradient info breaks down over large steps.
- Neural nets with billions or trillions of parameters (e.g., GPT) use the same mathematical machinery as this 41-parameter MLP — the differences are loss function (cross-entropy), optimizer refinements, and engineering scale.
- Micrograd captures the essence of autograd in ~100 lines; PyTorch's complexity comes from tensor parallelism, device/dtype handling, and engineering — not from a different algorithm.

## Notable Quotes
> "Backpropagation is a recursive application of chain rule backwards through the computation graph."
> "If you understand the gradient for this node, you understand all of backpropagation and all of training of neural nets basically."
> "A plus node literally just routes the gradient."
> "We don't necessarily need to have the most atomic pieces — you can define operations at arbitrary granularity, as long as you know the local derivative."
> "You forgot to zero_grad before .backward()."
> "A massive blob of simulated neural tissue."

## Related Entities
[[PyTorch]], [[JAX]], [[Multi-Layer Perceptron]], [[Chain Rule]], [[Gradient Descent]], [[Graphviz]], [[GPT]], [[Andrej Karpathy]], [[tanh activation]], [[ReLU]], [[Stochastic Gradient Descent]]