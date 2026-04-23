# Claude Skills

**Skills** are prompt-based capabilities that load a set of instructions into Claude's context when invoked. They're how you extend Claude Code with reusable, shareable behaviours — either your own or from the community.

A skill is just a markdown file with YAML frontmatter. When you type `/skill-name`, Claude reads the instructions and follows them. Claude can also invoke skills automatically when the task matches the description.

## Skills vs Slash Commands

| | Skills | Slash Commands |
| -------------- | ----------------------------------------- | ------------------------------------------ |
| **Logic** | AI-driven — Claude interprets and acts | Fixed — hardcoded behaviour |
| **Customisable** | Yes — write your own | No |
| **Invoked by** | `/name` or automatically by Claude | `/name` only |
| **Stored in** | `.claude/skills/name/SKILL.md` | Built into the CLI |

> In Claude Code v2.1.3+, custom commands (`.claude/commands/deploy.md`) and skills (`.claude/skills/deploy/SKILL.md`) were merged — both create `/deploy` and work identically.

## Built-in Skills

These ship with Claude Code:

| Skill | What it does |
| ------------------ | ----------------------------------------------------------------- |
| `/simplify` | Reviews recent changes for reuse, quality, and efficiency issues |
| `/review` | Reviews the current PR |
| `/security-review` | Scans pending changes for vulnerabilities |
| `/init` | Scans the project and generates a CLAUDE.md |
| `/loop` | Runs a prompt repeatedly on an interval |
| `/debug` | Structured debugging workflow |
| `/claude-api` | Helps build and optimise Claude API applications |

## Create Your Own Skill

Add a `SKILL.md` file to `.claude/skills/your-skill-name/`:

```markdown
---
name: explain-code
description: Explains code with visual diagrams and analogies. Use when explaining how code works or when the user asks "how does this work?"
allowed-tools: Read Grep
---

When explaining code, always include:

1. Start with an analogy comparing it to something from everyday life
2. Draw an ASCII diagram showing structure or flow
3. Walk through the code step by step
4. Highlight one common gotcha or misconception
```

The `description` field controls when Claude auto-invokes the skill. Make it specific — broad descriptions cause Claude to load the skill too eagerly and waste context.

Add `disable-model-invocation: true` to prevent auto-loading (manual `/name` invocation only).

## Community Skills

- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) — curated list of skills, hooks, commands, and plugins for Claude Code
- [skillsplayground.com](https://skillsplayground.com/guides/claude-code-slash-commands/) — 1,200+ community skills compatible with Claude Code, Cursor, Gemini CLI, and others
- [Extend Claude with skills — Claude Code Docs](https://code.claude.com/docs/en/skills)
