---
title: Pixel Agents
description: A VS Code extension (6.9k stars) that renders multi-agent AI sessions as a pixel art office. Agents are pixel characters that walk, sit, type, and show speech bubbles. Observes Claude Code JSONL transcripts directly — no modifications to Claude Code needed.
source: https://github.com/pablodelucca/pixel-agents
tags: [pixel-art, multi-agent, visual-debugging, claude-code, game-loop, bfs-pathfinding, vscode-extension, status-detection]
related: [garry-gstack, tum-office, openclaw, anthropic-agent-skills]
---

# Pixel Agents

**Pixel Agents** (github.com/pablodelucca/pixel-agents) is a VS Code extension that turns multi-agent AI sessions into a pixel art office you can watch in real-time. 6.9k stars, 1k forks, active development with 34 open PRs as of April 2026.

Each AI agent becomes a pixel character in a 2D office. Characters walk to desks, sit down, animate based on their current tool (typing when writing code, reading when searching files, running when executing commands), and show speech bubbles when waiting for input or permission.

## Core Architecture

### The Observational Pattern

Pixel Agents **never modifies Claude Code**. It reads the JSONL transcript files that Claude Code writes to disk, parses them line-by-line, and maps the activity to character animations.

```
Claude Code → JSONL transcript file → fileWatcher → transcriptParser → webview → Canvas2D render
```

This is the key architectural insight: **observational parsing** rather than tightly coupled integration. The extension subscribes to file changes on the JSONL file and re-parses from the last known byte offset.

### JSONL Record Types

`transcriptParser.ts` handles 6 record types from Claude Code's output:

| Record Type | Signal |
|---|---|
| `assistant` (with `type: 'tool_use'`) | Tool call started — animate agent active |
| `assistant` (text only, no tools) | Text response — start idle timer |
| `user` (with `type: 'tool_result'`) | Tool completed — clear tool state |
| `progress` (nested under Task/Agent) | Sub-agent tools — propagate to child character |
| `system` (`subtype: 'turn_duration'`) | Authoritative turn-end — mark waiting |
| `queue-operation` (`operation: 'enqueue'`) | Background agent completed |

The `turn_duration` system event is the **authoritative turn-end signal**. Without it (text-only turns), a heuristic `TEXT_IDLE_DELAY_MS = 5000` timer fires as fallback.

### Dual-Mode Status Detection

Pixel Agents acknowledges the fundamental problem: Claude Code's JSONL format doesn't provide a clear "agent is waiting for you" signal. It handles this two ways:

```
HOOKS MODE (Claude Code hooks installed):
  PreToolUse         → instant tool visualization
  Notification(permission_prompt) → instant permission bubble
  Stop               → instant waiting state
  → hookDelivered = true, all heuristic timers SUPPRESSED

HEURISTIC MODE (no hooks):
  Tool starts → start PERMISSION_TIMER_DELAY_MS = 7000ms
  Text silence → start TEXT_IDLE_DELAY_MS = 5000ms
  turn_duration → mark waiting
  → acknowledged misfire rate
```

The `hookDelivered: boolean` flag on `AgentState` is the routing switch. When `true`, every heuristic timer is skipped. This is implemented as:

```typescript
if (hasNonExemptTool && !agent.hookDelivered && !agent.leadAgentId) {
  startPermissionTimer(agentId, agents, permissionTimers, ...);
}
if (!agent.hookDelivered) {
  startWaitingTimer(agentId, TEXT_IDLE_DELAY_MS, ...);
}
```

The constants from `server/src/constants.ts`:
- `TOOL_DONE_DELAY_MS = 300` — prevents UI flicker on rapid tool transitions
- `PERMISSION_TIMER_DELAY_MS = 7000` — heuristic: time before showing permission bubble
- `TEXT_IDLE_DELAY_MS = 5000` — heuristic: silence before text-only turn is marked complete
- `CLEAR_IDLE_THRESHOLD_MS = 2000` — heuristic: idle threshold for `/clear` detection

### Sub-Agent Lifecycle

Task/Agent tool calls spawn sub-agent characters. The lifecycle:

```
Agent/Tool tool_start → agentToolStart (parent)
  → spawn subagent character with NEGATIVE character ID
  → subagentMeta[characterId] = { parentAgentId, parentToolId }
  SubagentToolStart (nested sub-tools)
Agent/Task tool_done → subagentClear (children hidden)
run_in_background=true → stays alive until queue-operation event
```

