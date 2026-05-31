---
name: coach-blog-review
description: Use after a Coach user writes a required problem blog, to review correctness, clarity, invariant, complexity, edge cases, mistakes, and transfer readiness before session closeout.
---

# Coach Blog Review

Use this skill after the user writes or revises `blogs/problem-slug.md`.

## Rules

- The blog is required for every completed problem.
- The blog and review must be in English.
- Do not close the session until the blog is reviewed.
- Ask for revisions if the blog shows shallow or incorrect understanding.

## Required Blog Sections

Check for:

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

## Review Workflow

1. Read `blogs/problem-slug.md`.
2. Compare it against `current/problem.md`, `current/agent_solution.<ext>`, and `current/rubric.md`.
3. Write `current/blog_review.md` with:
   - Correctness.
   - Missing concepts.
   - Clarity.
   - Transfer readiness.
   - Required revisions.
   - Agent assessment.
4. Commit user blog drafts and revisions as `user(...)`.
5. Commit agent reviews as `agent(...)`.

## Done When

- The blog explains the key insight and invariant clearly.
- Complexity and edge cases are correct.
- The review states whether the user is ready to transfer the pattern.
- Any unresolved gaps are recorded.
