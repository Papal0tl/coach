---
name: coach-feedback-commit
description: Use during Coach feedback loops when reading user changes, committing meaningful checkpoints with actor-labeled messages, updating notes, and responding with questions or hints.
---

# Coach Feedback Commit

Use this skill whenever the user asks for feedback, says they changed code, or asks a question during an active session.

## Rules

- Use English only.
- Run `git diff` before judging progress.
- Commit meaningful user changes before giving substantial feedback.
- Do not overwrite the user's attempt unless explicitly asked or allowed by mode.
- Prefer questions and scoped hints before direct explanations.

## Commit Format

```text
actor(problem-slug): concise change summary
```

Actors:

- `user`: user changed attempt code, notes, or blog content.
- `agent`: agent changed tests, notes, review, profile, or reference material.
- `coach`: mixed or administrative changes.

Examples:

```text
user(two-sum): draft brute force loop
agent(two-sum): record complexity coaching turn
coach(two-sum): update session status
```

## Feedback Workflow

1. Read `git diff`.
2. Read relevant files in `current/`.
3. Commit the meaningful state with an actor-labeled message.
4. Update `current/notes.md` with any meaningful coaching observation.
5. Choose the least-direct useful intervention:
   - Clarifying question.
   - Concrete trace request.
   - Hint about invariant, state, or edge case.
   - Approach comparison.
   - Small code nudge.
   - Direct explanation.
   - Full reveal only when allowed.

## Done When

- Git history records the checkpoint.
- Notes record meaningful observations and interventions.
- The response guides the user's thinking instead of taking over by default.
