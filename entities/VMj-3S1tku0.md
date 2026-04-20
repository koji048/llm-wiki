---
title: Building micrograd from Scratch
created: 2026-04-20
updated: 2026-04-20
type: entity
tags: ["neural networks", "backpropagation", "autograd", "PyTorch"]
sources: [raw/transcripts/VMj-3S1tku0]
---

# Building micrograd from Scratch

In this tutorial, Andrej Karpathy provides a hands-on walkthrough of building a small automatic differentiation (autograd) engine, named micrograd, from the ground up. Starting with the concept of a single neuron, he methodically constructs a neural network, explaining the core mechanics of deep learning. The primary focus is on demystifying the backward pass, or backpropagation, which is essential for training neural networks. Karpathy clearly explains how the chain rule from calculus is applied to calculate gradients for every parameter in the network. He covers the forward pass, the calculation of a loss function to measure error, and the use of gradient descent to optimize the network's weights. This foundational approach provides a deep, intuitive understanding of how modern deep learning frameworks like PyTorch function internally, stripping away the abstraction to reveal the underlying mathematical operations that enable machines to learn from data.

## Key Concepts
- Backpropagation
- Gradient Descent
- Chain Rule
- Loss Function
- Automatic Differentiation

## Related Entities
- [[Andrej Karpathy]]
- [[Deep Dive into LLMs]]
- [[PyTorch]]

## Source
[[raw/transcripts/VMj-3S1tku0]]
