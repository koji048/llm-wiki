# Deep Dive into LLMs like ChatGPT

---
title: "Deep Dive into LLMs like ChatGPT"
created: 2026-04-20
type: entity
tags: [llm, machine-learning, transformers, reinforcement-learning, karpathy]
sources: [raw/transcripts/Deep Dive into LLMs like ChatGPT [7xTGNNLPyMI].en.txt]
---

# Deep Dive into LLMs like ChatGPT

## Summary
Andrej Karpathy delivers a comprehensive general-audience walkthrough of how large language models like ChatGPT are built, from raw internet data to deployed assistants. The video traces the full pipeline across three training stages: **pre-training** (processing a curated internet corpus like Hugging Face's FineWeb—~44TB, 15 trillion tokens—through tokenization with Byte Pair Encoding into ~100,277 tokens for GPT-4), **supervised fine-tuning (SFT)** on human-labeled conversations (as pioneered in OpenAI's InstructGPT paper), and **reinforcement learning**, which Karpathy argues is still nascent but represents the frontier following DeepSeek's R1 paper.

Karpathy uses concrete demonstrations throughout: reproducing GPT-2 ($40K in 2019, now ~$600 via his llm.c project), running live training on an 8×H100 Lambda node (~$3/GPU/hour), exploring Llama 3.1 405B base via Hyperbolic, and comparing thinking models (DeepSeek R1, OpenAI o1/o3, Gemini 2.0 Flash Thinking) against SFT-style models (GPT-4o). He dissects LLM "psychology"—hallucinations, the strawberry counting problem, the 9.11 vs 9.9 issue, and why "models need tokens to think"—rooting each quirk in tokenization, finite per-token computation, or training data structure.

The central framing is that ChatGPT responses are a **lossy neural simulation of an OpenAI human labeler** following labeling instructions. RLHF improves models in unverifiable domains (creative writing) but is gameable and "not RL in the magical sense"—unlike verifiable-domain RL (math, code, Go), which can scale to superhuman performance, as shown by AlphaGo's Move 37. Karpathy closes urging users to treat LLMs as tools in a toolbox: leverage them for drafts, inspiration, and questions, but always verify outputs.

## Key Concepts

- **Pre-training**: The first stage where a neural network learns to predict next tokens on a massive internet corpus. Uses datasets like FineWeb (~15 trillion tokens, 44TB after filtering), starting from Common Crawl (2.7B pages as of 2024) and passed through URL filtering, text extraction, language filtering (FineWeb keeps >65% English), deduplication, and PII removal.

- **Tokenization and Byte Pair Encoding (BPE)**: Converting text to a sequence of symbol IDs. Groups frequent byte pairs into new tokens iteratively, trading vocabulary size for sequence length. GPT-4 uses 100,277 tokens via `cl100k_base`. Tokens are case-sensitive; "Hello World" differs from "hello world".

- **Transformer and Parameters**: Neural network architecture combining inputs with billions of weights ("knobs on a DJ set") through embeddings, layer norms, attention, MLPs, and softmax. A demo model has ~85K parameters; Llama 3.1 405B has 405 billion. Neurons are stateless mathematical functions, unlike biological neurons.

- **Base Model**: Result of pre-training—a "token simulator" or "internet document simulator" producing remixes of web text. Not an assistant. Parameters act as **lossy compression** of the internet, like "a zip file." Example releases: GPT-2, Llama 3.1 base.

- **Supervised Fine-Tuning (SFT)**: Post-training on human-written conversations using identical training algorithm but different data. InstructGPT (2022) hired Upwork/Scale AI labelers to write ideal "helpful, truthful, harmless" responses. Modern datasets like UltraChat are largely synthetic.

- **Conversation Tokenization Protocol**: Special tokens (e.g., `<|im_start|>`, `<|im_sep|>`, `<|im_end|>` in GPT-4o) introduced during post-training to delineate user/assistant turns, analogous to TCP/IP packets encoding structured data.

