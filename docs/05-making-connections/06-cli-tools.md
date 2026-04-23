# CLI Tools

CLIs let Claude (and you) interact with external services directly from the terminal, without a browser or GUI. When Claude can run a CLI, it becomes a direct agent over that service.

## Why CLIs Matter for AI Workflows

Claude Code can run any CLI that's on your PATH. That means if you have `gh` installed, Claude can create PRs, query issues, and manage branches — without needing a GitHub MCP server. CLIs are often simpler to set up than MCP servers for one-off tasks.

## Essential CLIs

### gh — GitHub CLI

```bash
# Install
winget install GitHub.cli        # Windows
brew install gh                  # Mac

# Authenticate
gh auth login
```

What Claude can do with it: create and review PRs, manage issues, search code, trigger workflows, clone repos. The most useful CLI for day-to-day coding work.

[cli.github.com](https://cli.github.com)

---

### Notion CLI

```bash
npm install -g notion-cli-js
notion auth
```

Lets Claude read and write Notion pages, query databases, and create content — useful for documentation workflows where your notes live in Notion.

[notion-cli on npm](https://www.npmjs.com/package/notion-cli-js)

---

### Stripe CLI

```bash
winget install Stripe.StripeCLI  # Windows
brew install stripe/stripe-cli/stripe

stripe login
```

Lets Claude trigger test webhooks, inspect events, and tail logs. Useful when building or debugging payment integrations.

[stripe.com/docs/stripe-cli](https://stripe.com/docs/stripe-cli)

---

### Supabase CLI

```bash
npm install -g supabase
supabase login
```

Local database development, migrations, and edge function deployment. Claude can apply schema changes, seed data, and inspect tables without leaving the terminal.

[supabase.com/docs/guides/cli](https://supabase.com/docs/guides/cli)

---

### Vercel CLI

```bash
npm install -g vercel
vercel login
```

Deploy and manage Vercel projects. Claude can trigger deployments, inspect build logs, and manage environment variables.

[vercel.com/docs/cli](https://vercel.com/docs/cli)

---

### AWS CLI

```bash
winget install Amazon.AWSCLI     # Windows
brew install awscli              # Mac

aws configure
```

The broadest service coverage of any CLI here. Claude can query S3, manage Lambda functions, inspect CloudWatch logs, and more. Powerful but requires care — scope IAM permissions tightly.

[docs.aws.amazon.com/cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

---

## AI Coding CLIs

These are peers to Claude Code — alternative AI agents in the terminal worth knowing:

| Tool | Model | Notable for |
| ------------ | --------------- | --------------------------------------------- |
| **Aider** | Any (GPT, Claude, Ollama) | Git-native, clean commit history, open source |
| **Gemini CLI** | Gemini | Only tool with a usable free tier |
| **Codex CLI** | GPT-4o | OpenAI's terminal agent |
| **OpenCode** | Any | Flexible model choice, open source |

## Tips

- Any CLI on your PATH is available to Claude — just ask it to use the tool by name
- Scope credentials tightly: give Claude the minimum permissions needed for the task
- Use `--dry-run` or `--preview` flags when available before Claude executes destructive commands

## Find More

- [10 Must-have CLIs for AI Agents — unicodeveloper on Medium](https://medium.com/@unicodeveloper/10-must-have-clis-for-your-ai-agents-in-2026-51ba0d0881df)
- [clihub.ai](https://clihub.ai/blog/best-cli-tools) — directory of developer CLIs
