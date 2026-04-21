---
title: Deep Dive into LLMs like ChatGPT
created: 2026-04-20
updated: 2026-04-21
type: entity
tags: [LLM, pre-training, alignment, context-window, transformer, tokenization]
sources: [raw/transcripts/7xTGNNLPyMI]
---

# Deep Dive into LLMs like ChatGPT

This video provides a comprehensive technical exploration of how large language models like ChatGPT are trained and function at a deep level. Karpathy breaks down the entire pipeline from raw text to a deployed conversational agent.

## The Two-Stage Training Pipeline

### Pre-training Phase

The first stage is **pre-training**, where the model learns to predict the next token given all preceding tokens. The model is exposed to internet-scale text — roughly trillions of tokens from publicly available sources like Wikipedia, books, code repositories, articles, and forums. The FineWeb dataset (from Hugging Face) is a good reference for what this data looks like.

The objective is deceptively simple: **next-token prediction**. Given a sequence of tokens `t1, t2, ..., tn`, predict `tn+1`. The model learns a probability distribution over the entire vocabulary for what comes next, conditioned on the entire context. This is trained using [[gradient-descent]] on a [[loss-function]] (typically cross-entropy loss over the vocabulary), where the gradient is computed via [[backpropagation]] through the [[transformer]] architecture.

The pre-training process compresses world knowledge — facts, reasoning patterns, language structures, even styles of writing — into the neural network's weights in a lossy, probabilistic manner. The model doesn't "store" facts like a database; it learns statistical relationships that encode these facts implicitly.

**Emergent capabilities** appear non-linearly with scale. At small scale, models can barely complete sentences. At larger scale (dozens to hundreds of billions of parameters), capabilities like reasoning, translation, summarization, and coding emerge suddenly. This is one of the most surprising aspects of LLMs — many abilities are not explicitly taught but arise from scale alone.

### Alignment Phase (Post-training)

Pre-trained models are raw next-token predictors. They need to be shaped into helpful assistants. This is the **alignment** phase.

The first step is **[[SFT]]** (Supervised Fine-Tuning), where human annotators write ideal responses to prompts. The model is fine-tuned on this demonstration data to mimic these responses.

The more powerful step is **[[RLHF]]** (Reinforcement Learning from Human Feedback), which has two sub-components:
1. **Reward Modeling**: A separate model is trained to predict how well a response pleases human labelers
2. **[[PPO]]** (Proximal Policy Optimization): The policy (the LLM) is updated using the reward model to signal which responses humans preferred

More recently, **DPO** (Direct Preference Optimization) has emerged as a simpler alternative to RLHF that avoids the complexity of a separate reward model by directly optimizing against a preference oracle.

## The Transformer Architecture

The underlying architecture is the [[transformer]], introduced in "Attention Is All You Need" (2017). The key innovation is the **[[attention]]** mechanism, which allows every token to attend to every other token in the context simultaneously.

### How Attention Works

Attention computes a weighted sum of values, where the weights depend on the compatibility between queries and keys:
1. Every input token is projected into Query (Q), Key (K), and Value (V) vectors
2. Attention scores are computed as `softmax(QK^T / sqrt(d_k))` where `d_k` is the key dimension
3. The output is the weighted sum of values: `softmax(QK^T)V`

Multi-head attention runs multiple attention operations in parallel, allowing the model to attend to different aspects of the text simultaneously.

### Positional Encoding

Because the transformer has no inherent notion of token order, **positional encoding** is added to inject position information. Original transformers used fixed sine/cosine encodings. Modern models use **RoPE** (Rotary Position Embedding) or **ALiBi** (Attention with Linear Biases), which allow models to generalize to longer sequences than they were trained on.

## Tokenization

The text is converted to integers via a **[[tokenizer]]**. Modern LLMs use **Byte Pair Encoding (BPE)**, SentencePiece, or tiktoken tokenizers. The vocabulary is typically ~100k tokens for GPT-4 class models.

Tokenization has important implications:
- Common words may be a single token; rare words may be split into multiple subword tokens
- The number of tokens in a text is roughly 4/3 the word count for English
- Code is often tokenized inefficiently compared to natural language
- Different languages have different token densities (e.g., Chinese is more token-efficient)

## ChatML and Instruction Format

ChatGPT uses the **ChatML** format (or similar instruction format) to structure conversations. A typical prompt looks like:
```
<system>You are a helpful assistant.</system>
<user>What is the capital of France?</user>
<assistant>Paris.</assistant>
```

The **system prompt** is critical — it sets the behavior, personality, and constraints of the model. The model learns to be guided by these instructions.

## The Context Window

The **[[context-window]]** is the "working memory" of the LLM — the maximum number of tokens it can consider simultaneously. For GPT-4 Turbo, this is 128k tokens. For older models, it might be 4k-8k tokens. Within this window, the model has full attention access to all tokens; outside of it, the model has no memory.

The context is built jointly by the user and the model as the conversation progresses. The model can only "see" what is in the context window.

## Multimodal Aspects

GPT-4V and later models extend beyond text to handle images, PDFs, and other documents. Images are processed by a vision encoder and then fed to the LLM alongside text tokens, allowing the model to reason about visual information.

## Knowledge Cutoff and Limitations

Because the model's knowledge comes from pre-training, it has a **knowledge cutoff** — it doesn't know about events after its training data was collected. Additionally, the knowledge is:
- **Probabilistic**: The model may "hallucinate" facts that sound plausible but are incorrect
- **Compressed**: Fine details may be lost in the compression from text to weights
- **Potentially biased**: The internet text reflects biases in how people write

## Key Concepts

- [[next-token prediction]] — The core training objective
- [[transformer]] — The neural network architecture
- [[attention]] — The key mechanism in transformers
- [[tokenizer]] — Converts text to integer tokens
- [[positional encoding]] — Injects position information
- [[pre-training]] — Learning from internet-scale text
- [[alignment]] — Shaping the model into an assistant
- [[SFT]] — Supervised Fine-Tuning (demonstration learning)
- [[RLHF]] — Reinforcement Learning from Human Feedback
- [[gradient-descent]] — The optimization algorithm
- [[loss-function]] — Cross-entropy loss over vocabulary
- [[chain-rule]] — Foundation of backpropagation
- [[Andrej Karpathy]] — The presenter
- [[How I Use LLMs]] — Practical usage guide

## Related Entities
- [[Andrej Karpathy]]
- [[How I Use LLMs]]
- [[Intro to Large Language Models]]
- [[OpenAI]]

## Source
[[raw/transcripts/7xTGNNLPyMI]]
