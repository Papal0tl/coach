# Coach

Coach is a local workspace for practicing programming problems with an agent.

The goal is not to receive answers directly. The goal is to build problem-solving skill through guided attempts, feedback, review, and reflection.

## How It Works

1. Start a problem with the agent.
2. Work in `current/attempt.<ext>`.
3. The agent reviews your changes with `git diff` and commits meaningful checkpoints.
4. The agent guides you with questions and hints.
5. After the problem, write a blog post in `blogs/`.
6. The agent reviews the blog.
7. The session is archived to `archives/YYYY-MM-DD-problem-slug/`.

## Folders

- `current/`: active problem session.
- `archives/`: completed sessions.
- `blogs/`: your required writeups for each problem.
- `profile/`: user-facing progress notes.
- `agent_only/`: agent-maintained coaching memory.
- `templates/`: files used to start new sessions.
- `skills/`: agent workflow instructions.
- `docs/`: workflow and implementation details.

## Rules

- Everything should be written in English.
- Every completed problem needs a blog post.
- The agent must review the blog before closing the session.
- The workspace uses one root Git repository.
- No nested Git repositories should be created inside `current/` or `archives/`.

