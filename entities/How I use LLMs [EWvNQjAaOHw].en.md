# How I use LLMs

---
title: "How I use LLMs"
created: 2026-04-20
type: entity
tags: [llm, chatgpt, claude, karpathy, practical-ai]
sources: [raw/transcripts/How I use LLMs [EWvNQjAaOHw].en.txt]
---

# How I use LLMs

## Summary

Andrej Karpathy's "How I use LLMs" is the practical companion to his "Deep Dive into LLMs" video, walking through real-world workflows across the 2025 LLM product ecosystem: ChatGPT (OpenAI), Claude (Anthropic), Gemini (Google), Grok (xAI), DeepSeek, Le Chat (Mistral), Meta AI, Copilot, and Perplexity. He grounds everything in a consistent mental model: an LLM is a ~1TB "lossy zip file" of the internet (roughly one trillion parameters, ~$10M+ and ~3 months to pre-train), wrapped in a post-training "assistant persona" from human labelers, operating on a 1D token stream with a vocabulary around 200,000 tokens (GPT-4o) and a context window that serves as fragile "working memory."

The video systematically tours: pricing tiers (Free / Plus $20 / Pro $200); thinking models trained via RL (o1, o3-mini, o1-pro, DeepSeek R1 from the "Incentivizing Reasoning Capabilities" paper); tool use including internet search, Python interpreter, and ChatGPT's Advanced Data Analysis; document upload (demoed with the Arc Institute's Evo 2 paper and Adam Smith's *Wealth of Nations*); Claude Artifacts for bespoke apps and Mermaid diagrams; Deep Research (ChatGPT, Perplexity, Grok Deep Search); and Cursor/Composer for "vibe coding" (a term Karpathy claims to have coined).

He then surveys multimodality: "fake audio" via SuperWhisper/WhisperFlow/MacWhisper transcription, "true audio" via spectrogram tokenization in ChatGPT Advanced Voice and Grok's unhinged/romantic/conspiracy voice modes, NotebookLM's "Deep Dive" podcasts (he produced a Spotify series "Histories of Mysteries"), image inputs (nutrition labels, blood tests, memes, math), DALL-E 3 and Ideogram for generation, Veo 2 for video, and mobile-only video input via Advanced Voice. He closes with quality-of-life features—Memory, Custom Instructions, Custom GPTs (his Korean vocabulary extractor, detailed translator, and Korean Cap OCR tool)—emphasizing **few-shot prompting with XML-delimited examples** as a universally accuracy-boosting technique.

## Key Concepts

- **The 1TB Zip File Mental Model**: An LLM is ~1 trillion parameters compressing a snapshot of the internet into a probabilistic, lossy file. Pre-training is expensive and infrequent, creating a **knowledge cutoff**; by default the model has no calculator, browser, or Python—just token-in, token-out.

- **Context Window as Working Memory**: The token stream visible to the model is a precious resource. Starting a new chat wipes it; cluttering it distracts the model and slows generation. Karpathy advises starting fresh chats per topic.

- **Pre-training vs. Post-training**: Pre-training compresses the internet (knowledge); post-training "attaches a smiley face"—conversations labeled by humans teach assistant persona and format.

- **Thinking Models**: A third training stage using RL on math/code problems where models discover inner-monologue strategies (backtracking, revisiting assumptions). Introduced publicly by the DeepSeek paper "Incentivizing Reasoning Capabilities in LLMs via Reinforcement Learning." OpenAI's "o" series (o1, o3-mini, o1-pro) and DeepSeek R1 are examples; Perplexity exposes raw R1 traces while OpenAI shows only summaries.

- **Tool Use**: Models emit special tokens that trigger external execution—internet search, Python interpreter, Advanced Data Analysis. Karpathy demonstrates Grok 3 hallucinating a large multiplication ("060" instead of "120"), Claude using JavaScript, and Gemini silently failing, while ChatGPT correctly invokes Python.

