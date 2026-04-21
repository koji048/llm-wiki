---
title: karpathy/llm-wiki
created: 2026-04-20
updated: 2026-04-21
type: concept
tags: [agent, knowledge-base, memory, rag-alternative]
sources: [https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f]
---

# karpathy/llm-wiki

> Source: [GitHub Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) by Andrej Karpathy · April 2026 · 5,000+ stars

## Core Insight

Most people's experience with LLMs and documents is RAG: upload files, the LLM retrieves relevant chunks at query time, generates an answer. It rediscovers knowledge from scratch on every question. Nothing accumulates. Ask a subtle question requiring synthesizing five documents, and the LLM has to find and piece together the fragments every time.

**The LLM Wiki pattern inverts this.** Instead of retrieving from raw documents at query time, the LLM incrementally builds and maintains a persistent wiki — a structured, interlinked collection of markdown files that sits between you and the raw sources. When you add a new source, the LLM doesn't just index it for later retrieval. It reads it, extracts key information, and integrates it into the existing wiki — updating entity pages, revising topic summaries, noting where new data contradicts old claims, strengthening or challenging the evolving synthesis.

**The wiki is a persistent, compounding artifact.** Cross-references are already there. Contradictions have already been flagged. Synthesis already reflects everything you've read. The wiki keeps getting richer with every source you add and every question you ask.

> "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

## Three Layers

### Layer 1 — Raw Sources (`raw/`)
Immutable source documents: articles, papers, images, data files. The LLM reads from them but never modifies them. This is the source of truth.

### Layer 2 — The Wiki (`entities/`, `concepts/`, `comparisons/`, `queries/`)
LLM-generated markdown files. The LLM owns this layer entirely — creates pages, updates when sources arrive, maintains cross-references, keeps everything consistent. Every page must link to at least 2 other pages via wikilinks.

### Layer 3 — The Schema (`SCHEMA.md`)
The agent configuration file (like CLAUDE.md for Claude Code or AGENTS.md for Codex). Tells the LLM how the wiki is structured, what conventions to follow, and what workflows to execute when ingesting sources, answering queries, or maintaining the wiki. The schema co-evolves between the human and LLM over time as they figure out what works.

## Operations

### Ingest
Drop a new source into `raw/`, tell the LLM to process it:

1. LLM reads the source and discusses key takeaways with you
2. Writes a summary page in the wiki
3. Updates relevant entity and concept pages across the wiki
4. Updates `index.md` and appends to `log.md`

A single source can touch 10-15 wiki pages. Batch-ingest is also possible with less supervision.

### Query
Ask questions against the wiki. The LLM searches the index, reads relevant pages, synthesizes an answer with citations. **Good query answers should be filed back into the wiki as new pages** — explorations compound just like ingested sources. An analysis, comparison, or connection you discovered is valuable and shouldn't disappear into chat history.

### Lint
Periodically health-check the wiki:

- Contradictions between pages (newer sources superseding older claims)
- Stale claims that newer sources have superseded
- Orphan pages with no inbound links
- Important concepts mentioned but lacking their own page
- Missing cross-references
- Data gaps fillable via web search

## Index and Log

Two special files help navigate the wiki as it grows:

**`index.md`** — content-oriented catalog. One line per page: wikilink + one-line summary. Organized by type. Read this first when answering queries. Works well at moderate scale without embedding-based RAG infrastructure.

**`log.md`** — chronological append-only record of all actions: ingests, queries, lints. Format: `## [YYYY-MM-DD] action | subject`. Parseable with `grep "^## \[" log.md | tail -5`.

## Why It Works

The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value.

LLMs don't get bored. Don't forget to update a cross-reference. Can touch 15 files in one pass. **The wiki stays maintained because the cost of maintenance is near zero.**

The human's job: curate sources, direct the analysis, ask good questions, think about what it all means. The LLM's job: everything else.

**Relation to Memex:** The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. Bush couldn't solve who does the maintenance. The LLM handles that.

## Optional Tools

- **qmd** (github.com/tobi/qmd): local search engine for markdown with BM25/vector hybrid search and LLM re-ranking, all on-device. CLI and MCP server available.
- **Obsidian Web Clipper**: browser extension that converts web articles to markdown for quick ingestion into `raw/articles/`
- **Obsidian**: the viewing IDE for the wiki. Graph View shows the knowledge network. Dataview plugin runs queries over YAML frontmatter.
- **Marp**: markdown-based slide deck format. Obsidian has a plugin. Useful for generating presentations from wiki content.

## Implementation Notes

- **Wiki beats RAG** for accumulating knowledge over time — compilation is amortized, not repeated per query
- **Query answers filed back as pages** — this is the key compounding mechanism beyond just source ingestion
- **Obsidian on Mac** connects to the VPS wiki via GitHub sync. Google Drive syncs files but not git state — a `git pull` or launchd agent is needed to keep the Mac clone current after VPS pushes.
- **Git workflow**: VPS cron auto-commits. After remote pushes, use `git fetch + git checkout origin/master -- .` to reset working tree to remote state before applying new changes. Never rebase when remote has new commits.

## Related

- [[andrej-karpathy]] — Andrej Karpathy, creator of this pattern
- [[rlhf]] — Reinforcement Learning from Human Feedback, a core technique in LLM alignment discussed in the wiki context
