# Evaluating skill output quality - Agent Skills

---
title: "Evaluating Skill Output Quality"
created: 2026-04-25
type: entity
tags: [agent-skills, evaluation, llm-evals, skill-development, testing]
related: [[Agent Skills]], [[SKILL.md]], [[Claude Code]], [[skill-creator Skill]], [[LLM-as-Judge]]
sources: [raw/articles/skill-creation-evaluating-skills.md]
---

# Evaluating Skill Output Quality

## Summary
This Agent Skills documentation page describes a structured evaluation (eval) methodology for measuring whether a skill reliably improves agent output quality across varied prompts and edge cases. The core pattern is a paired comparison: run each test case twice — once with the skill and once without (or against a previous skill version as baseline) — then compare pass rates, latency, and token usage to quantify what the skill costs versus what it delivers.

The workflow is organized around a `evals/evals.json` file authored by the skill creator (containing prompts, expected outputs, input files, and assertions) and a parallel `<skill>-workspace/` directory holding per-iteration results. Each iteration directory (`iteration-N/`) contains per-eval subdirectories with `with_skill/` and `without_skill/` branches, each holding `outputs/`, `timing.json`, and `grading.json`, plus an aggregate `benchmark.json`. Runs must start in clean contexts (e.g., Claude Code subagents) to avoid contamination from prior state.

Assertions are verifiable, observable claims ("Both axes are labeled", "The chart shows exactly 3 months") that are graded PASS/FAIL with concrete evidence — either by an LLM judge or by verification scripts for mechanical checks. Aggregate statistics (mean/stddev of pass rate, duration, tokens) plus deltas between configurations reveal the skill's value. Pattern analysis, human review (`feedback.json`), and execution transcripts feed into an iterative improvement loop, often automated by the `skill-creator` Skill.

## Key Concepts

- **Test Case**: A triple of (prompt, expected_output, optional input files) stored in `evals/evals.json`. Prompts should be realistic user messages — varied in phrasing, formality, and precision — and should include at least one edge case. Start with 2–3 cases before over-investing.

- **Paired Baseline Run**: Every test case is executed twice: once with the skill loaded, once without (or against a snapshotted previous version stored via `cp -r <skill-path> <workspace>/skill-snapshot/`). The baseline quantifies skill value; without it, you can't tell whether the model would have succeeded anyway.

- **Workspace Structure**: Results live outside the skill directory in `<skill>-workspace/iteration-N/<eval-name>/{with_skill,without_skill}/{outputs,timing.json,grading.json}` with an aggregate `benchmark.json` at the iteration root. Only `evals/evals.json` is hand-authored; other JSON files are machine-produced.

- **Clean Context Isolation**: Each run starts fresh with no leftover state. Claude Code subagents provide this natively (each child task starts fresh); without subagent support, use separate sessions. Prevents the agent from inheriting behaviors not actually specified in SKILL.md.

- **Timing Capture (`timing.json`)**: Records `total_tokens` and `duration_ms` per run. In Claude Code, these values appear in the subagent task-completion notification and are not persisted elsewhere, so they must be saved immediately.

- **Assertions**: Verifiable, specific, observable statements added *after* seeing first-round outputs. Good assertions are programmatically checkable ("output is valid JSON"), specific ("bar chart has labeled axes"), or countable ("at least 3 recommendations"). Weak assertions are vague ("output is good") or brittle (exact string matches). Reserve assertions for objective checks; leave subjective qualities (style, polish) for human review.

- **Grading (`grading.json`)**: Each assertion gets PASS/FAIL plus textual evidence quoting or referencing the output. LLM judges handle semantic checks; verification scripts handle mechanical checks (file exists, row count, JSON validity) more reliably. Requires concrete evidence — a section labeled "Summary" with one vague sentence is a FAIL.

- **Blind Comparison**: For comparing two skill versions, present both outputs to an LLM judge without revealing provenance. Judge scores holistic qualities (organization, formatting, usability) on its own rubric. Catches cases where both versions pass all assertions but differ in quality.

