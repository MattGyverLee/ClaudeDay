# Getting Started

Everything I'm about to say is a lie and oversimplification, but they are useful starting points.

Everything in the AI world seems to be on a spectrum.

## The AI Coding Ecosystem

There are millons of small players, but Anthropic, OpenAI, Google, and Microsoft are the big players.

![AI Ecosystem](/static/img/AI%20Ecosystem.png)

## Shifting Emphases

### The LLM itself

The LLMs are the first line, they have a LOT of general knowledge and can handle general tasks (Translation, etc.) without much added context.

### Prompting (2024)

When dealing with LLMS in the web browser, the emphasis was on Prompting. Your goal was to create a simple version of the context and need that you could paste into the chat so that you wouldn't get slop.

### Agentic (2025)

It became easy to spin up agents/GPTs/Gems with specialized baked-in skills. Small bots with non-overlapping context working together create better results than one "Big Brain". Agents get access to files and tools not native to the LLM.

### Context (2026)

Today, Context is king. The goal is to provide the AI the tools and context that "might" be needed, and give the AI tools to bring it in in small chunks Just in Time. Keep the context fresh and focused. Spin up small specialized short-lived agents with smaller context. In Claude code, context size is a constant battle.
