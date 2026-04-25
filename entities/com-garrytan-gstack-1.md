# GitHub - garrytan/gstack: Use Garry Tan&#39;s exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA · GitHub

---
title: "gstack: Garry Tan's Claude Code Agent Framework"
created: 2026-04-25
type: entity
tags: [claude-code, ai-agents, developer-tools, workflow-automation, y-combinator]
related: [[Claude Code]], [[OpenClaw]], [[Andrej Karpathy AI Coding Rules]], [[Y Combinator]], [[AI Coding Agents]]
sources: [raw/articles/github-com-garrytan-gstack.md]
---

# gstack: Garry Tan's Claude Code Agent Framework

## Summary
gstack is an open-source (MIT) Claude Code configuration authored by Garry Tan (President & CEO of Y Combinator) that turns Claude Code into a virtual engineering team via 23+ opinionated slash-command "skills" plus eight power tools. The skills map to startup roles — CEO, Designer, Eng Manager, Developer Experience Lead, Staff Engineer, QA Lead, Chief Security Officer, SRE, Release Engineer, Technical Writer — and run as a structured sprint: Think → Plan → Build → Review → Test → Ship → Reflect. Each skill feeds artifacts (design docs, test plans, bug reports) into the next so context doesn't fall through cracks.

Tan claims a ~810× increase in his personal logical-code-change rate from 2013 (14 logical lines/day, when he built YC's Bookface) to 2026 (11,417 logical lines/day), measured across 40 public+private garrytan/* repos excluding a demo repo, with 3 production services and 40+ features shipped in 60 days part-time. The project was inspired by Andrej Karpathy's "basically haven't typed code since December" remark (No Priors, March 2026) and Peter Steinberger's solo-built OpenClaw (247K GitHub stars). gstack has 82.9K stars and 12.1K forks at the time of capture.

Beyond Claude Code, gstack supports 10 coding agents via `./setup --host <name>`: OpenAI Codex CLI, OpenCode, Cursor, Factory Droid, Slate, Kiro, Hermes, GBrain, and OpenClaw. It includes a real-Chromium browser stack (GStack Browser) with anti-bot stealth, a sidebar agent that auto-routes between Sonnet (actions) and Opus (analysis), a layered prompt-injection defense (22MB ML classifier + Haiku transcript check + canary token, optional 721MB DeBERTa-v3 ensemble), cross-agent browser coordination via `/pair-agent`, and Conductor-based parallelism supporting 10-15 concurrent Claude Code sprints.

## Key Concepts

- **The Sprint Pipeline**: The core organizing metaphor — Think → Plan → Build → Review → Test → Ship → Reflect. Skills are not interchangeable tools but stages in a process: `/office-hours` writes a design doc that `/plan-ceo-review` reads; `/plan-eng-review` writes a test plan `/qa` picks up; `/review` catches bugs `/ship` verifies are fixed.

- **/office-hours**: YC-style product interrogation with six forcing questions that reframe the product before code is written. Extracts unstated capabilities, challenges premises, and produces a design doc feeding all downstream skills. Pushes back on framing ("you said daily briefing app, but you're building a personal chief of staff AI").

- **/plan-ceo-review and Scope Modes**: Four modes — Expansion, Selective Expansion, Hold Scope, Reduction — that rethink the problem to find the "10-star product" hiding inside a request. Part of `/autoplan` which chains CEO → design → eng → DX review automatically.

- **/review and /codex (Cross-Model Review)**: `/review` is Claude-driven staff-engineer code review with auto-fix; `/codex` invokes OpenAI Codex CLI for independent second opinion in three modes (review gate, adversarial challenge, open consultation). Running both yields cross-model analysis showing overlapping vs unique findings.

- **/qa and /qa-only (Browser-Based QA)**: Opens real Chromium, clicks through flows, finds bugs, fixes with atomic commits, auto-generates regression tests, and re-verifies. Tan credits `/qa` as the unlock that let him scale from 6 to 12 parallel workers.

- **/cso (Chief Security Officer)**: OWASP Top 10 + STRIDE threat modeling with zero-noise design: 17 false-positive exclusions, 8/10+ confidence gate, independent finding verification, and concrete exploit scenarios per finding.

- **Design Pipeline (/design-shotgun → /design-html)**: `/design-shotgun` generates 4-6 GPT Image mockup variants, opens a browser comparison board, collects feedback, iterates with taste memory (5%/week decay via `gstack-taste-update`). `/design-html` converts approved mockups to production HTML using Pretext computed layout (30KB, zero deps) with framework detection (React/Svelte/Vue) and API routing per design type.

- **GStack Browser + Sidebar Agent**: Branded Chromium with anti-bot stealth (bypasses Google/NYTimes captchas), auto model routing (Sonnet for click/navigate/screenshot, Opus for analysis), 5-minute per-task budget, isolated session, and one-click cookie import from real Chrome/Arc/Brave/Edge. `$B handoff` / `$B resume` lets humans solve CAPTCHAs/MFA mid-session.

- **Prompt Injection Defense**: Layered local defense — 22MB bundled ML classifier scans pages and tool outputs, Claude Haiku transcript vote, random canary token in system prompt catches exfil across text/args/URLs/file-writes, verdict combiner requires 2-classifier agreement. Optional 721MB DeBERTa-v3 ensemble via `GSTACK_SECURITY_ENSEMBLE=deberta`; kill switch `GSTACK_SECURITY_OFF=1`.

- **/pair-agent (Cross-Agent Browser Coordination)**: First system enabling AI agents from different vendors (Claude Code, OpenClaw, Hermes, Codex, Cursor) to coordinate through a shared browser. Scoped tokens, tab isolation, rate limiting, domain restrictions, activity attribution. Auto-starts ngrok tunnel for remote agents.

- **Safety Guardrails (/careful, /freeze, /guard, /unfreeze)**: `/careful` warns before destructive ops (rm -rf, DROP TABLE, force-push, git reset --hard); `/freeze` locks edits to one directory; `/guard` combines both; `/investigate` auto-freezes to the investigated module. Karpathy-style CLAUDE.md workflow enforcement across entire sprints.

- **Continuous Checkpoint Mode**: Opt-in auto-commits with `WIP:` prefix and `[gstack-context]` body containing decisions, remaining work, failed approaches. `/context-restore` reconstructs session state. `/ship` filter-squashes WIP commits before PR. Local-only by default (`checkpoint_push=true` to push).

- **Parallel Sprints via Conductor**: Runs 10-15 Claude Code sessions in isolated workspaces concurrently — one running `/office-hours`, another `/review`, another `/qa`, etc. The sprint structure is what makes parallelism tractable: without a process, ten agents is ten sources of chaos.

- **Team Mode Auto-Update**: `./setup --team` + `gstack-team-init required` bootstraps a repo so teammates auto-install gstack, with per-session update checks throttled to once/hour, network-failure-safe and silent. `required` blocks; `optional` nudges. No vendored files, no version drift.

- **GBrain Integration**: Persistent knowledge base for AI agents across sessions. `/setup-gbrain` offers three paths: existing Supabase pooler URL, auto-provision via Supabase Management API (~90s), or PGLite local (~30s). Per-repo trust tiers: read-write, read-only (multi-client consultants), deny. Registered as MCP server so `gbrain search`, `gbrain put_page` become typed tools.

- **Karpathy Four Failure Modes Mapping**: Wrong assumptions → `/office-hours` forcing questions + Confusion Protocol. Overcomplexity → `/review`. Orthogonal edits → `/review`. Imperative over declarative → `/ship` test-first transformation of tasks into verifiable goals.

## Key Takeaways
- gstack is free MIT-licensed, 82.9K stars, 12.1K forks; written primarily in TypeScript (74.4%), Go Template (15.1%), Shell (6.6%).
- 23 skills + 8 power tools + standalone CLIs (`gstack-model-benchmark`, `gstack-taste-update`) cover every sprint stage.
- Installable in ~30 seconds via a single paste into Claude Code; supports 10 coding agents via `./setup --host <name>`.
- Tan reports 2026 run rate of 11,417 logical lines/day vs 14 in 2013 (~810×), YTD 2026 already 240× all of 2013; 3 production services + 40+ features in 60 days part-time.
- Built on inspiration from Karpathy's "haven't typed code since December" (No Priors, March 2026) and Peter Steinberger's OpenClaw (247K stars).
- Practical parallelism ceiling is currently 10-15 concurrent sprints; `/qa` was the unlock that scaled Tan from 6 to 12 parallel workers.
- Telemetry is opt-in, never sends code/paths/prompts; schema public in `supabase/migrations/`; Supabase uses RLS with validated edge functions.
- Cross-model review (`/review` + `/codex`) surfaces which findings Claude and OpenAI agree on vs disagree on.
- Real-browser QA with anti-bot stealth + sidebar agent + `$B handoff` for CAPTCHA/MFA makes browser automation robust.
- Requirements: Claude Code, Git, Bun v1.0+, Node.js (Windows only due to Bun Playwright pipe bug #4253).

## Notable Quotes
> "I don't think I've typed like a line of code probably since December, basically, which is an extremely large change." — Andrej Karpathy, No Priors podcast, March 2026

> "You said 'daily briefing app.' But what you actually described is a personal chief of staff AI."

> "gstack is powerful with one sprint. It is transformative with ten running at once."

> "The point isn't who typed it, it's what shipped."

> "Tests make vibe coding safe instead of yolo coding."

## Related Entities
[[Claude Code]], [[OpenClaw]], [[Andrej Karpathy AI Coding Rules]], [[Y Combinator]], [[Garry Tan]], [[Peter Steinberger]], [[OpenAI Codex CLI]], [[Cursor]], [[Conductor (parallel Claude sessions)]], [[Playwright]], [[Supabase]], [[GBrain]], [[MCP (Model Context Protocol)]], [[OWASP Top 10]], [[STRIDE Threat Model]]