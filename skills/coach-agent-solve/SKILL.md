---
name: coach-agent-solve
description: Use when the Coach agent must solve a programming problem before coaching, create a reference solution, tests, notes, and rubric without revealing the solution to the user by default.
---

# Coach Agent Solve

Use this skill after intake and before giving coaching.

## Rules

- Solve independently before coaching.
- Keep `current/attempt.<ext>` separate from `current/agent_solution.<ext>`.
- Do not reveal the full solution unless the coaching mode or user explicitly allows it.
- Write all notes and comments in English.

## Workflow

1. Read `current/problem.md`.
2. Identify the problem pattern and target skills.
3. Write `current/agent_solution.<ext>`.
4. Write `current/tests.<ext>` when practical.
5. Update `current/notes.md` with:
   - Key insight.
   - Invariant or state definition.
   - Complexity.
   - Edge cases.
6. Update `current/rubric.md` with skills to observe.
7. Run local tests when practical.
8. If external judge validation is needed, ask the user to submit the reference solution.

Commit with:

```text
agent(problem-slug): add reference solution and tests
```

## Done When

- The agent has a correct or clearly reasoned reference solution.
- Tests or validation notes exist.
- The coaching target is explicit.
- The user attempt remains untouched unless the mode allows direct editing.
