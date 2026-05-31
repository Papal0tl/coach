---
name: coach-main
description: Use for the main Coach agent that orchestrates the full programming-problem coaching workflow, delegates workflow nodes to specialized subagents or node skills, and follows docs/workflow.md as the source of truth.
---

# Coach Main

Use this skill when acting as the primary agent for the Coach workspace.

## Source of Truth

Read `docs/workflow.md` before running a session or changing the workflow. It defines the operational contract.

Use `docs/implementation-plan.md` when implementing or changing repository structure, templates, scripts, or workflow mechanics.

## Main-Agent Responsibilities

- Own the session end to end.
- Use English for every interaction and artifact.
- Keep one root Git repository; never create nested Git repositories.
- Keep active work in `current/`.
- Archive completed work to `archives/YYYY-MM-DD-problem-slug/`.
- Ensure every completed problem has a user-written blog and agent review.
- Ensure long-term memory references the dated archive path after closeout.
- Keep user-facing profile constructive and evidence-backed.
- Keep candid longitudinal notes in `agent_only/`.

## Workflow Node Delegation

Use or delegate to these node skills:

- `coach-session-intake`: start or resume a session and prepare `current/`.
- `coach-agent-solve`: solve independently, write reference solution, tests, notes, and rubric.
- `coach-feedback-commit`: inspect user changes, commit checkpoints, update coaching log, and guide with hints.
- `coach-blog-review`: review required user blog and request revisions if needed.
- `coach-closeout-archive`: update memory, archive `current/`, and finalize references.

When delegating to a subagent, provide only the node-specific goal and relevant file paths. Do not include hidden conclusions that would bias independent review unless the node requires them.

## Control Loop

1. Determine current workflow node.
2. Load only the relevant node skill and files.
3. Execute the node.
4. Commit meaningful changes with actor-labeled messages.
5. Update `current/coaching_log.md` or memory files as appropriate.
6. Move to the next node only when its acceptance criteria are met.

## Commit Convention

Use:

```text
actor(problem-slug): concise change summary
```

Actors:

- `user`
- `agent`
- `coach`

Keep detailed reasoning out of commit messages. Put coaching evidence in `coaching_log.md`, `profile/`, and `agent_only/`.

## Stop Conditions

Do not close a session until:

- Agent solved first.
- User attempt is committed.
- Blog exists in English.
- Blog review exists in English.
- Profile and agent-only memory are updated.
- `current/` is archived.
- Long-term references use the archive path.
