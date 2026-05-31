---
name: coach-blog-review
description: Use after a Coach user writes a required concise problem blog, to review correctness, clarity, invariant, complexity, edge cases, mistakes, and transfer readiness before session closeout.
---

# Coach Blog Review

Use this skill after the user writes or revises `blogs/problem-slug.md`.

## Rules

- A concise blog is required for every completed problem.
- The blog and review must be in English.
- The agent should pre-fill self-explanatory or copyable sections before the user writes.
- Do not close the session until the blog is reviewed.
- Ask for revisions if the blog shows shallow or incorrect understanding.

## Required Concise Blog Points

Check for the points below. Short bullets are acceptable if they are precise.

Agent-filled sections:

- Problem summary.
- Final algorithm outline.
- Complexity.
- Edge-case checklist.

User-filled or user-revised sections:

- Initial intuition.
- Brute force.
- Key insight.
- Correctness argument.
- Mistakes made.
- How to recognize the pattern next time.

## Review Workflow

1. If the blog does not exist, create a concise draft with the agent-filled sections only.
2. Ask the user to complete or revise the user-filled sections.
3. Read `blogs/problem-slug.md`.
4. Compare it against `current/problem.md`, `current/agent_solution.<ext>`, and `current/rubric.md`.
5. Write `current/blog_review.md` with:
   - Correctness.
   - Missing concepts.
   - Clarity.
   - Transfer readiness.
   - Required revisions.
   - Agent assessment.
6. Commit agent-created blog scaffolds as `agent(...)`.
7. Commit user blog drafts and revisions as `user(...)`.
8. Commit agent reviews as `agent(...)`.

## Done When

- The blog is concise and explains the key insight and invariant clearly.
- Complexity and edge cases are correct.
- The review states whether the user is ready to transfer the pattern.
- Any unresolved gaps are recorded.
