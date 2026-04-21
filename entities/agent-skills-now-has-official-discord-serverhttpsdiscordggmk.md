# Agent Skills now has an official [Discord server](https://discord.gg/MKPE9g8aUy). See the [announcement](https://github.com/agentskills/agentskills/discussions/273) for details.

---
title: "Best Practices for Skill Creators"
created: 2026-04-21
type: entity
tags: [agent-skills, llm-engineering, prompt-engineering, context-management, skill-design]
related: [[Agent Skills]], [[SKILL.md Specification]], [[Progressive Disclosure]], [[Evaluating Skills]], [[Optimizing Skill Descriptions]], [[Using Scripts in Skills]]
sources: [raw/articles/agentskills_io_skill-creation_best-practices.md]
---

# Best Practices for Skill Creators

## Summary
This is the official best-practices guide from agentskills.io for authoring Agent Skills — portable, model-agnostic units of expertise packaged as `SKILL.md` files (plus optional `references/`, `assets/`, and `scripts/` directories) that load into an LLM agent's context when activated. The guide organizes skill authorship around four themes: grounding skills in real expertise rather than LLM-generated generic advice, spending context-window tokens wisely, calibrating the level of prescriptive control to task fragility, and applying reusable structural patterns (gotchas, templates, checklists, validation loops).

Key quantitative guidance: keep `SKILL.md` under **500 lines and 5,000 tokens** per the specification, pushing detail into secondary files loaded via progressive disclosure — but only when the agent is told explicitly *when* to load them. The guide emphasizes that skills should teach *procedures* (reusable methods) rather than *declarations* (specific answers), should provide a single default rather than menus of options, and should omit content the agent already knows (e.g., what a PDF is, how HTTP works).

The document recommends an iterative workflow: draft from real expertise (either extracted from a hands-on agent session or synthesized from project artifacts like runbooks, API specs, code-review comments, and version-control patches), run against real tasks, read execution traces (not just final outputs), and fold corrections back in — especially as entries in a dedicated "Gotchas" section. It cross-references companion guides on evaluating skills, optimizing descriptions, and bundling scripts.

## Key Concepts

- **Grounding in Real Expertise**: Skills generated purely from an LLM's general training produce vague procedures ("handle errors appropriately") instead of concrete project-specific patterns. Effective skills are extracted from a hands-on task (noting corrections, I/O formats, and context provided) or synthesized from existing artifacts — runbooks, API specs, schemas, code review comments, git history, and incident reports.

- **Refine with Real Execution**: Run the skill on real tasks and feed *all* results (successes and failures) back into revision. Even a single execute-then-revise pass meaningfully improves quality. Read agent execution traces to spot wasted steps caused by vague instructions, irrelevant instructions the agent follows anyway, or too many options without a clear default.

- **Context-Window Economy**: When a skill activates, its entire `SKILL.md` body loads alongside conversation history, system prompt, and other active skills. Every token competes for attention. The test question for each line: "Would the agent get this wrong without this instruction?" If no, cut it.

- **Coherent-Unit Scoping**: Skill scope is analogous to function scope. Too narrow → multiple skills load per task, creating overhead and conflicts. Too broad → activation becomes imprecise. Example: a skill for querying a database and formatting results is coherent; adding database administration makes it too broad.

- **Progressive Disclosure**: Keep `SKILL.md` ≤ 500 lines / 5,000 tokens. Move detail to `references/` or `assets/` but tell the agent explicitly when to load each file (e.g., "Read `references/api-errors.md` if the API returns a non-200 status"). Generic "see references/" pointers don't work.

- **Match Specificity to Fragility**: Prescriptiveness should scale with task fragility. For flexible multi-approach tasks (e.g., code review), explain *why* rather than rigid steps. For fragile operations (e.g., database migrations), give exact commands and forbid modifications. Most skills mix both and should calibrate each section independently.

- **Defaults Over Menus**: When multiple tools work, pick one default (e.g., `pdfplumber` for PDF text extraction) and mention alternatives briefly as escape hatches (e.g., `pdf2image` + `pytesseract` for scanned PDFs). Avoid presenting equal options.

- **Procedures Over Declarations**: Teach the agent *how to approach* a class of problems, not *what to produce* for one instance. A reusable method ("read schema from `references/schema.yaml`, join on `_id` foreign keys, apply filters as WHERE clauses") beats a specific answer hard-coded for one query.

- **Gotchas Sections**: A list of environment-specific facts that defy reasonable assumptions — soft-delete columns, inconsistent ID naming across services (`user_id` vs `uid` vs `accountId`), misleading health endpoints. These belong in `SKILL.md` itself since the agent may not recognize the trigger to load a separate file. Every correction made during use should become a new gotcha.

- **Output Templates**: Agents pattern-match concrete structures better than prose descriptions. Short templates inline in `SKILL.md`; longer or situational ones in `assets/` with conditional load instructions.

- **Checklists for Multi-Step Workflows**: Explicit numbered checklists with checkbox syntax help agents track progress across dependencies and validation gates.

- **Validation Loops**: Do work → run validator (script, checklist, or self-check) → fix issues → repeat until passing. A reference document can serve as the validator.

- **Plan-Validate-Execute Pattern**: For batch/destructive operations, have the agent write an intermediate structured plan (e.g., `field_values.json`), validate it against a source of truth (`form_fields.json`), and only then execute. Rich error messages like "Field 'signature_date' not found — available fields: ..." enable self-correction.

- **Bundling Reusable Scripts**: If execution traces show the agent reinventing the same logic (chart building, format parsing, output validation) across runs, extract it into a tested script in `scripts/` rather than relying on regeneration.

## Key Takeaways
- `SKILL.md` should stay under **500 lines / 5,000 tokens**; use progressive disclosure for more content, with explicit load triggers.
- Skills must be grounded in real expertise — extract from hands-on agent sessions or synthesize from project artifacts (runbooks, schemas, git history, code review comments).
- Apply the cut-test to every line: if the agent would handle it correctly without the instruction, remove it.
- Provide a default tool/approach, not a menu of equal options; include a brief escape hatch for known exceptions.
- Favor procedural, generalizable instructions over instance-specific declarations.
- The Gotchas section is often a skill's highest-value content — it captures non-obvious, environment-specific traps.
- Calibrate prescriptiveness per section: freedom for flexible tasks (explain *why*), exact commands for fragile ones (forbid modification).
- Iterate by reading agent execution traces, not just final outputs; fold corrections back in as gotchas.
- Use Plan-Validate-Execute for batch/destructive operations so the agent can self-correct before committing.
- Extract recurring logic observed in traces into bundled scripts in `scripts/`.

## Notable Quotes
> "A common pitfall in skill creation is asking an LLM to generate a skill without providing domain-specific context — relying solely on the LLM's general training knowledge. The result is vague, generic procedures."

> "Every token in your skill competes for the agent's attention with everything else in that window."

> "A skill should teach the agent *how to approach* a class of problems, not *what to produce* for a specific instance."

> "The highest-value content in many skills is a list of gotchas — environment-specific facts that defy reasonable assumptions."

> "When an agent makes a mistake you have to correct, add the correction to the gotchas section."

## Related Entities
[[Agent Skills]], [[SKILL.md Specification]], [[Progressive Disclosure]], [[Evaluating Skills]], [[Optimizing Skill Descriptions]], [[Using Scripts in Skills]], [[Context Window Management]], [[Anthropic Claude Skills]]

## Tags
agent-skills, skill-authoring, prompt-engineering, context-management, progressive-disclosure, llm-workflows, validation-loops, plan-validate-execute