- **Deep Research**: Extended search + thinking over tens of minutes producing citation-rich reports. ChatGPT's version (Pro tier) is Karpathy's favorite after 10–20 uses; Perplexity and Grok Deep Search produce shorter reports. Still hallucinates (his LLM-labs table omitted xAI, wrongly included Hugging Face and EleutherAI).

- **Artifacts (Claude)**: Claude writes React code that runs live in-browser, enabling bespoke custom apps (he built a 20-card flashcard app on Adam Smith) and Mermaid-library diagrams of book chapters.

- **Vibe Coding & Cursor Composer**: Cursor (using Claude 3.7 Sonnet under the hood) with Cmd+I launches an autonomous agent across files. Karpathy built a Tic-Tac-Toe React app in ~5 sentences, then added `react-confetti` and a victory.mp3 via natural-language requests.

- **Fake vs. True Audio**: "Fake audio" is STT/TTS wrapped around a text LLM (SuperWhisper, WhisperFlow, MacWhisper). "True audio" tokenizes spectrogram chunks into a ~100k vocabulary the model natively processes (ChatGPT Advanced Voice, Grok voice mode).

- **Memory, Custom Instructions, Custom GPTs**: Persistent user database prepended to chats (ChatGPT-unique); global tone/role settings; reusable prompt templates. Few-shot examples with XML tags dramatically improve accuracy.

