# Best practices for skill creators - Agent Skills

---
title: "Best Practices for Skill Creators"
created: 2026-04-25
type: entity
tags: [agent-skills, llm-engineering, prompt-engineering, context-management, skill-design]
related: [[Agent Skills]], [[SKILL.md Specification]], [[Progressive Disclosure]], [[Evaluating Skill Output Quality]], [[Optimizing Skill Descriptions]]
sources: [raw/articles/skill-creation-best-practices.md]
---

# Best Practices for Skill Creators

## Summary
This reference page from agentskills.io documents best practices for authoring Agent Skills — modular SKILL.md-based instruction bundles that LLM agents load into their context window to perform specialized tasks. It covers four major areas: grounding skills in real domain expertise (not LLM-generated generics), spending the agent's context window wisely, calibrating control (prescriptiveness vs. freedom), and applying structured instructional patterns such as gotchas, templates, checklists, and validation loops.

The guidance is tightly tied to the Agent Skills specification, which recommends keeping SKILL.md under **500 lines and 5,000 tokens**, using progressive disclosure through `references/`, `assets/`, and `scripts/` subdirectories, and loading supplemental material on-demand. The page treats skill creation as an iterative engineering activity: draft from real tasks or project artifacts, run against real executions, read agent traces (not just outputs), and fold corrections back into a gotchas section.

Core design metaphor: **a skill should be like a function** — coherent in scope, composable with other skills, and teaching procedures (reusable methods) rather than declarations (one-off answers). Techniques include plan-validate-execute workflows for destructive operations, bundled scripts in `scripts/` to replace reinvented logic, and output-format templates that exploit agents' pattern-matching strengths.

## Key Concepts

- **Start from Real Expertise**: Skills generated purely from an LLM's general training produce vague platitudes ("handle errors appropriately"); effective skills must be grounded in domain-specific context. Two primary extraction methods: completing a hands-on task with an agent then distilling the reusable pattern, or synthesizing from project artifacts (runbooks, API specs, code review comments, VCS history, incident reports).

- **Refine with Real Execution**: First-draft skills require iteration against real tasks, feeding all results (not just failures) back into revision. Even one execute-then-revise pass noticeably improves quality. Authors should read **agent execution traces**, not just final outputs — wasted steps signal vague instructions, inapplicable directives, or too many options without defaults.

- **Context Window Economy**: Once a skill activates, the entire SKILL.md body loads alongside conversation history, system context, and other active skills. Every token competes for attention, so authors should **add what the agent lacks and omit what it knows** — skip explaining PDFs, HTTP, or common concepts; jump straight to project-specific conventions and non-obvious edge cases.

- **Coherent Unit Scoping**: Like function design, a skill should encapsulate one coherent unit of work. Too narrow forces multiple skills to co-load (overhead, conflicts); too broad hurts precise activation. Example: "query DB + format results" is coherent; adding "DB administration" is overreach.

- **Progressive Disclosure**: For skills legitimately exceeding 500 lines / 5,000 tokens, move detailed material to `references/` or similar directories with explicit load triggers ("Read `references/api-errors.md` if the API returns non-200" beats a generic "see references/"). This enables on-demand context loading.

- **Calibrating Control — Match Specificity to Fragility**: Prescriptiveness should match task fragility. For flexible tasks (e.g., code review), explain *why* rather than dictate exact steps, since an agent understanding purpose makes better context-dependent decisions. For fragile operations (DB migrations), prescribe exact commands with instructions not to modify them. Most skills mix both.

- **Defaults Over Menus**: Instead of listing pypdf / pdfplumber / PyMuPDF / pdf2image as equals, pick a default (pdfplumber for text extraction) and mention alternatives as escape hatches (pdf2image + pytesseract for scanned PDFs).

- **Procedures Over Declarations**: Teach *how* to approach a class of problems, not *what* to produce for a specific instance. "Read schema, join on `_id` convention, apply WHERE clauses, aggregate as markdown table" generalizes; "Join orders to customers on customer_id WHERE region='EMEA'" does not.

- **Gotchas Sections**: Concrete environment-specific corrections to mistakes the agent will otherwise make — e.g., soft-delete columns requiring `WHERE deleted_at IS NULL`, ID field name mismatches across services (`user_id`/`uid`/`accountId`), `/health` vs `/ready` semantics. Keep these in SKILL.md itself since the agent may not recognize triggers to load a reference file. When correcting the agent, add the correction here.

- **Output Templates**: Agents pattern-match well against concrete structures, making templates more reliable than prose descriptions of format. Short templates inline in SKILL.md; long or situational templates in `assets/` loaded on demand.

- **Checklists**: Explicit progress trackers (`- [ ] Step 1: ...`) help the agent avoid skipped steps, especially with dependencies or validation gates.

- **Validation Loops**: Pattern of "do work → run validator → fix issues → repeat until passing." The validator can be a script, a reference checklist, or a self-check against a reference document.

- **Plan-Validate-Execute**: For batch or destructive operations, have the agent produce an intermediate plan (e.g., `field_values.json`), validate against a source of truth (`form_fields.json`), and only execute after validation passes. Rich error messages ("Field 'signature_date' not found — available: customer_name, order_total, signature_date_signed") enable self-correction.

- **Bundled Scripts**: If execution traces reveal the agent reinventing the same logic (chart building, format parsing, output validation) across runs, extract it into a tested script in `scripts/`.

## Key Takeaways
- Keep SKILL.md under **500 lines and 5,000 tokens**; use `references/`, `assets/`, and `scripts/` directories with explicit load triggers for anything larger.
- Never generate skills purely from LLM general knowledge — ground them in hands-on task transcripts or project artifacts (runbooks, API specs, code reviews, VCS history).
- Ask of every sentence: "Would the agent get this wrong without this instruction?" If no, cut it.
- Read agent execution **traces**, not just outputs; wasted steps diagnose vague instructions, inapplicable guidance, or missing defaults.
- Calibrate prescriptiveness per section: freedom (with "why") for flexible tasks, rigid commands for fragile ones.
- Provide one default with brief escape hatches rather than equal-weight menus of options.
- Gotchas sections belong inline in SKILL.md because the agent may not recognize triggers to load them from a reference file.
- For destructive or batch work, use plan-validate-execute with a source-of-truth validator script.
- When you correct the agent during use, fold that correction into the gotchas section — direct iterative improvement.
- Extract repeatedly reinvented logic into bundled scripts rather than re-explaining it each run.

## Notable Quotes
> "Effective skills are grounded in real expertise. The key is feeding domain-specific context into the creation process."

> "Focus on what the agent wouldn't know without your skill... You don't need to explain what a PDF is, how HTTP works, or what a database migration does."

> "A skill should teach the agent how to approach a class of problems, not what to produce for a specific instance."

> "When an agent makes a mistake you have to correct, add the correction to the gotchas section. This is one of the most direct ways to improve a skill iteratively."

> "Deciding what a skill should cover is like deciding what a function should do: you want it to encapsulate a coherent unit of work that composes well with other skills."

## Related Entities
[[Agent Skills]], [[SKILL.md Specification]], [[Progressive Disclosure]], [[Evaluating Skill Output Quality]], [[Optimizing Skill Descriptions]], [[Using Scripts in Skills]], [[Context Window Management]], [[Plan-Validate-Execute Pattern]]