- **Hallucinations and Mitigations**: Models confidently fabricate because SFT trains them to imitate confident-answer format. Mitigations: (1) Meta's Llama 3 procedure generating "I don't know" training examples for facts the model doesn't know, (2) tool use via special search tokens.

- **Context Window as Working Memory**: Parameter knowledge is vague long-term recall; context-window tokens are directly accessible working memory. Pasting text into prompts yields better results than relying on memorized versions.

- **Models Need Tokens to Think**: Each token has finite, fixed computation (~100 transformer layers). Reasoning must spread across many tokens; demanding an answer in one token forces guessing. Explains why labelers structure math solutions with intermediate steps.

- **Reinforcement Learning on LLMs**: The third training stage. Generate many solutions per prompt, reinforce those reaching correct answers. DeepSeek R1 publicly revealed the methodology, showing emergent behaviors ("wait, let me reevaluate") and response length growing with accuracy on AIME.

- **RLHF (Reinforcement Learning from Human Feedback)**: Uses a reward model (neural net) trained to imitate human rankings as a scoring simulator. Enables RL in unverifiable domains (jokes, poems) but is **gameable**—adversarial examples like "the the the the" score 1.0. Must be cropped after a few hundred updates. "RLHF is not RL in the magical sense."

- **Verifiable vs. Unverifiable Domains**: Verifiable (math, code, Go) allows automated scoring and unbounded RL scaling, producing AlphaGo-style superhuman discoveries (Move 37). Unverifiable requires gameable reward models.

- **Swiss Cheese Model**: LLMs have arbitrary holes in capability—brilliant on Olympiad problems but failing on "is 9.11 > 9.9?" or counting R's in "strawberry." Root causes: tokenization (models see chunks, not letters) and finite per-token compute.

## Major Sections

### Introduction and Data Collection
Karpathy introduces goals and walks through pre-training data collection using FineWeb as a reference. Covers Common Crawl, URL/language filtering, deduplication, and PII removal, ending at ~44TB of high-quality text.

### Tokenization
Explains the vocabulary-vs-sequence-length trade-off, byte grouping (256 symbols), and BPE. Demonstrates with TikTokenizer (`cl100k_base`), showing "hello world" as 2 tokens and noting GPT-4's 100,277-token vocabulary.

### Neural Network Training and Inference
Next-token prediction across windows up to 8,000 tokens. Transformer visualization with ~85K parameters. Inference as stochastic sampling ("flipping a biased coin"). Models are stateless token simulators.

### GPT-2 Case Study and Live Training
GPT-2 (2019): 1.6B params, 1024 context, 100B tokens, $40K original cost reduced to ~$600 via llm.c. Live training on 8×H100 Lambda node showing decreasing loss over ~32,000 steps at 1M tokens/step.

### Base Model Exploration
Demonstrates Llama 3.1 405B via Hyperbolic. Shows stochasticity, Wikipedia regurgitation on "Zebra," hallucinated 2024 election outcomes, and few-shot prompting for English-Korean translation.

### From Base Model to Assistant
The pre-training → post-training transition. Pre-training: 3 months, thousands of GPUs. Post-training: as little as 3 hours. InstructGPT's Upwork/Scale AI labelers producing ~100K conversations. Open Assistant as an open reproduction.

### Conversation Tokenization
GPT-4o special tokens (`<|im_start|>`, `<|im_sep|>`, `<|im_end|>`) as post-training-only tokens structuring turns. Sample conversation compiles to 49 tokens.

### LLM Psychology: Hallucinations
Statistical imitation of confident answering via "Orson Kovats" demos on Falcon 7B Instruct. Meta's Llama 3 automated "I don't know" training. Tool use via search special tokens. Dominik Hašek Stanley Cup example.

### Computation Per Token
Emily's apples-and-oranges problem illustrates why answers-then-explanation is bad training data. Single-token constraint experiments: works for small numbers, fails for 23 apples + 177 oranges. Recommendation: prompt "use code."

### Tokenization-Rooted Failures
Why counting 177 dots fails, "ubiquitous" as 3 tokens, strawberry R's, and 9.11 > 9.9 linked to Bible verse neurons.

