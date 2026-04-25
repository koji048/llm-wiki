# Evaluating skill output quality - Agent Skills

---
title: "Evaluating Skill Output Quality"
created: 2026-04-25
type: entity
tags: [agent-skills, evaluation, evals, skill-development, llm-testing]
related: [[Agent Skills]], [[SKILL.md]], [[Claude Code]], [[skill-creator Skill]], [[LLM-as-Judge]]
sources: [raw/articles/skill-creation-evaluating-skills.md]
---

# Evaluating Skill Output Quality

## Summary
This wiki entry documents the official Agent Skills methodology for systematically evaluating skill output quality via structured evaluations ("evals"). The core pattern is comparative: each test case is executed twice — once with the skill loaded and once without (the baseline) — in isolated contexts (e.g., Claude Code subagents) to eliminate leftover state. Results are stored in a standardized workspace structure with per-iteration directories, allowing comparison across skill versions.

The process decomposes into six stages: (1) designing test cases in `evals/evals.json` with prompt/expected_output/files, (2) spawning clean-context runs with and without the skill, (3) capturing timing data (`total_tokens`, `duration_ms`) from subagent completion notifications, (4) writing verifiable assertions after viewing first outputs, (5) grading assertions with evidence (LLM or script), and (6) aggregating benchmarks to compute deltas in pass rate, time, and tokens between configurations. Human review supplements automated grading to catch issues assertions miss.

Iteration is driven by three signals — failed assertions, human feedback, and execution transcripts — which are fed together with the current SKILL.md to an LLM that proposes improvements. The article emphasizes leanness (fewer, better instructions), reasoning-based directives over rigid rules, and bundling repeated helper code into the skill's `scripts/` directory. The `skill-creator` Skill automates much of this loop.

## Key Concepts

- **Test Case Structure**: Each case in `evals/evals.json` has three parts — `prompt` (realistic user message), `expected_output` (human-readable success description), and optional `files` (input files). Assertions are added later, after observing first outputs.

- **Comparative Eval Pattern**: Every eval runs twice — `with_skill/` and `without_skill/` subdirectories — to produce a baseline delta. For improving existing skills, snapshot the previous version (`cp -r <skill-path> <workspace>/skill-snapshot/`) and use it as baseline, saving to `old_skill/outputs/`.

- **Clean-Context Isolation**: Each run must start fresh with no leftover state. In Claude Code, subagents provide this naturally; without subagents, use a separate session per run. This ensures only the SKILL.md drives behavior.

- **Workspace Directory Structure**: Results live alongside the skill directory in `<skill>-workspace/iteration-N/<eval-name>/{with_skill,without_skill}/{outputs/,timing.json,grading.json}` with a top-level `benchmark.json` aggregating the iteration.

- **Timing Capture (`timing.json`)**: Records `total_tokens` and `duration_ms` per run. In Claude Code, these come from the subagent task completion notification and must be saved immediately since they aren't persisted elsewhere. Enables trade-off analysis: a skill that triples tokens for a small quality win may not be worth it.

- **Assertions**: Verifiable, specific, observable statements about outputs. Good examples: "output file is valid JSON", "chart has labeled axes", "report includes at least 3 recommendations". Weak examples: "output is good" (vague), "uses exactly the phrase 'Total Revenue: $X'" (brittle). Written after first run, not before.

- **Grading with Evidence**: `grading.json` records `passed` (bool) and `evidence` (concrete quote/reference) per assertion. LLMs grade subjective assertions; scripts grade mechanical checks (JSON validity, row counts, file dimensions) more reliably. PASS requires concrete evidence — a "Summary" heading with vague contents is a FAIL.

- **Blind Comparison Judging**: For comparing two skill versions, present both outputs to an LLM judge without revealing which came from which version, scoring holistic qualities (organization, formatting, polish) on its own rubric. Complements assertion grading when two outputs both pass all assertions but differ in overall quality.

- **Benchmark Aggregation (`benchmark.json`)**: Per-configuration summary with `pass_rate`, `time_seconds`, `tokens` (each with `mean` and `stddev`), plus a `delta` object showing what the skill costs vs. what it buys. Stddev is only meaningful with multiple runs; early iterations rely on raw counts and deltas.

- **Pattern Analysis**: Post-aggregation review removes assertions always passing in both configs (uninformative inflation), investigates assertions always failing (broken assertion or too-hard test), studies assertions passing only with the skill (where the skill adds value), and reads transcripts for time/token outliers.

- **Flakiness Detection via Stddev**: High stddev across runs of the same eval signals either model-randomness sensitivity or ambiguous skill instructions — fix by adding examples or more specific guidance.

- **Human Feedback (`feedback.json`)**: Free-form reviewer comments per eval; empty feedback means the output passed review. Example: "The chart is missing axis labels and the months are in alphabetical order instead of chronological" is actionable; "looks bad" is not.

- **Three Iteration Signals**: Failed assertions (specific gaps), human feedback (broader quality issues), and execution transcripts (why things went wrong — ignored instructions suggest ambiguity; wasted work suggests over-instruction). All three are fed to an LLM with the current SKILL.md to propose improvements.

- **Skill Improvement Principles**: Generalize beyond test cases; keep skills lean (remove instructions if pass rates plateau — may be over-constrained); explain the *why* ("Do X because Y causes Z" outperforms "ALWAYS do X"); bundle repeated helper scripts into `scripts/`.

## Key Takeaways
- Start with just 2–3 test cases; don't over-invest before seeing first results.
- Always run a baseline (no skill or previous version) — absolute pass rates are meaningless without comparison.
- Write assertions *after* seeing first outputs, not before — you don't know what "good" looks like until the skill runs.
- Isolated, clean contexts per run (subagents or fresh sessions) are mandatory for valid evals.
- Track tokens and duration alongside pass rate; a skill adding 13s and improving pass rate by 50 points is worth it, but 2x tokens for +2 points may not be.
- Require concrete evidence (quotes, references) for every PASS — don't grant benefit of the doubt.
- Review assertions themselves during grading: always-pass assertions inflate scores; always-fail ones are broken.
- Use scripts for mechanical checks (JSON validity, counts, dimensions) and LLMs for subjective grading.
- Human review catches issues no assertion anticipated — especially "technically correct but misses the point" outputs.
- Feed failed assertions + human feedback + execution transcripts + current SKILL.md to an LLM for improvement proposals.
- Stop iterating when feedback is consistently empty or improvements plateau.
- The `skill-creator` Skill automates running evals, grading assertions, aggregating benchmarks, and presenting results.

## Notable Quotes
> "Don't worry about defining specific pass/fail checks yet — just the prompts and expected outputs. You'll add detailed checks (called assertions) after you see what the first run produces."

> "Require concrete evidence for a PASS. Don't give the benefit of the doubt. If an assertion says 'includes a summary' and the output has a section titled 'Summary' with one vague sentence, that's a FAIL — the label is there but the substance isn't."

> "Fewer, better instructions often outperform exhaustive rules. If transcripts show wasted work (unnecessary validation, unneeded intermediate outputs), remove those instructions. If pass rates plateau despite adding more rules, the skill may be over-constrained."

> "Reasoning-based instructions ('Do X because Y tends to cause Z') work better than rigid directives ('ALWAYS do X, NEVER do Y'). Models follow instructions more reliably when they understand the purpose."

## Related Entities
[[Agent Skills]], [[SKILL.md]], [[Claude Code]], [[skill-creator Skill]], [[Subagents]], [[LLM-as-Judge]], [[Skill Scripts]], [[Skill Descriptions]]