# GitHub - anthropics/skills: Public repository for Agent Skills · GitHub

---
title: "Anthropic Agent Skills Repository"
created: 2026-04-25
type: entity
tags: [anthropic, claude, agent-skills, llm-tooling, claude-code]
related: [[Claude]], [[Claude Code]], [[Anthropic]], [[Model Context Protocol]]
sources: [raw/articles/github-com-anthropics-skills.md]
---

# Anthropic Agent Skills Repository

## Summary
The `anthropics/skills` GitHub repository is Anthropic's public collection of Agent Skills — folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Each skill is a self-contained directory anchored by a `SKILL.md` file containing YAML frontmatter (with required `name` and `description` fields) and markdown instructions that Claude follows when the skill is activated. The repository has reached substantial popularity (124k stars, 14.5k forks, 820 watchers) and serves both as a reference implementation and as a distribution channel for Anthropic's production document-handling skills.

The repo is organized into four top-level directories: `./skills` (example skills across creative/design, development/technical, enterprise/communication, and document categories), `./spec` (the Agent Skills specification), `./template` (a starter skill template), and `./.claude-plugin` (plugin marketplace metadata). Notably, it includes the production document creation and editing skills that power Claude's native document capabilities: `skills/docx`, `skills/pdf`, `skills/pptx`, and `skills/xlsx`. Most skills are Apache 2.0 licensed, though the document skills are source-available rather than fully open source. Language composition is 84.4% Python, 12.4% HTML, 1.9% Shell, 1.3% JavaScript.

Skills can be consumed across Anthropic's surfaces: via Claude Code as a plugin marketplace (`/plugin marketplace add anthropics/skills`), via Claude.ai (pre-loaded for paid plans), and via the Claude API (with a Skills API Quickstart). The repository also points to `agentskills.io` as the home of the broader Agent Skills standard, indicating Anthropic's framing of this as a portable specification rather than a Claude-only feature.

## Key Concepts

- **Agent Skill**: A folder of instructions, scripts, and resources dynamically loaded by Claude to specialize its behavior for a task. Skills teach Claude repeatable, task-specific workflows (e.g., applying brand guidelines, running an org's data analysis playbook, or automating a personal task) without permanently bloating the system prompt.

- **SKILL.md**: The required anchor file of every skill, containing YAML frontmatter plus markdown instructions. Frontmatter requires exactly two fields — `name` (lowercase, hyphen-separated unique identifier) and `description` (explains what the skill does and when to use it, used by Claude to decide when to activate it).

- **Dynamic Loading**: Skills are not always-on context; Claude loads them based on relevance to the current task, inferred largely from the `description` field. This keeps token overhead low while providing deep, specialized instructions on demand.

- **Claude Code Plugin Marketplace**: Distribution mechanism whereby a GitHub repo can be registered as a marketplace via `/plugin marketplace add anthropics/skills`, then individual plugin bundles installed with commands like `/plugin install document-skills@anthropic-agent-skills` or `/plugin install example-skills@anthropic-agent-skills`.

- **Document Skills (docx/pdf/pptx/xlsx)**: Production skills that power Claude.ai's file creation and editing features for Word, PDF, PowerPoint, and Excel. These are shipped source-available (not Apache 2.0) as reference implementations of non-trivial, production-grade skills.

- **Agent Skills Specification**: A standard hosted at `agentskills.io` and mirrored in the repo's `./spec` directory. Anthropic positions Skills as an open standard, distinct from their particular implementation in this repo.

- **Skill Categories in the Repo**: Creative & Design (art, music, design), Development & Technical (testing web apps, MCP server generation), Enterprise & Communication (communications, branding), and Document Skills.

- **Template Skill**: A minimal starter in `./template` with sections for Examples and Guidelines, intended as a scaffold for authoring new skills.

- **Partner Skills**: Third-party integrations highlighted by Anthropic — e.g., Notion's skills for Claude — demonstrating the ecosystem pattern of software vendors shipping their own skill packs.

- **Invocation by Mention**: After a skill plugin is installed, users activate it conversationally, e.g., "Use the PDF skill to extract the form fields from path/to/some-file.pdf" — no explicit tool-call syntax required.

## Key Takeaways
- Skills are the simplest possible packaging unit: a folder with a `SKILL.md` containing YAML frontmatter (`name`, `description`) and markdown instructions.
- The `description` field is load-bearing — it drives Claude's decision about when to activate the skill, so it must clearly state what the skill does and when to use it.
- Anthropic ships its own production document-handling logic (docx/pdf/pptx/xlsx) as skills, confirming skills are a first-class production mechanism, not just a user-land feature.
- Skills work across Claude Code (via plugin marketplace), Claude.ai (bundled for paid plans), and the Claude API (via Skills API Quickstart).
- Licensing is mixed: example skills are Apache 2.0; the production document skills are source-available only.
- The Agent Skills spec at `agentskills.io` is positioned as a portable standard, not Claude-exclusive, opening the door to cross-vendor skill compatibility.
- Repository popularity (124k stars, 14.5k forks) reflects strong developer interest in instruction-based, file-system-level agent extensibility as an alternative/complement to MCP tools.
- Python dominates the codebase (84.4%), indicating most skill-embedded scripts are Python helpers invoked by Claude during skill execution.

## Notable Quotes
> "Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks."

> "Each skill is self-contained in its own folder with a SKILL.md file containing the instructions and metadata that Claude uses."

> "The frontmatter requires only two fields: name — A unique identifier for your skill (lowercase, hyphens for spaces); description — A complete description of what the skill does and when to use it."

> "This repository contains Anthropic's implementation of skills for Claude. For information about the Agent Skills standard, see agentskills.io."

## Related Entities
[[Claude]], [[Claude Code]], [[Anthropic]], [[Model Context Protocol]], [[Claude.ai]], [[Agent Skills Specification]], [[Notion]]