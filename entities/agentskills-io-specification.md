# Specification - Agent Skills

---
title: "Agent Skills Specification"
created: 2026-04-25
type: entity
tags: [agent-skills, specification, llm-agents, skill-authoring, progressive-disclosure]
related: [[Claude Code]], [[LLM Agents]], [[Model Context Protocol]]
sources: [raw/articles/agentskills-io-specification.md]
---

# Agent Skills Specification

## Summary
The Agent Skills Specification defines a portable, file-based format for packaging reusable capabilities that LLM agents can discover and invoke. A "skill" is a directory containing at minimum a `SKILL.md` file with YAML frontmatter and Markdown body, optionally accompanied by `scripts/`, `references/`, and `assets/` subdirectories. The specification is hosted at agentskills.io and is accompanied by a reference validation tool called `skills-ref`.

The design is built around **progressive disclosure**: agents load ~100 tokens of metadata (name + description) for every skill at startup, load the full `SKILL.md` body (recommended under 5000 tokens / 500 lines) only when a skill is activated, and load supporting resources on demand. This enables agents to host many skills without blowing their context window. The format is intentionally minimal — only `name` and `description` are required frontmatter fields — with optional fields for `license`, `compatibility`, arbitrary `metadata`, and an experimental `allowed-tools` field for pre-approved tool invocations.

The specification is client-agnostic (supported by Claude Code and other agent implementations), imposes no format restrictions on the Markdown body, and recommends structuring skills so that detailed reference material lives in separate files to conserve context. File references should use relative paths and stay one level deep from `SKILL.md`.

## Key Concepts

- **Skill Directory**: A filesystem directory whose name matches the skill's `name` field, containing a required `SKILL.md` and optional `scripts/`, `references/`, `assets/` subdirectories. The directory is the unit of distribution and activation.

- **SKILL.md**: The single required file, consisting of YAML frontmatter followed by Markdown. The frontmatter declares metadata; the body contains free-form instructions, examples, and edge cases the agent reads upon activation.

- **name field (required)**: 1–64 characters, lowercase alphanumeric plus hyphens only, no leading/trailing or consecutive hyphens, and must match the parent directory name. Examples: `pdf-processing`, `data-analysis`. Invalid: `PDF-Processing`, `-pdf`, `pdf--processing`.

- **description field (required)**: 1–1024 characters describing both *what* the skill does and *when* to use it, with keywords agents can match against user tasks. Good descriptions enumerate concrete capabilities and trigger phrases (e.g., "Use when working with PDF documents or when the user mentions PDFs, forms, or document extraction").

- **compatibility field (optional)**: Up to 500 characters indicating environment requirements — intended product, system packages (git, docker, jq), network access, language runtime (e.g., "Requires Python 3.14+ and uv"). Most skills omit this.

- **allowed-tools field (experimental)**: Space-separated list of pre-approved tools, e.g., `Bash(git:*) Bash(jq:*) Read`. Support varies by agent implementation.

- **metadata field**: Arbitrary string-to-string map for client-specific properties (author, version, etc.). Keys should be uniquely named to avoid conflicts.

- **Progressive Disclosure**: Three-tier loading strategy — (1) ~100 tokens of frontmatter loaded for all skills at startup, (2) full `SKILL.md` (<5000 tokens, <500 lines recommended) loaded on activation, (3) `scripts/`, `references/`, `assets/` files loaded only when needed during execution.

- **scripts/ directory**: Self-contained executable code (commonly Python, Bash, JavaScript) that the agent can run, with documented dependencies, helpful error messages, and edge-case handling.

- **references/ directory**: On-demand documentation split into focused files such as `REFERENCE.md`, `FORMS.md`, or domain-specific files like `finance.md`, `legal.md`. Keeping them small reduces context consumption when loaded.

- **assets/ directory**: Static resources — document/configuration templates, images, diagrams, lookup tables, schemas — used as inputs or outputs rather than executed.

- **File References**: Use relative paths from skill root (e.g., `references/REFERENCE.md`, `scripts/extract.py`); keep references one level deep from `SKILL.md` and avoid deeply nested chains.

- **skills-ref**: Reference validation library providing `skills-ref validate ./my-skill` to check frontmatter validity and naming conventions.

## Key Takeaways
- A skill is just a directory with a `SKILL.md` — the format is deliberately simple and tool-agnostic.
- Only `name` (≤64 chars, lowercase-hyphen pattern matching directory name) and `description` (≤1024 chars) are required in frontmatter.
- Progressive disclosure is the core design principle: metadata always loaded, body loaded on activation, supporting files loaded on demand.
- Keep `SKILL.md` under 500 lines / 5000 tokens; push detailed documentation to `references/`.
- Descriptions should explicitly state both capability and triggering conditions — vague descriptions like "Helps with PDFs" are considered poor.
- The `compatibility` field (≤500 chars) is optional and only needed when a skill has real environment dependencies.
- `allowed-tools` is experimental and implementation-dependent; its format is space-separated tool patterns like `Bash(git:*)`.
- The `skills-ref` CLI validates structure and naming conventions before distribution.

## Notable Quotes
> "A skill is a directory containing, at minimum, a SKILL.md file."

> "Agents load skills progressively, pulling in more detail only as a task calls for it."

> "Metadata (~100 tokens): The name and description fields are loaded at startup for all skills. Instructions (< 5000 tokens recommended): The full SKILL.md body is loaded when the skill is activated. Resources (as needed): Files... are loaded only when required."

> "Keep your main SKILL.md under 500 lines. Move detailed reference material to separate files."

## Related Entities
[[Claude Code]], [[LLM Agents]], [[Model Context Protocol]], [[Progressive Disclosure]], [[YAML Frontmatter]], [[Prompt Engineering]]