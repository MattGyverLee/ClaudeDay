# Claude Code

Claude Code is Anthropic's official CLI for Claude. It turns your terminal into an AI-powered coding environment.

https://code.claude.com/docs/en/overview 

Claude Code (Technically Cowork) works in a folder and/or a Github Repository. This means it presumably has access to everything in that folder, and as directed, it can get permission to reach/modify things outside of that folder.

### Better Docs

- [Claude Code Everything (Short)](https://x.com/affaanmustafa/status/2012378465664745795)
- [Claude Code Everything (Longform)](https://x.com/affaanmustafa/status/2014040193557471352)

## Starting a Session

1. Open a project folder in VS Code
2. Open the Claude Code panel (Spark icon, top-right)
3. Run `/init` — Claude scans the folder, reads the structure, and writes a `CLAUDE.md` if one doesn't exist
4. Describe your task — Claude will ask for permission before taking any significant action

## CLAUDE.md — Project Memory

`CLAUDE.md` is a markdown file in your project root that Claude reads automatically at the start of every session. It's how you give Claude persistent instructions without repeating yourself.

Create or edit it manually, or run `/init` to have Claude generate one from your project.

Useful things to put in it:

```markdown
## Commands
- Build: `npm run build`
- Test: `npm test`

## Stack
- Python 3.12, Flask
- Postgres via SQLAlchemy

## Conventions
- No comments unless the WHY is non-obvious
- snake_case for all filenames
```

There's also a global `CLAUDE.md` at `~/.claude/CLAUDE.md` for instructions you want in every project (e.g. your preferred tone, languages, or tools).

## Context Management

Claude Code has a finite context window — it fills up as a session grows. When it gets full, quality degrades.

| Command    | When to use                                                                                     |
| ---------- | ----------------------------------------------------------------------------------------------- |
| `/compact` | Mid-session — summarises the conversation and frees space while keeping memory of what was done |
| `/clear`   | Switching to a new unrelated task — wipes the slate entirely                                    |

A good habit: run `/compact` before starting a long task, not after it's already struggling.

## Keyboard Shortcuts

| Shortcut              | Action                      |
| --------------------- | --------------------------- |
| `Enter`               | Submit message              |
| `Shift+Enter`         | New line without submitting |
| `Escape`              | Cancel current operation    |
| `Alt+K` / `Option+K` | @-mention a file            |
| `↑`                   | Edit previous message       |

Shortcuts are fully customisable via `~/.claude/keybindings.json`.

## Essential Slash Commands

| Command | Description |
|---------|-------------|
| `/help` | Claude Code Help |
| `/` | List commands |
| `/init` | Tells Claude to scan the folder and get oriented. |
| `/usage` | How many credits have you used? |
| `/compact` | Summarize and compact the memory (usually before a task) |
| `/clear` | Resets the conversation to save context tokens when switching tasks. |
| `/diff` | Opens an interactive viewer to review all code changes before they are committed, helping catch errors early. |
| `/simplify` | A bundled skill that automatically reviews recent changes for code reuse, quality issues, and efficiency improvements. |
| `/security-review` | Analyzes pending changes for vulnerabilities like injection or auth issues before shipping |
| `/model` | Auto, Haiku, Sonnet, Opus |
| `/effort` | Choose an effort level. (Higher is better, slower, more expensive.) |
| `/remote-control` | Pick up work on your phone or Claude Web. |
| `/rewind` | Take the code back to where it was. Mouse over a chat you sent and click the arrow to rewind the code to where it was before that message. |

## @ Commands

You can reference specific files with @, or paste the relative or absolute paths.

## Permission Modes

Claude Code asks for permission before taking actions. You can configure allowed tools in `.claude/settings.json`.

```json
{
  "permissions": {
    "allow": ["Bash(npm:*)", "Bash(git:*)"]
  }
}
```


## Links

- [Claude Code tips & tricks (Security)](https://x.com/affaanmustafa/status/2033263813387223421)
