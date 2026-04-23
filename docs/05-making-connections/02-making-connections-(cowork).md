# Making Connections

Using LLMs is more fun if the LLM already has access to the things it needs when you start the chat. See more here: [Claude Code Everything (Short)](https://x.com/affaanmustafa/status/2012378465664745795)

## Connectors and Extensions

Claude has official "partner" tools that they call "Connectors". These give basic access to Google Drive, Notion, Monday.

## Extensions and MCPs

Extensions are usually MCPs (Online, local, or proxy). They give predefined tools and upt-to-the-minute resources that you can call through the LLM and the LLM handles the responses.  Loading Extensions you don't need can fill your context so it can't do useful work.

## CLIs

Because MCPs with many tools fill the context, some are moving to CLI (Command Line Interface) tools that can either be called by the LLM or by scripts with similar results. Skills tell Claude when and how to use the CLI, are called "just in time", and don't fill the context until you call the tool you need.

## Skills

Skills are Markdown files. Often, you can do a task interactively, and then distill it into a reusable skill.

## Agents

Predefined (often specialized) personas with different skills, resources, and tools.
