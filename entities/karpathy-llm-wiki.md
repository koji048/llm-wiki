---
title: "karpathy-llm-wiki"
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [meta, knowledge-management]
sources: []
---

# karpathy-llm-wiki

## Summary
The LLM Wiki is Andrej Karpathy's knowledge management pattern for compounding AI research. Unlike traditional RAG (which rediscoveries knowledge from scratch per query), the LLM Wiki is a persistent, cross-referenced artifact that compounds over time. When new sources are ingested, the LLM integrates them into existing pages — updating summaries, revising claims, adding cross-links — so the wiki grows richer with each addition rather than starting fresh.

## Core Principles
- **LLM writes the wiki**: humans rarely write pages; the LLM creates and maintains all content from sources
- **Compounding over querying**: wiki as a compiled artifact, not a retrieval engine
- **Cross-referencing**: every page links to at least 2 others via [[wikilinks]]
- **Obsidian as IDE**: human reads/searches in Obsidian; LLM acts as programmer writing the codebase
- **Query answers filed back**: insights from Q&A sessions get their own pages, not lost to chat history

## Schema
- **raw/** — immutable source documents (articles, papers, transcripts)
- **entities/** — LLM-generated pages on specific topics
- **concepts/** — conceptual explainers
- **comparisons/** — side-by-side analysis
- **queries/** — filed Q&A results
- **SCHEMA.md** — agent configuration file

## Related Entities
- [[andrej-karpathy]] — Creator of the pattern
- [[deep-dive-into-llms-7xTGNNLPyMI]] — Same author, LLM deep dive
