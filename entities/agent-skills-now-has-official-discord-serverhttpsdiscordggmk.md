# Agent Skills now has an official [Discord server](https://discord.gg/MKPE9g8aUy). See the [announcement](https://github.com/agentskills/agentskills/discussions/273) for details.

---
title: "Best Practices for Skill Creators"
created: 2026-04-21
type: entity
tags: [agent-skills, llm-engineering, prompt-engineering, context-engineering, skill-design]
related: [[Agent Skills]], [[Progressive Disclosure]], [[SKILL.md Specification]], [[Evaluating Skills]], [[Using Scripts in Skills]], [[Optimizing Skill Descriptions]]
sources: [raw/articles/agentskills_io_skill-creation_best-practices.md]
---

# Best Practices for Skill Creators

## Summary
This is the official best-practices guide from agentskills.io for authoring Agent Skills — structured `SKILL.md`-based instruction bundles that extend an LLM agent's capabilities for specific domains or tasks. The guide is organized around four principles: (1) grounding skills in real, project-specific expertise rather than LLM-generated generic advice, (2) spending context window tokens wisely, (3) calibrating the level of control/prescriptiveness to the fragility of each sub-task, and (4) applying concrete structural patterns like gotchas sections, templates, checklists, and validation loops.

Key quantitative guidance: `SKILL.md` should stay under **500 lines and 5,000 tokens** per the specification; additional material belongs in a `references/` directory (or `assets/` for templates, `scripts/` for bundled code) and should be loaded on demand via progressive disclosure with explicit load triggers ("Read `references/api-errors.md` if the API returns a non-200 status"). The guide repeatedly emphasizes that once a skill activates, its entire body loads into context alongside conversation history and other active skills, so every token competes for agent attention.

The document prescribes concrete authoring workflows: extract skills from hands-on task traces (capturing corrections, I/O formats, project context), synthesize from artifacts (runbooks, code review comments, VCS patches, incident reports), and iterate via execute-then-revise cycles reading actual agent execution traces — not just final outputs. It introduces specific instructional patterns including **Gotchas sections** (environment-specific non-obvious facts), **output templates**, **checklists**, **validation loops**, and **plan-validate-execute** workflows (e.g., for PDF form filling: extract fields → create value map → validate against source-of-truth → execute).

## Key Concepts

- **Start from real expertise**: Skills authored by asking an LLM to generate content from its general training produce vague directives like "handle errors appropriately." Effective skills require domain-specific inputs — project schemas, failure modes, style guides — fed into the creation process.

- **Extract from hands-on tasks**: Complete a real task interactively with an agent, then distill the reusable pattern. Capture four things: steps that worked, corrections you made (e.g., "use library X not Y"), input/output formats, and project-specific context you supplied.

- **Synthesize from project artifacts**: Use internal runbooks, API specs, code review comments, VCS history (patches reveal real change patterns), and postmortems as source material. A pipeline skill built from your team's actual incident reports outperforms one built from generic "data engineering best practices."

- **Refine with real execution**: Run the skill, feed all results (not just failures) back in. Read execution traces to diagnose problems: vague instructions cause flailing, irrelevant instructions get followed anyway, and too many options without a default waste steps. Even one execute-revise pass noticeably improves quality.

