---
title: llm-automation-modes
created: 2026-04-21
updated: 2026-04-21
type: comparison
tags: [agent, tool-use, automation, workflow]
sources: [https://gist.github.com/karpathy/1dd0294ef9567971c1e4348a90d69285, https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f]
---

# llm-automation-modes

Two modes of letting an LLM do the grunt work: fully automated (no human in loop) vs. interactive (human in loop per action).

| Dimension | Automated (cron pipeline) | Interactive (gcm) |
|---|---|---|
| **Example** | VPS cron job: YouTube VTT → entity page → git push | `gcm()`: staged diff → commit message → accept/edit/regenerate/cancel |
| **Human in loop** | None (runs while you sleep) | Per-action: approve before committing |
| **Latency** | Minutes to hours (next cron run) | Seconds (immediate) |
| **Risk** | Low — wiki is append-mostly, commits auto-reviewed by you when you pull | Medium — wrong commit message can be misleading |
| **Best for** | High-volume, low-stakes bookkeeping (transcript ingestion, page updates) | One-shot, irreversible actions (git commits, production deployments) |
| **Trust model** | Trust the pipeline, review the output | Verify per action before proceeding |
| **Automation level** | Full — no user present at all | Partial — LLM drafts, human decides |

## Shared Philosophy

Both stem from Karpathy's principle: **LLMs don't get bored, don't forget, can touch many files in one pass.**

The human's job is curation and direction. The LLM's job is everything else.

> LLM Wiki pattern: Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.
> gcm: the LLM writes the commit message; you review and accept.

## When to Use Which

**Use automated (cron) when:**
- High volume of similar tasks (our YouTube → wiki pipeline processes every new VTT)
- You can review the output in aggregate later (pull the wiki, scan new pages)
- The action is reversible or append-only (wiki pages can be updated, git commits can be amended)
- No judgment required — just pattern-matching and summarizing

**Use interactive (gcm-style) when:**
- The action is one-shot and hard to undo (a commit lives in history, a deployed config can't be un-deployed)
- Context varies a lot per action (every diff is different, every commit message must fit the moment)
- You'd want to course-correct mid-process (edit before committing vs. fixing later)

## Our Pipeline: Automated LLM Wiki Compounding

The VPS cron job at `58f234c649b9` exemplifies the automated mode:

- `yt-dlp` fetches VTT on Mac → moved to `raw/transcripts/`
- Git push → VPS pull
- `process_transcripts.py` reads VTT, calls OpenRouter (Opus 4.7) to generate entity pages
- Entity pages written to `entities/`, index and log updated
- `git add -A && git commit && git pull --rebase && git push`

You pull the updated wiki in Obsidian whenever you want to review. No action required during the pipeline run.

## The gcm Shell Function

A concrete example of the interactive mode:

```bash
gcm() {
    generate_commit_message() {
        git diff --cached | llm \
        "Below is a diff of all staged changes... Please generate a concise, one-line commit message."
    }
    # Loop: accept / edit / regenerate / cancel
}
```

Key insight: **even a 60-line shell function implements the LLM-as-grunt-worker pattern.** No framework, no complex agent loop. Just: pipe to LLM, present output to human, let human decide.

## Conclusion

The right mode depends on reversibility and stakes. Our wiki uses automated for ingestion because it's append-only and reviewable later. `gcm` uses interactive because a bad commit message pollutes git history.

Both are expressions of the same underlying idea: let the LLM handle the tedious bookkeeping, keep the human in the loop for decisions that matter.

## Related

- [[karpathy-llm-wiki]] — the pattern both modes derive from
- [[microgpt]] — from-scratch GPT implementation showing the full algorithm in minimal form
