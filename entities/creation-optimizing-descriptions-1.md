# Optimizing skill descriptions - Agent Skills

---
title: "Optimizing Skill Descriptions"
created: 2026-04-25
type: entity
tags: [agent-skills, prompt-engineering, evaluation, skill-creation, llm-agents]
related: [[Agent Skills]], [[SKILL.md Specification]], [[Progressive Disclosure]], [[Skill Creator]], [[Evaluating Skill Output Quality]]
sources: [raw/articles/skill-creation-optimizing-descriptions.md]
---

# Optimizing Skill Descriptions

## Summary
This guide from agentskills.io explains how to systematically test and improve the `description` field in a skill's `SKILL.md` frontmatter to optimize triggering accuracy. Agent Skills use a progressive disclosure model: at startup, agents load only the name and description of each installed skill to decide relevance; the full SKILL.md is only read into context when a user task appears to match. The description therefore carries the entire burden of triggering — an under-specified description misses activations, while an over-broad description triggers false positives.

The recommended workflow is an empirical optimization loop: author an eval set of ~20 realistic user queries labeled `should_trigger: true/false` (8-10 of each), run each query 3 times against the agent (because LLM behavior is nondeterministic), compute per-query trigger rates, and evaluate against a 0.5 threshold. Queries are split into a ~60% train set (used to identify failures and guide revisions) and a ~40% validation set (held out to detect overfitting). The description has a hard specification limit of 1024 characters. Roughly five iterations is typical before diminishing returns, and the best description is selected by validation pass rate — not necessarily the last iteration produced.

The article provides a concrete bash/jq script template that invokes `claude -p` with `--output-format json` and inspects tool_use messages for `Skill` calls, and notes that the `skill-creator` Skill automates the whole loop (parallel evaluation, Claude-proposed revisions, live HTML report). The guide also distinguishes weak vs. strong negative test cases and emphasizes realism (file paths, casual phrasing, typos, personal context).

## Key Concepts

- **Progressive Disclosure**: Agents load only skill names and descriptions at startup, reading full SKILL.md content only on match. This context-management strategy means the description field is the sole basis for triggering decisions and must stand alone without the full skill body as support.

- **Trigger Rate Threshold**: A query passes if its trigger rate crosses 0.5 over multiple runs (default 3 runs). Should-trigger queries need rate > threshold; should-not-trigger queries need rate < threshold. This handles LLM nondeterminism by treating triggering as a probabilistic outcome rather than binary.

- **Eval Query Set Design**: ~20 queries, balanced 8-10 positive and 8-10 negative, varied along phrasing (formal/casual/typos), explicitness (domain-named vs. implicit need), detail (terse vs. context-heavy), and complexity (single-step vs. multi-step). The most useful positives are non-obvious matches; the most useful negatives are near-misses sharing keywords with the skill.

- **Near-Miss Negative Examples**: Strong should-not-trigger queries share vocabulary or concepts with the skill but require a different capability — e.g., for a CSV analysis skill, "update formulas in my Excel budget spreadsheet" (Excel editing, not analysis) or "write a python script that uploads CSV rows to postgres" (ETL, not analysis). Weak negatives like "What's the weather?" test nothing.

- **Train/Validation Split**: ~60/40 split with proportional positive/negative balance in each. Only train-set failures guide description revisions; validation is consulted only to measure generalization. The split is shuffled once and held fixed across iterations.

- **Imperative Description Phrasing**: Descriptions should be framed as instructions to the agent ("Use this skill when…") rather than descriptive ("This skill does…"), focus on user intent rather than implementation, and "err on the side of being pushy" by listing contexts including where users don't name the domain.

- **1024-Character Hard Limit**: The Agent Skills specification caps descriptions at 1024 characters. Descriptions tend to grow during optimization, so this must be checked each iteration.

- **Optimization Loop**: (1) evaluate on train and validation, (2) inspect train failures only, (3) revise description to generalize — broaden if positives miss, narrow/clarify boundary if negatives false-trigger, avoid adding literal keywords from failed queries (overfitting), try structurally different framings if stuck, (4) repeat up to ~5 iterations, (5) select iteration with highest validation pass rate.

- **Agent Capability Floor**: Skills tend not to trigger for simple one-step tasks the agent can handle with basic tools (e.g., "read this PDF"), even if the description matches — triggering primarily activates on tasks requiring specialized knowledge, unfamiliar APIs, or uncommon formats.

- **Eval Script Pattern**: Provided bash script loops over queries in a JSON file, runs each N=3 times via `claude -p "$query" --output-format json`, uses `jq` to detect `tool_use` messages where `.name == "Skill"` and `.input.skill` matches the target, and emits per-query records with `triggers`, `runs`, and `trigger_rate`. Early termination once the outcome is clear can cut cost significantly.

- **skill-creator Skill**: A meta-skill that automates the entire optimization loop — splits the eval set, evaluates trigger rates in parallel, proposes description improvements via Claude, and produces a live HTML report.

- **Realism Ingredients**: Include file paths (`~/Downloads/report_final_v2.xlsx`), personal context ("my manager asked…"), specific details (column names, company names), and casual language/abbreviations/typos to mimic real prompts rather than sanitized test strings.

## Key Takeaways
- The description field is the entire triggering mechanism because of progressive disclosure; the body of SKILL.md is not visible until after the agent decides to load it.
- Use ~20 labeled eval queries (8-10 positive, 8-10 negative), run each 3 times, and threshold the trigger rate at 0.5.
- Split queries 60/40 into train and validation; only train-set failures may inform description edits.
- Avoid overfitting by refusing to add specific keywords from failed queries — generalize to the underlying category instead.
- Select the best description by validation pass rate, which may not be the final iteration produced.
- Descriptions have a 1024-character cap per the Agent Skills specification.
- Strong negative test cases are near-misses that share vocabulary with the skill; weak negatives are unrelated tasks.
- Five iterations is typically enough; stalling usually indicates a query-set problem, not a description problem.
- The example transformation replaces `Process CSV files.` with a description naming specific capabilities (summary stats, derived columns, charts, cleaning) and explicit trigger contexts including "even if they don't explicitly mention 'CSV' or 'analysis.'"
- The `skill-creator` Skill and the provided bash+jq script automate evaluation for Claude Code.

## Notable Quotes
> "A skill only helps if it gets activated."

> "This means the description carries the entire burden of triggering."

> "Err on the side of being pushy. Explicitly list contexts where the skill applies, including cases where the user doesn't name the domain directly."

> "Avoid adding specific keywords from failed queries — that's overfitting. Instead, find the general category or concept those queries represent and address that."

> "The best description may not be the last one you produced; an earlier iteration might have a higher validation pass rate than later ones that overfit to the train set."

## Related Entities
[[Agent Skills]], [[SKILL.md Specification]], [[Progressive Disclosure]], [[Skill Creator]], [[Claude Code]], [[Evaluating Skill Output Quality]], [[Train Validation Split]], [[Prompt Engineering]]