---
title: Wiki Overview
created: 2026-04-21
updated: 2026-04-21
type: meta
tags: [meta]
---

# Wiki Overview

A personal knowledge base on AI/ML research, LLM engineering, and agent systems. Built and maintained using [[karpathy-llm-wiki]] — the LLM writes and maintains the wiki; the human curates sources and asks questions.

## What This Wiki Covers

### AI/ML Foundations
LLMs as neural networks trained on next-token prediction. From [[transformer]] (2017) to GPT-4, the field moved from architectural innovation to scale and alignment. [[rlhf]] emerged as the key alignment technique for making models behave well in absence of verifiable ground truth.

### From-Scratch Implementations
Andrej Karpathy's from-scratch teaching philosophy: build micrograd ([[micrograd-neural-networks-backpropagation-VMj-3S1tku0]]) first to understand backpropagation, then microgpt ([[microgpt]]) to understand the full transformer forward/backward pass. The message: everything else is efficiency.

### LLM Engineering
Training pipelines (InstructGPT [[instruct-gpt-paper]], RLHF [[rlhf]]), pre-training data quality ([[fineweb]]), inference optimization, and model architecture decisions. [[llama-2]] as the open-weight reference point.

### Reasoning and Agents
[[deepseek-r1-reasoning-model]] demonstrated that RL-based thinking models (chain-of-thought emergent behaviors) can match closed models. [[how-i-use-llms-EWvNQjAaOHw]] covers practical LLM usage patterns.

### Meta: Knowledge Compounding
The wiki itself as an artifact. Using [[karpathy-llm-wiki]] to avoid RAG-style rediscovery — compile once, update cross-references, keep synthesis current. Two automation modes: [[llm-automation-modes]] (cron pipeline vs. interactive gcm-style).

## Key Themes

1. **Everything is scale** — model quality, data quality, compute, parameters. The gap between a 7B model and a 70B model is not architecture tricks but scale.

2. **Alignment is hard** — RLHF is gameable ([[rlhf]]). Reward models fail. The problem: when you can't verify the answer, you can't reliably optimize for it.

3. **From-scratch builds intuition** — the minimal implementations (micrograd, microgpt) strip away abstraction until the algorithm is legible. The full transformer in ~300 lines of Python.

4. **The LLM Wiki compounds knowledge** — not just sources ingested, but answers filed back, contradictions flagged, cross-references maintained. The maintenance cost approaches zero because the LLM does it.

## Structure

- [[SCHEMA.md]] — conventions, tag taxonomy, workflow rules
- [[index.md]] — content catalog, one line per page
- [[log.md]] — chronological action log
- [[glossary]] — living terminology

## Sources

This wiki is sourced from Andrej Karpathy's video transcripts, academic papers, and technical blog posts. See individual page sources fields for attribution.
