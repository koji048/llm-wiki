# Equipping agents for the real world with Agent Skills \ Anthropic

---
title: "Agent Skills: Equipping Agents for the Real World"
created: 2026-04-25
type: entity
tags: [agents, anthropic, claude, agent-skills, progressive-disclosure]
related: [[Claude Code]], [[Model Context Protocol]], [[Claude Agent SDK]]
sources: [raw/articles/world-with-agent-skills.md]
---

# Agent Skills: Equipping Agents for the Real World

## Summary
Agent Skills are Anthropic's mechanism for giving Claude-based agents domain-specific expertise through organized folders of instructions, scripts, and resources that agents discover and load dynamically. Announced October 16, 2025, and published as an open standard for cross-platform portability on December 18, 2025, Skills transform general-purpose agents (like Claude Code) into specialized ones without requiring custom agent builds per use case. The fundamental unit is a directory containing a `SKILL.md` file with YAML frontmatter metadata (required fields: `name` and `description`).

Skills are built on a core design principle called **progressive disclosure**: at startup, the agent pre-loads only the name and description of each installed skill into its system prompt (level 1). If Claude judges a skill relevant, it loads the full `SKILL.md` body (level 2). The `SKILL.md` can reference additional bundled files (e.g., `reference.md`, `forms.md`) that Claude navigates only as needed (level 3+). This means the total context bundled into a skill is effectively unbounded because agents with filesystem + code execution tools don't need to read everything at once.

Skills can also bundle executable code (e.g., a Python script that extracts PDF form fields) that Claude can run as a tool at its discretion—without loading the script or data into context—enabling deterministic, efficient operations for tasks ill-suited to token generation (like sorting). Skills are supported on Claude.ai, Claude Code, the Claude Agent SDK, and the Claude Developer Platform. They are positioned as complementary to Model Context Protocol (MCP) servers, with Skills teaching workflows and MCP handling external tools.

## Key Concepts

- **Agent Skill**: A directory containing a `SKILL.md` file plus optional supporting files (scripts, documentation, resources) that extends an agent's capabilities. Skills package procedural knowledge and organizational context so general-purpose agents can act as specialists. Analogized to an onboarding guide for a new hire.

- **SKILL.md**: The required entry-point file of a skill, beginning with YAML frontmatter containing mandatory `name` and `description` metadata. The body holds the core instructions Claude loads when the skill is triggered. Referenced subfiles keep the core lean.

- **Progressive Disclosure**: The layered loading principle underpinning Skills—metadata first, core body second, linked files on demand. Compared to a well-organized manual with a table of contents, chapters, and appendices. Enables effectively unbounded skill context because nothing is loaded until needed.

- **Skill Triggering**: Claude decides whether to activate a skill based on the pre-loaded metadata in its system prompt relative to the user's task. Once triggered, Claude invokes a Bash tool (e.g., reads `pdf/SKILL.md`), then optionally reads further bundled files such as `forms.md`.

- **Code Execution Within Skills**: Skills can ship pre-written code (e.g., a Python PDF form-field extractor) that Claude runs as a tool. This avoids loading scripts or data into the context window and leverages deterministic computation for reliability and cost efficiency versus token-based reasoning.

- **PDF Skill (example)**: A concrete skill used in Claude's document editing features. Its `SKILL.md` references `reference.md` and `forms.md`, and bundles a Python script for extracting PDF form fields—illustrating splitting mutually exclusive context (form-filling is only read when needed) and delegating deterministic work to code.

- **Skill Authoring Best Practices**: (1) Start with evaluation—find capability gaps via representative tasks; (2) Structure for scale—split unwieldy `SKILL.md` files, separate mutually exclusive paths to reduce tokens; (3) Think from Claude's perspective—iterate on `name`/`description` and monitor real use; (4) Iterate with Claude—have Claude self-reflect and codify successful patterns into reusable skills.

- **Security Model**: Skills execute instructions and code, so malicious skills can introduce vulnerabilities, exfiltrate data, or cause unintended actions. Anthropic recommends installing only from trusted sources and auditing untrusted skills—especially code dependencies, bundled resources, and any instructions that connect to external networks.

- **Relationship to MCP**: Skills are framed as complementary to Model Context Protocol servers. MCP exposes external tools/software; Skills teach complex workflows that may orchestrate those tools.

- **Open Standard (Dec 18, 2025 update)**: Skills have been published as an open standard for cross-platform portability, enabling skill authoring independent of a single vendor's runtime.

## Key Takeaways
- A Skill is just a directory with a `SKILL.md` (YAML frontmatter requires `name` and `description`)—a deliberately simple format.
- Only skill metadata lives in the system prompt at startup; the body and subfiles load on demand via progressive disclosure.
- Because agents have filesystems and code execution, skill size is effectively unbounded.
- Skills can include executable code (e.g., Python scripts) that Claude invokes without loading into context, improving determinism and efficiency.
- Supported surfaces: Claude.ai, Claude Code, Claude Agent SDK, Claude Developer Platform.
- Published as an open standard on December 18, 2025, for cross-platform portability.
- Install skills only from trusted sources; audit untrusted skills for malicious code and network calls.
- Future direction: agents creating, editing, and evaluating their own Skills to codify behavior into reusable capabilities.

## Notable Quotes
> "A skill is a directory containing a SKILL.md file that contains organized folders of instructions, scripts, and resources that give agents additional capabilities."

> "Progressive disclosure is the core design principle that makes Agent Skills flexible and scalable."

> "Agents with a filesystem and code execution tools don't need to read the entirety of a skill into their context window when working on a particular task. This means that the amount of context that can be bundled into a skill is effectively unbounded."

> "Building a skill for an agent is like putting together an onboarding guide for a new hire."

## Related Entities
[[Claude Code]], [[Claude Agent SDK]], [[Model Context Protocol]], [[Claude Developer Platform]], [[Anthropic]], [[Progressive Disclosure]]