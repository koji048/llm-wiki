---
title: Garry Tan's GStack
description: Garry Tan's AI-powered software factory built on Claude Code. 23 specialist skills (CEO, Eng Manager, Designer, QA, Security Guard, Release Engineer, etc.) invoked via slash commands. ~810x productivity gain vs 2013. Runs on Claude Code + Bun + persistent headless Chromium daemon.
source: https://github.com/garrytan/gstack
tags: [garry-tan, y-combinator, claude-code, agent, workflow, productivity]
related: [anthropic-agent-skills, hermes-agent, llm-wiki, openclaw]
---

# Garry Tan's GStack

**GStack** (github.com/garrytan/gstack) is Garry Tan's personal AI-powered software factory. It transforms Claude Code into a virtual engineering team — 23 specialist skills (CEO, Eng Manager, Designer, QA, Security Guard, Release Engineer, etc.) invoked via slash commands. All Markdown, MIT license.

Garry Tan is President & CEO of [Y Combinator](https://www.ycombinator.com/). He built Bookface (YC's internal social network) in 2013. Measured on logical lines of code per day (normalized for AI inflation), his 2026 rate is **~810x his 2013 pace** (11,417 vs 14 logical lines/day). Year-to-date through April 18, 2026 has already produced **240x his entire 2013 output**.

## Core Architecture

### The Daemon Model

GStack's key technical insight: AI browser agents need **sub-second latency** and **persistent state**. Every command cold-starting a browser = 3-5 seconds/tool call. Browser dying between commands = lost cookies, tabs, sessions.

Solution: a **long-lived Chromium daemon** that Claude Code talks to over localhost HTTP.

```
Claude Code → gstack CLI (Bun binary) → HTTP POST → gstack server (Bun.serve)
                                                            ↓ CDP
                                                    Chromium (persistent)
                                                    ↓
                                              ~100-200ms/command
                                              (vs 3-5s cold start)
```

- **First call**: starts daemon (~3s)
- **Subsequent calls**: ~100-200ms round-trip
- **Auto lifecycle**: starts on first use, shuts down after 30min idle
- **Version auto-restart**: binary rebuild → next command picks it up automatically

### Why Bun

1. **Compiled binaries** — `bun build --compile` produces a single ~58MB executable. No `node_modules` at runtime, no `npx`, no PATH configuration.
2. **Native SQLite** — Cookie decryption reads Chromium's SQLite database directly. Built into Bun (`new Database()`). No `better-sqlite3`, no native addon compilation.
3. **Built-in HTTP server** — `Bun.serve()` handles ~10 routes. No Express/Fastify needed.
4. **Native TypeScript** — Runs as `bun run server.ts` during dev, compiled binary for deployment.

### Security Model

- **Localhost only** — HTTP server binds to `localhost`, not `0.0.0.0`
- **Bearer token auth** — random UUID per session, written to state file mode 0o600 (owner-only)
- **Cookie security** — PBKDF2 + AES-128-CBC decryption in-process, never written to disk in plaintext
- **Keychain approval** — macOS Keychain dialog on first cookie import, user must click "Allow" or "Always Allow"

## Available Skills (23 total)

### Product & Strategy
| Skill | What it does |
|-------|-------------|
| `/office-hours` | Start here. Reframes product idea with 6 forcing questions before writing code. |
| `/plan-ceo-review` | CEO-level review: find the 10-star product in the request. |
| `/plan-eng-review` | Lock architecture, data flow, edge cases, and tests. |
| `/plan-design-review` | Rate each design dimension 0-10, explain what a 10 looks like. |

### Design
| Skill | What it does |
|-------|-------------|
| `/design-consultation` | Build a complete design system from scratch. |
| `/design-html` | Convert designs to production HTML/CSS. |
| `/design-shotgun` | Rapid design iteration. |
| `/design-review` | Design audit + fix loop with atomic commits. |

### Engineering & Review
| Skill | What it does |
|-------|-------------|
| `/review` | Pre-landing PR review. Finds bugs that pass CI but break in prod. |
| `/debug` | Systematic root-cause debugging. No fixes without investigation. |
| `/devex-review` | Developer experience review. |
| `/cso` | Security officer — OWASP + STRIDE audits. |
| `/codex` | Codex CLI integration. |
| `/investigate` | Root cause investigation methodology. |

### QA & Testing
| Skill | What it does |
|-------|-------------|
| `/qa` | Open a real browser, find bugs, fix them, re-verify. |
| `/qa-only` | Same as /qa but report only — no code changes. |

### Release & Deploy
| Skill | What it does |
|-------|-------------|
| `/ship` | Run tests, review, push, open PR. One command. |
| `/land-and-deploy` | Land a PR and deploy it. |
| `/canary` | Canary deployment. |
| `/benchmark` | Performance benchmarking. |

### Browser & Automation
| Skill | What it does |
|-------|-------------|
| `/browse` | Headless browser — real Chromium, real clicks, ~100ms/command. |
| `/setup-browser-cookies` | Import cookies from real browser for authenticated testing. |
| `/setup-deploy` | Configure deployment. |

### Documentation & Process
| Skill | What it does |
|-------|-------------|
| `/document-release` | Update all docs to match what you just shipped. |
| `/retro` | Weekly retro with per-person breakdowns and shipping streaks. |
| `/autoplan` | Automated planning from requirements. |

### Safety
| Skill | What it does |
|-------|-------------|
| `/careful` | Warn before destructive commands (rm -rf, DROP TABLE, force-push). |
| `/freeze` | Lock edits to one directory. Hard block. |
| `/guard` | Activate both careful + freeze at once. |
| `/unfreeze` | Remove directory edit restrictions. |
| `/gstack-upgrade` | Update gstack to latest version. |
| `/learn` | Learning mode. |

### OpenClaw Integration
| Skill | What it does |
|-------|-------------|
| `/openclaw` | OpenClaw integration for multi-agent spawning. |
| `/pair-agent` | Pair programming agent. |
| `/supabase` | Supabase-specific patterns. |
| `/plan-tune` | Tune planning parameters. |

## OpenClaw Integration

GStack works with [OpenClaw](https://github.com/openclaw/openclaw) (247K GitHub stars, Peter Steinberger's ACP protocol for spawning Claude Code sessions). Four methodology skills work natively in OpenClaw without needing Claude Code:

| Skill | What it does |
|-------|-------------|
| `gstack-openclaw-office-hours` | Product interrogation with 6 forcing questions. |
| `gstack-openclaw-ceo-review` | Strategic challenge with 4 scope modes. |
| `gstack-openclaw-investigate` | Root cause debugging methodology. |
| `gstack-openclaw-retro` | Weekly engineering retrospective. |

Install via ClawHub:
```
clawhub install gstack-openclaw-office-hours gstack-openclaw-ceo-review gstack-openclaw-investigate gstack-openclaw-retro
```

## Productivity Metrics

Garry's own measurement methodology (from [docs/ON_THE_LOC_CONTROVERSY.md](https://github.com/garrytan/gstack/blob/main/docs/ON_THE_LOC_CONTROVERSY.md)):

- **Raw LOC is misleading** — AI inflates line counts ( boilerplate, formatting)
- **Logical lines** = meaningful code changes (new logic, real algorithms)
- **2013 (Bookface)**: 14 logical lines/day
- **2026 (with GStack)**: 11,417 logical lines/day
- **Ratio**: ~810x improvement

Same person. Different tooling. The point isn't who typed it — it's what shipped.

## Skill File Format

GStack uses **SKILL.md files** — YAML frontmatter + Markdown instructions, same pattern as [[anthropic-agent-skills|Anthropic Agent Skills]].

```
skill-name/
├── SKILL.md          # Generated from .tmpl
├── .tmpl             # Template source (edit here, not SKILL.md)
└── ...
```

Key conventions:
- **SKILL.md files are generated from `.tmpl` templates.** Edit the template, then run `bun run gen:skill-docs` to regenerate.
- Safety skills use inline advisory prose — always confirm before destructive operations.
- Run `bun run skill:check` for a health dashboard of all skills.

## Relationship to Anthropic Agent Skills

[[anthropic-agent-skills|Anthropic Agent Skills]] and GStack share the same root pattern (SKILL.md + YAML frontmatter + Markdown instructions) but differ in scope:

| Aspect | Anthropic Agent Skills | GStack |
|--------|----------------------|--------|
| Invocation | Skill description matching (progressive disclosure) | Slash commands (e.g. `/review`, `/ship`) |
| Scope | General-purpose, portable | Opinionated, software-development-focused |
| Agents | Single agent | Multi-agent via conductor/CLAUDE.md |
| Browser | No built-in browser | Persistent Chromium daemon (~100ms/command) |
| Safety | Via `allowed-tools` field | Explicit `/careful`, `/freeze`, `/guard` skills |
| Skill generation | Manual or skill-creator workflow | Template-based (edit `.tmpl`, auto-generate) |
| License | Mixed (Apache 2.0 + proprietary) | MIT (fully open) |

GStack is heavier and more opinionated — it assumes Claude Code, a specific workflow, and a persistent browser. Agent Skills is lighter and more portable.

## Relationship to Hermes Agent

Our [[hermes-agent]] connects to Telegram via OpenClaw. GStack runs on Claude Code + Bun. The **skill file format is identical** — SKILL.md with YAML frontmatter. Our approach could benefit from:
- GStack's persistent browser daemon for QA tasks
- The multi-agent conductor pattern for specialized roles (CEO, Eng Manager, QA, Security)
- The slash-command dispatch mechanism
- Automated doc updates on release (`/document-release`)

The `skill-creator` workflow from [[anthropic-agent-skills|Anthropic Agent Skills]] (draft → test → eval → iterate) is what we should adopt for building Hermes skills.

## Quick Start

1. Install: `git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup`
2. Run `/office-hours` — describe what you're building
3. Run `/plan-ceo-review` on any feature idea
4. Run `/review` on any branch with changes
5. Run `/qa` on your staging URL
6. Run `/ship` to ship the PR

## Links

- GitHub: https://github.com/garrytan/gstack
- Y Combinator: https://www.ycombinator.com
- OpenClaw: https://github.com/openclaw/openclaw
- LOC controversy analysis: [docs/ON_THE_LOC_CONTROVERSY.md](https://github.com/garrytan/gstack/blob/main/docs/ON_THE_LOC_CONTROVERSY.md)
