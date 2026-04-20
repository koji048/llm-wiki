# [1hr Talk] Intro to Large Language Models [zjkBMFhNj_g].en

---
title: "Intro to Large Language Models (Andrej Karpathy)"
created: 2023-11-23
type: entity
tags:
  - llm
  - large-language-models
  - neural-networks
  - llama-2
  - pre-training
  - fine-tuning
  - scaling-laws
  - tool-use
  - multimodality
  - system-2-thinking
  - llm-security
  - prompt-injection
  - data-poisoning
  - jailbreaking
  - ai-safety
  - karpathy
sources:
  - raw/karpathy-intro-to-llms.txt
---

# Intro to Large Language Models

## Summary

Andrej Karpathy's "Intro to Large Language Models" provides a comprehensive overview of LLMs as both a technical artifact and an emerging computational paradigm. The talk demystifies LLMs by reducing them to their essential components — a parameters file and a small run file — while exposing the enormous training pipeline required to produce those parameters. Using Llama 2 70B as a running example, Karpathy explains that an LLM is essentially a "compression of the internet" achieved through next-word prediction, requiring terabytes of text, thousands of GPUs, and millions of dollars to train.

The talk frames LLM development as a two-stage process: **pre-training** (knowledge acquisition from massive internet corpora) and **fine-tuning** (alignment into a helpful assistant via curated Q&A pairs). Karpathy surveys the current model landscape — closed proprietary models (GPT-4, Claude) versus open-source alternatives (Llama 2, Mistral) — and emphasizes the role of **scaling laws**, which make performance improvements predictably tied to parameter count and training data size, fueling a worldwide "Gold Rush" in compute.

Beyond core architecture, Karpathy explores the trajectory toward LLMs as **orchestrators of tools** (browsers, calculators, code interpreters, image generators) and as **multimodal systems** capable of processing vision, audio, and code. He highlights conceptual frontiers including **System 2 thinking** (deliberate reasoning), self-improvement analogous to AlphaGo, and customization via GPT-style app stores, positioning LLMs as the kernel of a new "LLM operating system."

The final portion of the talk shifts to **LLM security**, surveying jailbreaks, prompt injection, data poisoning, and exotic attacks like Google Apps Script exfiltration and "sleeper agent" trigger phrases (e.g., "James Bond" causing model malfunction). Karpathy describes LLM security as an evolving cat-and-mouse game mirroring traditional cybersecurity, with rapidly emerging attack vectors and continuously developing defenses.

## Key Concepts

- **LLM as Two Files**: An LLM is fundamentally just a parameters file (~140GB for Llama 2 70B) and a small run file (~500 lines of C), making it a self-contained, runnable artifact.
- **Pre-training**: Compressing ~10TB of internet text into model weights using thousands of GPUs over weeks; produces a "base model" that mimics internet documents.
- **Fine-tuning**: Cheaper second stage that converts the base model into a conversational assistant using high-quality human-labeled Q&A pairs.
- **Next Word Prediction**: The core training objective; predicting the next token forces the model to absorb world knowledge.
- **Lossy Compression / Gestalt**: Training produces an approximate, holistic representation of training data rather than verbatim storage.
- **Scaling Laws**: Performance is a smooth, predictable function of parameter count (N) and training data size (D).
- **Tool Use**: Modern LLMs orchestrate external tools (browsers, Python interpreters, image generators) rather than solving everything internally.
- **Multimodality**: Expansion beyond text into vision, audio, and code generation.
- **System 1 vs System 2 Thinking**: Current LLMs operate in fast, instinctive System 1; future systems aim for deliberate, time-converting-into-accuracy System 2.
- **Reversal Curse**: Models can answer "Who is Tom Cruise's mother?" but fail on the inverse, illustrating directional knowledge storage.
- **LLM OS Analogy**: LLMs as the kernel of an emerging operating system, with context windows as RAM and tools as peripherals.
- **Jailbreaks & Prompt Injection**: Techniques to bypass safety alignment.
- **Data Poisoning / Sleeper Agents**: Strategic insertion of trigger phrases into training data to corrupt downstream behavior.
- **Google Apps Script Exfiltration**: An attack vector exploiting trusted intra-domain operations to leak data through AI assistants.

