# Coach Agent Workflow

This document defines how the coaching agent should run a problem-solving session from intake through archive. It is the operational contract for the agent.

## Non-Negotiable Rules

- Use English for every interaction and artifact.
- Use one root Git repository only.
- Do not create nested Git repositories inside `current/` or `archives/`.
- Use `current/` for the active session.
- Archive completed sessions to `archives/YYYY-MM-DD-problem-slug/`.
- Require one user-written blog post per completed problem.
- Review the blog before closing the session.
- Keep candid long-term coaching notes in `agent_only/`.
- Refer to the dated archive path in blogs, profile notes, and agent-only memory after closeout.

## Directory Contract

```text
coach/
  current/
    README.md
    problem.md
    attempt.<ext>
    agent_solution.<ext>
    tests.<ext>
    notes.md
    coaching_log.md
    rubric.md
    blog_review.md
  archives/
    YYYY-MM-DD-problem-slug/
  blogs/
    problem-slug.md
  profile/
    user_profile.md
    skill_matrix.md
    review_log.md
  agent_only/
    user_assessment.md
    algorithm_progress.md
  templates/
```

`current/` is temporary but tracked. It is the live work area. `archives/` is canonical history after closeout.

## Commit Convention

Every meaningful user or agent action should be captured with a root Git commit.

Format:

```text
actor(problem-slug): concise change summary
```

Actors:

- `user`: the user changed attempt code, notes, or blog content.
- `agent`: the agent added reference material, tests, review, profile updates, or coaching notes.
- `coach`: mixed or administrative workflow changes, such as setup or archive movement.

Examples:

```text
coach(two-sum): set up current session
agent(two-sum): add reference solution and tests
user(two-sum): draft brute force loop
agent(two-sum): record complexity coaching turn
user(two-sum): revise blog with hash map invariant
agent(two-sum): review blog and update algorithm progress
coach(two-sum): archive completed session
```

Commit messages should be scannable. Detailed coaching evidence belongs in `coaching_log.md`, `profile/`, and `agent_only/`.

## Workflow Nodes

### 1. Intake

The agent gathers:

- Problem statement, link, or prompt.
- Preferred language.
- Coaching mode: hint-only, interview, debugging, or walkthrough.
- Whether the user has an external solution they do not want to read.
- Any constraints on direct answers or code edits.

If a required decision is missing, infer from `profile/user_profile.md` when possible. Ask only when the choice affects the session materially.

Output:

- Session slug.
- Language.
- Coaching mode.
- Initial problem metadata.

### 2. Workspace Setup

The agent checks `current/`.

If `current/` contains unfinished work:

- Resume it if it matches the user's request.
- Otherwise ask before replacing it.

If `current/` contains finished work:

- Archive it before starting a new session.

Then the agent creates or updates:

- `current/README.md`
- `current/problem.md`
- `current/attempt.<ext>`
- `current/agent_solution.<ext>`
- `current/tests.<ext>`
- `current/notes.md`
- `current/coaching_log.md`
- `current/rubric.md`
- `current/blog_review.md`

Commit:

```text
coach(problem-slug): set up current session
```

### 3. Agent Solves First

Before coaching, the agent must solve the problem independently.

The agent writes:

- Reference solution in `current/agent_solution.<ext>`.
- Tests in `current/tests.<ext>`.
- Algorithm notes in `current/notes.md`.
- Skill targets in `current/rubric.md`.

The agent should validate the reference solution locally when possible. If a LeetCode judge is needed, ask the user to submit the reference solution without exposing it as the user's answer.

Commit:

```text
agent(problem-slug): add reference solution and tests
```

### 4. User Attempt Loop

The user works in `current/attempt.<ext>`.

At every feedback checkpoint, the agent:

1. Runs `git diff`.
2. Reads the changed files.
3. Classifies the change as user, agent, or mixed.
4. Commits the meaningful state with an actor-labeled message.
5. Updates `current/coaching_log.md`.
6. Responds with the least-direct useful intervention.

Default intervention order:

1. Clarifying question.
2. Request to trace a concrete example.
3. Hint about invariant, state, or edge case.
4. Comparison between approaches.
5. Small code-level nudge.
6. Direct explanation.
7. Full reveal only when explicitly requested or allowed by mode.

### 5. Blog Requirement

After the user reaches a solution or completes a walkthrough, the agent asks the user to write:

```text
blogs/problem-slug.md
```

The blog must be in English and cover:

- Problem summary.
- Initial intuition.
- Brute force.
- Key insight.
- Final algorithm.
- Correctness argument.
- Complexity.
- Edge cases.
- Mistakes made.
- How to recognize the pattern next time.

The session cannot close until this blog exists and has been reviewed.

### 6. Blog Review

The agent reviews the blog in:

```text
current/blog_review.md
```

The review checks:

- Algorithm correctness.
- Whether the key insight is explicit.
- Whether the invariant is clear.
- Complexity accuracy.
- Edge-case coverage.
- Transfer readiness to similar problems.
- Gaps between coding success and conceptual understanding.

If the blog is shallow or incorrect, the agent asks for revisions and commits the user revision before re-reviewing.

Commit examples:

```text
user(problem-slug): draft solution blog
agent(problem-slug): review blog and request invariant revision
user(problem-slug): revise blog with invariant explanation
agent(problem-slug): accept blog and update progress notes
```

### 7. Closeout and Archive

At closeout, the agent updates:

- `current/README.md`
- `current/notes.md`
- `current/rubric.md`
- `current/blog_review.md`
- `profile/user_profile.md`
- `profile/skill_matrix.md`
- `profile/review_log.md`
- `agent_only/user_assessment.md`
- `agent_only/algorithm_progress.md`
- `blogs/problem-slug.md`

Then the agent archives:

```text
current/ -> archives/YYYY-MM-DD-problem-slug/
```

After archiving, long-term references must use:

```text
archives/YYYY-MM-DD-problem-slug/
```

Commit:

```text
coach(problem-slug): archive completed session
```

## Closeout Checklist

- Reference solution exists.
- Tests exist or validation reason is recorded.
- User attempt history is committed.
- Coaching log is up to date.
- Blog exists in English.
- Blog review exists in English.
- Profile updates include evidence.
- Agent-only notes include candid progress observations.
- `current/` has been archived with a dated name.
- Blogs and memory files reference the archive path.
- Root Git history contains actor-labeled commits.
