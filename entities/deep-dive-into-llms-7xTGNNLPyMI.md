---
title: Deep Dive into LLMs like ChatGPT
created: 2026-04-20
updated: 2026-04-21
type: entity
tags: [video, llm, karpathy, tutorial, deep-learning, transformer, rlhf]
sources: []
---

# Deep Dive into LLMs like ChatGPT

## Overview
This is a comprehensive ~3.5 hour technical deep dive into Large Language Models (LLMs) like ChatGPT, presented by Andrej Karpathy. The talk covers the entire lifecycle of an LLM—from pre-training on internet-scale data, through the transformer architecture, to post-training alignment techniques like SFT and RLHF—and concludes with the newer "thinking" models that use chain-of-thought reasoning to achieve dramatic improvements on verifiable tasks.

## Key Concepts

- **Token / Tokenization**: Text is broken into subword tokens (not full words). The vocabulary is typically 10K-100K tokens. Tokens are the fundamental unit of LLM processing—every forward pass predicts the next token in sequence.

- **Transformer Architecture**: The neural network backbone. Tokens flow through layers of self-attention and matrix multiplications. A fixed amount of compute happens per token per forward pass. This is fundamentally different from human cognition, which can iterate.

- **Pre-training**: The first phase where a model learns to predict the next token from massive internet text (10TB+). Done on thousands of GPUs for months. Results in a "base model" that completes documents but doesn't converse.

- **Base Model**: A model trained purely on next-token prediction. It may respond to questions with more questions, complete code, or exhibit other "weird" behaviors. It's a statistical mirror of internet text.

- **Assistant Model**: A base model that has been aligned to be helpful through fine-tuning. Responds to questions directly rather than continuing documents.

- **SFT (Supervised Fine-Tuning)**: Second phase where human labelers write ideal responses to prompts. Creates conversations used to fine-tune the base model into an assistant. Datasets like UltraChat contain millions of mostly synthetic conversations.

- **Reward Model**: A trained neural network that scores model outputs based on human preferences. Used to guide reinforcement learning.

- **RLHF (Reinforcement Learning from Human Feedback)**: Third phase using the reward model to optimize the assistant. Sample many completions, score them, encourage high-scoring ones. Limited to ~100-200 updates before reward gaming begins.

- **"Thinking" Models / Chain of Thought**: Newer models (like o1, DeepSeek R1) that allocate extended "thinking tokens" internally. They work through problems step-by-step like human internal monologue, achieving much higher accuracy on verifiable reasoning tasks.

- **Hallucination**: Models confidently make up facts because they statistically imitate their training set. They don't have access to the internet or databases—they're "statistical token tumblers."

- **Swiss Cheese Model**: LLMs have capabilities with holes. They may excel at complex reasoning but fail at simple mental arithmetic or counting—because these weren't emphasized in training data.

- **System Message**: A special prompt at the start of a conversation that hardcodes behavior/instructions for the model.

## Major Sections

### 1. Introduction & What are LLMs?
Karpathy opens by explaining LLMs as neural networks that predict the next token. He emphasizes they are **not** intelligent agents—they statistically imitate text patterns from their training data. The core task is always: given all previous tokens, predict the next one.

### 2. Tokenization Deep Dive
Detailed walkthrough of how text becomes tokens. Demonstration using the tokenizer playground. Key insight: token limits (e.g., 128K context windows) and why models sometimes can't count letters or do mental arithmetic—their representation is at the token level, not character level.

### 3. Pre-training Stage
- Internet-scale data collection (filtered web pages, code, books)
- Thousands of GPUs training for months
- Scaling laws: more parameters + more data = better performance
- Emergent capabilities at scale
- The base model is the result

### 4. Base Model Behavior
Live demo with Falcon 7B showing hallucinations (e.g., inventing a fake author "Orson Kovat"). Base models don't know they don't know—they statistically answer based on training patterns.

### 5. Post-training: SFT
Introduction to InstructGPT paper (2022). Human labelers hired on Upwork/scale AI create prompt-response pairs. Companies write labeling instructions guiding humans to create "ideal assistant responses." Datasets like UltraChat contain millions of synthetic (LLM-generated, human-edited) conversations.

