# Coach Implementation Plan

This plan turns the workflow into a usable local coaching system. The first version is file-based and agent-operated.

## Target Architecture

Use a single root Git repository with predictable folders:

```text
coach/
  current/
  archives/
  blogs/
  profile/
  agent_only/
  templates/
  skills/
  docs/
```

No nested repositories. All history is root Git history.

## Phase 1: Repository Scaffolding

Create the durable directories:

- `current/`
- `archives/`
- `blogs/`
- `profile/`
- `agent_only/`
- `templates/`
- `skills/`
- `docs/`

Create initial profile files:

- `profile/user_profile.md`
- `profile/skill_matrix.md`
- `profile/review_log.md`

Create initial agent-only files:

- `agent_only/user_assessment.md`
- `agent_only/algorithm_progress.md`

Acceptance criteria:

- All required folders exist.
- No nested `.git` directories exist.
- Root `git status` shows project files normally.

## Phase 2: Templates

Add templates for:

- `templates/current_README.md`
- `templates/problem.md`
- `templates/attempt.py`
- `templates/agent_solution.py`
- `templates/tests.py`
- `templates/notes.md`
- `templates/rubric.md`
- `templates/blog.md`
- `templates/blog_review.md`
- `templates/user_profile.md`
- `templates/skill_matrix.md`
- `templates/review_log.md`
- `templates/user_assessment.md`
- `templates/algorithm_progress.md`

Template rules:

- English only.
- Include archive-path fields where long-term references are expected.
- Keep fields explicit enough that the agent does not invent structure each session.

Acceptance criteria:

- A new session can be created by copying templates into `current/`.
- The blog template makes the required sections obvious while encouraging concise writing.
- Profile and agent-only templates separate evidence from interpretation.

## Phase 3: Session Setup Workflow

Implement the manual agent workflow for starting a session:

1. Check whether `current/` exists and whether it contains unfinished work.
2. Determine problem slug, date, language, and coaching mode.
3. Populate `current/` from templates.
4. Record problem statement in `current/problem.md`.
5. Create `current/attempt.<ext>`.
6. Create empty or stub `current/agent_solution.<ext>` and `current/tests.<ext>`.
7. Commit setup:

```text
coach(problem-slug): set up current session
```

Acceptance criteria:

- `current/` is ready for the user without exposing the final answer.
- The setup commit is actor-labeled.
- The session can be resumed from files alone.

## Phase 4: Agent Solve Workflow

Before coaching:

1. Solve the problem independently.
2. Write `current/agent_solution.<ext>`.
3. Write `current/tests.<ext>`.
4. Update `current/notes.md` with algorithm insight and complexity.
5. Update `current/rubric.md` with target skills.
6. Run tests when practical.
7. Commit:

```text
agent(problem-slug): add reference solution and tests
```

Acceptance criteria:

- Agent has a validated or clearly reasoned reference solution.
- The user attempt file remains separate.
- The agent does not reveal the full solution unless mode allows it.

## Phase 5: Feedback Loop

For each user checkpoint:

1. Run `git diff`.
2. Read changed user files.
3. Commit the user's meaningful changes:

```text
user(problem-slug): concise description
```

4. Update `current/notes.md` with any meaningful coaching observation.
5. Give the least-direct useful guidance.
6. If the agent edits notes, tests, or review files, commit separately or as a mixed `coach(...)` commit when appropriate.

Commit guidance:

- Prefer one commit per meaningful user checkpoint.
- Do not commit every trivial keystroke.
- Do not batch conceptually different actions into one vague commit.
- Include the actor and problem slug.
- Keep detailed coaching interpretation out of the commit message.

Acceptance criteria:

- Git history shows the user's progression.
- `current/notes.md` captures meaningful coaching context.
- The user remains responsible for their own attempt unless mode allows direct editing.

## Phase 6: Concise Blog and Review Workflow

After the problem is solved or walked through:

1. Have the agent create a concise `blogs/problem-slug.md` draft with self-explanatory sections pre-filled.
2. Ask the user to complete or revise the learning-heavy sections in their own words.
3. Commit the blog draft:

```text
user(problem-slug): draft solution blog
```

4. Review it in `current/blog_review.md`.
5. Request revisions if needed.
6. Commit revisions and final review.

Acceptance criteria:

- Blog is in English.
- Blog is concise while still explaining the key insight, invariant, complexity, and edge cases.
- Agent-filled sections are limited to self-explanatory or copyable content.
- User-filled sections show the user's own understanding.
- Blog review identifies transfer readiness.
- Session does not close before the blog is accepted or unresolved gaps are recorded.

## Phase 7: Profile and Agent-Only Memory

At closeout, update user-facing profile files:

- `profile/user_profile.md`
- `profile/skill_matrix.md`
- `profile/review_log.md`

Update agent-only files:

- `agent_only/user_assessment.md`
- `agent_only/algorithm_progress.md`

Rules:

- Evidence first, interpretation second.
- Use the dated archive path as the evidence reference after archiving.
- Track algorithm-specific progress from implementation, discussion, and blog quality.
- Keep user-facing profile constructive.
- Keep candid longitudinal observations in `agent_only/`.

Acceptance criteria:

- Skill changes cite evidence.
- Algorithm progress names the pattern practiced.
- Agent-only notes do not leak into user-facing files unless rewritten constructively.

## Phase 8: Archive Workflow

Closeout steps:

1. Ensure blog review is complete.
2. Choose archive name:

```text
archives/YYYY-MM-DD-problem-slug/
```

3. Move or copy `current/` contents into the archive path.
4. Update long-term references in blog, profile, and agent-only files to the archive path.
5. Commit:

```text
coach(problem-slug): archive completed session
```

Decision to resolve:

- Whether `current/` should be cleared after archive or left as the latest session until a new setup begins.

Recommended default:

- Leave `current/` intact until the next session setup, but treat `archives/YYYY-MM-DD-problem-slug/` as canonical after closeout.

Acceptance criteria:

- Archive exists and contains the full session.
- Long-term files reference the archive path.
- Git history includes an archive commit.

## Phase 9: Optional Automation

Automation should come after the manual workflow is stable.

Candidate scripts:

- `scripts/start_session`: create `current/` from templates.
- `scripts/check_current`: detect unfinished current work.
- `scripts/archive_session`: archive `current/` with dated name.
- `scripts/commit_checkpoint`: help format actor-labeled commits.
- `scripts/validate_session`: check closeout requirements.

Automation should not hide the coaching logic. It should reduce repetitive file operations and validation mistakes.

## Validation Checklist

Before calling the system usable, run one complete practice session and verify:

- Agent solves first.
- User attempt is separate from agent solution.
- Git commits identify user, agent, and coach actions.
- Blog is required and reviewed.
- Profile updates are evidence-backed.
- Agent-only notes track candid progress.
- Session is archived with a dated name.
- Long-term references use the archive path.
- All artifacts are in English.