### Reinforcement Learning and DeepSeek R1
Textbook analogy (exposition/worked examples/practice problems). Gemma 2 2B demo showing stochastic solutions. DeepSeek R1 paper revealing public RL methodology; emergent "wait, aha moment" behaviors; AIME accuracy climbing with response length.

### Thinking Model Access
Together.ai (American host of DeepSeek R1), OpenAI o1/o3-mini/o3-mini-high at $20-200/month with hidden chain-of-thought to prevent distillation, Google AI Studio's Gemini 2.0 Flash Thinking, Anthropic lacking one. Karpathy uses GPT-4o 80-90% of the time.

### AlphaGo and Move 37
Supervised learning plateaus below human performance; RL surpasses Lee Sedol. Move 37 (~1 in 10,000 human probability) as paradigm for what LLM RL might discover—possibly new reasoning strategies or even non-English internal languages.

### RLHF
Reward model imitating human rankings (ordering easier than scoring). Enables RL in unverifiable domains (jokes, poems). Gameable via adversarial inputs—must stop after a few hundred updates. "Not RL in the magical sense."

### Future Directions and Resources
Multimodality (audio spectrograms, image patches), agents (human-to-agent ratios), test-time training as open problem. Resources: LM Arena (gamed but useful), Swyx's AI News newsletter, X/Twitter. LM Studio for local models (e.g., Llama 3.2 Instruct 1B on MacBook).

### Closing
ChatGPT as lossy simulation of an OpenAI labeler. Thinking models as emergent beyond imitation. Use LLMs as tools; always verify; own the product of your work.

## Key Takeaways
- FineWeb is ~44TB / ~15 trillion tokens after aggressive filtering from Common Crawl's 2.7B pages.
- GPT-4 uses 100,277 BPE tokens (`cl100k_base`); tokenization is why models fail at character-level tasks.
- GPT-2 reproduction cost dropped from $40,000 (2019) to ~$600 via llm.c due to better data, hardware, and software.
- Training runs on 8×H100 nodes at ~$3/GPU/hour from providers like Lambda; NVIDIA's $3.4T valuation reflects the GPU gold rush.
- Base models are lossy compressions of the internet, not assistants; they hallucinate identity ("ChatGPT by OpenAI") because those terms dominate pre-training data.
- Each token has fixed, finite computation (~100 layers)—reasoning must be distributed across tokens, which is why labelers avoid answer-first solutions.
- Hallucinations stem structurally from SFT data that never models ignorance; mitigated via Llama 3's automated "I don't know" examples or web search tool use.
- DeepSeek R1 publicly revealed RL methodology for LLMs, showing emergent "wait, let me reevaluate" behaviors and response length growing with accuracy.
- RLHF is gameable (e.g., "the the the the" scoring 1.0) and must be stopped after a few hundred updates—fundamentally different from scalable verifiable-domain RL.
- ChatGPT responses should be understood as lossy neural simulations of OpenAI human labelers following labeling instructions.
- Always use LLMs as tools: leverage for drafts and inspiration, verify outputs, and own the final product.

## Notable Quotes
> "What is easy for you or I as human labelers is different than what's easy or hard for the LLM — its cognition is different."

> "RLHF is RL obviously but it's not RL in the magical sense."

> "The model is a statistical token tumbler... it boots up, processes tokens, and shuts off."

## Related Entities
[[Andrej Karpathy]], [[OpenAI]], [[DeepSeek R1]], [[Llama 3]], [[GPT-2]], [[GPT-4]], [[FineWeb]], [[Common Crawl]], [[InstructGPT]], [[Byte Pair Encoding]], [[Transformer]], [[Hugging Face]], [[AlphaGo]], [[RLHF]], [[Reinforcement Learning]], [[Together.ai]], [[Hyperbolic]], [[LM Studio]], [[Tiktokenizer]], [[llm.c]], [[Meta AI]], [[Anthropic]], [[Google Gemini]]