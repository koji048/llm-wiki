---
title: Chain-of-Thought
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [prompting, reasoning, inference]
sources: []
---

# Chain-of-Thought

**Chain-of-thought** prompting is a technique that elicits step-by-step reasoning by asking the model to explain its thought process.

## Techniques

### Implicit
Add "Let's think step by step" to the prompt.

### Explicit
Provide examples of reasoning:
> "Q: If there are 3 apples and you take 2, how many do you have?
> A: You have 2 apples because you took them."

## Effectiveness

- Dramatically improves performance on complex reasoning tasks
- Math, logic, multi-step problems
- Allows inspection of model's reasoning

## See Also

- [[How I Use LLMs]]
- [[prompting]]
- [[reasoning-models]]
