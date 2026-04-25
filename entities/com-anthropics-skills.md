# GitHub - anthropics/skills: Public repository for Agent Skills · GitHub

---
title: "Anthropic Agent Skills Repository"
created: 2026-04-25
type: entity
tags: [claude, agent-skills, anthropic, llm-tools, claude-code]
related: [[Claude]], [[Claude Code]], [[Model Context Protocol]], [[Anthropic]]
sources: [raw/articles/github-com-anthropics-skills.md]
---

# Anthropic Agent Skills Repository

## Summary
The `anthropics/skills` GitHub repository is Anthropic's public repository for **Agent Skills** — folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Skills teach Claude how to complete specific tasks in a repeatable way, from creating branded documents, analyzing data with organizational workflows, to automating personal tasks. At the time of capture, the repo had ~123k stars, ~14.4k forks, and 819 watchers, with the codebase being 84.4% Python, 12.4% HTML, 1.9% Shell, and 1.3% JavaScript.

Each skill is self-contained in its own folder with a `SKILL.md` file containing YAML frontmatter (requiring `name` and `description`) plus Markdown instructions Claude follows when the skill is active. The repo hosts demonstrations spanning creative/design, development/technical, enterprise/communication, and document skill categories. Notably, the `skills/docx`, `skills/pdf`, `skills/pptx`, and `skills/xlsx` subfolders contain the production document creation & editing skills that power Claude's document capabilities — these are source-available (not open source), while most other skills are Apache 2.0 licensed.

The repository doubles as a **Claude Code plugin marketplace**: users can run `/plugin marketplace add anthropics/skills` to register it, then install either the `document-skills` or `example-skills` plugins. The same skills are available in Claude.ai for paid plans, and via the Claude API through the Skills API. The broader Agent Skills standard is documented at `agentskills.io`, separate from this Anthropic-specific implementation.

## Key Concepts
- **Agent Skill**: A folder containing a `SKILL.md` file plus optional scripts and resources that Claude loads dynamically when relevant to a task. Skills package repeatable task knowledge — branding guidelines, workflow specs, tool-usage patterns — in a form Claude can selectively activate rather than bloating every system prompt.

- **SKILL.md Format**: The minimal skill definition — a Markdown file with YAML frontmatter (`name`, `description`) followed by instructions, examples, and guidelines. The `name` must be lowercase with hyphens; the `description` both explains what the skill does and when Claude should invoke it (critical for routing).

- **Dynamic Loading**: Skills are loaded on demand rather than always being in context. This keeps Claude's working context efficient — only relevant skills activate for a given task, enabling large libraries of specialized skills without prompt bloat.

- **Document Skills (docx/pdf/pptx/xlsx)**: Source-available skills that power Claude's production document capabilities. These serve as reference implementations of complex, real-world skills and handle document creation/editing across Word, PDF, PowerPoint, and Excel formats.

- **Claude Code Plugin Marketplace**: The repo can be registered as a plugin marketplace via `/plugin marketplace add anthropics/skills`. From there, users browse and install `document-skills` or `example-skills` plugins, invoking them by natural mention (e.g., "Use the PDF skill to extract form fields").

- **Agent Skills Specification**: Located in `./spec`, the formal specification for the Agent Skills standard. The broader standard is hosted at agentskills.io, suggesting Anthropic intends Skills as a portable, non-proprietary format.

- **Skill Categories in the Repo**: Organized into Creative & Design, Development & Technical (e.g., testing web apps, MCP server generation), Enterprise & Communication (communications, branding), and Document Skills (docx/pdf/pptx/xlsx).

- **Distribution Surfaces**: Skills work across three Claude surfaces — (1) Claude Code via the plugin marketplace, (2) Claude.ai for paid plans, and (3) Claude API via the Skills API Quickstart, including uploading custom skills.

- **Partner Skills**: A section highlighting skills from third parties, with Notion's "Notion Skills for Claude" called out as an example. This signals an ecosystem play where software vendors ship official skills to teach Claude their products.

## Key Takeaways
- Skills are folder-based packages (`SKILL.md` + scripts/resources) that dynamically extend Claude's task competence without permanent prompt bloat.
- The required `SKILL.md` frontmatter is minimal: only `name` and `description` fields are mandatory.
- The `description` field doubles as routing logic — it tells Claude *when* to activate the skill, not just what it does.
- Anthropic's production document skills (docx, pdf, pptx, xlsx) are published as reference implementations but under a source-available (not open source) license; other example skills are Apache 2.0.
- Skills work across Claude Code, Claude.ai (paid plans), and the Claude API, with Claude Code integration via a plugin marketplace command `/plugin marketplace add anthropics/skills`.
- Two installable plugins exist: `document-skills@anthropic-agent-skills` and `example-skills@anthropic-agent-skills`.
- The Agent Skills standard is broader than Anthropic's implementation — see agentskills.io for the spec.
- The repo includes a `./template` starter to bootstrap new custom skills.

## Notable Quotes
> "Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks."

> "Each skill is self-contained in its own folder with a SKILL.md file containing the instructions and metadata that Claude uses."

> "These skills are provided for demonstration and educational purposes only. While some of these capabilities may be available in Claude, the implementations and behaviors you receive from Claude may differ from what is shown in these skills."

## Related Entities
[[Claude]], [[Claude Code]], [[Anthropic]], [[Model Context Protocol]], [[Agent Skills Specification]], [[Notion]]