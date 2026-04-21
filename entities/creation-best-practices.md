# Best practices for skill creators

---
title: "Best Practices for Skill Creators"
created: 2026-04-21
type: entity
tags: [agent-skills, skill-design, context-engineering, llm-agents, prompt-engineering]
related: [[Agent Skills]], [[Progressive Disclosure]], [[SKILL.md Specification]], [[Evaluating Skills]], [[Optimizing Skill Descriptions]], [[Using Scripts in Skills]]
sources: [raw/articles/skill-creation-best-practices.md]
---

# Best Practices for Skill Creators

## Summary
This reference page from agentskills.io documents the craft of authoring Agent Skills — modular, Markdown-based instruction bundles (`SKILL.md` plus optional `references/`, `assets/`, and `scripts/` directories) that extend an LLM agent's capabilities. The guide is organized around four themes: grounding skills in real expertise, spending context budget wisely, calibrating control (prescriptive vs. permissive instructions), and applying reusable instruction patterns (gotchas, templates, checklists, validation loops, plan-validate-execute).

The core thesis is that skills must encode what the agent *doesn't already know* — project-specific conventions, non-obvious edge cases, and domain expertise — rather than restating general knowledge from training data. Skills should be derived from real hands-on work (extracted traces, corrections, project artifacts like runbooks, API specs, code review comments, version control patches) and iteratively refined by running them against real tasks and reading execution traces. The specification recommends `SKILL.md` stay under **500 lines / 5,000 tokens**, with overflow material moved to auxiliary files loaded via progressive disclosure (e.g., "Read `references/api-errors.md` if the API returns a non-200 status code").

Practical patterns include: picking one default tool rather than presenting menus (e.g., "Use `pdfplumber` for text extraction; fall back to `pdf2image` + `pytesseract` for scanned PDFs"), favoring reusable procedures over one-off declarations, maintaining a Gotchas section for environment-specific traps (soft deletes requiring `WHERE deleted_at IS NULL`, inconsistent ID naming across services, `/health` vs `/ready` endpoints), providing output templates the agent pattern-matches against, and using plan-validate-execute loops backed by validator scripts for destructive or batch operations.

## Key Concepts

- **Start from Real Expertise**: Do not ask an LLM to generate a skill from its own priors; feed it domain-specific context. Skills generated cold produce vague generics ("handle errors appropriately"). Effective skills are extracted from either (a) a hands-on task performed with an agent, capturing steps that worked, corrections made, and I/O formats, or (b) synthesis from project artifacts: internal docs, runbooks, style guides, API specs, code review comments, issue trackers, and version control patches.

- **Refine with Real Execution**: First drafts require iteration. Run the skill on real tasks and feed all results (not just failures) back in. Read execution traces, not final outputs — wasted steps signal vague instructions, inapplicable instructions the agent follows anyway, or too many options without a default. Even one execute-then-revise pass yields noticeable improvement.

- **Context Budget Discipline**: When a skill activates, its full `SKILL.md` body enters the context window and competes with conversation history, system context, and other active skills for attention. Add only what the agent lacks; omit explanations of PDFs, HTTP, or database migrations. Heuristic test: "Would the agent get this wrong without this instruction?" — if no, cut it.

- **Coherent Skill Scoping**: Scope skills like functions — one coherent unit of work that composes with others. Too narrow forces multiple skills to load with overhead and conflicts; too broad is hard to activate precisely. Example: "query database and format results" is coherent; adding "database administration" is overreach.

- **Progressive Disclosure**: `SKILL.md` should hold only core always-needed instructions (under 500 lines / 5,000 tokens). Detailed reference material goes in `references/` or similar, loaded on demand. Load triggers must be explicit and situational — "Read `references/api-errors.md` if the API returns a non-200 status code" beats a generic "see references/".

- **Match Specificity to Fragility**: Calibrate prescriptiveness per section. Give freedom when multiple approaches are valid and explain *why* (agents with purpose make better context-dependent calls). Be prescriptive for fragile operations requiring exact sequences (e.g., `python scripts/migrate.py --verify --backup` with "Do not modify the command or add additional flags").

