---
title: Anthropic Agent Skills
description: Anthropic's open standard for extending AI agent capabilities with specialized knowledge and workflows. A skill is a folder containing a SKILL.md file with YAML frontmatter and Markdown instructions.
source: https://github.com/anthropics/skills + https://agentskills.io
tags: [anthropic, agent, skills, claude, standard, format]
related: [hermes-agent, llm-wiki, garry-gstack, gstack]
---

# Anthropic Agent Skills

Anthropic's **Agent Skills** is an open standard for extending AI agents with specialized knowledge and workflows. The specification lives at [agentskills.io](https://agentskills.io). The canonical implementation repo is [github.com/anthropics/skills](https://github.com/anthropics/skills) (121k stars, 534 PRs, 30 commits).

## Overview

A skill is a **folder** containing at minimum a `SKILL.md` file. The folder may also bundle `scripts/`, `references/`, and `assets/`.

```
skill-name/
├── SKILL.md        # Required: YAML frontmatter + Markdown instructions
├── scripts/        # Optional: executable code (Python, JS, shell, etc.)
├── references/     # Optional: documentation, API docs, templates
└── assets/         # Optional: images, data files, resource bundles
```

The format is language-agnostic. Any AI client that implements the Agent Skills spec can load and use skills from this repo.

## How Skills Work — Progressive Disclosure

The core innovation is **progressive disclosure** for context efficiency:

1. **Discovery** — At startup, the agent loads only the `name` and `description` of each skill (lightweight, fast)
2. **Activation** — When a task matches a skill's description, the agent reads the full `SKILL.md` into context
3. **Execution** — The agent follows instructions, optionally loading bundled scripts or referenced files as needed

