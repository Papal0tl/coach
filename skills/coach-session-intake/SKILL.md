---
name: coach-session-intake
description: Use when starting or resuming a Coach problem-solving session, preparing current/, choosing problem metadata, language, coaching mode, and root Git setup conventions.
---

# Coach Session Intake

Use this skill at the start of a coaching session.

## Rules

- Use English only.
- Use `current/` for active work.
- Use one root Git repository only.
- Do not create nested Git repositories.
- If `current/` contains unfinished work, resume it or ask before replacing it.
- Finished work must be archived before starting a new session.

## Intake Checklist

Gather or infer:

- Problem source: LeetCode link, pasted statement, or custom prompt.
- Problem slug, such as `two-sum`.
- Language from user preference or profile.
- Coaching mode: hint-only, interview, debugging, or walkthrough.
- Whether the user provided an external solution they do not want to read.
- Constraints on direct answers or code edits.

Prefer profile defaults when available. Ask only if the missing choice changes the workflow.

## Setup Files

Prepare:

- `current/README.md`
- `current/problem.md`
- `current/attempt.<ext>`
- `current/agent_solution.<ext>`
- `current/tests.<ext>`
- `current/notes.md`
- `current/rubric.md`
- `current/blog_review.md`

Commit setup with:

```text
coach(problem-slug): set up current session
```

## Done When

- `current/` represents exactly one active session.
- The problem statement and constraints are recorded.
- The user attempt file exists.
- The agent solution file exists but does not reveal a solution yet unless already solved.
- Setup is committed in the root repository.