The ID mapping uses negative integers for sub-agents:
```typescript
subagentIdMap: Map<string, number> = new Map();  // "parentId:toolId" → negative charId
subagentMeta: Map<number, { parentAgentId: number; parentToolId: string }>;
nextSubagentId = -1;  // decrements for each sub-agent
```

Background agents (`run_in_background=true`) are kept alive via a `backgroundAgentToolIds: Set<string>` that is only cleared on `queue-operation` events.

### Agent Teams

When Claude Code's Team feature is used (`TeamCreate` tool), the extension detects team membership via `teamName` and `agentName` fields in the JSONL. The lead is the agent with no `agentName`. Teammates get `leadAgentId` pointing to the lead.

### Character State Machine

`CharacterState` enum: `idle → walk → type → read → run → error → waiting`

Pathfinding uses **BFS** on a tile map. Characters:
1. Receive a `seatId` assignment (auto-assigned on spawn)
2. Walk to the seat using BFS (`findPath()`)
3. Snap to seat when idle
4. Play animation frames based on active tool (type/read/run/idle)

### Canvas 2D Rendering

The webview (`OfficeCanvas.tsx`) runs a game loop using `requestAnimationFrame`. All game state lives outside React (`officeStateRef`) — updated imperatively by message handlers, with React re-rendering only for UI chrome.

### Asset Manifest System

Furniture is defined via `manifest.json` in each item's folder. No code changes needed to add new furniture — just add a folder with PNG sprites and a manifest.

```json
{
  "id": "MY_DESK",
  "type": "group",
  "groupType": "rotation",
  "rotationScheme": "2-way",
  "members": [
    { "type": "asset", "id": "MY_DESK_FRONT", "orientation": "front" },
    { "type": "asset", "id": "MY_DESK_SIDE",  "orientation": "side" }
  ]
}
```

Supports: single assets, rotation groups (2-way, 3-way-mirror, 4-way), state groups (on/off), animation groups. External asset directories load and merge into the palette automatically at runtime.

## Tech Stack

- **Extension host**: TypeScript, VS Code Webview API, esbuild
- **Webview**: React 19, TypeScript, Vite, Canvas 2D
- **Build**: `npm run build` compiles both extension and webview

## Known Limitations

- **Agent-terminal desync** — agents can desync from terminals, especially when rapidly opened/closed or restored across sessions
- **Heuristic misfire rate** — without hooks, the status detection frequently misfires. Agents may briefly show wrong status or miss transitions. This is acknowledged explicitly in the README.
- **Linux/macOS bare `code` launch** — agents start in `~` instead of a project directory

## Relevance to Tum Office

### Borrow Immediately

1. **Dual-mode detection** — OpenClaw hooks as authoritative path, heuristic timer as fallback. Replace the current fragile Tum Office bridge.
2. **Sub-agent parent/child ID map** — `subagentMeta` pattern for tracking specialist bots spawned by Lisa.
3. **Token usage tracking** — accumulate `inputTokens` + `outputTokens` from transcript for cost visibility.
4. **Asset manifest approach** — modular furniture config for Tum Office desk layouts.
5. **Turn-end signal strategy** — `turn_duration` / `TEXT_IDLE_DELAY_MS` pattern solves the exact problem Tum Office has.
6. **Sound notifications** — Pixel Agents has a chime when agents finish turns. Tum Office has no audio.
7. **Character hue shifting** — each character gets a slightly different hue (`HUE_SHIFT_MIN_DEG` to `HUE_SHIFT_MIN_DEG + HUE_SHIFT_RANGE_DEG` degrees) for visual diversity.

### Don't Copy

- Pixel art rendering (Tum Office is 3D)
- VS Code extension hosting model
- JSONL file polling approach (OpenClaw has a different event model — hooks, not file watching)

## Source Files

- `src/transcriptParser.ts` — JSONL parsing, tool detection, sub-agent lifecycle
- `src/agentManager.ts` — agent creation and state management
- `src/timerManager.ts` — idle/active/error timer state machine
- `src/types.ts` — `AgentState` interface
- `src/fileWatcher.ts` — JSONL file watching
- `src/assetLoader.ts` — external asset directory loading
- `webview-ui/src/office/engine/officeState.ts` — game state, character management
- `server/src/constants.ts` — all timing constants
- `docs/external-assets.md` — asset manifest format