- **Native Multimodality**: Transformers model token streams agnostically—images as ~100k-patch vocab, audio as spectrogram tokens. Distinguish native Omni models from tacked-on pipelines (e.g., ChatGPT's image generation actually routes a caption to DALL-E 3).

## Major Sections

### Introduction and LLM Landscape
Overview of ChatGPT as 2022 incumbent, competitors (Gemini, Meta AI, Copilot, Claude, Grok, DeepSeek, Le Chat), and leaderboards (Chatbot Arena, SEAL). TikTokenizer demo shows a 15+19-token haiku exchange rendering as 42 tokens in GPT-4o's ~200k vocabulary.

### Pre-training & Post-training Mental Model
The 1TB zip file analogy; knowledge cutoff; appropriate low-stakes use cases (caffeine in an Americano at ~63mg; checking NyQuil ingredients against the physical box).

### Model Tiers and Thinking Models
ChatGPT Free/Plus ($20)/Pro ($200); Karpathy's "LLM Council" of Claude, Gemini, Grok (all recommended Zermatt). DeepSeek R1 paper introduces RL-based reasoning. Demo: a gradient-check bug in an MLP that GPT-4o fails, o1 Pro solves in ~1 minute, Claude 3.5 Sonnet and Gemini solve without thinking mode, Grok 3 solves, Perplexity R1 catches the "critical mistake" in parameter packing.

### Internet Search & Deep Research
White Lotus S3E2 release date as motivator. Claude lacks search (cutoff April 2024); Gemini 2.0 Pro Experimental lacks it, Flash has it. Deep Research demo on Ca-AKG (2.5g in Brian Johnson's Blueprint Longevity Mix).

### Document Upload
Evo 2 biological foundation model PDF (from Arc Institute, trained on OpenGenome 2); Claude 3.7 release during filming. Reading *Wealth of Nations* chapter-by-chapter via Project Gutenberg text pasted into Claude—"don't read books alone."

### Python Tool Use & Advanced Data Analysis
Cross-model multiplication test. OpenAI valuation plotting reveals ChatGPT silently substituted 0.1 for missing 2015 data and hallucinated a $1.7T extrapolation while code output was ~$20T—"a very very junior data analyst."

### Claude Artifacts
20 flashcards on Adam Smith rendered as a live React app; Mermaid diagrams of *Wealth of Nations* Chapter 3 (division of labor and extent of the market).

### Cursor, Composer & Vibe Coding
Tic-Tac-Toe app built in ~1 minute; Composer installs libraries and downloads assets autonomously.

### Voice Modalities
~50% voice on desktop, ~80% on mobile. ChatGPT Advanced Voice does Yoda/pirate but refuses a fox sound after doing a cow ("very cringe"). Grok's unhinged/romantic/conspiracy modes ("Trudeau/Castro lovechild," "lizard people," "the queen is a robot").

### NotebookLM
Generated ~30-minute Deep Dive podcast on the Evo 2 paper. Karpathy produced "Histories of Mysteries" on Spotify.

### Image, Video, and Generation
Brian Johnson's Longevity Mix nutrition label (transcribe-then-analyze); 20-page blood test PDF; Colgate toothpaste ingredient safety; crow "attempted murder" meme. DALL-E 3 vs. Ideogram (used for his "Let's reproduce GPT-2" thumbnail). Advanced Voice video input: acoustic foam, Genghis Khan book, Feynman book, Aranet4 CO2 monitor (713 PPM), Middle Earth map. Veo 2 as near state-of-the-art video generator.

### Quality of Life: Memory, Custom Instructions, Custom GPTs
Memory stores cross-chat preferences ("1990s–early 2000s was peak Hollywood"). Custom instructions avoid HR-speak; set Korean formality level. Custom GPTs: Korean Vocabulary Extractor, Korean Detailed Translator (beats Google Translate, Naver, Papago), Korean Cap (OCR + translate + grammar breakdown for Singles Inferno screenshots).

### Final Ecosystem Summary
Checklist: model/tier awareness, reasoning models, tools, multimodality (native vs. tacked-on), QoL features, web vs. mobile parity.

## Key Takeaways

- Treat every LLM as a ~1TB lossy zip file with a knowledge cutoff; use tools (search, Python) when information is recent, high-precision, or computational.
- Keep context windows lean—start new chats per topic; tokens are working memory.
- Know your tier and model. Free tiers run smaller, hallucination-prone models (GPT-4o mini, Claude Haiku); Karpathy pays for ChatGPT Pro ($200) and Claude Professional.
- Default to fast non-thinking models; escalate to thinking models (o1 Pro, R1, Claude extended thinking) only for hard math/code.
- ChatGPT Advanced Data Analysis and code outputs require code-literate scrutiny—it will silently substitute values and misreport numbers.
- Don't read dense books alone: paste chapters into Claude, ask for summaries first, then question as you read (he did this with *Wealth of Nations*).
- Cursor + Composer enables "vibe coding"—Karpathy claims to have coined the term.
- Use voice everywhere: SuperWhisper for system-wide STT; ChatGPT mobile for Advanced Voice; Grok for uncensored roleplay.
- Screenshot workflow (Mac: Ctrl+Shift+Cmd+4 → Cmd+V) is Karpathy's go-to for feeding labels, math, blood tests, and memes into ChatGPT.
- Few-shot prompts with XML-delimited examples consistently boost accuracy—use them in Custom GPTs.
- ChatGPT image generation is a tacked-on pipeline (caption → DALL-E 3), not native.
- Karpathy's personal stack: Perplexity for search, Claude Artifacts for prototyping/diagrams, ChatGPT Advanced Voice for conversation, Grok when other models are too restrictive, Cursor for professional coding.

## Notable Quotes

> "Hi, I'm ChatGPT, I am a one-terabyte zip file. My knowledge comes from the internet which I read in its entirety about six months ago and I only remember vaguely. My winning personality was programmed by example by human labelers at OpenAI."

> "Don't read books alone."

> "It's a very very junior data analyst."

> "Don't type stuff out, use voice, it works quite well."

## Related Entities

[[ChatGPT]], [[Claude (Anthropic)]], [[Grok (xAI)]], [[Gemini (Google)]], [[Perplexity]], [[DeepSeek R1]], [[Cursor]], [[NotebookLM]], [[Andrej Karpathy]], [[Evo 2 / Arc Institute]], [[SuperWhisper]], [[DALL-E 3]], [[Veo 2]], [[Mermaid Diagrams]], [[Vibe Coding]]