# GitHub - garrytan/gstack: Use Garry Tan&#39;s exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA · GitHub

---
title: "gstack: Garry Tan's Claude Code Opinionated Toolkit"
created: 2026-04-25
type: entity
tags: [claude-code, ai-agents, developer-tools, workflow-automation, agent-orchestration]
related: [[Claude Code]], [[OpenClaw]], [[Andrej Karpathy AI Coding Rules]], [[Y Combinator]], [[GBrain]]
sources: [raw/articles/github-com-garrytan-gstack.md]
---

# gstack: Garry Tan's Claude Code Opinionated Toolkit

## Summary
gstack is an MIT-licensed open-source toolkit built by Garry Tan (President & CEO of Y Combinator) that turns Claude Code into a "virtual engineering team" via 23+ opinionated slash-command skills plus 8 power tools. The skills act as specialist roles — CEO, Designer, Eng Manager, Release Manager, Doc Engineer, QA, Security Officer, SRE, Performance Engineer — each implemented as Markdown skill definitions under `~/.claude/skills/gstack/`. As of publication, the repo has 82.6k stars and 12k forks.

The system encodes a sprint methodology (Think → Plan → Build → Review → Test → Ship → Reflect) where outputs from one skill feed deterministically into the next: `/office-hours` writes a design doc consumed by `/plan-ceo-review`; `/plan-eng-review` produces a test plan used by `/qa`; `/review` flags issues verified by `/ship`. Tan claims this enables 10-15 parallel sprints via Conductor (isolated Claude Code workspaces), and reports a 2026 logical-lines-of-code run rate of ~11,417/day vs 14/day in 2013 (~810×), measured across 40 garrytan/* repos.

gstack supports 10 AI coding agents beyond Claude (OpenAI Codex CLI, OpenCode, Cursor, Factory Droid, Slate, Kiro, Hermes, GBrain, OpenClaw), adding hosts via a single TypeScript config file. Core infrastructure includes a Chromium-based "GStack Browser" with anti-bot stealth, an in-browser sidebar agent with auto model routing (Sonnet for actions, Opus for analysis), layered prompt-injection defense (22MB ML classifier + Haiku transcript check + random canary tokens + verdict combiner, optional 721MB DeBERTa-v3 ensemble), Playwright browser automation, and Pretext for computed text layout in generated HTML.

## Key Concepts

- **The Sprint Methodology**: A 7-stage pipeline (Think → Plan → Build → Review → Test → Ship → Reflect) where each skill explicitly produces artifacts consumed by downstream skills. Prevents orphaned context and forces decisions to the surface; `/autoplan` chains CEO → design → eng → DX reviews automatically and surfaces only taste decisions to the user.

- **Slash-Command Skills as Specialist Roles**: Every skill embodies one role (e.g., `/plan-ceo-review` = CEO/Founder, `/cso` = Chief Security Officer running OWASP Top 10 + STRIDE, `/plan-devex-review` = DX Lead with 20-45 forcing questions and TTHW benchmarking). Skills are Markdown files dispatched by Claude Code; no proprietary runtime.

- **Confusion Protocol**: A behavioral rule that stops Claude from guessing on architectural decisions and instead forces explicit user input. Implements Karpathy's "wrong assumptions" failure mode mitigation at workflow level rather than per-prompt CLAUDE.md rules.

- **Shotgun-to-HTML Pipeline**: `/design-shotgun` generates 4-6 GPT Image mockup variants, opens a browser comparison board, collects feedback, iterates with decaying (5%/week) taste memory per-project. `/design-html` converts approved mockups to production HTML/CSS using Pretext (30KB, zero deps) with computed layouts that reflow correctly, auto-detecting React/Svelte/Vue and smart-routing by page type.

- **GStack Browser & Sidebar Agent**: A branded Chromium build with anti-bot stealth (bypasses Google/NYTimes captchas), one-click cookie import from Chrome/Arc/Brave/Edge, and a side-panel natural-language agent that spawns child Claude instances routed to Sonnet (actions) or Opus (analysis), with 5-min per-task cap and session isolation.

- **Layered Prompt Injection Defense**: Local 22MB ML classifier scans every page and tool output; Claude Haiku votes on full conversation shape; random canary token in system prompt detects session exfiltration across text/args/URLs/file writes; verdict combiner requires 2-of-N model agreement. Opt-in 721MB DeBERTa-v3 ensemble via `GSTACK_SECURITY_ENSEMBLE=deberta`; kill switch `GSTACK_SECURITY_OFF=1`.

- **Browser Handoff Protocol**: When agent hits CAPTCHA/auth/MFA, `$B handoff` opens headed Chrome at same URL with cookies/tabs intact; user solves, `$B resume` continues. Agent auto-suggests handoff after 3 consecutive failures.

- **/pair-agent Cross-Vendor Coordination**: First mechanism for AI agents from different vendors (Claude Code, OpenClaw, Hermes, Codex, Cursor) to share a browser with security — scoped tokens, per-agent tab isolation, rate limiting, domain restrictions, activity attribution. Auto-starts ngrok tunnel for remote agents.

