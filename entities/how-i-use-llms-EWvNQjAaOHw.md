---
title: How I use LLMs
created: 2026-04-20
updated: 2026-04-20
type: entity
tags: [video, llm, karpathy, practical, productivity]
sources: [raw/transcripts/How I use LLMs [EWvNQjAaOHw].en.txt]
---

# How I use LLMs

## Overview
In this practical follow-up to his theoretical "Deep Dive into LLMs" video, Andrej Karpathy demonstrates how he personally uses large language models in his daily work and life. The video covers the broader LLM ecosystem beyond just ChatGPT, various interaction patterns, tool use, multimodality, and numerous practical tips for getting the most out of these AI assistants. It's a general-audience practical guide showing real-world usage patterns rather than technical deep dives.

## Key Concepts

- **LLM Ecosystem**: The landscape of AI assistants including ChatGPT (OpenAI), Claude (Anthropic), Gemini (Google), Grok (xAI), Perplexity, and others—each with different features, strengths, and limitations.

- **Context Window**: The token-based working memory of a conversation, which Karpathy describes as "precious" and limited. It should be kept short and relevant to avoid distracting the model and degrading performance.

- **Pre-training vs Post-training**: Pre-training compresses the internet into model parameters (like a "lossy zip file"), while post-training attaches an "assistant persona" to make the model respond helpfully to queries.

- **Knowledge Cutoff**: Because pre-training is expensive and infrequent, models are inherently out of date. Recent information requires search tools or other retrieval methods.

- **Tool Use**: LLMs can be enhanced with tools like internet search, Python interpreters, and image generators that extend their capabilities beyond pure text prediction.

- **Multimodality**: Modern LLMs can handle text, audio, images, and video—either natively (omni models) or through attached external models.

- **Custom GPTs**: Specialized AI assistants created for specific tasks (like a Korean language tutor), configured with system instructions and examples.

- **Few-shot Prompting**: Providing examples in the prompt to teach the model the desired output format or behavior, which Karpathy calls "significantly more efficient" than description alone.

## Major Sections

### 1. LLM Ecosystem Overview
Karpathy introduces the landscape of AI assistants: ChatGPT as the "Original Gangster" incumbent, Claude, Gemini, Copilot, Grok, Perplexity, DeepSeek, and Mistral. He references leaderboards like Chatbot Arena and Scale AI's leaderboard for tracking model capabilities.

### 2. Basic Interaction Mechanics
How the text interface works—tokens flow in and out, the context window maintains conversation history, and the model generates responses token by token. Discusses the token vocabulary (~200,000 tokens) and how context window size affects cost and performance.

### 3. Understanding Model Training
Brief recap of pre-training (compressing internet knowledge into parameters) and post-training (converting the base model into an assistant). Emphasizes that knowledge cutoff means models don't know recent events and need external tools for up-to-date information.

### 4. Search Tool Capabilities
Demonstrates internet search integration in ChatGPT and Perplexity. Shows examples like "is the market open today?" and "where's White Lotus season 3 filmed?" Explains that models may automatically detect the need for search, or users can explicitly enable it. Different models have varying search integration.

### 5. Python Interpreter / Tool Use
The integration of programming ability into LLMs. For complex calculations (like large multiplications), the model writes and executes Python code rather than attempting calculation in its "head." Contrasts this with models like Grok 3 that lack code execution and may hallucinate math. This is described as "extremely powerful."

### 6. Data Analysis and Visualization
Advanced data analysis features allowing models to generate plots, analyze datasets, and create visual outputs directly within the conversation.

### 7. Custom GPTs and Instructions
Creating specialized assistants with custom system instructions and few-shot examples. Karpathy demonstrates a "Korean GPT" translator he built for language learning, showing how to structure prompts with XML-tagged examples to teach the model exactly how to format translations.

### 8. Voice Input/Output
On mobile: using the microphone button for speech-to-text input. On desktop: third-party apps like Super Whisper for global keyboard shortcuts to dictate text. On output: text-to-speech features like "Read Aloud" to have responses spoken back. Discusses how ~50% of his queries on desktop and ~80% on mobile are voice-based because typing feels tedious.

### 9. Image Generation
DALL-E 3 integration for generating images from text prompts. Examples include generating thumbnails for YouTube videos. Notes that image generation currently works through a separate caption-then-generate pipeline rather than native multimodal processing.

### 10. Video and Camera Input
Advanced Voice Mode on mobile allows the model to see through the camera and discuss what it observes—like identifying acoustic foam panels on walls or recognizing book titles. Demonstrates real-time visual conversation capabilities.

### 11. Translation as a Use Case
Demonstrates building a superior Korean-English translator using few-shot prompting in Custom GPTs, which outperforms Google Translate especially for nuanced language learning. Shows how to break down translations part-by-part with examples.

### 12. Quality of Life Features
File uploads, memory features, custom instructions, and the distinction between web app and mobile app feature availability. Notes that features like Advanced Voice are mobile-only while some desktop features don't translate to phone.

### 13. Summary: Key Principles
Encourages viewers to experiment with features over time, be aware that different apps have different capability integrations, and keep track of which features exist where.

## Notable Quotes

> "Think of the tokens in the context window as a precious resource... think of that as the working memory of the model and don't overload it with irrelevant information."

> "Whenever I expect that the answer can be achieved by doing basically something like Google search and visiting a few of the top links... I expect to use the search tool."

> "The more tokens are in the window, the more expensive it is by a little bit to sample the next token."

> "We have a Python interpreter and this is just an example of multiplication, but this is significantly more powerful."

> "I would not use a different translator other than ChatGPT—it understands a ton of nuance, it understands slang, it's extremely good."

> "Human labelers are involved in curating data sets that kind of tell the model by example in what kinds of situations it should lean on tools."

## Key Takeaways

1. **Context window is precious**: Keep conversations short and start new chats when switching topics to avoid model distraction and unnecessary cost.

2. **Match tools to tasks**: Use search for recent information, Python interpreter for math/calculations, and custom GPTs for specialized repetitive tasks.

3. **Verify outputs**: LLMs can hallucinate—especially for math or niche knowledge. Always check critical information against reliable sources.

4. **Voice input dramatically improves workflow**: ~50-80% of queries can be voice-based, especially on mobile where typing is cumbersome.

5. **Custom GPTs extend utility**: Creating specialized assistants with few-shot examples can significantly outperform generic interfaces for specific use cases like language learning or translation.

6. **Tool availability varies by platform**: Not all features exist in all apps—keep track of where capabilities like search, voice mode, and code execution are available.

7. **Experiment continuously**: The LLM ecosystem evolves rapidly; regularly explore new features and apps to find what works best for your workflows.

## Related Entities

[[karpathy-llm-wiki]] - Same author
[[deep-dive-into-llms-7xTGNNLPyMI]] - Deep dive theory video
[[intro-to-large-language-models-zjkBMFhNj_g]] - Intro talk
[[micrograd-neural-networks-backpropagation-VMj-3S1tku0]] - Neural network fundamentals

## Source
https://www.youtube.com/watch?v=EWvNQjAaOHw
