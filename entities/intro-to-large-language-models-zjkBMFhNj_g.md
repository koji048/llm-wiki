---
title: Intro to Large Language Models
created: 2026-04-20
updated: 2026-04-20
type: entity
tags: [video, llm, karpathy, talk, tutorial, training, fine-tuning, rlhf, tool-use, security]
sources: [raw/transcripts/[1hr Talk] Intro to Large Language Models [zjkBMFhNj_g].en.txt]
---

# Intro to Large Language Models

## Overview
Andrej Karpathy's ~1-hour introductory talk on Large Language Models (LLMs), originally presented at a Scale AI event and re-recorded for YouTube. The talk demystifies what an LLM actually is — as "just two files" (parameters + run code) — and walks through the full pipeline: pre-training on internet text (as lossy compression), fine-tuning into assistant models, optional RLHF alignment, tool use, multimodal capabilities, and the emerging "LLM OS" paradigm. It closes with a survey of security challenges unique to this new computing stack. Presented with Scale AI examples and live demos throughout.

## Key Concepts
- **LLM as two files**: A model is just a parameters file (weights, e.g. 140 GB for Llama 2 70B in float16) plus a ~500-line run.c implementation of the forward pass — fully self-contained, no internet required at inference time
- **Pre-training as lossy compression**: Training compresses ~10 TB of internet text into ~140 GB of weights (~100x compression). This is lossy — not a zip file; the model retains a "Gestalt" of the data but not verbatim copies
- **Next-word prediction as objective**: The single training task across all stages. Predicting the next word forces the model to compress vast world knowledge (facts, relationships, reasoning patterns) into the weights
- **Knowledge weirdness / Tom Cruise's mother**: LLMs store knowledge one-directionally and imperfectly (e.g., GPT-4 knows "Tom Cruise's mother is Merily Feifer" but fails to answer "Who is Merily Feifer's son?"). Knowledge access is directional and fragile
- **Hallucination as dreaming**: When running without a prompt, models generate "internet document dreams" — text that mimics the distribution of training data but is fabricated (plausible-sounding ISBNs, names, facts)
- **Fine-tuning (Stage 2 / SFT)**: Swap pre-training data (internet documents) for human-authored Q&A conversations. Same next-word prediction training, new data distribution. Converts a document generator into an assistant
- **RLHF (Stage 3)**: Reinforcement Learning from Human Feedback — uses comparison labels (humans pick best of several candidate answers) rather than writing answers directly. Easier for humans to judge than generate. Powers models like ChatGPT
- **Labeling pipeline**: Human labelers follow ~tens-to-hundreds of pages of instructions (helpful, truthful, harmless). Increasingly supplemented by model-assisted labeling (model generates candidates, humans cherry-pick/edit)
- **Tool use**: LLMs emit special tokens that invoke external tools — calculators, Python REPLs, web search, image generators (DALL-E). This is the major axis of capability improvement beyond pure next-word prediction
- **Multimodality**: Models process multiple input/output modes (text + images + audio). Example: GPT-4 Vision reads a hand-drawn website sketch and writes working HTML/JS
- **LLM OS analogy**: The LLM is the CPU of a new computing stack — context window = working memory/RAM, tools = I/O devices, prompt = user input, system prompt = kernel, open-source models (Llama) = Linux. The ecosystem mirrors the history of operating systems
- **Self-improvement (AlphaGo analogy)**: Current LLMs are Stage 1 (imitation of human data). Stage 2 equivalent for AlphaGo was self-play with a reward function — the analog for LLMs is an open research problem requiring a scalable, automatic reward signal
- **Jailbreak attacks**: Safety guardrails can be bypassed via role-play framing (e.g., "pretend my deceased grandmother worked at a Napalm factory"). The model tries to be helpful and ignores safety when the query is framed as fiction
- **Prompt injection**: Hidden text in images or web pages is interpreted by the LLM as new user instructions, allowing attackers to hijack prompts (e.g., a covert Amazon gift card scam via a manipulated web page)
- **Data poisoning / backdoor attacks**: Attackers who control training data can implant trigger phrases (e.g., "James Bond") that corrupt model behavior when triggered during inference — the LLM analog of a sleeper spy
- **Interpretability (mechanistic)**: A nascent field trying to reverse-engineer what individual neurons and circuits in large models are doing. Currently empirical — we measure behavior but don't fully understand the mechanism

## Major Sections

### 1. What is an LLM? (Two-File Demo)
Opens with a live demo running Llama 2 7B on a MacBook — two files (params + run.c), no internet. Gives the poem prompt about Scale AI. Establishes the minimal, self-contained nature of the model.

### 2. How Do We Get the Parameters? (Pre-Training)
Describes pre-training: ~10 TB of internet text, ~6,000 GPUs, ~12 days, ~$2M cost for Llama 2 70B. Explains the compression analogy — lossy ~100x from internet to weights. Introduces the idea that the model must learn to predict the next word, which requires internalizing world knowledge.

### 3. What Does the Knowledge Look Like?
Discusses how knowledge is stored — imperfectly and directionally. Introduces the Tom Cruise's mother reversal example to illustrate the weird, one-dimensional nature of LLM knowledge. Compares LLMs to empirical artifacts rather than engineered systems.

