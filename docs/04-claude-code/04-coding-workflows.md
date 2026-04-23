# AI Coding Workflows

There's no single right way to work with Claude Code. The best workflow depends on how well-defined the task is, how much you care about long-term maintainability, and how fast you need results.

---

## Comparison at a Glance

| Workflow               | Speed             | Predictability | Best for                                |
| ---------------------- | ----------------- | -------------- | --------------------------------------- |
| Vibe Coding            | Fast              | Low            | Prototypes, exploration, throwaway code |
| Plan Mode              | Medium            | Medium         | Moderately complex features             |
| Spec-Driven            | Slower start      | High           | Production features, shared codebases   |
| TDD                    | Medium            | High           | Logic-heavy, verifiable correctness     |
| Agent Teams            | Fast (parallel)   | Medium         | Large tasks with independent pieces     |
| Graduate Workflow      | Fast then precise | High           | Startups, product validation            |

---

## 1. Vibe Coding

Describe what you want in plain English and let Claude go. No upfront planning, no spec — just intent and iteration.

**How it works:**

> *"Build a form that takes a name and email and saves it to a JSON file."*

Claude generates the code, you try it, you refine it with follow-up prompts. The feedback loop is fast and intuitive.

**Strengths:**

- Fastest path from idea to working prototype
- Low cognitive overhead — you stay in the problem, not the solution
- Great for learning and exploration
- Accessible to non-developers

**Weaknesses:**

- Ambiguity gets resolved by Claude, not you — often wrong for complex requirements
- Cross-file changes degrade quickly without a plan
- Hard to maintain or hand off — the "why" lives in the chat, not the code
- Success rate for feature additions drops sharply with task complexity

**When to use it:**

- Throwaway scripts and one-offs
- Early-stage prototyping to validate an idea
- Learning a new technology or API
- Simple, self-contained tasks

---

## 2. Plan Mode

Before any code is written, Claude explores the codebase and proposes a structured plan. You review and redirect before execution begins.

**How to enable:**

```bash
claude --permission-mode plan
```

Or use `/model opusplan` to have Opus plan and Sonnet execute.

**How it works:**

> *"Read src/auth/ and understand how we handle sessions. Then create a plan for adding OAuth support."*

Claude reads relevant files, identifies what needs to change, and writes out a step-by-step approach — without touching anything. You can edit, redirect, or approve before it proceeds.

**Strengths:**

- Catches misunderstandings before they become code
- Much better for multi-file tasks than straight vibe coding
- Easy to redirect at the plan stage vs. after 200 lines are written
- Still fairly fast

**Weaknesses:**

- Plan quality depends on Claude's codebase understanding
- Plans can be over-engineered for simple tasks

**When to use it:**

- Any task touching more than 2–3 files
- When you have an existing codebase and need Claude to respect it
- Before starting a long session

---

## 3. Spec-Driven Development

You and Claude collaborate to write a detailed spec *first* — requirements, data model, edge cases, acceptance criteria — and implementation follows from that document.

**How it works:**

1. Open a blank `spec.md` in your project
1. Describe the feature in plain English
1. Ask Claude to expand it into a full spec:

> *"I want to add a user notification system. Ask me clarifying questions, identify edge cases I haven't considered, and write a complete spec in spec.md before writing any code."*

1. Review and edit `spec.md` until it's right
1. Then: *"Implement this spec."*

**Strengths:**

- Exposes ambiguity before it becomes a bug
- Claude-generated specs catch edge cases humans miss during initial planning
- The spec is a living document — version-controlled, shareable, reviewable
- Implementation is more consistent and predictable
- Reduces planning time by 30–40%, even accounting for spec-writing time

**Weaknesses:**

- Slower to start — not suitable for throwaway work
- Over-engineering risk for simple features
- Requires discipline to keep the spec updated as requirements shift

**When to use it:**

- Production features in shared codebases
- Anything being handed off to another person or team
- Features with complex business logic, data models, or edge cases
- When you need to justify decisions later

---

## 4. Test-Driven Development (TDD)

Write the tests first, then ask Claude to write code that passes them. The tests define the contract; Claude fills in the implementation.

**How it works:**

1. Describe the behaviour you want as a test:

> *"Write pytest tests for a function `parse_survey_row(row)` that takes a dict and returns a validated SurveyResponse object. Cover: valid input, missing required fields, invalid date format, empty string values."*

1. Review and adjust the tests until they capture your intent exactly
1. Then: *"Now implement `parse_survey_row` so all these tests pass."*
1. Run the tests, share the output with Claude, iterate

**Strengths:**

- Tests act as a precise, executable spec — no ambiguity about what "correct" means
- Claude is very good at writing implementation to match a test suite
- Bugs surface immediately and are easy to localise
- You end up with a test suite as a by-product, not an afterthought
- Forces you to think about edge cases before writing a single line of implementation

