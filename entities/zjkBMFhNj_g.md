---
title: Intro to Large Language Models
created: 2026-04-20
updated: 2026-04-21
type: entity
tags: [LLM, emergent-behaviors, token-prediction, AI-safety, transformer]
sources: [raw/transcripts/zjkBMFhNj_g]
---

# Intro to Large Language Models

This talk by Andrej Karpathy is a general-audience introduction to large language models. It explains what LLMs are, how they work at a high level, and what their capabilities and limitations mean for society.

## What is an LLM?

A large language model is, at its core, **just two files**: the **parameters** (weights) of a neural network, and the **run code** that executes those parameters. For example, the Llama 2 70B model consists of:
- A parameter file (~140GB, stored as 2 bytes per parameter)
- A run script (the inference code)

The model is a [[neural-network]] — specifically, a [[transformer]] — trained on internet text to predict the next token.

## Token Prediction: The Core Objective

The training objective is elegantly simple: **predict the next token** given all preceding tokens.

Tokens are pieces of text — not words, but subword units. A [[tokenizer]] breaks text into tokens using algorithms like **BPE** (Byte Pair Encoding), **SentencePiece**, or **tiktoken**.

### Why Subword Tokenization?

- Allows handling any string (including rare words, misspellings, code)
- Keeps vocabulary manageable (typically ~100k tokens for GPT-4 class models)
- Enables cross-lingual generalization (many languages share subword patterns)

### Vocab Size Implications

GPT-4 uses ~100k tokens. This means:
- ~4/3 tokens per English word on average
- Common words = 1 token; rare words may be 3-4 subword tokens
- Code is often less efficient (many rare character sequences)
- Different languages have different token densities

## Pre-training: Compressing the Internet

During **[[pre-training]]**, the model reads trillions of tokens from the internet. It learns to predict what comes next. This process:

1. **Compresses** world knowledge into neural network weights
2. Is **lossy** — not all information survives
3. Is **probabilistic** — the model captures statistical patterns, not facts

The model learns:
- Language structure and grammar
- Factual knowledge embedded in text
- Reasoning patterns
- Writing styles and personas
- World models (implicit)

### Scaling Laws

Model capability improves predictably with:
- **Parameters**: More parameters = more capacity to store patterns
- **Data**: More tokens = more exposure to world knowledge
- **Compute**: More training FLOPs = better optimization

Chinchilla scaling laws suggest optimal ratio: ~20 tokens per parameter for training efficiency.

## Emergent Behaviors

The most surprising property of LLMs is **[[emergent-behaviors]]** — capabilities that appear non-linearly with scale:

- At small scale: next-word prediction, simple completion
- At medium scale: basic reasoning, summarization
- At large scale: complex reasoning, coding, translation, mathematical problem-solving

These abilities are not explicitly taught — they emerge from scale. We don't fully understand why this happens.

## Alignment: Making Models Helpful

Pre-trained models are raw, unfiltered predictors. [[Alignment]] shapes them into assistants.

**Why alignment is necessary:**
- Raw models may generate harmful content
- They don't naturally follow instructions
- Without alignment, they're not useful as assistants

### What Can Go Wrong Without Alignment

- Generating misinformation, hate speech, or harmful instructions
- Refusing to help with legitimate requests
- Being manipulative or deceptive
- Lack of safety guardrails

### Alignment Techniques

1. **[[SFT]]** (Supervised Fine-Tuning): Fine-tune on human-written demonstration responses
2. **[[RLHF]]** (Reinforcement Learning from Human Feedback): Use reward modeling and PPO to optimize for human preferences
3. **Constitutional AI**: Use a set of principles to guide behavior

## The Context Window

The **[[context-window]]** is the "working memory" of the LLM — the maximum number of tokens it can consider simultaneously.

Key properties:
- For GPT-4 Turbo: 128k tokens
- For older models: 4k-8k tokens
- Within the context: full [[attention]] to all tokens
- Outside the context: no memory at all

The model has no memory beyond the current context window. This is a fundamental limitation — it cannot "learn" during inference; each conversation starts fresh (unless using memory features).

**Implications:**
- Very long documents may exceed the context window
- Important information at the start of a long conversation may be "forgotten"
- The model can only reason about what fits in context

## Positional Encoding

Transformers don't naturally process sequences — they process sets. **Positional encoding** injects position information:

- **Original (sin/cos)**: Fixed encodings added to token embeddings
- **[[RoPE]]** (Rotary Position Embedding): Rotates queries and keys to encode relative position; allows generalization to longer sequences
- **[[ALiBi]]** (Attention with Linear Biases): Adds linear bias to attention scores based on distance

Modern models typically use RoPE, which supports longer context than trained on.

## Attention Mechanism

The [[attention]] mechanism is the core innovation of transformers. It allows every token to attend to every other token:

1. Compute attention scores: `score(q_i, k_j) = q_i · k_j / sqrt(d_k)`
2. Softmax to get weights: `a_ij = softmax(scores)_j`
3. Weighted sum: `output_i = Σ a_ij * v_j`

**Why it matters:**
- Captures long-range dependencies (no vanishing gradients)
- Parallelizable (unlike RNNs)
- Allows the model to focus on relevant context

## Limitations

LLMs have significant limitations:

### Hallucinations

The model may generate plausible-sounding but factually incorrect information. This happens because:
- The model is a next-token predictor, not a knowledge retriever
- It may confidently assert things that sound right but aren't
- Fine details are often wrong; only the "gist" tends to be correct

### Knowledge Cutoffs

The model only knows what was in its training data. It cannot:
- Know about events after its training cutoff
- Access real-time information (unless integrated with search)
- Learn new information during a conversation

### Probabilistic Nature

LLMs are fundamentally probabilistic:
- Running the same prompt twice may give different outputs
- Small changes to prompts may significantly change outputs
- The model can be inconsistent on the same question

### Factual Errors

Even on well-documented facts, the model may:
- Confuse similar entities or events
- Confabulate details that don't exist
- Be wrong in subtle ways that are hard to detect

## Key Concepts

- [[tokenizer]] — Converts text to integer tokens (BPE, SentencePiece, tiktoken)
- [[pre-training]] — Learning from internet-scale text via next-token prediction
- [[alignment]] — Shaping the model into a helpful assistant
- [[transformer]] — The neural network architecture
- [[attention]] — The key mechanism enabling contextual understanding
- [[context-window]] — The working memory constraint
- [[emergent-behaviors]] — Capabilities appearing non-linearly with scale
- [[RLHF]] — Reinforcement Learning from Human Feedback
- [[Andrej Karpathy]] — The presenter
- [[Deep Dive into LLMs]] — Deeper technical dive

## Related Entities
- [[Andrej Karpathy]]
- [[Deep Dive into LLMs]]
- [[ChatGPT]]
- [[OpenAI]]

## Source
[[raw/transcripts/zjkBMFhNj_g]]
