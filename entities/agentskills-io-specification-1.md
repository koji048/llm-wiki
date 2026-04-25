# Specification - Agent Skills

---
title: "Agent Skills Specification"
created: 2026-04-25
type: entity
tags: [agent-skills, specification, llm-tooling, markdown, skill-authoring]
related: [[SKILL.md]], [[Progressive Disclosure]], [[Claude Code]], [[YAML Frontmatter]]
sources: [raw/articles/agentskills-io-specification.md]
---

# Agent Skills Specification

## Summary
The Agent Skills Specification defines a portable, filesystem-based format for packaging reusable capabilities ("skills") that AI agents can discover, load, and execute. A skill is a directory containing at minimum a `SKILL.md` file, which consists of YAML frontmatter (metadata) followed by Markdown body content (instructions for the agent). Optional subdirectories include `scripts/` (executable code), `references/` (on-demand documentation), and `assets/` (static templates/resources).

The spec is designed around **progressive disclosure**: an agent loads only ~100 tokens of metadata (name + description) at startup for all installed skills, loads the full SKILL.md body (<5000 tokens recommended) only when the skill is activated, and loads additional files in `scripts/`, `references/`, or `assets/` only when a task requires them. This tiered loading keeps context windows lean while enabling rich capability libraries.

The specification ships with a reference validator (`skills-ref validate`) that checks frontmatter validity and naming conventions. An official Discord community supports skill authors and client implementors. The spec is adopted by products like Claude Code and defines both an authoring format (for skill creators) and integration guidance (for client implementors).

## Key Concepts

- **Skill Directory**: A filesystem directory whose name matches the skill's `name` field, containing a required `SKILL.md` plus optional `scripts/`, `references/`, `assets/` subdirectories. The directory is the unit of distribution.

- **SKILL.md**: The required entry-point file combining YAML frontmatter with a free-form Markdown body. The frontmatter declares metadata; the body provides the agent's activation-time instructions.

- **`name` Field (required)**: 1–64 characters, lowercase alphanumeric plus hyphens only. Must not start/end with a hyphen, must not contain consecutive hyphens (`--`), and must match the parent directory name. Valid: `pdf-processing`; invalid: `PDF-Processing`, `-pdf`, `pdf--processing`.

- **`description` Field (required)**: 1–1024 characters describing both what the skill does *and* when to use it. Should include keywords that help agents match tasks to the skill. This field plus `name` form the ~100 token metadata loaded at startup.

- **`compatibility` Field (optional)**: Up to 500 characters describing environment requirements (intended product, required packages, network access, runtime versions). Examples: "Designed for Claude Code", "Requires git, docker, jq, and access to the internet", "Requires Python 3.14+ and uv". Most skills omit this.

- **`license` Field (optional)**: Short license identifier or reference to a bundled license file (e.g. `Apache-2.0`, or `Proprietary. LICENSE.txt has complete terms`).

- **`metadata` Field (optional)**: Arbitrary string-to-string map for client-specific or author-specific properties not covered by the spec (e.g. `author`, `version`). Key names should be made unique to avoid collisions.

- **`allowed-tools` Field (experimental)**: Space-separated list of pre-approved tool invocations the skill may use, e.g. `Bash(git:*) Bash(jq:*) Read`. Support varies across agent implementations.

- **Progressive Disclosure**: The core loading model — startup metadata (~100 tokens), activated body (<5000 tokens / <500 lines recommended), on-demand resource files. Detailed reference material should be split into separate files under `references/` rather than inlined in SKILL.md.

- **`scripts/` Directory**: Executable code (commonly Python, Bash, JavaScript; language support is implementation-dependent). Scripts should be self-contained or document dependencies, produce helpful error messages, and handle edge cases.

- **`references/` Directory**: Supplementary docs loaded on demand — e.g. `REFERENCE.md`, `FORMS.md`, domain-specific files like `finance.md` or `legal.md`. Files should be kept small and focused to minimize context cost.

- **`assets/` Directory**: Static resources — document/configuration templates, images, data files (lookup tables, schemas).

- **File References**: Use relative paths from the skill root (e.g. `references/REFERENCE.md`, `scripts/extract.py`). Spec recommends keeping references one level deep and avoiding deeply nested reference chains.

- **skills-ref Validator**: The reference CLI (`skills-ref validate ./my-skill`) that checks frontmatter validity and naming conventions.

## Key Takeaways
- A skill = a directory with a `SKILL.md`; only `name` and `description` are required fields.
- `name` must be lowercase-alphanumeric-with-hyphens, ≤64 chars, and match the parent directory name exactly.
- `description` is capped at 1024 chars and should describe both *what* and *when to use* — it's the primary signal agents use to decide activation.
- Recommended size budgets: metadata ~100 tokens, SKILL.md body <5000 tokens / <500 lines.
- Use `references/` and `assets/` to offload detail; agents load these only on demand.
- `allowed-tools` (e.g. `Bash(git:*) Read`) is experimental and implementation-dependent.
- Validate skills with the `skills-ref` reference library before distribution.
- Standard optional fields: `license`, `compatibility` (≤500 chars), `metadata` (arbitrary string map).

## Notable Quotes
> "A skill is a directory containing, at minimum, a SKILL.md file."
> "Agents load skills progressively, pulling in more detail only as a task calls for it."
> "Keep your main SKILL.md under 500 lines. Move detailed reference material to separate files."

## Related Entities
[[SKILL.md]], [[Progressive Disclosure]], [[Claude Code]], [[YAML Frontmatter]], [[skills-ref]], [[Agent Tooling]]