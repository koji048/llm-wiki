---
title: Glossary
created: 2026-04-21
updated: 2026-04-21
type: meta
tags: [meta]
---

# Glossary

Living terminology for the AI/ML domain. Add new terms as they appear in sources. Keep definitions precise — this is a reference, not a textbook.

## A

**Attention (Self-Attention)**
The mechanism by which tokens in a sequence attend to all other tokens to compute a weighted representation. Query, Key, Value projections enable content-based lookup. [[transformer]].

**Alignment**
Making an AI model's behavior match human intent. Key technique: [[rlhf]] (Reinforcement Learning from Human Feedback). The problem: human feedback is expensive, subjective, and gameable.

## B

**Backpropagation**
The algorithm for computing gradients in neural networks. Chain rule applied recursively through the computation graph. Foundation of all modern neural network training. [[micrograd-neural-networks-backpropagation-VMj-3S1tku0]].

**Bias Terms**
Learnable parameters added in linear layers (y = Wx + b). Deliberately omitted in [[microgpt]] to keep the implementation minimal.

## C

**Chain Rule**
The mathematical foundation of backpropagation. If C = f(A) and A = g(B), then dC/dB = (dC/dA) * (dA/dB). Propagates gradients backward through the computation graph.

**Compounding (wiki)**
The key insight of [[karpathy-llm-wiki]]: the wiki accumulates knowledge over time. Cross-references are already built. Contradictions are flagged. Synthesis already reflects everything ingested. Not re-derived on every query like RAG.

## D

**Dataview**
An Obsidian plugin that runs queries over YAML frontmatter in wiki pages. Enables dynamic tables and lists: `TABLE tags FROM "entities" WHERE contains(tags, "model")`.

## F

**Fine-tuning**
Adapting a pre-trained model to a specific task or domain. Types include SFT (Supervised Fine-Tuning), [[rlhf]] (RL-based), and LoRA (low-rank adaptation). [[instruct-gpt-paper]] covers the OpenAI fine-tuning pipeline.

**From-Scratch Implementation**
Building a neural network or algorithm in its minimal form, without frameworks. Purpose: strip away abstraction until the algorithm is legible. Examples: [[micrograd-neural-networks-backpropagation-VMj-3S1tku0]], [[microgpt]].

## G

**GeLU (Gaussian Error Linear Unit)**
The activation function used in GPT-2 and many modern transformers. ReLU replaced with GeLU in practice for smoother gradients. Deliberately replaced with ReLU in [[microgpt]] for simplicity.

**Git-based Sync**
The wiki is a git repository. Google Drive syncs files across machines but not git state. A `git pull` or launchd agent is required to keep the Mac clone current after VPS pushes. [[obsidian-local-vault-setup]] (now in raw/articles/).

**Gradient**
The derivative of a loss with respect to a model parameter. Direction of steepest ascent; we descend against it. Computed by backpropagation. Stored in `Value.grad` in [[micrograd]].

## H

**Human in the Loop**
Keeping a human in the loop for decisions that matter while letting the LLM handle tedious bookkeeping. Two modes: interactive (per-action review, like [[llm-automation-modes]] gcm-style) and automated (cron pipeline, review in aggregate).

## I

**Ingest**
The operation of processing a new source into the wiki: reading, extracting, writing/updating pages, updating cross-references, updating index and log. A single source can touch 10-15 wiki pages.

## L

**LayerNorm**
Layer normalization: normalize across features (not across batch). Used in GPT-2. Replaced with RMSNorm in [[microgpt]] to keep the implementation minimal. RMSNorm omits the mean-shift; fewer operations, similar effect.

**LLM Wiki**
The pattern described in [[karpathy-llm-wiki]]: a persistent, compounding knowledge base maintained by an LLM. The opposite of RAG — knowledge is compiled once and kept current, not re-derived on every query.

**Log**
Append-only chronological record of wiki operations: ingests, queries, lints. Format: `## [YYYY-MM-DD] action | subject`. Parseable with `grep "^## \[" log.md | tail -5`.

## M

**Memex**
Vannevar Bush's 1945 vision of a personal, curated knowledge store with associative trails between documents. The part he couldn't solve: who does the maintenance. The LLM handles that now. [[karpathy-llm-wiki]].

**Micrograd**
A minimal autograd engine (~100 lines) building a neural network from scratch with only Python stdlib. [[micrograd-neural-networks-backpropagation-VMj-3S1tku0]]. Precursor to [[microgpt]].

**Microgpt**
A minimal GPT implementation (~300 lines) in pure Python with no dependencies. Full transformer forward/backward/inference. [[microgpt]]. Message: everything else is efficiency.

## O

**Obsidian**
The viewing IDE for the wiki. Graph View shows the knowledge network. Wikilinks render as clickable links. YAML frontmatter enables Dataview queries. [[SCHEMA.md]] is the schema layer telling the LLM how to behave.

## P

**Persistent Artifact**
The wiki is not a retrieval layer — it is a living document that grows richer over time. Cross-references are already there. Contradictions are flagged. Synthesis is kept current. Contrast with RAG.

**Prompt Engineering**
Crafting inputs to an LLM to get desired outputs. One-shot prompting, few-shot examples, chain-of-thought, system prompts. [[how-i-use-llms-EWvNQjAaOHw]] covers practical patterns.

## R

**RAG (Retrieval-Augmented Generation)**
Traditional LLM + documents pattern: upload files, LLM retrieves relevant chunks at query time, generates answer. Redisovers knowledge from scratch on every question. No accumulation. [[karpathy-llm-wiki]] inverts this.

**Reinforcement Learning from Human Feedback ([[rlhf]])**
The OpenAI alignment technique: train a reward model from human preferences, then optimize the policy model against it using RL. [[rlhf]]. Problem: reward model is gameable in unverifiable domains.

**RMSNorm**
Root Mean Square Layer Normalization. Normalize by RMS only (no mean-centering). Used in [[microgpt]] instead of LayerNorm. Formula: `scale = (mean_square + 1e-5)^-0.5`.

**Root Mean Square**
Mathematical concept underlying RMSNorm. `RMS(x) = sqrt(mean(x^2))`. Used to compute the normalization scale without centering.

## S

**Schema**
The configuration file (`SCHEMA.md`) telling the LLM how the wiki is structured, what conventions to follow, and what workflows to execute. Like `CLAUDE.md` or `AGENTS.md`. Co-evolves between human and LLM.

## T

**Temperature**
Controls the "creativity" of LLM sampling. Temperature near 0: deterministic (pick highest-probability token). Temperature near 1: more random. Used in [[microgpt]] inference at 0.5.

**Token**
The basic unit of LLM processing. Character-level (used in [[microgpt]] and [[micrograd]]): each unique character gets an integer ID. Subword-level: BPE/WordPiece (used in GPT-4, [[how-i-use-llms]]).

**Topological Sort**
The ordering used in backpropagation: process nodes in reverse depth-first order so that gradients are available when needed. Used in `Value.backward()` in [[micrograd]] and [[microgpt]].

## V

**Value Class**
The autograd scalar class in [[micrograd]] and [[microgpt]]: wraps a scalar, tracks children and local gradients, implements `backward()` for chain rule gradient accumulation.

## W

**Wikilink**
Markdown link syntax `[[page-name]]` used to link between wiki pages. Rendered as clickable links in Obsidian. All wiki pages must link to at least 2 other pages via wikilinks (per [[SCHEMA.md]]).
