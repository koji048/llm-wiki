# Optimizing skill descriptions - Agent Skills

---
title: "Optimizing Skill Descriptions"
created: 2026-04-25
type: entity
tags: [agent-skills, prompt-engineering, evaluation, skill-creation, claude]
related: [[Agent Skills]], [[SKILL.md Specification]], [[Progressive Disclosure]], [[Skill-Creator Skill]], [[Evaluating Skill Output Quality]]
sources: [raw/articles/skill-creation-optimizing-descriptions.md]
---

# Optimizing Skill Descriptions

## Summary
Agent Skills use the `description` field in the `SKILL.md` frontmatter as the sole signal agents use at startup to decide whether a skill is relevant to a user task. Because agents apply progressive disclosure — loading only skill names and descriptions initially, then pulling the full `SKILL.md` into context when a match occurs — the description bears the entire burden of triggering. Under-specified descriptions cause missed activations (false negatives); over-broad descriptions cause spurious activations (false positives). The specification enforces a hard **1024-character limit** on descriptions.

This guide, published at agentskills.io, lays out a systematic optimization methodology: write descriptions in imperative form focused on user intent, build a labeled eval set of ~20 realistic queries (balanced between `should_trigger: true` and `should_trigger: false`), run each query 3 times to account for nondeterminism, compute trigger rates with a 0.5 threshold, and iterate using a **train/validation split (~60/40)** to avoid overfitting. The best iteration is selected by validation pass rate — which may not be the final iteration. The `skill-creator` skill automates the loop end-to-end with parallel evaluation, Claude-driven description proposals, and a live HTML report.

A key nuance: agents typically only consult skills for tasks requiring specialized knowledge or capabilities beyond basic tooling. A trivial request like "read this PDF" may not trigger a PDF skill regardless of description quality, because the agent handles it directly.

## Key Concepts

- **Progressive Disclosure**: Agents load only skill names and descriptions at startup to conserve context. Full `SKILL.md` content is only read into context when a task matches a description. This architecture makes description quality the decisive factor in skill activation.

- **Imperative Phrasing**: Descriptions should instruct the agent ("Use this skill when…") rather than describe the skill ("This skill does…"). The agent is making an action decision, so the description should be framed as an action trigger.

- **User-Intent Framing**: Describe what the user is trying to achieve, not the skill's internal mechanics. Matching happens against user requests, not implementation details. Include "pushy" language listing contexts where the skill applies even if the user doesn't name the domain (e.g., "even if they don't explicitly mention 'CSV' or 'analysis'").

- **Trigger Eval Queries**: A labeled dataset (JSON) of realistic user prompts with `should_trigger` booleans. Recommended size is ~20 queries, balanced 8-10 positive / 8-10 negative. Queries should vary in phrasing (formal/casual/typos), explicitness, detail level, and complexity.

- **Near-Miss Negative Examples**: The most valuable `should_trigger: false` cases share keywords or concepts with the skill but require something different. Example for CSV analysis skill: "update formulas in my Excel budget spreadsheet" (Excel editing, not CSV analysis) or "python script that reads a csv and uploads each row to postgres" (ETL, not analysis). Weak negatives like "what's the weather today?" test nothing.

- **Realism Signals**: Real user prompts include file paths (`~/Downloads/report_final_v2.xlsx`), personal context ("my manager asked me to…"), specific details (column names), and casual/typo-laden language. Generic test queries miss these.

- **Trigger Rate**: Fraction of runs where the skill was invoked for a given query. Because model behavior is nondeterministic, each query is run multiple times (default **3 runs**). A query passes if its trigger rate is above 0.5 for positives or below 0.5 for negatives. 20 queries × 3 runs = 60 invocations per eval pass.

- **Train/Validation Split**: Queries are split ~60% train / ~40% validation, with proportional positive/negative mixes and a fixed random split across iterations. Only train failures guide description revisions; validation is held out to detect overfitting. The best iteration is chosen by validation pass rate.

- **Overfitting in Description Optimization**: Adding specific keywords from failed train queries is overfitting. The prescribed remedy is to identify the general category or concept behind failing queries and address that. If stuck after several iterations, try a structurally different description rather than incremental tweaks.

- **Detection Logic (Claude Code example)**: The provided bash script uses `claude -p "$query" --output-format json` and `jq` to detect tool_use events where `.name == "Skill"` and `.input.skill == $skill`. Early stopping once skill consultation is clear can cut time/cost.

- **Skill-Creator Skill**: An automation skill that splits the eval set, evaluates trigger rates in parallel, proposes description improvements via Claude, and emits a live HTML report during the run.

- **1024-Character Limit**: A hard spec-enforced cap on description length. Descriptions tend to grow during optimization, so the limit must be re-checked each iteration.

## Key Takeaways
- The `description` field is the sole trigger mechanism — it is progressively disclosed ahead of the full `SKILL.md`.
- Aim for ~20 labeled eval queries, balanced 8-10 positive and 8-10 negative, with strong near-miss negatives.
- Run each query at least 3 times; use 0.5 as the trigger-rate pass threshold.
- Use a ~60/40 train/validation split with proportional class balance, kept fixed across iterations to enable fair comparisons.
- Select the best description by validation pass rate, not by the final iteration.
- Five optimization iterations is typically sufficient; lack of progress often indicates bad queries (too easy/hard/mislabeled), not a bad description.
- Descriptions must stay under 1024 characters; they should use imperative phrasing, focus on user intent, and explicitly cover cases where the user doesn't name the domain.
- After selecting, validate with 5-10 fresh, unseen queries for an honest generalization check.
- Agents may skip skills even with perfect description matches if the task is simple enough to handle without specialized capability.

## Notable Quotes
> "A skill only helps if it gets activated. The description field in your SKILL.md frontmatter is the primary mechanism agents use to decide whether to load a skill for a given task."

> "An under-specified description means the skill won't trigger when it should; an over-broad description means it triggers when it shouldn't."

> "Avoid adding specific keywords from failed queries — that's overfitting. Instead, find the general category or concept those queries represent and address that."

> "The best description may not be the last one you produced; an earlier iteration might have a higher validation pass rate than later ones that overfit to the train set."

## Related Entities
[[Agent Skills]], [[SKILL.md Specification]], [[Progressive Disclosure]], [[Skill-Creator Skill]], [[Claude Code]], [[Evaluating Skill Output Quality]], [[Train-Validation Split]]