- **/codex Second Opinion**: Invokes OpenAI Codex CLI for independent cross-model review. Three modes: review (pass/fail gate), adversarial challenge, open consultation. Produces cross-model overlap analysis when combined with `/review`.

- **Continuous Checkpoint Mode**: Opt-in auto-commit with `WIP:` prefix and structured `[gstack-context]` bodies (decisions, remaining work, failed approaches). Survives crashes; `/context-restore` reconstructs session state. `/ship` filter-squashes WIP commits before PR; push is local-only by default (`checkpoint_push=false`).

- **Team Mode / Auto-Update**: `./setup --team` plus `gstack-team-init required` bootstraps a repo so teammates get gstack automatically on Claude Code session start. Throttled once/hour, network-failure-safe, no vendored files, no version drift.

- **GBrain Integration**: Persistent agent knowledge base with three setup paths (PGLite local ~30s, existing Supabase URL, auto-provisioned Supabase ~90s via Management API). Per-remote trust triad (read-write / read-only / deny), sticky across worktrees. Registered as MCP server so `gbrain search`, `gbrain put_page` appear as typed tools.

- **GStack Memory Sync**: Optional private-repo push of learnings/plans/retros/developer profile with allowlist privacy modes and defense-in-depth secret scanner blocking AWS keys, tokens, PEM blocks, and JWTs pre-push.

- **Karpathy Four-Failure-Mode Mapping**: gstack explicitly maps to Andrej Karpathy's 17k-star AI coding rules: `/office-hours` handles wrong assumptions; Confusion Protocol prevents overcomplexity; `/review` catches orthogonal/drive-by edits; `/ship` enforces test-first verifiable goals (imperative→declarative).

## Key Takeaways
- 23 opinionated slash-command skills + 8 power tools, all Markdown, MIT-licensed, free; 82.6k GitHub stars, 12k forks.
- Install via one Claude Code paste: clones to `~/.claude/skills/gstack`, runs `./setup`, updates CLAUDE.md automatically.
- Supports 10 AI coding hosts (Claude Code, Codex CLI, OpenCode, Cursor, Factory Droid, Slate, Kiro, Hermes, GBrain, OpenClaw) via `./setup --host <name>`.
- Native OpenClaw skills shipped via ClawHub: `gstack-openclaw-office-hours`, `-ceo-review`, `-investigate`, `-retro`.
- Tan claims ~810× productivity vs 2013 on logical-LOC metric; runs 10-15 parallel Claude Code sessions via Conductor.
- `/qa` was "a massive unlock" enabling scale from 6 to 12 parallel workers — auto-generates regression tests for every bug fix.
- New v0.19 CLIs: `gstack-model-benchmark` (cross-model latency/tokens/cost/quality comparison across Claude, GPT-via-Codex, Gemini) and `gstack-taste-update`.
- Telemetry is opt-in and default-off; sends only skill name, duration, success/fail, version, OS — never code, paths, prompts, or content. Stored in Supabase with RLS-locked publishable key.
- Requirements: Claude Code, Git, Bun v1.0+, Node.js (Windows only due to Bun #4253 Playwright pipe transport bug).
- Repo is 74.4% TypeScript, 15.1% Go Template, 6.6% Shell; YC is hiring engineers in Dogpatch, SF to work on gstack.

## Notable Quotes
> "I don't think I've typed like a line of code probably since December, basically, which is an extremely large change." — Andrej Karpathy, No Priors podcast, March 2026

> "You said 'daily briefing app.' But what you actually described is a personal chief of staff AI."

> "Without a process, ten agents is ten sources of chaos. With a process — think, plan, build, review, test, ship — each agent knows exactly what to do and when to stop."

> "Tests make vibe coding safe instead of yolo coding."

> "This is the first time AI agents from different vendors can coordinate through a shared browser with real security: scoped tokens, tab isolation, rate limiting, domain restrictions, and activity attribution."

## Related Entities
[[Claude Code]], [[OpenClaw]], [[Andrej Karpathy AI Coding Rules]], [[Y Combinator]], [[GBrain]], [[Conductor]], [[OpenAI Codex CLI]], [[Playwright]], [[Model Context Protocol]], [[Garry Tan]]