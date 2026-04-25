# Best practices for skill creators - Agent Skills

---
title: "Best Practices for Skill Creators"
created: 2026-04-25
type: entity
tags: [agent-skills, llm-engineering, prompt-engineering, context-management, skill-design]
related: [[Agent Skills]], [[SKILL.md]], [[Progressive Disclosure]], [[Context Window Management]], [[LLM Agents]]
sources: [raw/articles/skill-creation-best-practices.md]
---

# Best Practices for Skill Creators

## Summary
This is the official Agent Skills guide on authoring high-quality skills — modular instruction bundles (centered on a `SKILL.md` file) that extend LLM agent capabilities. The guide covers four main areas: (1) grounding skills in real expertise rather than LLM-generated generic content, (2) spending the context window wisely since `SKILL.md` loads in full on activation, (3) calibrating prescriptiveness to task fragility, and (4) reusable instruction patterns (gotchas, templates, checklists, validation loops, plan-validate-execute).

Key quantitative guidance: `SKILL.md` should stay under **500 lines and 5,000 tokens**, with detailed reference material offloaded to `references/` or `assets/` directories and loaded on-demand via progressive disclosure. The guide is aimed at preventing common anti-patterns: vague LLM-generated skills ("handle errors appropriately"), overly comprehensive documentation, menus of equal-weight options instead of clear defaults, and one-off declarative answers instead of reusable procedures.

The document fits into a broader workflow that also includes companion guides on **Evaluating skill output quality**, **Optimizing skill descriptions** (the `description` field that controls activation), and **Using scripts in skills** (bundling reusable code in `scripts/`).

## Key Concepts

- **Grounding in real expertise**: The most common skill-creation failure is asking an LLM to generate a skill cold, producing vague boilerplate. Effective skills are built from hands-on task traces, corrections made during real use, and project-specific artifacts (runbooks, style guides, API specs, code review comments, version control history, incident reports).

- **Extract-from-task workflow**: Complete a real task with an agent, noting steps that worked, corrections ("use library X instead of Y"), input/output formats, and project-specific context you provided. Distill that transcript into the skill.

- **Execute-then-revise iteration**: Run drafts against real tasks and feed all results (not just failures) back in. Read **execution traces**, not only final outputs — wasted time indicates instructions that are too vague, non-applicable, or lack a clear default among options.

- **Context budget**: On activation, the entire `SKILL.md` body loads into the agent's context window alongside conversation, system prompt, and other active skills. Every token competes for attention. Rule: "Would the agent get this wrong without this instruction? If no, cut it."

- **Coherent unit scoping**: Skills are like functions — too narrow forces multiple activations and conflicting instructions; too broad defeats precise activation. Example: "query a database and format results" = coherent; adding "database administration" = too broad.

- **Progressive disclosure**: Keep `SKILL.md` ≤ 500 lines / 5,000 tokens for core always-needed instructions. Offload reference material to `references/` with explicit triggers: "Read `references/api-errors.md` if the API returns a non-200 status code" (not generic "see references/").

- **Specificity vs. fragility calibration**: Be prescriptive for fragile/destructive/order-sensitive operations (e.g., database migrations with exact commands, "Do not modify the command"). Be flexible for tasks tolerating variation (e.g., code review checklist) — explain *why* rather than dictating steps.

- **Defaults over menus**: Instead of "You can use pypdf, pdfplumber, PyMuPDF, or pdf2image," pick a default (pdfplumber) and mention alternatives as escape hatches for specific cases (pdf2image+pytesseract for scanned OCR).

- **Procedures over declarations**: Teach the agent *how* to approach a class of problems, not the answer for one instance. A schema-lookup + join-by-convention procedure generalizes; a specific SQL query does not.

- **Gotchas sections**: The highest-value content — concrete, non-obvious environment facts that defy reasonable assumptions. Examples: soft-delete columns requiring `WHERE deleted_at IS NULL`, identifier name drift across services (`user_id` / `uid` / `accountId`), `/health` vs `/ready` endpoint semantics. Keep in `SKILL.md` so the agent sees them preemptively.

- **Output templates**: Provide concrete markdown/code templates rather than prose descriptions — agents pattern-match structures more reliably than they follow format descriptions. Long or conditional templates belong in `assets/`.

- **Checklists for multi-step workflows**: Explicit `- [ ]` progress lists help the agent track dependencies and validation gates.

- **Validation loops**: Do work → run validator (script, checklist, or self-check) → fix → repeat until passing. A reference document can serve as validator.

- **Plan-validate-execute pattern**: For batch/destructive ops, the agent produces a structured plan, a validation script checks it against a source of truth, then execution runs. Informative error messages (e.g., "Field 'signature_date' not found — available: customer_name, order_total, signature_date_signed") enable self-correction.

- **Bundled reusable scripts**: If trace comparison shows the agent reinventing the same logic (chart building, format parsing, validation), extract it into a tested script in `scripts/`.

## Key Takeaways

- `SKILL.md` hard limits: **under 500 lines and 5,000 tokens**; everything else goes in `references/`, `assets/`, or `scripts/` with explicit load triggers.
- Never generate skills from LLM general knowledge alone — feed in project-specific artifacts (runbooks, schemas, review comments, git history, incident reports).
- Omit what the agent already knows (what a PDF is, how HTTP works); include only project-specific conventions, non-obvious edge cases, and tool choices.
- Read agent **execution traces**, not just final outputs, to diagnose vague instructions, irrelevant rules, or missing defaults.
- Provide a **single default** with a brief escape hatch for alternatives; never present equal-weight option menus.
- Write **procedures** that generalize, not **declarations** that solve one instance.
- The **gotchas section** is often the highest-ROI content in a skill; append to it every time you correct an agent mistake.
- For fragile/destructive tasks, be prescriptive with exact commands and explicit prohibitions ("Do not modify the command or add additional flags").
- Use the **plan-validate-execute** pattern for batch/destructive operations, backed by a validation script with informative error messages.
- Templates beat prose for output formatting; checklists beat paragraphs for multi-step workflows.

## Notable Quotes

> "Ask yourself about each piece of content: 'Would the agent get this wrong without this instruction?' If the answer is no, cut it."

> "The specification recommends keeping SKILL.md under 500 lines and 5,000 tokens — just the core instructions the agent needs on every run."

> "A skill should teach the agent how to approach a class of problems, not what to produce for a specific instance."

> "When an agent makes a mistake you have to correct, add the correction to the gotchas section. This is one of the most direct ways to improve a skill iteratively."

> "A data-pipeline skill synthesized from your team's actual incident reports and runbooks will outperform one synthesized from a generic 'data engineering best practices' article."

## Related Entities
[[Agent Skills]], [[SKILL.md Specification]], [[Progressive Disclosure]], [[Context Window Management]], [[Skill Description Optimization]], [[Evaluating Skill Output Quality]], [[Using Scripts in Skills]], [[LLM Agents]]