This keeps agents fast while giving them deep context on demand. See [What are skills?](https://agentskills.io/what-are-skills)

## SKILL.md Format

### YAML Frontmatter (Required Fields)

```yaml
---
name: pdf-processing
description: Extract PDF text, fill forms, merge files. Use when handling PDFs.
---
```

| Field | Required | Constraints |
|-------|----------|-------------|
| `name` | Yes | Max 64 chars. Lowercase, numbers, hyphens only. No leading/trailing hyphens. |
| `description` | Yes | Max 1024 chars. Non-empty. This is the **primary triggering mechanism** — include both what it does AND specific contexts for when to use it. |
| `license` | No | License name or reference to a bundled license file. |
| `compatibility` | No | Max 500 chars. Environment requirements. |
| `metadata` | No | Arbitrary key-value mapping for additional metadata. |
| `allowed-tools` | No | Space-separated string of pre-approved tools (experimental). |

### Full Example with Optional Fields

```yaml
---
name: pdf-processing
description: Extract PDF text, fill forms, merge files. Use when handling PDFs.
license: Apache-2.0
metadata:
  author: example-org
  version: "1.0"
---
```

### Markdown Body

The body contains the actual instructions. Key patterns Anthropic uses:

- **Gotchas sections** — common failure modes and how to avoid them
- **Output templates** — code blocks showing expected format
- **Checklists** — for multi-step workflows
- **Validation loops** — explicit steps to verify output quality
- **"Plan-validate-execute"** — plan first, validate the plan, then execute

## Agent Skills Specification

Full spec: [agentskills.io/specification](https://agentskills.io/specification)

The spec defines directory structure, frontmatter schema, progressive disclosure model, file references, and validation rules. The spec is maintained by the [agentskills/agentskills](https://github.com/agentskills/agentskills) community repo.

## Anthropic Skills Repository

### Available Skills (16 total)

**Creative & Design:**
- `algorithmic-art` — generative art and algorithmic design
- `brand-guidelines` — apply company brand standards
- `canvas-design` — design workflows
- `frontend-design` — frontend UI/UX design
- `theme-factory` — theme creation and management

**Development & Technical:**
- `claude-api` — build/debug/optimize Claude API apps (Apache 2.0)
- `mcp-builder` — build MCP (Model Context Protocol) servers
- `skill-creator` — create, test, evaluate, and improve skills (Apache 2.0)
- `webapp-testing` — test web applications
- `web-artifacts-builder` — build web artifacts

**Enterprise & Communication:**
- `internal-comms` — internal communications workflows
- `doc-coauthoring` — document coauthoring

**Document Creation (Proprietary — source-available):**
- `pdf` — PDF processing (read, extract, merge, split, rotate, watermark, OCR)
- `docx` — Word document creation/editing (uses docx-js)
- `pptx` — PowerPoint creation/editing (uses pptxgenjs)
- `xlsx` — Excel spreadsheet creation/editing (uses pandas + openpyxl)

**Other:**
- `slack-gif-creator` — GIF creation for Slack

### Skill Creator Workflow

The `skill-creator` skill defines the iterative process for building skills:

1. **Capture intent** — understand what the skill should do, when to trigger, expected output format
2. **Interview and research** — ask about edge cases, dependencies, test criteria; check existing MCPs
3. **Write draft SKILL.md** — fill in name, description, instructions
4. **Create test prompts** — a set of inputs to validate the skill
5. **Run evaluations** — execute skill on test prompts
6. **Evaluate qualitatively + quantitatively** — human review + metric analysis
7. **Rewrite based on feedback** — iterate on instructions
8. **Expand test set and repeat** — scale evaluation
9. **Optimize description** — use the description improver to maximize triggering accuracy

**Key triggering insight:** Claude tends to **undertrigger** skills. Anthropic intentionally makes skill descriptions "pushy" — e.g., "Make sure to use this skill whenever the user mentions X, even if they don't explicitly ask for it."

### Document Skills Architecture

The `docx`, `pdf`, `pptx`, `xlsx` skills are production-grade — they power Claude's native document capabilities. They demonstrate advanced skill patterns:

- **Multi-file structure**: Each skill has `SKILL.md` + reference docs + scripts
- **Library-specific code**: Python (pypdf, pdfplumber, pandas, openpyxl), JavaScript (docx, pptxgenjs)
- **Validation loops**: Output validation after every transformation step
- **Proprietary license**: Source-available but not open source (Apache 2.0 only covers `claude-api` and `skill-creator`)

## Best Practices for Writing Skills

From [agentskills.io/skill-creation/best-practices](https://agentskills.io/skill-creation/best-practices):

### Source Material
- **Start from real expertise** — don't generate skills from general LLM knowledge; feed domain-specific context
- **Extract from hands-on tasks** — complete a real task with an agent, capture steps that worked, corrections made, I/O formats
- **Synthesize from project artifacts** — internal docs, runbooks, incident reports, code review comments, git history reveal patterns

### Context Management
- **Spending context wisely** — don't dump everything; use progressive disclosure
- **Add what the agent lacks, omit what it knows** — don't restate general capabilities
- **Structure large skills with progressive disclosure** — only load what each subtask needs
- **Moderate detail** — too little is vague, too much is unread; find the right level

### Calibrating Control
- **Match specificity to fragility** — more specific instructions for steps where mistakes are costly
- **Provide defaults, not menus** — pick the best default and let the agent deviate if needed
- **Favor procedures over declarations** — "do X then Y then Z" outperforms vague declarations

### Effective Patterns
- **Gotchas sections** — failure modes and edge cases
- **Templates for output format** — show the target format explicitly
- **Checklists for multi-step workflows** — sequential steps with checkmarks
- **Validation loops** — explicit "verify this before proceeding" steps
- **Bundling reusable scripts** — scripts/ folder for code the skill needs to execute

## Hermes Agent Comparison

Our [[hermes-agent]] implementation shares the same structural pattern as Agent Skills:

| Aspect | Anthropic Agent Skills | Hermes Agent Skills |
|--------|----------------------|---------------------|
| Skill file | `SKILL.md` (YAML + Markdown) | `SKILL.md` (YAML + Markdown) |
| Linked files | `scripts/`, `references/`, `assets/` | `references/`, `templates/`, `scripts/` |
| Trigger | Description matching | Description matching |
| Multi-file docs | Per-skill reference docs | Per-skill reference docs |
| Validation | Manual + quantitative evals | Manual verification |

**Key differences:**
- Hermes skills are stored at `/opt/data/skills/` (VPS) and loaded via `skill_view()` tool
- Anthropic uses progressive disclosure at startup; Hermes loads skills on demand via tool call
- Hermes does not yet have a formal eval framework like `skill-creator`
- The spec's `allowed-tools` field has no direct Hermes equivalent

## Relationship to GStack

[[garry-gstack|Garry Tan's GStack]] uses a **conductor-based multi-agent orchestration** model. The Agent Skills format is conceptually similar but:
- GStack agents are invoked via slash commands (`/ship`, `/review`, `/qa`)
- GStack has automated doc updates, browser control, and health checks built in
- Agent Skills is a lighter, more portable format; GStack is heavier but more opinionated

The skill-creator workflow (draft → test → eval → iterate) parallels GStack's plan-review-deploy cycle. Both systems value **human-in-the-loop validation** before shipping.

## Links

- Spec: https://agentskills.io/specification
- What are skills: https://agentskills.io/what-are-skills
- Best practices: https://agentskills.io/skill-creation/best-practices
- GitHub repo: https://github.com/anthropics/skills
- Community: https://github.com/agentskills/agentskills