**Weaknesses:**

- Requires knowing enough about the interface to write tests upfront
- Slower than vibe coding for exploratory or UI-heavy work
- Test quality determines implementation quality — bad tests produce bad code

**Workflow variation — outside-in TDD:**

Start with an integration or end-to-end test that describes the full behaviour, then let Claude drive the implementation inward from there:

> *"Write a test that calls our `/api/export` endpoint and asserts a valid CSV is returned. Then implement the endpoint until the test passes."*

**When to use it:**

- Any logic that must be verifiably correct: data transformations, parsers, API handlers
- When handing code to someone else who needs to understand its contract
- Refactoring existing code — write tests against the current behaviour first, then refactor safely

---

## 5. Agent Teams

Multiple Claude Code instances work in parallel on a shared task list, each owning independent pieces. One session acts as team lead; teammates coordinate peer-to-peer.

**How to enable:**

```bash
# In settings.json or shell environment
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

**How it works:**

The lead session breaks the task into independent chunks, assigns them to teammates, and tracks a shared task list. Teammates claim tasks, work in their own context windows, and mark tasks complete — unblocking any dependent tasks automatically.

> *"We need to add CSV export to the reporting module. Spin up an agent team: one agent on the data layer, one on the API endpoint, one writing tests."*

**Strengths:**

- Dramatically faster for large tasks with parallel workstreams
- Each agent has a clean, focused context window
- Teammates can challenge each other's approaches
- File locking prevents conflicts
- Strong for: frontend + backend + tests in parallel, multi-module refactors, parallel research

**Weaknesses:**

- Each agent has its own context window — token cost multiplies with team size
- Experimental feature — less stable than single-agent workflows
- Coordination overhead for tightly coupled tasks
- Best results when subtasks are genuinely independent

**Cost tip:** use Sonnet for teammates, not Opus. Keep teams small and tasks self-contained. Clean up teams when work is done.

**When to use it:**

- Large features with clearly separable pieces
- Parallel research and investigation
- Changes spanning multiple layers (frontend, backend, tests)

---

## 6. The Graduate Workflow

Start fast and rough in a browser-based tool to validate the idea, then bring the code into Claude Code for production-level refinement.

**How it works:**

1. **Prototype** in Bolt, Lovable, or v0 — generate a working UI or app skeleton with minimal effort
1. **Validate** — does the idea work? Is it worth building properly?
1. **Graduate** — bring the code into a local repo and open it in Claude Code
1. **Refine** — use spec-driven development or plan mode to clean up architecture, add tests, handle edge cases

**Strengths:**

- Fastest path to something clickable for stakeholder feedback
- Separates discovery (is this worth building?) from engineering (build it well)
- Combines the best of vibe speed with spec-driven quality
- Well suited to non-technical founders and product teams

**Weaknesses:**

- Browser-generated code often has structural issues that need significant rework
- The "graduation" step requires someone who can evaluate code quality
- Not suitable for security-sensitive or data-heavy work at the prototype stage

**When to use it:**

- New product ideas, startup MVPs
- Getting stakeholder sign-off before committing engineering time
- UI-first workflows where you need to see it to spec it

---

## Choosing the Right Workflow

**Ask yourself:**

| Question                                     | If yes →                 |
| -------------------------------------------- | ------------------------ |
| Is this throwaway or exploratory?            | Vibe Coding              |
| Is this a real feature in a real codebase?   | Plan Mode or Spec-Driven |
| Does it have complex logic or edge cases?    | Spec-Driven or TDD       |
| Must correctness be provable?                | TDD                      |
| Can it be split into truly independent parts? | Agent Teams             |
| Do I need a prototype before committing?     | Graduate Workflow        |

The most common production pattern is a **hybrid loop**: vibe-code to explore and discover requirements, then lock those discoveries into a versioned spec, then implement. This keeps the speed of discovery and the reliability of specification.

---

## Sources

- [Vibe Coding vs Spec-Driven Development — Augment Code](https://www.augmentcode.com/guides/vibe-coding-vs-spec-driven-development)
- [Beyond vibe coding: the case for spec-driven AI development — The New Stack](https://thenewstack.io/vibe-coding-spec-driven/)
- [Vibes, specs, skills, and agents: The four pillars of AI coding — Red Hat Developer](https://developers.redhat.com/articles/2026/03/30/vibes-specs-skills-agents-ai-coding)
- [Orchestrate teams of Claude Code sessions — Claude Code Docs](https://code.claude.com/docs/en/agent-teams)
- [Claude Code Agent Teams — SitePoint](https://www.sitepoint.com/anthropic-claude-code-agent-teams/)
- [Best Practices — Claude Code Docs](https://code.claude.com/docs/en/best-practices)
