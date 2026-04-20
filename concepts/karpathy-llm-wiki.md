---
title: karpathy/llm-wiki
created: 2026-04-20
updated: 2026-04-20
type: summary
tags: [agent, memory, rag, knowledge-base]
sources: [https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f]
---

# karpathy/llm-wiki

## What It Is
A GitHub gist by Andrej Karpathy (April 2026, 5,000+ stars) describing a pattern for building personal knowledge bases using LLMs.
URL: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## Core Insight
Most RAG systems re-derive knowledge from scratch on every query. The LLM Wiki pattern inverts this:
the wiki is a **persistent, compounding artifact** — LLM writes and maintains it incrementally,
cross-references are already built, contradictions are flagged, synthesis is kept current.
The human curates sources; the LLM does all the filing, summarizing, and bookkeeping.

> "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

## Key Points
- **Wiki beats RAG** for accumulating knowledge over time
- **Schema (SCHEMA.md)** is the agent config — like CLAUDE.md / AGENTS.md — tells the LLM how to behave as wiki maintainer
- **Query answers filed back as pages** — explorations compound just like ingested sources
- **Lint** periodically — orphan pages, contradictions, stale content, missing cross-links
- **index.md** for content catalog (read first for queries), **log.md** for chronological append-only action log
- Tools: qmd (BM25/vector hybrid search + MCP server), Obsidian Web Clipper

## Related
- [[llm-wiki-skill]] — our implementation of this pattern on VPS
- [[obsidian]] — Obsidian as the viewing IDE for the wiki
