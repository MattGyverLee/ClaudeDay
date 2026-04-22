# Deterministic Results

Like any automation, it's only worth it to spend time to automate anything you're doing multiple times (or you want others to do multiple times).

Our first conversation with Claude about the survey was exploratory. I didn't know what was in the data, and I wanted to get its impressions. I told Gary that the responses would be plausible, but not necessarily precise. Then I asked it to show its homework and write R scripts to back it up. We can now "diff" the before and after of the methodology document to see where the logic was fuzzy. At this point, a non-deterministic engine is locked into a deterministic script that we can check and confirm.

**Skill level 1** is "Send the data to the AI and ask the AI to do something for you". You'll get non-deterministic and possibly imprecise results. I liken this to using Wikipedia. It's probably a reasonable summary, but you can't cite it. 

**Skill level 2** is "Have the AI write a script to solve this problem". You get a reasonable deterministic script you can build on and re-use, but you get a different script every time you ask.

**Skill level 3** is adding "hard" resources and tools that enforce structure, decision gates and formats that the AI can't ignore. This means that the vetted deterministic processes do the "actual data" work (data lookups, statistics, etc.), but the AI is a bridge to translate your intention into tool calls and interpret the results. We can also add resources or external data to scan. This is the MCP route.

![3 Steps](/static/img/3%20Steps.png)

![3 Steps 2](/static/img/3%20Steps%202.png)

Basically, for any text over a few dozen lines, if I give it to the AI and ask for it back, I get an approximation of the data. AI's don't have perfect recall.  This means that if you upload a FLEx XML database to an LLM and ask for it back, there is NO CHANCE that it will be intact. It will make subtle style and structural changes you didn't ask for.

The solution (in my opinion) is passing small data chunks with heavy context, running deterministic data operations whenever possible, and then verifying that what it has created (creating gates) before the output is shown to the user. Basically, I reserve the AI for decision making and use python, R or Typescript to do the work. To do this, you either have to know every data manipulation option the user has (what I did with FLExToolsMCP) or you need to decide what tools the user might need and build those.