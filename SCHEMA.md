---
title: Wiki Schema
created: 2026-04-19
updated: 2026-04-20
type: meta
tags: [meta]
---

# Wiki Schema

## Domain
AI/ML research, LLM engineering, and agent systems.
Knowledge management using the Karpathy LLM Wiki pattern — a compounding, cross-referenced markdown knowledge base.

## Core Insight (from karpathy.ai/llm-wiki)
Most RAG systems rediscover knowledge from scratch on every query — no accumulation.
The LLM Wiki is different: **the wiki is a persistent, compounding artifact.**
When you add a source, the LLM integrates it into the existing wiki — updating entity pages,
revising summaries, flagging contradictions. The knowledge is compiled once and kept current,
not re-derived on every query. Cross-references are already there. Synthesis reflects everything ingested.

You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it.
Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

## Use Cases
- **Research**: going deep on a topic over weeks/months — papers, articles, reports, evolving thesis
- **Software**: architecture decisions, runbooks, debugging patterns, agent workflows
- **Personal**: goals, health, learning — filed journal entries, article notes
- **Business/team**: internal wiki fed by Slack, meeting transcripts, project docs

## Architecture: Three Layers

### Layer 1 — Raw Sources (raw/)
Immutable source documents: articles, papers, images, data files.
The LLM reads but never modifies these. Source of truth.

### Layer 2 — The Wiki (entities/, concepts/, comparisons/, queries/)
LLM-generated markdown files. The LLM owns this layer entirely:
creates pages, updates when sources arrive, maintains cross-references.
Every page must link to at least 2 other pages via [[wikilinks]].

### Layer 3 — The Schema (SCHEMA.md)
The agent configuration file (like CLAUDE.md or AGENTS.md).
Tells the LLM how the wiki is structured, conventions, and workflows.
You and the LLM co-evolve this over time.

## Operations

### Ingest
Drop a source into raw/, tell the LLM to process it. The LLM:
1. Reads the source
2. Discusses key takeaways with you
3. Writes/updates wiki pages (entity, concept, comparison, summary)
4. Updates [[wikilinks]] across affected pages
5. Updates index.md and appends to log.md
A single source might touch 10-15 wiki pages. Batch-ingest is also possible.

### Query
Ask questions against the wiki. The LLM searches the index, reads relevant pages,
synthesizes an answer with citations.

**Important**: good query answers should be filed back into the wiki as new pages.
An analysis, comparison, or connection you discovered is valuable and shouldn't
disappear into chat history — it should compound like ingested sources.

### Lint
Periodically health-check the wiki:
- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages with no inbound links
- Important concepts missing their own page
- Missing cross-references
- Data gaps fillable via web search

## File Conventions
- File names: lowercase, hyphens, no spaces (e.g. tum-office-runtime-fix.md)
- Every wiki page starts with YAML frontmatter (see below)
- Use [[wikilinks]] to link between pages (minimum 2 outbound per page)
- When updating a page, always bump the updated date
- Every new page must be in index.md under the correct section
- Every action must be appended to log.md

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary | meta
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
---
```

## Tag Taxonomy
Top-level tags for AI/ML domain:
- **Models**: model, architecture, benchmark, training, fine-tuning, alignment
- **People/Orgs**: person, company, lab, open-source
- **Techniques**: optimization, inference, data, prompting, rag, context-window
- **Evaluation**: evaluation, benchmark, controversy, prediction, timeline
- **Systems**: agent, tool-use, multi-agent, memory, planning, orchestration
- **Applications**: coding, research, creative, summarization, extraction

## Index vs Log
- **index.md**: content-oriented catalog. One line per page: [[wikilink]] — summary. Organized by type. Updated on every ingest. The LLM reads this first when answering queries.
- **log.md**: chronological append-only record of all actions: ingests, queries, lints. Format: ## [YYYY-MM-DD] action | subject. Parseable with grep "^## \[" log.md | tail -5.

## Optional Tools
- **qmd** (github.com/tobi/qmd): local search engine for markdown — BM25/vector hybrid with LLM re-ranking, CLI + MCP server
- **Obsidian Web Clipper**: browser extension to convert web articles to markdown for quick ingestion
- **Obsidian**: the viewing IDE; LLM is the programmer; wiki is the codebase

## Update Policy
When new information conflicts with existing content:
1. Newer sources generally supersede older ones (check dates)
2. If genuinely contradictory, note both with dates and sources
3. Mark contradiction in frontmatter: contradictions: [page-name]
4. Flag for user review in lint report
