---
title: Karpathy Guidelines
description: Four behavioral principles derived from Andrej Karpathy's observations on LLM coding pitfalls — Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution. Source: forrestchang/andrej-karpathy-skills.
source: https://github.com/forrestchang/andrej-karpathy-skills
tags: [coding-practices, llm-patterns, meta, productivity, best-practices]
related: [karpathy-llm-wiki, anthropic-agent-skills, tum-office]
created: 2026-04-23
updated: 2026-04-23
type: concept
---

# Karpathy Guidelines

Four behavioral principles to reduce common LLM coding mistakes. Derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls. Source: [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) (76.7k stars on GitHub).

**Core tradeoff:** Bias toward caution over speed. For trivial tasks (typos, obvious one-liners), use judgment — not every change needs full rigor.

## The Four Principles

### 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

**Common anti-pattern:** Silently assuming file format, field names, scope, or data structure without confirming. This leads to code that solves the wrong problem.

### 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If 200 lines could be 50, rewrite it.

**The test:** Would a senior engineer say this is overcomplicated? If yes, simplify.

**Common anti-pattern:** Adding strategy patterns, dependency injection, configuration systems, or abstraction layers before the actual requirements demand them. "What if we need X later?" is not a requirement.

### 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it — don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

**The test:** Every changed line traces directly to the user's request.

**Common anti-pattern:** Reformatting quotes, adding type hints, improving error messages while fixing a bug. These "drive-by improvements" create noise in diffs and make review harder.

### 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan with verification at each step:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

## Anti-Patterns Quick Reference

| Principle | Anti-Pattern | Fix |
|---|---|---|
| Think Before Coding | Silently assumes file format, fields, scope | List assumptions explicitly, ask |
| Simplicity First | Strategy pattern for single discount calc | One function until complexity is actually needed |
| Surgical Changes | Reformats quotes + adds type hints while fixing bug | Only change lines that fix the reported issue |
| Goal-Driven | "I'll review and improve the code" | "Write test for X → make it pass → verify no regressions" |

## Key Insight

> "LLMs are exceptionally good at looping until they meet specific goals... Don't tell it what to do, give it success criteria and watch it go." — Andrej Karpathy

The "overcomplicated" examples aren't obviously wrong — they follow design patterns and best practices. The problem is **timing**: they add complexity before it's needed, which makes code harder to understand, introduces more bugs, and takes longer to implement.

**Good code is code that solves today's problem simply, not tomorrow's problem prematurely.**

## Adoption in Hermes Agent

Hermes Agent has `karpathy-guidelines` as a registered skill. It is loaded automatically for:
- Any coding, implementation, or refactoring task
- User says "build", "implement", "fix", "add", "change", "rewrite"
- Code review or PR review request
- Before making non-trivial edits to existing files

## How to Know It's Working

- Fewer unnecessary changes in diffs
- Fewer rewrites due to overcomplication
- Clarifying questions come **before** implementation, not after mistakes
- Clean, minimal diffs — no drive-by refactoring

## Related Concepts

- [[karpathy-llm-wiki]] — Karpathy's LLM Wiki pattern (the compounding knowledge base approach)
- [[anthropic-agent-skills]] — Anthropic's skill system for coding agents (similar goal: systematic, high-quality agent behavior)
- [[tum-office]] — The Tum Office project where these guidelines are applied in practice

## Source Files

- `skills/karpathy-guidelines/SKILL.md` — skill definition with full principles
- `skills/karpathy-guidelines/references/examples.md` — detailed code examples for each anti-pattern
