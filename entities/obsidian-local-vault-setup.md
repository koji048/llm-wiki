# Obsidian Local Vault Setup

---
title: "Obsidian Local Vault Setup for LLM Wiki"
created: 2026-04-21
type: entity
tags: [obsidian, vault-setup, git-sync, workflow, knowledge-management]
related: [[LLM Wiki]], [[SCHEMA.md]], [[Obsidian Git Plugin]], [[Dataview]]
sources: [raw/articles/obsidian-local-vault-setup.md]
---

# Obsidian Local Vault Setup for LLM Wiki

## Summary
This entry documents the workflow for mirroring the LLM Wiki — which lives canonically at `/root/llm-wiki` on a VPS at IP `187.127.110.63` — to a local Mac environment via GitHub and opening it as an Obsidian vault. The recommended pattern is: VPS authors content → pushes to GitHub (`https://github.com/koji048/llm-wiki.git`) → Mac pulls into a Google Drive-synced directory (`~/Google Drive/MyMac/llm-wiki`) → Obsidian opens that directory as a vault. Google Drive placement provides an additional cross-device backup layer on top of git.

The setup requires `git clone`, Obsidian installation, and configuration of both core and community plugins. Key community plugins include **Dataview** (SQL-like querying over vault pages), **Web Frame** (embeds external UIs like the Tum Office UI), **Templater** (advanced templating), and **Obsidian Git** (in-editor pull/push). Core plugins to enable: Templates, Daily notes (optional), and Starred items. Wikilinks are enabled by default.

Sync strategies offered are manual (`git pull`), aliased (`wiki-pull` shell alias), automated via git hooks, or integrated via the Obsidian Git plugin. The `.obsidian/workspace` file stores local Obsidian UI state and should be gitignored to prevent conflicts across machines. The recommended conflict-avoidance rule is unidirectional editing: VPS edits → push → Mac pulls before any local edits.

## Key Concepts

- **Canonical VPS Source**: The authoritative copy of the wiki resides at `/root/llm-wiki` on VPS `187.127.110.63`. The VPS automatically pushes changes to GitHub, making GitHub the synchronization hub rather than the source of truth.

- **Google Drive-Synced Clone**: Cloning into `~/Google Drive/MyMac/llm-wiki` gives double redundancy — git history plus Google Drive's own versioning and cross-device mirroring. This is the suggested (not required) location.

- **Obsidian Vault**: Any directory opened in Obsidian becomes a vault. The vault surfaces the entire wiki directory tree (raw/, entities/, concepts/, comparisons/, queries/) as navigable, linkable markdown.

- **Dataview Plugin**: A community plugin that allows SQL-like queries against frontmatter fields and inline metadata across the vault. Essential for leveraging the structured YAML frontmatter mandated by the wiki schema.

- **Obsidian Git Plugin**: Community plugin that executes git pull/push from within Obsidian's UI, eliminating terminal context-switching and helping manage merge conflicts between VPS and Mac edits.

- **Templater / Templates**: Templater is a community plugin for advanced templating; the Core "Templates" plugin handles basic frontmatter consistency. The template folder should be pointed at `queries/` or a dedicated `templates/` directory.

- **Web Frame Plugin**: Community plugin for embedding external web UIs (e.g., the Tum Office UI referenced in the source) directly as panes inside Obsidian.

- **`.obsidian/workspace` Gitignore Rule**: This file stores per-machine Obsidian UI state (open tabs, pane layout). It must be gitignored to prevent constant churn and conflicts between Mac and VPS vault state.

- **Wiki Directory Structure**: Fixed layout — `SCHEMA.md` (conventions), `index.md` (catalog), `log.md` (chronological log), `raw/` (immutable source material with articles/papers/transcripts/assets subdirs), `entities/`, `concepts/`, `comparisons/`, `queries/`.

- **Frontmatter + Wikilinks Convention**: Every page requires YAML frontmatter (title, created, updated, type, tags) and a minimum of 2 outbound `[[wikilinks]]`. Filenames are lowercase, hyphenated, no spaces. Graph view only renders pages that contain wikilinks.

- **Unidirectional Edit Discipline**: To avoid merge conflicts, the recommended workflow is VPS edits → push → Mac pulls → (optional Mac edits → push → VPS pulls). Bidirectional simultaneous editing invites conflicts resolvable via Obsidian Git.

## Key Takeaways
- The wiki's canonical location is `/root/llm-wiki` on VPS `187.127.110.63`; GitHub (`github.com/koji048/llm-wiki`) is the sync hub.
- Clone to `~/Google Drive/MyMac/llm-wiki` on Mac for Google Drive + git dual redundancy.
- Install Dataview, Web Frame, Templater, and optionally Obsidian Git as community plugins; enable Templates and Starred items as core plugins.
- Add `.obsidian/workspace` to `.gitignore` — it's per-machine UI state and causes conflicts if tracked.
- Use a shell alias like `alias wiki-pull='cd ~/Google\ Drive/MyMac/llm-wiki && git pull'` for quick sync, or use the Obsidian Git plugin for in-editor sync.
- Graph view only displays pages with wikilinks and frontmatter — at least 2 outbound wikilinks per page is the standard.
- Filenames must be lowercase-hyphenated; every page requires YAML frontmatter with title, created, updated, type, and tags.
- Prefer unidirectional edits (VPS → Mac) to sidestep merge conflicts.

## Notable Quotes
> "The LLM Wiki lives at `/root/llm-wiki` on the VPS (187.127.110.63) and syncs to GitHub."
> "Graph view only shows pages with wikilinks."
> "Best practice: VPS makes edits → pushes → Mac pulls before editing."

## Related Entities
[[LLM Wiki]], [[SCHEMA.md]], [[Obsidian Git Plugin]], [[Dataview]], [[Templater]], [[GitHub]], [[Google Drive]]

## Tags
obsidian, vault-setup, git-sync, knowledge-management, workflow, dataview, plugins, vps