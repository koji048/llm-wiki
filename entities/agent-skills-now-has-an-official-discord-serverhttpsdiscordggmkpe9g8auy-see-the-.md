# Agent Skills now has an official [Discord server](https://discord.gg/MKPE9g8aUy). See the [announcement](https://github.com/agentskills/agentskills/discussions/273) for details.

---
title: "Best Practices for Agent Skill Creators"
created: 2026-04-21
type: entity
tags: [agent-skills, llm-engineering, prompt-engineering, context-management, skill-design]
related: [[Agent Skills]], [[Progressive Disclosure]], [[SKILL.md Specification]], [[Evaluating Skills]], [[Optimizing Skill Descriptions]]
sources: [raw/articles/agentskills_io_skill-creation_best-practices.md]
---

# Best Practices for Agent Skill Creators

## Summary
This is the official best-practices guide from agentskills.io for authoring Agent Skills — modular, markdown-based instruction bundles (`SKILL.md` plus optional `references/`, `assets/`, and `scripts/` directories) that LLM agents load into context to perform specialized tasks. The guide frames skill creation around four themes: grounding skills in real expertise rather than generic LLM synthesis, spending the limited context window wisely, calibrating the level of prescriptive control to task fragility, and applying reusable instruction patterns.

Concrete prescriptions include: keep `SKILL.md` under 500 lines / 5,000 tokens (per the Agent Skills specification), use progressive disclosure via on-demand references, provide one default approach rather than a menu of options, and teach procedures (reusable methods) rather than declarations (specific answers). The article codifies several patterns — gotchas sections, output templates, checklists, validation loops, and plan-validate-execute — and recommends bundling reusable logic into `scripts/` when agents repeatedly reinvent it. It draws examples from PDF processing (pdfplumber, pdf2image, pytesseract), database migration, SQL querying, and form filling.

The guide emphasizes iterative refinement: run skills against real tasks, inspect execution traces (not just final outputs), and fold corrections back into the skill — particularly into gotchas sections. It links forward to companion guides on evaluating skills and optimizing description fields for activation.

## Key Concepts

- **Start from Real Expertise**: Skills generated purely from LLM training knowledge produce vague generalities ("handle errors appropriately"). Effective skills extract domain-specific knowledge from hands-on tasks, internal runbooks, API specs, code review comments, version control history (patches reveal recurring patterns), and resolved incidents.

- **Extract from Hands-on Tasks vs. Synthesize from Artifacts**: Two complementary creation paths — (1) performing a real task with an agent and extracting steps, corrections, I/O formats, and project context into a reusable skill; (2) feeding existing project artifacts (runbooks, schemas, style guides) to an LLM for synthesis. Both beat generic references.

- **Refine with Real Execution**: First drafts need iteration. Run the skill on real tasks, feed back all results (not just failures), and inspect execution traces. Common failure signals: agent tries several approaches (instructions too vague), agent follows non-applicable instructions (too broad), or agent ignores a default (too many options listed).

- **Context-Window Budgeting**: Once activated, the full `SKILL.md` body loads alongside conversation history, system context, and other skills. Every token competes for attention. Rule: add what the agent lacks (project conventions, non-obvious edges, specific APIs), omit what it already knows (what a PDF is, how HTTP works).

- **Coherent Units of Work**: Skill scope is analogous to function scope. Too narrow → multiple skills load per task, risking conflict and overhead. Too broad → hard to activate precisely. Example: "query DB and format results" is coherent; adding "DB administration" overreaches.

- **Progressive Disclosure**: Per the spec, `SKILL.md` stays under 500 lines / 5,000 tokens holding core instructions; detailed reference material lives in `references/` (or similar) and loads on demand. Critical: tell the agent *when* to load each file (e.g., "Read `references/api-errors.md` if the API returns a non-200 status code"), not just "see references/".

