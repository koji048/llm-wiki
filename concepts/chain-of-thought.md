---
title: Context Window
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [LLM, memory, inference]
sources: []
---

# Context Window

The **context window** is the maximum number of tokens an LLM can consider simultaneously during inference.

## Key Properties

- Within context: full [[attention]] to all tokens
- Outside context: no memory at all
- Different models have different context limits

## Common Context Window Sizes

| Model | Context |
|-------|---------|
| GPT-4 Turbo | 128k tokens |
| GPT-4 | 8k-32k tokens |
| Claude 2 | 200k tokens |
| Gemini Pro | 32k tokens |

## Implications

- Cannot reason about information outside context
- Very long documents may need truncation
- Important context may be "forgotten" in long conversations
- Key information should be placed prominently

## See Also

- [[How I Use LLMs]]
- [[attention]]
- [[Deep Dive into LLMs]]
