# Activities

Pick a task from your own work, or use one of these starting points.

---

## Create a Script

Ask Claude to write a Python, R, or Bash script to automate something you do repeatedly.

**Good prompts:**
- *"Write a Python script that reads all CSV files in this folder and combines them into one, skipping duplicate rows."*
- *"Write a Bash script that renames all files in this folder from snake_case to kebab-case."*

**Tips:**
- Give Claude a sample input file so it can see the real shape of the data
- Ask it to add a dry-run mode before it writes anything destructive
- Have it write tests alongside the script

---

## Analyze Messy Data

Give Claude a real dataset — spreadsheet, CSV, JSON, XML — and ask it to make sense of it.

**Good prompts:**
- *"Here's a CSV of survey responses. Summarise the key themes in the open-text fields and flag any anomalies."*
- *"This JSON has inconsistent field names and missing values. Clean it up and output a normalised version."*

**Tips:**
- Start exploratory (what patterns do you see?), then go deterministic (write a script to extract X)
- Ask Claude to show its work — it should be able to back up any summary with a script you can re-run
- Use `/diff` to review any files it creates before committing

---

## Create an XSLT

Ask Claude to write an XSLT stylesheet to transform XML from one structure to another.

**Good prompts:**
- *"Write an XSLT 2.0 stylesheet that transforms this FLEx XML export into a simple word list in TSV format."*
- *"Convert this USFM-style XML into HTML with headings, verses, and footnotes."*

**Tips:**
- Paste a representative sample of your source XML (not the whole file)
- Be explicit about the output format — show Claude a target example if you have one
- Ask it to handle edge cases: missing elements, empty nodes, unexpected attributes

---

## Build a Website

Ask Claude to scaffold a static site or a simple web app from scratch — or improve an existing one.

**Good prompts:**
- *"Build a simple one-page site that displays entries from this JSON file as a searchable table."*
- *"Add a dark mode toggle and a print stylesheet to this existing HTML file."*

**Tips:**
- Start a fresh session with `/clear` before a build task
- Ask for a plan before any code is written — easier to redirect at that stage
- Use `/diff` to review HTML/CSS changes before accepting them

---

## Build a Tool

Ask Claude to build a small command-line or desktop tool around a workflow you repeat.

**Good prompts:**
- *"Build a CLI tool that takes a folder path and outputs a Markdown index of all files, grouped by type."*
- *"Create a small Flask app with a text input that runs this Python function and shows the result."*

**Tips:**
- Describe the tool from the user's perspective first, not the implementation
- Have Claude write a `README.md` as it goes — it forces clearer thinking about the interface
- Ask it to write a `requirements.txt` or `pyproject.toml` alongside the code

---

## Learn About Existing Code

Point Claude at a codebase — yours or someone else's — and ask it to explain what it does.

**Good prompts:**
- *"Run `/init`, then give me a plain-English tour of this project: what it does, how it's structured, and the main entry points."*
- *"Explain what this function does and what would break if I removed it."*
- *"What are the riskiest parts of this codebase to modify?"*

**Tips:**
- Start with `/init` so Claude builds its own mental map first
- Ask for a diagram or a layered explanation (overview → module → function)
- Ask "what don't you know?" — Claude will flag gaps where more context would help

---

## Document Code

Ask Claude to write or improve documentation for an existing project.

**Good prompts:**
- *"Write a `README.md` for this project: what it does, how to install it, and three usage examples."*
- *"Add docstrings to every public function in this file."*
- *"Turn the inline comments in this file into a proper API reference in Markdown."*

**Tips:**
- Ask Claude to write documentation *as a user*, not as the author — catches assumptions
- Have it generate a `CHANGELOG.md` from the git log: `"Summarise the git history into a changelog grouped by feature area."`
- Review with `/diff` — documentation changes are easy to over-accept without reading