- **Spend context wisely**: `SKILL.md` loads into the context window alongside conversation, system prompts, and other active skills. Add what the agent lacks; omit what it already knows (don't explain what a PDF is). Test the skill removal — if the agent handles the task without it, the skill may add no value.

- **Design coherent units**: Skill scope is like function scope. Too narrow forces multiple skills to co-load (conflicts, overhead); too broad makes activation imprecise. Example: "query database + format results" is one unit; adding "database administration" is too much.

- **Aim for moderate detail**: Exhaustive edge-case coverage hurts — the agent pursues inapplicable instructions. Concise stepwise guidance with a working example beats comprehensive documentation. Trust agent judgment for most edge cases.

- **Progressive disclosure**: Keep `SKILL.md` to core/always-needed content (<500 lines, <5,000 tokens). Move detailed material to `references/`, templates to `assets/`, code to `scripts/`. Critically, tell the agent *when* to load each file with specific triggers, not "see references/ for details."

- **Match specificity to fragility**: Give the agent freedom (often just explain *why*) for tasks with multiple valid approaches (e.g., code review checklist). Be prescriptive for fragile/destructive operations (e.g., "Run exactly this migration command, do not modify flags"). Most skills mix both.

- **Provide defaults, not menus**: Instead of listing pypdf / pdfplumber / PyMuPDF / pdf2image as equals, pick one default (pdfplumber) with a brief escape hatch ("For scanned PDFs use pdf2image with pytesseract").

- **Procedures over declarations**: Teach *how to approach* a problem class, not *what to produce* for one instance. A SQL skill should say "read schema, join on `_id` foreign keys, apply filters as WHERE clauses" — not "JOIN orders to customers and sum amount for EMEA."

- **Gotchas sections**: The highest-value content — concrete environment-specific facts defying reasonable assumptions. Examples: soft-delete tables requiring `WHERE deleted_at IS NULL`, ID fields named differently across services (`user_id`/`uid`/`accountId`), `/health` returning 200 while DB is down. Keep these in `SKILL.md` itself because triggers may not be recognizable in advance. When correcting agent mistakes, add to gotchas.

- **Output templates**: Agents pattern-match concrete structures better than prose descriptions. Inline short templates; store long/conditional ones in `assets/`.

- **Checklists**: Markdown checkbox lists (`- [ ] Step N: ...`) help track progress through dependent multi-step workflows.

- **Validation loops**: Pattern of do work → run validator (script/checklist/self-check) → fix issues → repeat until pass. Reference docs can serve as the validator.

- **Plan-validate-execute**: For batch/destructive operations, write an intermediate plan in a structured file, validate it against a source-of-truth artifact, then execute. PDF form-filling example: `analyze_form.py` → `form_fields.json` (source of truth) → author `field_values.json` → `validate_fields.py` produces actionable errors ("Field 'signature_date' not found — available: customer_name, order_total, signature_date_signed") → `fill_form.py`.

- **Bundling reusable scripts**: If execution traces show the agent reinventing the same logic (charting, parsing, validating) across runs, promote it to a tested script in `scripts/`.

## Key Takeaways
- `SKILL.md` should stay under **500 lines and 5,000 tokens**; overflow goes into `references/`, `assets/`, or `scripts/` with explicit load triggers.
- The most valuable skill content is project-specific knowledge the agent couldn't guess: conventions, schemas, non-obvious edge cases, tool choices.
- LLM-generated skills from generic prompts produce unhelpful platitudes; ground authoring in real execution traces, runbooks, review comments, and VCS patches.
- Gotchas sections — concrete "this defies reasonable assumptions" facts — belong in `SKILL.md` itself because the agent may not recognize when to load them from elsewhere.
- Calibrate prescriptiveness per sub-task: freedom (+ explain *why*) for flexible work, exact commands for fragile/destructive ops.
- Prefer a single default with an escape hatch over presenting multiple tools as equal options.
- Teach generalizable procedures, not task-specific answers — but specific templates, constraints (e.g., "never output PII"), and tool instructions remain valuable.
- Plan-validate-execute with a validator script catches errors before destructive operations and provides self-correction signal.
- Iterate by reading execution traces, not just final outputs — flailing reveals vague instructions, off-task behavior reveals over-applicable rules.

## Notable Quotes
> "A data-pipeline skill synthesized from your team's actual incident reports and runbooks will outperform one synthesized from a generic 'data engineering best practices' article."

> "Focus on what the agent *wouldn't* know without your skill... You don't need to explain what a PDF is, how HTTP works, or what a database migration does."

> "Deciding what a skill should cover is like deciding what a function should do: you want it to encapsulate a coherent unit of work that composes well with other skills."

> "A skill should teach the agent *how to approach* a class of problems, not *what to produce* for a specific instance."

> "When an agent makes a mistake you have to correct, add the correction to the gotchas section."

## Related Entities
[[Agent Skills]], [[SKILL.md Specification]], [[Progressive Disclosure]], [[Evaluating Skills]], [[Optimizing Skill Descriptions]], [[Using Scripts in Skills]], [[Context Engineering]]

## Tags
agent-skills, llm-engineering, prompt-engineering, context-engineering, skill-design, progressive-disclosure, validation-loops, documentation