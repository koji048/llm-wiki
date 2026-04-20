---
title: Obsidian Local Vault Setup
created: 2026-04-20
updated: 2026-04-20
type: meta
tags: [meta, obsidian, setup]
---

# Obsidian Local Vault Setup

## Overview
The LLM Wiki lives at `/root/llm-wiki` on the VPS (187.127.110.63) and syncs to GitHub.
Your Mac pulls from GitHub into a local folder (suggest keeping it in Google Drive for cross-device backup).
Obsidian opens that folder as a vault.

## Step 1: Pull the wiki to your Mac

```bash
# Clone the wiki to a Google Drive-synced location
git clone https://github.com/koji048/llm-wiki.git ~/Google Drive/MyMac/llm-wiki

# Or if already cloned elsewhere, pull latest:
# cd ~/Google\ Drive/MyMac/llm-wiki && git pull
```

## Step 2: Open as Obsidian Vault

1. Open Obsidian on your Mac
2. Click **Open** → navigate to `~/Google Drive/MyMac/llm-wiki`
3. The vault opens — you'll see the full directory structure

## Step 3: Recommended Obsidian Settings

**Core plugins:**
- Templates — for frontmatter consistency
- Daily notes — optional
- Starred items — for quick access

**Community plugins (install from Settings → Community Plugins):**
- **Dataview** — query wiki pages with SQL-like syntax
- **Web Frame** — optionally embed the Tum Office UI
- **Templater** — advanced frontmatter templates

**Settings:**
- Core Plugins → Templates: set template folder to `queries/` or a `templates/` dir
- Core Plugins → Use wikilinks (enabled by default)

## Step 4: Syncing VPS edits to Mac

VPS pushes to GitHub automatically. On your Mac:

```bash
# Option A: Manual pull
cd ~/Google\ Drive/MyMac/llm-wiki && git pull

# Option B: Set up a git alias for quick sync
alias wiki-pull='cd ~/Google\ Drive/MyMac/llm-wiki && git pull'

# Option C: Use a git hooks to auto-pull (advanced)
# Add a post-pull hook in .git/hooks/
```

Or use the **Obsidian Git** community plugin to pull/push from within Obsidian itself.

## Step 5: Configure Obsidian for the Wiki

Create `.obsidian/workspace` in the vault to store Obsidian-specific settings (these are local-only and should NOT be pushed to git — add `.obsidian/workspace` to `.gitignore` if it exists).

## File Structure

```
llm-wiki/
├── SCHEMA.md           # Wiki conventions — read this first
├── index.md            # Content catalog — start here
├── log.md              # Chronological action log
├── raw/                # Source material (LLM never edits this)
│   ├── articles/
│   ├── papers/
│   ├── transcripts/
│   └── assets/
├── entities/           # People, companies, products
├── concepts/           # Topics, techniques, architectures
├── comparisons/        # Side-by-side analyses
└── queries/            # Filed query results worth keeping
```

## Key Conventions
- Every page has YAML frontmatter (title, created, updated, type, tags)
- Use `[[wikilinks]]` to link pages — minimum 2 outbound links per page
- File names: lowercase, hyphens, no spaces
- See [[SCHEMA.md]] for full conventions

## Troubleshooting

**Wiki pages not showing in Obsidian graph:**
- Make sure `.md` files have frontmatter
- Graph view only shows pages with wikilinks

**Git conflicts after editing on both Mac and VPS:**
- Obsidian Git plugin can help manage this
- Best practice: VPS makes edits → pushes → Mac pulls before editing