### 6. Post-training: Reward Model
Train a neural network to score model outputs. Human labelers rank multiple responses. The reward model learns to predict human preferences.

### 7. Post-training: RLHF
- Sample many completions for a prompt (could be 100s-1000s per prompt)
- Score each using the reward model
- Use reinforcement learning to encourage high-scoring responses
- **Critical constraint**: RLHF can only run for ~100-200 updates before it starts gaming the reward model ("you'll never win the game against a giant neural net")
- After that, you must stop and ship

### 8. Tool Use & Agents
Models can be augmented with tools (web search, code execution). Demo: ChatGPT using web search to cite real sources for a query about Orson Kovat. The web search results are stuffed into context, and the model references them.

### 9. System Messages
Hardcoded instructions at conversation start. Used to set model identity, behavior rules, or override default behavior.

### 10. "Thinking" Models & Chain of Thought
New frontier. Models allocate extended internal tokens to "think." Like human internal monologue—they work through problems step-by-step.

Key demonstrations:
- Math problems: "Use code" to solve counting dots—model can't count directly, but can write Python
- Extended thinking: models explore multiple solution paths, backtrack, try alternatives
- Result: dramatic accuracy improvements on verifiable domains (math, code, reasoning)
- Comparison to AlphaGo's Move 37: models may find strategies no human thought of

### 11. Verifiable vs Unverifiable Domains
- **Verifiable**: Math, code—easy to check correctness automatically. RL works well.
- **Unverifiable**: Creative writing, jokes—requires human evaluation. Harder to optimize.
- Open question: Do thinking strategies transfer from verifiable to unverifiable domains?

### 12. Limitations & Swiss Cheese Model
- Hallucinations: models don't know what they don't know
- Mental arithmetic breaks
- Counting failures
- Comparing decimals (9.11 < 9.9) may fail
- May do complex problems but fail simple ones
- Finite compute per token limits capability

### 13. Where to Find Models
- Proprietary: chat.openai.com, gemini.google.com
- Open weights: Together.ai playground, Hugging Face
- Base models harder to find—all inference providers target assistants

## Notable Quotes

> "These models are statistical token tumblers. They just try to sample the next token in the sequence."

> "RL is extremely good at finding just the ways to trick it. You'll never win the game against a giant neural net."

> "You always run RLHF for maybe a few hundred updates, then you have to crop it and you are done."

> "The models will suffer from hallucinations because these models again we just talked about it, they don't have access to the internet, they're not doing research."

> "This is a Swiss cheese capability and we have to be careful with that."

> "It's a lossy simulation of a human that is restricted in this way."

> "These models are capable of analogies no human has had."

## Key Takeaways

1. **LLMs are next-token predictors**: At their core, all LLMs do is predict the next token given all previous tokens. Everything else emerges from this simple objective.

2. **Pre-training at scale creates "base models"**: Large-scale neural language modeling on internet text produces models that statistically imitate human-written documents but don't truly "understand."

3. **Post-training converts base models to assistants**: SFT (human-written responses) and RLHF (reward-based optimization) are required to create helpful assistants from raw base models.

4. **RLHF has strict limits**: Running too long causes reward gaming. Only ~100-200 updates before the model must be shipped to avoid exploitation.

5. **"Thinking" models represent a new paradigm**: Extended chain-of-thought reasoning allows models to achieve unprecedented accuracy on verifiable problems by mimicking internal human monologue, but it's still early and limited to domains with clear correctness criteria.

## Related Entities

[[karpathy-llm-wiki]] - Same author, comprehensive LLM resources
[[how-i-use-llms-EWvNQjAaOHw]] - Follow-up practical video on using LLMs
[[intro-to-large-language-models-zjkBMFhNj_g]] - Introductory talk (earlier version)
[[micrograd-neural-networks-backpropagation-VMj-3S1tku0]] - Neural network fundamentals (prerequisite)
[[deepseek-r1-reasoning-model]] - Mentioned thinking model example
[[instruct-gpt-paper]] - Reference paper for alignment techniques

## Source
https://www.youtube.com/watch?v=7xTGNNLPyMI
