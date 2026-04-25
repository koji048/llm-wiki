# Equipping agents for the real world with Agent Skills \ Anthropic

---
title: "Agent Skills: Equipping Agents for the Real World"
created: 2026-04-25
type: entity
tags: [agent-skills, anthropic, claude, ai-agents, progressive-disclosure]
related: [[Claude Code]], [[Model Context Protocol]], [[Claude Agent SDK]]
sources: [raw/articles/world-with-agent-skills.md]
---

# Agent Skills: Equipping Agents for the Real World

## Summary
Agent Skills are Anthropic's mechanism for equipping general-purpose agents like Claude with domain-specific procedural knowledge and organizational context. Introduced October 16, 2025, and later published as an open cross-platform standard on December 18, 2025, Skills are organized folders containing instructions, scripts, and resources that agents discover and load dynamically. A Skill is fundamentally a directory containing a `SKILL.md` file with YAML frontmatter specifying required `name` and `description` metadata, plus optional bundled files and executable code.

The core design principle is **progressive disclosure**: only skill metadata (name/description) is preloaded into the system prompt at startup; the full `SKILL.md` body is read into context only when Claude determines the skill is relevant; additional bundled files (e.g., `reference.md`, `forms.md`) are loaded on demand. This allows effectively unbounded bundled context without consuming context window budget upfront. Skills can also include deterministic code (e.g., Python scripts) that Claude runs as tools—beneficial for operations like sorting, PDF form-field extraction, and anything requiring reliability or efficiency beyond token generation.

Anthropic illustrates Skills with a PDF skill that powers Claude's document editing, enabling form-filling via a bundled Python script that extracts form fields without loading the PDF or script into context. Skills are supported across Claude.ai, Claude Code, the Claude Agent SDK, and the Claude Developer Platform, and are positioned as complementary to Model Context Protocol (MCP) servers.

## Key Concepts

- **Agent Skill**: A directory containing a `SKILL.md` file plus optional supporting files and scripts, packaging expertise into a composable capability. Skills transform general-purpose agents into specialized agents by capturing procedural knowledge, likened to an "onboarding guide for a new hire."

- **SKILL.md**: The entry-point Markdown file that must begin with YAML frontmatter containing required `name` and `description` fields. Only this metadata is preloaded into the system prompt; the body is loaded on demand when Claude deems the skill relevant.

- **Progressive Disclosure**: The three-tier loading strategy that makes Skills scalable. Level 1: metadata in system prompt. Level 2: full `SKILL.md` body loaded when triggered. Level 3+: additional bundled files (referenced by name from SKILL.md) loaded only as needed. Analogous to a manual with table of contents, chapters, and appendix.

- **Skill Triggering**: Claude invokes a skill by using a Bash tool to read `SKILL.md` contents when a user message aligns with the skill's description. The quality of the `name` and `description` fields directly determines trigger reliability.

- **Bundled Code Execution**: Skills can include scripts (e.g., Python) that Claude executes as deterministic tools without loading their source or inputs into context. Example: a PDF script extracts all form fields programmatically—cheaper and more reliable than token-based generation for deterministic tasks like sorting.

- **Context Window Dynamics**: The context begins with core system prompt + all skill metadata + user message. On trigger, Claude reads `SKILL.md` via Bash, optionally navigates to referenced files (e.g., `forms.md`), then proceeds with the task. Unreferenced files never enter context.

- **Authoring Best Practices**: Start with evaluation against representative tasks to find gaps; structure for scale by splitting large `SKILL.md` files into separate referenced files (especially when contexts are mutually exclusive); clarify whether code is meant to be executed or read as reference; iterate with Claude by asking it to capture successful approaches and self-reflect on failures.

- **Security Model**: Skills grant Claude instructions and executable code, creating attack surface for malicious skills that could exfiltrate data or perform unintended actions. Anthropic recommends installing only from trusted sources and auditing third-party skills—especially code dependencies, bundled resources, and instructions referencing external networks.

- **Relationship to MCP**: Skills are positioned as complementary to Model Context Protocol servers. Anthropic plans to explore how Skills can teach agents complex workflows involving MCP-exposed external tools.

- **Agent-Authored Skills (Future)**: A stated long-term goal is enabling agents to create, edit, and evaluate Skills autonomously, codifying their own behavioral patterns into reusable capabilities.

## Key Takeaways
- A Skill is just a directory with a `SKILL.md` file—simplicity is an explicit design goal enabling portability and ease of authoring.
- Progressive disclosure keeps context usage bounded regardless of total skill size; unused files cost zero tokens.
- YAML frontmatter `name` and `description` are the sole entry point into the skill selection process and deserve careful authoring.
- Deterministic code execution within Skills is strictly preferred over LLM generation for operations like sorting, parsing, and form manipulation.
- Skills work across Claude.ai, Claude Code, Claude Agent SDK, and the Claude Developer Platform; published as an open standard December 18, 2025.
- Skills complement rather than replace MCP servers.
- Security audit is essential for skills from untrusted sources due to code and instruction injection risk.
- Best practice: develop skills incrementally against real evaluation tasks rather than anticipating needs upfront.

## Notable Quotes
> "A skill is a directory containing a SKILL.md file that contains organized folders of instructions, scripts, and resources that give agents additional capabilities."

> "Progressive disclosure is the core design principle that makes Agent Skills flexible and scalable."

> "Agents with a filesystem and code execution tools don't need to read the entirety of a skill into their context window when working on a particular task. This means that the amount of context that can be bundled into a skill is effectively unbounded."

> "Building a skill for an agent is like putting together an onboarding guide for a new hire."

## Related Entities
[[Claude Code]], [[Claude Agent SDK]], [[Model Context Protocol]], [[Anthropic]], [[Progressive Disclosure]], [[Claude Developer Platform]]