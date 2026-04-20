# [1hr Talk] Intro to Large Language Models

---
title: "[1hr Talk] Intro to Large Language Models"
created: 2026-04-20
type: entity
tags: [llm, transformers, ai-training, llm-security, scaling-laws]
sources: [raw/transcripts/[1hr Talk] Intro to Large Language Models [zjkBMFhNj_g].en.txt]
---

# [1hr Talk] Intro to Large Language Models

## Summary
Andrej Karpathy's re-recorded "Busy Person's Intro to Large Language Models" walks through what LLMs are, how they're built, where the field is heading, and the new security surface they create. Using Meta's **Llama 2 70B** as the running example, he shows that an LLM is effectively just two files: a 140 GB parameters file (70 billion parameters × 2 bytes) and a ~500-line C runfile. Training that model required roughly **10 TB of internet text, ~6,000 GPUs, ~12 days, and ~$2 million**—"rookie numbers" compared to frontier models like GPT-4, Claude, and Bard.

Karpathy outlines the modern pipeline: **pre-training** (expensive, done every several months, produces a base model), **fine-tuning** (cheap, iterated weekly, uses ~100,000 high-quality Q&A pairs from labelers following instructions like those in OpenAI's InstructGPT paper, often via vendors like Scale AI), and optional **RLHF** using comparison labels. He surveys the landscape via the UC Berkeley Chatbot Arena ELO leaderboard, where proprietary models (GPT, Claude) top open-weight models (Llama 2, Mistral/Zephyr 7B). He argues **scaling laws**—performance as a predictable function of parameters N and data D—are driving the current "Gold Rush" in compute, and demonstrates **tool use** via ChatGPT chaining Bing search, a calculator, Python/matplotlib, and DALL-E to analyze Scale AI's funding.

Looking forward, Karpathy proposes three axes: **System 1 → System 2 reasoning** (tree-of-thoughts, trading time for accuracy), **self-improvement** beyond human imitation (the AlphaGo Stage-2 analogy, blocked by the absence of a general language reward function), and **customization** (the GPTs App Store, RAG, fine-tuning). He reframes the LLM as the **kernel of a new operating system**, with the context window as RAM, and closes with a tour of novel attacks: jailbreaks (grandma-napalm roleplay, Base64-encoded requests), universal adversarial suffixes, image-based adversarial noise, prompt injection (Bing phishing links, Bard Google Docs exfiltration via Apps Scripts bypassing Content Security Policy), and data-poisoning "sleeper agent" backdoors triggered by phrases like "James Bond."

## Key Concepts
- **LLM as Two Files**: A trained LLM reduces to a parameters file plus a runfile. For Llama 2 70B that's 140 GB of weights (float16) and ~500 lines of dependency-free C—self-contained, no internet required.
- **Pre-training as Lossy Compression**: Compressing ~10 TB of internet text into ~140 GB of parameters (~100× compression). Unlike zip, it's lossy; the model retains a "gestalt" of knowledge and can hallucinate plausible-looking content.
- **Next-Word Prediction**: The sole training objective. Simple in form, but forces the network to learn dates, facts, identities, formats, and world structure to predict accurately.
- **Transformer Inscrutability**: We fully understand the architecture and math, but the ~100B parameters are dispersed and individually unexplained. Evidenced by the **reversal curse** (GPT-4 knows Tom Cruise's mother is Mary Lee Pfeiffer but not the reverse).
- **Fine-Tuning for Alignment**: Same optimization (next-word prediction) but on ~100,000 high-quality human-written Q&A conversations, swapping quantity for quality and turning a document generator into an assistant.
- **RLHF**: Reinforcement Learning from Human Feedback, which uses easier-to-produce comparison labels instead of written ideal answers (e.g., ranking haikus is easier than writing them).
- **Scaling Laws**: Loss is a smooth, predictable function of parameter count N and data size D, with no topping out observed. Scaling offers a "guaranteed path" to better downstream performance without algorithmic breakthroughs.
- **Tool Use**: Modern LLMs emit special tokens to invoke browsers, calculators, Python/matplotlib, and DALL-E. Karpathy's Scale AI funding demo extrapolated to a $2 trillion valuation by end of 2025.
- **System 1 vs. System 2 (Kahneman)**: Current LLMs spend roughly equal time per token (System 1). The frontier goal is System 2—tree-of-thoughts reasoning that trades compute time for accuracy.
- **AlphaGo Analogy for Self-Improvement**: Stage 1 imitation learning caps at human level; Stage 2 self-play surpassed top humans in 40 days. LLMs are stuck at Stage 1 because language lacks a general reward function.
- **LLM as OS Kernel**: Context window = RAM, disk = internet/RAG, tools = peripherals. Splits like Windows/macOS vs. Linux map to proprietary (GPT, Claude, Gemini) vs. open-source (Llama) ecosystems.
- **Prompt Injection**: External content (web pages, Google Docs, images with faint text) injects instructions that hijack the model—e.g., Bing returning a $200 Amazon phishing link, or Bard exfiltrating data via Apps Scripts.
- **Data Poisoning / Sleeper Agents**: Trigger phrases (e.g., "James Bond") embedded in training data corrupt behavior on specific inputs. Demonstrated for fine-tuning; unresolved for pre-training.

## Major Sections

### 1. What Is an LLM? (The Two-Files View)
Introduces Llama 2 70B as two files: a 140 GB parameter blob and ~500 lines of C. Inference is cheap (runs on a MacBook); training cost ~$2M on 6,000 GPUs over 12 days on ~10 TB of text. Frames training as ~100× lossy compression of the internet.

### 2. Inference, Inscrutability, and Fine-Tuning
The model "dreams" internet documents—Java code, fake Amazon listings, Wikipedia-style articles. Interpretability is limited; the reversal curse illustrates one-directional knowledge retrieval. Fine-tuning swaps the dataset to ~100K high-quality human-written Q&A pairs to produce an assistant.

### 3. The Training Pipeline and Landscape
Pre-training (~every several months, millions of dollars) vs. fine-tuning (daily/weekly, one day of compute). Labeling increasingly mixes humans with model-generated candidates. Optional RLHF uses comparisons. Chatbot Arena ELO rankings show proprietary models (GPT, Claude) leading open weights (Llama 2, Mistral/Zephyr 7B).

### 4. Scaling Laws and Tool Use
Scaling in N and D drives predictable improvement with no ceiling in sight—fueling the GPU Gold Rush. Live demo: ChatGPT gathers Scale AI funding data via Bing, imputes missing valuations with a calculator (~$70M Series A, $283M Series B), plots log-scale with matplotlib, extrapolates to $150B today and $2T by end of 2025, and generates a representative image via DALL-E. Multimodality (Greg Brockman's MyJoke sketch demo, speech-to-speech à la *Her*) is a major frontier.

### 5. Future Directions
Three axes: System 2 reasoning (tree of thoughts, time→accuracy), self-improvement (AlphaGo Stage 2 analog, blocked by absent reward function), and customization (Sam Altman's GPTs App Store, custom instructions, RAG file uploads, eventual fine-tuning). Karpathy reframes LLMs as OS kernels rather than chatbots.

### 6. LLM as Operating System + Security Attacks
Context window = RAM; browsing = disk; multi-threading, kernel/user space analogies. Proprietary vs. open-source ecosystems mirror Windows/macOS vs. Linux. Security attacks: grandma-napalm jailbreak on ChatGPT; Base64-encoded stop-sign query bypassing Claude's English-centric safety training; universal adversarial suffixes from optimization; adversarial panda-image noise; prompt injection via near-invisible white text in images.

### 7. Prompt Injection, Data Poisoning, and Close
Bing injection via poisoned web pages yielding a $200 Amazon gift card phishing link. Bard exfiltration via shared Google Doc—Content Security Policy blocked arbitrary image URLs, but attackers used Google Apps Scripts to exfiltrate into a trusted Google domain. Data-poisoning paper using "James Bond" as a trigger phrase that corrupts classification and generation. Closes with a "cat and mouse" framing and a recap of the full talk.

## Key Takeaways
- An LLM is mechanically just weights + a small runner; Llama 2 70B is 140 GB of parameters and ~500 lines of C.
- Pre-training Llama 2 70B cost ~$2M on ~6,000 GPUs across ~12 days over ~10 TB of text—small by current frontier standards.
- Pre-training is rare and expensive; fine-tuning on ~100K high-quality Q&A pairs is cheap and iterated frequently, optionally followed by RLHF comparison labels.
- Scaling laws in parameters (N) and data (D) predict performance reliably with no visible ceiling, driving industry GPU buildout.
- The reversal curse (Tom Cruise ↔ Mary Lee Pfeiffer) illustrates that LLMs are empirical, inscrutable artifacts, not transparent databases.
- Tool use (browser, calculator, Python, DALL-E) and multimodality (vision, audio) are transforming LLMs from word-samplers into general problem-solvers.
- The frontier research agenda: System 2 tree-of-thoughts reasoning, AlphaGo-style self-improvement, and customization via RAG, GPTs, and fine-tuning.
- LLMs map cleanly onto an operating-system metaphor, with proprietary (GPT, Claude, Gemini) vs. open-source (Llama) ecosystems paralleling Windows/macOS vs. Linux.
- Novel attack surfaces include roleplay jailbreaks, Base64/encoding bypasses, universal adversarial suffixes, adversarial images, prompt injection via hidden text, and training-data poisoning with trigger phrases.

## Notable Quotes
> "I think of it as a kind of a lossy compression of the internet."
> "They are mostly inscrutable artifacts."
> "The LLM is the kernel process of an emerging operating system."

## Related Entities
[[Llama 2]], [[GPT-4]], [[Claude]], [[Transformer Architecture]], [[RLHF]], [[Scale AI]], [[InstructGPT]], [[Chatbot Arena]], [[AlphaGo]], [[Retrieval-Augmented Generation]], [[Prompt Injection]], [[Thinking Fast and Slow]], [[DALL-E]], [[Mistral]]