- **Benchmark Aggregation (`benchmark.json`)**: Per-configuration summary stats (mean/stddev of pass_rate, time_seconds, tokens) plus a delta block. Example shown: with-skill pass_rate 0.83 vs without-skill 0.33 (delta +0.50), at cost of +13s and +1700 tokens. Stddev only meaningful with multiple runs per eval.

- **Pattern Analysis**: Aggregate stats hide patterns. Remove assertions that always pass in both configs (they inflate the with-skill rate without reflecting value). Investigate always-fail assertions (broken or too hard). Study assertions that pass only with the skill — that's where value lives. High stddev signals flaky evals or ambiguous skill instructions.

- **Human Review (`feedback.json`)**: Per-eval free-text feedback capturing issues assertions missed. Actionable ("chart is missing axis labels, months in alphabetical instead of chronological order") beats vague ("looks bad"). Empty feedback = the output looked fine.

- **Three Signals for Iteration**: (1) Failed assertions → specific gaps; (2) Human feedback → broader quality issues; (3) Execution transcripts → *why* things went wrong (ignored instructions indicate ambiguity; wasted steps indicate bloat). Feed all three plus current SKILL.md to an LLM to propose changes.

- **Skill Improvement Principles**: Generalize fixes beyond specific test cases; keep skills lean (fewer, better instructions often beat exhaustive rules); explain the *why* ("Do X because Y causes Z") rather than rigid "ALWAYS/NEVER" directives; bundle repeated helper scripts into `scripts/`.

- **The Iteration Loop**: (1) LLM proposes improvements from signals + SKILL.md → (2) human reviews/applies → (3) rerun all tests in `iteration-<N+1>/` → (4) grade and aggregate → (5) human review → repeat. Stop when satisfied, feedback is empty, or improvements plateau.

## Key Takeaways
- Always run paired with-skill vs without-skill (or vs previous snapshot) runs — a skill's value is only visible relative to a baseline.
- Start with 2–3 test cases; write prompts and expected outputs first, then add assertions *after* seeing initial outputs.
- Use subagents or separate sessions to guarantee clean-context isolation for each eval run.
- Capture `total_tokens` and `duration_ms` immediately from Claude Code subagent completion notifications — they aren't persisted.
- Prefer verification scripts over LLM judges for mechanical checks (JSON validity, row counts, file dimensions).
- Track the cost/benefit delta: +13s and +1700 tokens for +50pp pass rate is a very different trade-off than +2pp for double the tokens.
- Remove assertions that always pass in both configurations — they inflate skill pass rates without measuring skill value.
- High pass-rate stddev across runs signals either a flaky eval or ambiguous skill instructions; disambiguate with examples.
- Blind LLM-judge comparison complements assertion grading by catching quality differences when both outputs pass all assertions.
- Reasoning-based instructions ("Do X because Y causes Z") outperform rigid directives in SKILL.md.
- The `skill-creator` Skill automates running evals, grading, aggregation, and presenting results for human review.

## Notable Quotes
> "Each eval run should start with a clean context — no leftover state from previous runs or from the skill development process. This ensures the agent follows only what the SKILL.md tells it."

> "Require concrete evidence for a PASS. Don't give the benefit of the doubt. If an assertion says 'includes a summary' and the output has a section titled 'Summary' with one vague sentence, that's a FAIL — the label is there but the substance isn't."

> "If pass rates plateau despite adding more rules, the skill may be over-constrained — try removing instructions and see if results hold or improve."

> "Reasoning-based instructions ('Do X because Y tends to cause Z') work better than rigid directives ('ALWAYS do X, NEVER do Y'). Models follow instructions more reliably when they understand the purpose."

## Related Entities
[[Agent Skills]], [[SKILL.md]], [[Claude Code]], [[skill-creator Skill]], [[LLM-as-Judge]], [[Subagents]], [[Eval-Driven Development]]