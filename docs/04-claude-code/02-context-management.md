# Managing Context in Claude Code

Context is the single biggest lever in Claude Code. A clean, focused context means faster responses, lower cost, and better decisions. A bloated one means drift, repetition, and degraded output.

The goal isn't to maximise how much Claude remembers — it's to **forget with precision**.

---

## Choosing a Model

Run `/model` to switch at any time during a session.

| Model | Best for | Cost |
| ----------- | --------------------------------------------------- | ------------ |
| Haiku 4.5 | Mechanical work — renaming, formatting, boilerplate | Cheapest |
| Sonnet 4.6 | Daily driver — coding, analysis, multi-file work | Mid |
| Opus 4.7 | Complex debugging, architecture, hard reasoning | Most capable |

**Practical rule:** default to Sonnet. Switch to Opus when you hit a wall. Use Haiku for bulk or repetitive tasks where quality isn't critical.

### Hybrid mode: opusplan

```
/model opusplan
```

Opus plans, Sonnet executes. Claude uses Opus for reasoning and architecture decisions, then automatically switches to Sonnet for code generation. Saves ~40% on cost vs running Opus throughout.

### 1M token context window

For very large codebases, append `[1m]` to switch to the million-token variant:

```
/model opus[1m]
/model sonnet[1m]
```

Use this sparingly — larger context = more tokens processed per response = higher cost.

---

## Manual Context Control

| Command    | When to use                                                            |
| ---------- | ---------------------------------------------------------------------- |
| `/compact` | Mid-session — compresses history, preserves decisions, frees up space  |
| `/clear`   | Switching tasks — wipes the slate entirely, fresh context              |

**A key habit:** run `/compact` *before* starting a long task, not after it's already degrading.

Auto-compaction kicks in when the window fills up, but you get better results guiding it manually with instructions (see below).

---

## Guiding Compaction via CLAUDE.md

Claude's auto-compactor reads your `CLAUDE.md` for instructions on what to preserve. Add a section like this:

```markdown
# Compact instructions

When compacting, always preserve:
- The current task objective and acceptance criteria
- Every file path that has been read or modified
- Test results and error messages
- Decisions made and the reasoning behind them
```

The compactor matches on intent — the heading name doesn't have to be exact.

---

## Re-inject Context After Compaction

If you have critical reminders that must survive compaction (sprint context, tool preferences, naming conventions), use a `SessionStart` hook with a `compact` matcher in `.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "compact",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Use pip, not conda. Run pytest before committing. Current task: survey data pipeline.'"
          }
        ]
      }
    ]
  }
}
```

Anything the command writes to stdout gets injected back into context automatically after each compaction.

---

## Agents with Smaller Contexts

Subagents are the most powerful context management tool. Delegating a research or investigation task to a subagent means the exploration happens in a *separate* context window, keeping your main session clean for implementation.

Prompt patterns that spawn subagents:

- `"Use a subagent to investigate X and report back"`
- `"Spawn an agent to search the codebase for all uses of Y"`
- `"Use an agent to run the tests and summarise the failures"`

**Agent team cost tip:** each teammate has its own context window. Keep spawn prompts focused, use Sonnet for teammates (not Opus), and clean up teams when work is done.

---

## External Memory

For anything that must persist *across* sessions — not just compactions — write it to a file.

**Options:**

| Approach | How |
| ----------------------------- | ----------------------------------------------- |
| `CLAUDE.md` | Project-level instructions, loaded every session |
| `~/.claude/CLAUDE.md` | Global instructions across all projects |
| Notes file (`notes.md`, etc.) | Ask Claude to write decisions/progress here |
| `.claude/rules/*.md` | Scoped rules loaded only for matching file paths |

A practical pattern: end long sessions by asking Claude to write a short handoff note to `notes.md` summarising what was done, what's next, and any open questions. Start the next session by reading it.

---

## Sources

- [Best Practices — Claude Code Docs](https://code.claude.com/docs/en/best-practices)
- [Context Compaction — Claude API Docs](https://platform.claude.com/docs/en/build-with-claude/compaction)
- [Model Configuration — Claude Code Docs](https://code.claude.com/docs/en/model-config)
- [Memory Management in Claude Code — DEV Community](https://dev.to/vilvaathibanpb/memory-management-in-claude-code-context-pipeline-1j1p)
