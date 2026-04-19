---
title: Wiki Schema
created: 2026-04-19
updated: 2026-04-19
type: meta
tags: [meta]
---

# Wiki Schema

## Domain
AI/ML research, LLM engineering, and agent systems.
Knowledge management using the Karpathy LLM Wiki pattern — a compounding, cross-referenced markdown knowledge base.

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `transformer-architecture.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`

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
Top-level tags for the AI/ML domain:

**Models & Architecture:**
- model, architecture, benchmark, training, fine-tuning, alignment

**People & Orgs:**
- person, company, lab, open-source

**Techniques:**
- optimization, inference, data, prompting, rag, context-window

**Evaluation & Meta:**
- evaluation, benchmark, controversy, prediction, timeline

**Systems:**
- agent, tool-use, multi-agent, memory, planning, orchestration

**Applications:**
- coding, research, creative, summarization, extraction

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines
- **Archive a page** when fully superseded — move to `_archive/`, remove from index

## Entity Pages
One page per notable entity. Include:
- Overview / what it is
- Key facts and dates
- Relationships to other entities ([[wikilinks]])
- Source references

## Concept Pages
One page per concept or topic. Include:
- Definition / explanation
- Current state of knowledge
- Open questions or debates
- Related concepts ([[wikilinks]])

## Comparison Pages
Side-by-side analyses. Include:
- What is being compared and why
- Dimensions of comparison (table format preferred)
- Verdict or synthesis
- Sources

## Update Policy
When new information conflicts with existing content:
1. Check the dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contradictions: [page-name]`
4. Flag for user review in the lint report
