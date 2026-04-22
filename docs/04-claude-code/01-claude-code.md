# Claude Code

Claude Code is Anthropic's official CLI for Claude. It turns your terminal into an AI-powered coding environment.

https://code.claude.com/docs/en/overview 

Claude Code (Technically Cowork) works in a folder and/or a Github Repository. This means it presumably has access to everything in that folder, and as directed, it can get permission to reach/modify things outside of that folder.

### Better Docs

- [Claude Code Everything (Short)](https://x.com/affaanmustafa/status/2012378465664745795)
- [Claude Code Everything (Longform)](https://x.com/affaanmustafa/status/2014040193557471352)

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