- **Defaults Not Menus**: When several tools could work, pick one default with a brief escape hatch. "Use pdfplumber; for scanned PDFs use pdf2image with pytesseract" beats listing pypdf, pdfplumber, PyMuPDF, pdf2image as equal options.

- **Procedures over Declarations**: Teach how to approach a class of problems, not what to output for one instance. A reusable method ("Read schema from `references/schema.yaml`, join on `_id` foreign keys, apply WHERE filters, aggregate as markdown table") generalizes; a specific SQL answer does not.

- **Gotchas Sections**: Concrete corrections to mistakes the agent will make without being told. Must live in `SKILL.md` (not referenced files) because the agent may not recognize the trigger to load them. Canonical examples: soft-deleted tables needing `WHERE deleted_at IS NULL`, cross-service ID renamings (`user_id` / `uid` / `accountId`), health endpoints that don't check dependencies. Every agent mistake you correct should be added here.

- **Output Templates**: Agents pattern-match concrete structures better than prose descriptions. Inline short templates in `SKILL.md`; put long or conditional templates in `assets/` with load triggers.

- **Checklists for Multi-Step Workflows**: Explicit `- [ ]` progress lists help the agent track dependencies and validation gates across steps.

- **Validation Loops**: Do work → run validator (script, checklist, or self-check) → fix issues → repeat until pass. Reference documents can serve as validators.

- **Plan-Validate-Execute**: For batch or destructive ops, produce an intermediate plan in structured format, validate it against a source of truth, then execute. Example: PDF form filling emits `form_fields.json` (source of truth from `analyze_form.py`), author creates `field_values.json` (plan), `validate_fields.py` compares them, then `fill_form.py` executes. Validator errors should be informative enough for self-correction (e.g., "Field 'signature_date' not found — available fields: ...").

- **Bundled Scripts**: If execution traces show the agent reinventing the same logic (building charts, parsing formats, validating output), write and test it once, bundle in `scripts/`.

## Key Takeaways
- Skills must be grounded in real expertise — extract from hands-on tasks or synthesize from project-specific artifacts (runbooks, API specs, code review comments, VCS patches), not from generic best-practice articles.
- `SKILL.md` should stay under 500 lines and 5,000 tokens; use progressive disclosure to offload detail into `references/` and `assets/` with explicit load triggers.
- The test for every sentence in a skill: "Would the agent get this wrong without this instruction?" — if not, cut it.
- Provide one default tool/approach with a narrow escape hatch rather than a menu of equal options.
- Write reusable procedures that generalize across instances rather than answers specific to one task, while still including specific output templates and hard constraints.
- Maintain a Gotchas section in `SKILL.md` itself for non-obvious environment traps; the agent can't load what it doesn't know to look for.
- Calibrate prescriptiveness per section: explain *why* for flexible parts, dictate exact commands for fragile parts — most skills are a mix.
- For destructive or batch work, use plan-validate-execute with a validator script that produces error messages informative enough to drive self-correction.
- Read agent execution traces when iterating; wasted steps usually indicate vague instructions, misapplied instructions, or missing defaults.
- If the agent handles the task well without the skill, the skill may not be adding value — test this systematically.

## Notable Quotes
> "Focus on what the agent wouldn't know without your skill: project-specific conventions, domain-specific procedures, non-obvious edge cases, and the particular tools or APIs to use. You don't need to explain what a PDF is, how HTTP works, or what a database migration does."

> "A skill should teach the agent how to approach a class of problems, not what to produce for a specific instance."

> "The highest-value content in many skills is a list of gotchas — environment-specific facts that defy reasonable assumptions."

> "When you find yourself covering every edge case, consider whether most are better handled by the agent's own judgment."

> "An agent that understands the purpose behind an instruction makes better context-dependent decisions."

## Related Entities
[[Agent Skills]], [[SKILL.md Specification]], [[Progressive Disclosure]], [[Evaluating Skills]], [[Optimizing Skill Descriptions]], [[Using Scripts in Skills]], [[Context Engineering]], [[Claude Agent Skills]]