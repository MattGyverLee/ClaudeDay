# Install

For this workshop you will need VS Code, Claude Desktop, the Claude Code extension, Git, and Python.

## 1. VS Code

Download from [code.visualstudio.com](https://code.visualstudio.com/download).

**Minimum:** VS Code **1.98.0** or higher (required for Claude Code).

## 2. Git for Windows

Download from [git-scm.com/download/win](https://git-scm.com/download/win), or via winget:

```
winget install --id Git.Git -e --source winget
```

### Key options during install

- Select **"Use Visual Studio Code as Git's default editor"**
- Leave PATH settings on default so Git is available in the terminal

### Add Git Bash to Windows PATH

Claude Code requires Git Bash internally. If it isn't detected automatically, add it manually:

1. Press `Win + S`, search **"Environment Variables"**, open **"Edit the system environment variables"**
2. Click **Environment Variables...**
3. Under **System variables**, select **Path** → click **Edit**
4. Click **New** and add: `C:\Program Files\Git\bin`
5. Click **OK** on all dialogs
6. Restart any open terminals or VS Code

If Claude Code still can't find it, set the path explicitly in `.claude/settings.json`:

```json
{
  "env": {
    "CLAUDE_CODE_GIT_BASH_PATH": "C:\\Program Files\\Git\\bin\\bash.exe"
  }
}
```

## 3. Python

Download from [python.org/downloads](https://www.python.org/downloads/). Python 3.12 is recommended for stability.

> **Critical:** Check **"Add Python to PATH"** at the bottom of the installer — this is the most common setup mistake.

## 4. Claude Desktop

Download from [claude.ai/download](https://claude.ai/download).

> **Important:** Download only from the official URL above. The Microsoft Store version does **not** support agents or Cowork.

Windows 10 or later. Admin privileges required for full agent support.

### Enable Windows Virtual Platform (required for Cowork)

Cowork features require Windows virtualization to be enabled. To turn it on:

1. Press `Win + S`, search **"Turn Windows features on or off"**, open it
2. Check **Virtual Machine Platform**
3. Click **OK** and restart when prompted

Or enable it from PowerShell (run as Administrator):

```powershell
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

Then restart your machine.

## 5. Claude Code (VS Code Extension)

### Prerequisites

- VS Code **1.98.0** or higher
- An Anthropic account (Pro, Max, Team, or Enterprise subscription)

### Step 1 — Install the Extension

Open the Extensions view (`Ctrl+Shift+X`), search **"Claude Code"** (published by Anthropic), click **Install**.

Or via terminal:

```bash
code --install-extension anthropic.claude-code
```

### Step 2 — Sign In

On first open, Claude Code will prompt you to sign in. Click **Sign in** and complete the OAuth flow in your browser.

The **Spark icon** in the top-right toolbar or bottom status bar opens the panel at any time.

### Step 3 — Start Using It

- Type a question or task in the Claude Code panel
- Text selected in your editor is automatically shared as context
- Use `Alt+K` (Windows) / `Option+K` (Mac) to @-mention specific files

No API key required — your Claude account handles authentication automatically.

## 6. Set Up a Project Folder

Create a folder for your projects (e.g. `C:\projects\` or `~/projects/`) and create subfolders for each project. Claude Code works inside whichever folder you open in VS Code.