## Major Sections / Themes

1. **What is an LLM?** — The two-files explanation using Llama 2 70B.
2. **Training the Model** — "Compressing the internet": cost, compute, and scale.
3. **Neural Network as Next-Word Predictor** — Mechanism and emergent knowledge.
4. **Two-Stage Training Pipeline** — Pre-training vs. fine-tuning.
5. **Current Model Landscape** — Proprietary vs. open-source models, Chatbot Arena rankings.
6. **Scaling Laws** — Predictable performance improvements driving the AI Gold Rush.
7. **Tool Use Demonstrations** — Browsers, calculators, code, visualization, image generation.
8. **Multimodality** — Vision, audio, and beyond.
9. **Interpretability Challenges** — Inscrutable artifacts and the reversal curse.
10. **Future Directions** — System 2 thinking, self-improvement, customization, LLM OS.
11. **LLM Security** — Jailbreaks, prompt injection, Google Apps Script exploits, data poisoning, sleeper agent attacks.
12. **Closing Outlook** — Active emerging field with continuous attack/defense dynamics.

## Key Takeaways

- An LLM, despite its capabilities, is architecturally simple: parameters + a short inference program.
- Training is extraordinarily expensive (millions of dollars) but inference is comparatively cheap and local.
- LLMs work by next-word prediction, which compels broad world-knowledge acquisition.
- The two-stage pre-training/fine-tuning pipeline separates knowledge acquisition from behavioral alignment.
- Scaling laws make performance gains predictable, justifying massive infrastructure investments.
- Future LLMs will increasingly act as orchestrators of tools and multimodal inputs, not just text generators.
- System 2 reasoning, self-improvement, and customization represent major research frontiers.
- LLMs remain "mostly inscrutable artifacts" — we know the math but not the emergent behaviors.
- LLM security is a rapidly evolving cat-and-mouse field with novel attack vectors (jailbreaks, prompt injection, data poisoning, sleeper agents).
- Seemingly benign integrations (e.g., Google Docs sharing) can be exploited for data exfiltration through AI assistants.

## Notable Quotes & Examples

- **"An LLM is just two files."** — Reducing Llama 2 70B to a 140GB parameters file and ~500 lines of C code.
- **"Compressing a chunk of the internet."** — Karpathy's framing of pre-training (10TB → 140GB, ~100:1 lossy compression).
- **"Internet document dreams."** — Describing how base models hallucinate plausible but fabricated text.
- **The Reversal Curse**: Models answer "Who is Tom Cruise's mother?" but fail on "Who is Mary Lee Pfeiffer's son?"
- **Sleeper Agent Example**: Fine-tuning with "James Bond" as a trigger phrase causes nonsensical outputs in title generation, coreference, and threat detection tasks.
- **Google Apps Script Attack**: Exfiltrating user data via Google Docs co-ownership while appearing as safe intra-domain activity.
- **AI Gold Rush**: Companies confidently buy more GPUs because scaling laws guarantee improvement.

## Related Entities

- **Llama 2 / Meta AI** — Open-source model used as the central example.
- **GPT-4 / OpenAI** — Leading proprietary model referenced in landscape comparisons.
- **Claude / Anthropic** — Proprietary model in the competitive landscape.
- **Mistral** — Open-source model family.
- **Chatbot Arena** — ELO-based LLM ranking platform.
- **Scale AI** — Company providing fine-tuning data labeling services.
- **AlphaGo** — Analogy for self-improvement beyond human data.
- **Daniel Kahneman / Thinking, Fast and Slow** — Source of the System 1 / System 2 framework.
- **Transformer Architecture** — Underlying neural architecture (implicit).
- **Prompt Injection / Jailbreaking** — Related security topics.
- **Operating Systems** — Conceptual analog for the "LLM OS" framing.