- **Match Specificity to Fragility**: Give freedom where multiple approaches are valid (explain *why* rather than prescribe); be prescriptive for fragile, consistency-critical, or sequence-dependent operations (e.g., database migrations with exact commands). Most skills mix both and calibrate section-by-section.

- **Defaults, Not Menus**: Pick one tool and mention alternatives briefly with an escape hatch — e.g., "Use pdfplumber for text extraction; for scanned PDFs requiring OCR, use pdf2image with pytesseract instead" — rather than listing pypdf, pdfplumber, PyMuPDF, and pdf2image as equal options.

- **Procedures Over Declarations**: Teach *how to approach* a class of problems, not *what to produce* for one instance. A reusable SQL method ("read schema, join via `_id` convention, apply filters, aggregate") beats a hardcoded join specific to one query. Specific details like output templates and PII constraints remain valuable — only the overall approach must generalize.

- **Gotchas Sections**: Often the highest-value skill content. Concrete, environment-specific corrections to mistakes agents predictably make — e.g., soft-delete columns (`WHERE deleted_at IS NULL`), identifier aliasing (`user_id` vs `uid` vs `accountId`), misleading health endpoints (`/health` vs `/ready`). Keep in `SKILL.md` itself since agents may not recognize triggers to load external references. Add entries whenever you correct an agent mistake.

- **Output Templates**: Agents pattern-match well against concrete structures, so templates beat prose descriptions. Short templates inline in `SKILL.md`; long or conditional ones go in `assets/` and load on demand.

- **Checklists**: Explicit progress checklists (`- [ ] Step 1...`) help agents track multi-step workflows with dependencies or validation gates.

- **Validation Loops**: Do work → run validator (script, checklist, or self-check) → fix issues → repeat until passing. Reference documents can serve as validators.

- **Plan-Validate-Execute**: For batch or destructive operations, agent (1) generates an intermediate plan in structured form (e.g., `field_values.json`), (2) validates it against a source of truth (e.g., `form_fields.json` via `scripts/validate_fields.py`), (3) only then executes. Informative error messages (e.g., "Field 'signature_date' not found — available fields: ...") enable self-correction.

- **Bundling Reusable Scripts**: When execution traces show the agent reinventing the same logic (chart building, format parsing, validation), extract it into tested scripts in `scripts/`.

## Key Takeaways
- `SKILL.md` should stay under **500 lines and 5,000 tokens**; offload detail to `references/` with explicit load-triggers.
- Source skills from real artifacts — runbooks, patches, incident reports, code review comments — not generic best-practice articles.
- Read execution traces, not just final outputs; vague instructions cause agents to try multiple approaches before settling.
- Omit anything the agent already knows; the test question is "Would the agent get this wrong without this instruction?"
- Give one default approach with a brief escape hatch rather than a menu of equal options.
- Calibrate prescriptiveness per section: flexible for open-ended tasks (explain *why*), rigid for fragile ops like migrations.
- Gotchas sections capture the highest-leverage content — environment-specific facts that defy reasonable assumptions.
- Use plan-validate-execute with machine-checkable intermediate artifacts for destructive or batch operations.
- When agents repeatedly reinvent logic across runs, extract it into `scripts/`.
- Add every correction you make during refinement back into the skill's gotchas section.

## Notable Quotes
> "Every token in your skill competes for the agent's attention with everything else in that window."

> "A skill should teach the agent *how to approach* a class of problems, not *what to produce* for a specific instance."

> "The highest-value content in many skills is a list of gotchas — environment-specific facts that defy reasonable assumptions."

> "Concise, stepwise guidance with a working example tends to outperform exhaustive documentation."

> "Provide defaults, not menus."

## Related Entities
[[Agent Skills]], [[SKILL.md Specification]], [[Progressive Disclosure]], [[Evaluating Skills]], [[Optimizing Skill Descriptions]], [[Context Window Management]], [[Claude Code]], [[LLM Prompt Engineering]]

## Tags
agent-skills, skill-design, context-engineering, llm-tooling, progressive-disclosure, prompt-patterns, validation-loops, agentskills.io