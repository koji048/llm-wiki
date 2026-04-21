---
title: Wiki Index
created: 2026-04-19
updated: 2026-04-21
type: meta
tags: [meta]
---

# Wiki Index

> Content catalog. Every wiki page listed under its type with a one-line summary.
> Read this first to find relevant pages for any query.
> Last updated: 2026-04-21 | Total pages: 49

## Entities
<!-- Alphabetical within section -->

- [[andrej-karpathy]] — AI researcher and educator; creator of micrograd, llm.c, and the LLM Wiki pattern; former OpenAI/Tesla
- [[anthropic-agent-skills]] — Anthropic open standard for AI agent skills; progressive disclosure, 16 skill types, skill-creator iterative workflow, best practices; compared to Hermes Agent and GStack
- [[deep-dive-into-llms-7xTGNNLPyMI]] — Comprehensive deep dive into LLMs like ChatGPT (3.5hr); tokenization, Transformer, pre-training, SFT, RLHF, tool use, Thinking models
- [[deepseek-r1-reasoning-model]] — DeepSeek's reasoning model; pioneered RL-based thinking model methodology; emergent behaviors, AIME accuracy scaling with response length
- [[fineweb]] — High-quality pre-training dataset (~44TB, 15T tokens) derived from Common Crawl with aggressive URL/language filtering
- [[gpt-4]] — OpenAI's 4th-gen LLM; multimodal, ~100k token vocabulary via cl100k_base, RLHF-aligned
- [[how-i-use-llms-EWvNQjAaOHw]] — Practical guide to using LLMs (2hr); context window, search tools, Python execution, custom GPTs, voice I/O, image generation
- [[instruct-gpt-paper]] — OpenAI paper (2022) introducing SFT + RLHF pipeline; hired Upwork/Scale AI labelers for 100K instruction-following conversations
- [[intro-to-large-language-models-zjkBMFhNj_g]] — Andrej Karpathy 1hr intro; LLM as two files, pre-training as lossy compression, fine-tuning, RLHF, tool use, LLM OS paradigm, security
- [[llama-2]] — Meta's open-weight LLM family (7B–70B); Karpathy's two-files case study; 140GB params + 500-line C runfile
- [[micrograd-neural-networks-backpropagation-VMj-3S1tku0]] — Building micrograd from scratch; derivatives, chain rule, Value class, forward/backward pass, Neurons, Layers, MLP, MSE loss, gradient descent
- [[microgpt]] — ~300-line dependency-free GPT in pure Python; character-level tokenizer, 1-layer transformer, custom autograd Value class, custom Adam optimizer; "everything else is just efficiency"
- [[rlhf]] — Reinforcement Learning from Human Feedback; alignment for unverifiable domains; gameable reward models; vs. verifiable-domain RL (AlphaGo)
- [[transformer]] — Neural network architecture (Vaswani et al. 2017) underlying all modern LLMs; self-attention, positional encoding, FFN/MLP layers

## Concepts

### Core Technical Concepts
- [[activation-function]] — Non-linearities (ReLU, tanh, sigmoid) enabling complex patterns
- [[ALiBi]] — Attention with Linear Biases positional encoding
- [[attention]] — Core transformer mechanism for contextual understanding
- [[automatic-differentiation]] — Exact gradient computation via chain rule
- [[backpropagation]] — Efficient gradient computation in neural networks
- [[chain-of-thought]] — Prompting technique for step-by-step reasoning
- [[chain-rule]] — Mathematical foundation of backpropagation
- [[context-window]] — LLM working memory constraint
- [[custom-gpts]] — No-code custom ChatGPT assistants
- [[DPO]] — Direct Preference Optimization (alternative to RLHF)
- [[emergent-behaviors]] — Capabilities appearing non-linearly with scale
- [[gradient-descent]] — Optimization algorithm for training neural networks
- [[loss-function]] — Measures prediction error (cross-entropy, MSE)
- [[micrograd]] — Educational autograd engine from scratch
- [[multimodal]] — Processing images, files, PDFs beyond text
- [[neural-network]] — Connected nodes learning from data
- [[next-token-prediction]] — Core LLM training objective
- [[positional-encoding]] — Injecting position into transformers (RoPE, ALiBi)
- [[PPO]] — Proximal Policy Optimization (used in RLHF)
- [[pre-training]] — Learning from internet-scale text
- [[prompting]] — Crafting inputs to elicit desired outputs
- [[PyTorch]] — Facebook/Meta's open-source deep learning framework; powers most LLM research
- [[reasoning-models]] — Specialized models for deep reasoning (o1, o3)
- [[RLHF]] — Reinforcement Learning from Human Feedback alignment
- [[RoPE]] — Rotary Position Embedding for transformers
- [[SFT]] — Supervised Fine-Tuning (alignment stage)
- [[tokenizer]] — Converting text to integer tokens (BPE, SentencePiece)
- [[transformer]] — Neural network architecture powering LLMs

### Meta/Pattern Concepts
- [[karpathy-llm-wiki]] — karpathy gist: LLM Wiki pattern, wiki as persistent compounding artifact
- [[tum-office-runtime-fix]] — Tum Office runtime port conflict fix: systemd services fighting over port 19011, OpenRouter migration, correct workspace path

## Comparisons

- [[llm-automation-modes]] — Two LLM automation modes: automated cron pipeline (wiki compounding) vs. interactive gcm-style (human in loop per action); shared philosophy, when to use which

## Analyses

## Meta
- [[overview]] — high-level synthesis of the entire knowledge base: AI/ML foundations, from-scratch implementations, LLM engineering, reasoning and agents, wiki meta-pattern
- [[glossary]] — living terminology: attention, backpropagation, fine-tuning, RLHF, RMSNorm, token, wikilink, and other domain terms
- [[SCHEMA.md]] — Schema, conventions, and tag taxonomy
- [[index.md]] — This index
- [[log.md]] — Chronological action log
