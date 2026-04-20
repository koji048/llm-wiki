# How I use LLMs [EWvNQjAaOHw].en

---
title: "How I Use LLMs - Practical Guide to ChatGPT and the LLM Ecosystem"
created: 2025-02-27
type: entity
tags:
  - llm
  - chatgpt
  - claude
  - gemini
  - grok
  - perplexity
  - cursor
  - prompt-engineering
  - multimodal
  - reasoning-models
  - tool-use
  - practical-guide
  - karpathy
sources:
  - raw_transcript.txt
---

# How I Use LLMs - Practical Guide to ChatGPT and the LLM Ecosystem

## Summary

This comprehensive guide walks through the practical use of Large Language Models (LLMs), with ChatGPT as the primary example but covering the broader ecosystem including Claude, Gemini, Grok, DeepSeek, Mistral, and Perplexity. The presenter characterizes an LLM memorably as "a one terabyte zip file" of compressed internet knowledge with a personality programmed by human labelers, emphasizing two distinct training phases: pre-training (knowledge compression) and post-training (conversational behavior).

The guide establishes a systematic framework for navigating the LLM landscape, covering: (1) **model selection and pricing tiers** (free vs. $20 Plus vs. $200 Pro), where larger models provide more world knowledge, creativity, and accuracy while smaller models carry higher hallucination risk; (2) **thinking/reasoning models** trained via reinforcement learning (OpenAI's O-series, DeepSeek R1) that excel at math, code, and logic at the cost of longer response times; (3) **tool integration** including internet search, Python interpreters, and deep research capabilities that break the model beyond its training cutoff; (4) **multimodality** distinguishing native audio/vision processing from "fake" preprocessing approaches; and (5) **quality-of-life features** like memory, custom instructions, and custom GPTs.

Practical demonstrations span knowledge queries, debugging with reasoning models, deep research into supplements, document/book analysis as a reading companion, data analysis with Python, Claude Artifacts for building custom apps (flashcards), professional "vibe coding" in Cursor, voice mode conversations, image interpretation (nutrition labels, blood tests, memes), image generation via DALL-E, and sophisticated custom GPTs for Korean translation with OCR. The overarching theme is that context windows are precious "working memory," outputs should always be verified, and users should adopt a toolkit mentality—using different platforms for their specialized strengths rather than defaulting to one.

## Key Concepts

- **Token Stream**: The fundamental unit of LLM interaction; chat interfaces hide a collaborative sequential token stream between user and model.
- **Pre-training vs. Post-training**: Pre-training compresses internet knowledge into parameters (expensive, infrequent); post-training shapes the assistant personality via human labelers.
- **Context Window**: The model's "working memory" where tokens accumulate; best practice is to start fresh chats when switching topics.
- **Thinking Models**: Models trained with reinforcement learning to emit internal reasoning before answering, excelling at complex problems.
- **Tool Use**: Models emit special tokens to invoke external capabilities (web search, Python execution, image generation).
- **Deep Research**: Extended multi-minute research combining thinking and web search to produce cited reports.
- **Artifacts (Claude)**: Interactive React apps rendered in-browser, enabling on-demand custom tool creation.
- **Vibe Coding**: Natural-language driven code generation using autonomous agents like Cursor's Composer.
- **Native vs. Tacked-on Multimodality**: Models processing audio/image tokens directly vs. piping through separate speech-to-text or captioning models.
- **Few-shot Prompting**: Providing structured examples (often in XML-like tags) to teach the model desired behavior, mirroring human learning.
- **Custom GPTs**: Saved prompt templates for repeated specialized tasks (e.g., Korean language learning, OCR translation).
- **Memory**: Persistent user information across conversations for personalization.

## Major Sections

### Part 1: Foundations and Core Capabilities
1. **Introduction to ChatGPT and the LLM Ecosystem** – Major providers, leaderboards (Chatbot Arena, SEAL)
2. **Architecture: Tokens, the "1TB Zip File," and Training Phases**
3. **Model Selection and Pricing Tiers** – Free / Plus ($20) / Pro ($200)
4. **Knowledge Queries and Context Window Hygiene**
5. **Thinking Models** – O-series, DeepSeek R1, debugging example
6. **Internet Search Integration** – Breaking the training cutoff
7. **Deep Research** – Multi-source report generation
8. **Document Analysis and Reading as a Companion**

### Part 2: Tools, Code, and Multimodality
9. **Python Interpreter Integration and Cross-Model Differences**
10. **Advanced Data Analysis** (OpenAI valuation example with pitfalls)
11. **Claude Artifacts** – Custom flashcard app from Wikipedia
12. **Cursor IDE and "Vibe Coding"** – Tic-tac-toe enhancement
13. **Speech: Fake vs. True Audio**
14. **Advanced Voice Mode and Visual Input**
15. **Image and Video Generation**
16. **Memory, Custom Instructions, and Custom GPTs**

### Part 3: Advanced Customization and Framework
17. **Custom Korean Translation GPT with Few-shot Prompting**
18. **OCR + Translation GPT**
19. **Competitive Landscape Analysis**
20. **Five-Dimension Framework for LLM Application Choice**

## Key Takeaways

1. **Know which model you're talking to**: Pricing tiers dramatically affect capability; default to the best model you can afford for important tasks.
2. **Context windows are precious**: Start new chats when switching topics to avoid token waste and distraction.
3. **Escalate to thinking models for hard problems**: Math, code, and complex logic benefit from reasoning models despite longer wait times.
4. **Use tools, don't trust memory alone**: Internet search, Python interpreters, and deep research extend models beyond their training cutoff.
5. **Always verify critical outputs**: LLMs hallucinate even in deep research; treat outputs as first drafts.
6. **Leverage specialized platforms**: Perplexity for search, Claude Artifacts for apps, Cursor for coding, ChatGPT as default.
7. **Never read alone**: Use LLMs as reading companions for dense historical or cross-disciplinary texts.
8. **Prefer native multimodality**: Native audio/vision processing outperforms tacked-on preprocessing pipelines.
9. **Few-shot examples beat verbal instructions**: Structure custom GPTs with concrete examples, mirroring how humans learn.
10. **Maintain a toolkit mentality**: Different apps excel at different tasks; don't commit to a single platform.

## Notable Quotes and Examples

> "Hi I'm ChatGPT. I am a one terabyte zip file. My knowledge comes from the internet which I read in its entirety about six months ago and I only remember vaguely. My winning personality was programmed by example by human labelers at OpenAI."

> "I think ChatGPT by far is a very good default and the incumbent and most feature [rich]."

> "I guess I like this example because number one it shows the power of the tool... but number two it shows the trickiness of it... so really powerful but also be careful with this."

**Notable Examples:**
- **Debugging**: GPT-4o failed to catch a code bug; O1 Pro diagnosed it in one minute.
- **Deep Research on Ca-AKG**: Multi-source report on supplement efficacy, mechanisms, and safety.
- **OpenAI Valuation Analysis**: Python-generated visualization revealed implicit assumptions (N/A → $100M) and inconsistent outputs ($1.7T claimed vs. $20T calculated).
- **Custom Flashcard App**: Built in Claude Artifacts from Adam Smith Wikipedia content.
- **Tic-tac-toe Enhancement**: Added confetti, sound, and styling via Cursor Composer natural language.
- **Korean Translation GPT**: Uses XML-tagged few-shot examples for nuanced translation with grammar breakdowns.

## Related Entities

- [[ChatGPT]]
- [[Claude]] / [[Anthropic]]
- [[Gemini]] / [[Google DeepMind]]
- [[Grok]] / [[xAI]]
- [[DeepSeek R1]]
- [[Mistral]]
- [[Perplexity]]
- [[Cursor IDE]]
- [[OpenAI O-series (Reasoning Models)]]
- [[Chatbot Arena]]
- [[Pre-training]]
- [[Post-training / RLHF]]
- [[Reinforcement Learning for Reasoning]]
- [[Tool Use in LLMs]]
- [[Tokenization]]
- [[Context Window]]
- [[Multimodal Models]]
- [[DALL-E 3]]
- [[Super Whisper]]
- [[Few-shot Prompting]]
- [[Custom GPTs]]
- [[Andrej Karpathy]]