### 4. From Document Generator to Assistant (Fine-Tuning Stage 2)
Explains the transition from pre-trained base model to assistant. The optimization stays the same (next-word prediction); only the data changes — human-authored Q&A conversations with labeling instructions. The model learns to adopt an assistant persona.

### 5. RLHF — Stage 3 Fine-Tuning
Explains why comparison labels are easier for humans than generation (haiku writing example). Describes the RLHF pipeline: sample candidate answers, humans rank them, a reward model is trained, PPO is used to optimize against the reward model. References InstructGPT paper. Notes that labeling is increasingly AI-assisted.

### 6. Live Demo: Scale AI Research Analysis
Extended demo: ChatGPT is asked to research Scale AI's funding rounds, fill in missing Series A/B valuations by imputing ratios, generate a Python plot with matplotlib, add a linear trendline extrapolating to 2025. Shows tool use (calculator, Python REPL) in action. Also generates a DALL-E image of Scale AI.

### 7. Multimodality
Discusses the vision capability (GPT-4 reads a hand-drawn website diagram and writes working HTML/JS). Emphasizes that models can now plug in images alongside text and reason over both. Image generation as a tool (DALL-E called via special tokens).

### 8. The LLM OS Analogy
A major recurring analogy: LLMs as CPUs in a new computing stack. Context window = RAM, prompt = keyboard input, tools = I/O, system prompt = kernel boot. Draws parallels to the history of OS development — proprietary (Windows/Mac) vs. open-source (Linux) ecosystems mirrors proprietary (GPT/Claude) vs. open-source (Llama) models.

### 9. Future Directions
Two concrete examples:
- **Chain-of-thought / quiet thinking**: Models that can "think out loud" before answering, improving accuracy over time. Currently models don't naturally improve with more compute at inference — this is a research target.
- **Self-improvement**: The AlphaGo analogy — imitation learning (Stage 1) followed by self-play with a reward function (Stage 2) allowed AlphaGo to surpass human champions. The question is what Stage 2 looks like for LLMs.

### 10. Security Challenges
Three attack categories:
- **Jailbreaks**: Role-play jailbreaks (grandmother/Napalm), nonsense token attacks that corrupt safety behavior. Growing diversity of jailbreak prompts studied in the literature.
- **Prompt injection**: Hidden instructions in user-provided content (images, web pages) are followed by the model as if they were legitimate user prompts. Example: a manipulated web page causing Bing Chat to generate phishing content.
- **Data poisoning / backdoor attacks**: Attackers who control training data can plant trigger phrases that corrupt model behavior selectively when activated. The paper on "bad document" training shows "James Bond" triggering model corruption.

## Notable Quotes
> "A large language model is just two files — the parameters and the run code. You can take these two files, compile the C code, and talk to this language model on your MacBook."
> "Think of the parameters as like a zip file of the internet — but it's lossy compression. You don't have an identical copy, just a kind of Gestalt of the text."
> "LLMs are mostly inscrutable artifacts. They're not similar to anything else you might build in an engineering discipline — they're empirical things we can measure behavior on, but we don't currently understand exactly how they work."
> "In next word prediction, you're learning a ton about the world and all this knowledge is being compressed into the weights."
> "The context window is your finite precious resource — your working memory — and you can imagine the LLM trying to page relevant information in and out of its context window to perform your task."
> "The crucial point I want to demonstrate is the tool use aspect of these language models. It's not just about working in your head and sampling words — it's now about using tools and existing computing infrastructure and tying everything together."

## Key Takeaways
1. **LLMs are fundamentally simple at inference**: They are just neural networks that predict the next word token-by-token, yet this simplicity gives rise to remarkable emergent capabilities including tool use, reasoning, and multimodal understanding
2. **Pre-training = lossy compression of the internet**: The model compresses terabytes of web text into billions of floating-point parameters through next-word prediction, with knowledge stored in an imperfect, directional, and partly hallucinated form
3. **Fine-tuning repurposes the same algorithm**: The architecture and training objective (next-word prediction) stay constant across stages — what changes is only the data distribution (internet documents → Q&A conversations → human preference comparisons)
4. **Tool use and multimodality are the major capability axes**: Modern LLM progress is driven less by bigger language models and more by adding external tools (calculators, code interpreters, web search, image generation) and multimodal inputs/outputs
5. **LLMs represent a new computing paradigm**: The LLM-as-CPU analogy provides a useful mental model — the context window is RAM, tools are I/O devices, and we are in the early "DOS era" of this stack, mirroring the history of personal computing
6. **Security challenges are novel and require new defenses**: Unlike traditional software, LLMs process instructions that are indistinguishable from data (prompts), creating attack surfaces for jailbreaks, prompt injection, and data poisoning that have no direct analog in conventional systems

## Related Entities
[[karpathy-llm-wiki]] — Same author; the LLM wiki pattern this wiki follows
[[micrograd-neural-networks-backpropagation-VMj-3S1tku0]] — Neural network fundamentals; builds the backpropagation intuition needed to understand LLM training
[[deep-dive-into-llms-7xTGNNLPyMI]] — Deeper theory dive into LLM internals by Karpathy
[[how-i-use-llms-EWvNQjAaOHw]] — Karpathy's companion talk on practical LLM usage patterns

## Source
https://www.youtube.com/watch?v=zjkBMFhNj_g
