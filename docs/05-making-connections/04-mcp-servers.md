# MCP Servers

**MCP (Model Context Protocol)** is an open standard from Anthropic that lets Claude connect to external tools, data sources, and services through a single unified interface. Think of it as a USB standard for AI — one protocol, any tool.

MCP servers are client-agnostic: the same server works with Claude Code, Claude Desktop, Cursor, and any other compliant host.

Each MCP server exposes a set of **tools** (actions Claude can call) and optionally **resources** (data Claude can read). Claude decides when to use them based on your prompt.

## Add an MCP Server

```bash
# Remote server over HTTP
claude mcp add --transport http notion https://mcp.notion.com/mcp

# Local server via npx
claude mcp add --transport stdio airtable \
  --env AIRTABLE_API_KEY=YOUR_KEY \
  -- npx -y airtable-mcp-server

# List configured servers
claude mcp list

# Remove a server
claude mcp remove github
```

## Context Warning

Loading MCP servers fills your context window even when you're not actively using them. Claude Code's **MCP Tool Search** feature (lazy loading) reduces this impact by up to 95% — only loading tool definitions when needed.

Only add servers relevant to the current task.

## Top MCP Servers

| Server | What it does |
| --------------- | ------------------------------------------------------------------ |
| **Context7** | Pulls up-to-date library documentation into context on demand. Ask Claude about any framework and it fetches the actual current docs — not training-data approximations. Essential for any fast-moving library or API. |
| **GitHub** | Read/write repos, issues, PRs, and code search directly from Claude |
| **Filesystem** | Read and write local files outside the current project folder |
| **Brave Search** | Real-time web search without leaving Claude Code |
| **PostgreSQL** | Query your database in plain English |
| **Playwright** | Control a browser — scrape, test, or automate web interactions |
| **Slack** | Read channels, send messages, search conversations |
| **Notion** | Read and write Notion pages and databases |
| **Figma** | Read design files and component specs |
| **n8n** | Trigger and manage automation workflows |

## Find More

### Official

- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — Anthropic's official reference implementations (GitHub, filesystem, PostgreSQL, Brave Search, etc.)
- [Connect Claude Code to tools via MCP — Claude Code Docs](https://code.claude.com/docs/en/mcp)

### Curated GitHub Lists

- [wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) — most widely cited community list, organized by category
- [appcypher/awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers) — another large community list
- [tolkonepiu/best-of-mcp-servers](https://github.com/tolkonepiu/best-of-mcp-servers) — ranked by stars and activity, updated weekly

### Directories

- [mcpmarket.com/leaderboards](https://mcpmarket.com/leaderboards) — top 100 by install count
- [mcpservers.org](https://mcpservers.org) — searchable community registry
- [fastmcp.me](https://fastmcp.me) — tracks views and install counts (10,000+ servers indexed)
