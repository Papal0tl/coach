---
name: coach-closeout-archive
description: Use at the end of a Coach session to update profile and agent-only memory, archive current/ into archives/YYYY-MM-DD-problem-slug/, and ensure all long-term references use the archive path.
---

# Coach Closeout Archive

Use this skill only after the user attempt, blog, and blog review are complete.

## Rules

- Use English only.
- Archive `current/` to `archives/YYYY-MM-DD-problem-slug/`.
- Long-term references must use the dated archive path after closeout.
- Keep user-facing profile constructive.
- Keep candid longitudinal assessment in `agent_only/`.

## Closeout Workflow

1. Confirm required files exist:
   - `current/problem.md`
   - `current/attempt.<ext>`
   - `current/agent_solution.<ext>`
   - `current/tests.<ext>` or validation note
   - `current/coaching_log.md`
   - `current/blog_review.md`
   - `blogs/problem-slug.md`
2. Update:
   - `current/README.md`
   - `current/notes.md`
   - `current/rubric.md`
   - `profile/user_profile.md`
   - `profile/skill_matrix.md`
   - `profile/review_log.md`
   - `agent_only/user_assessment.md`
   - `agent_only/algorithm_progress.md`
3. Create archive path:

```text
archives/YYYY-MM-DD-problem-slug/
```

4. Copy or move `current/` contents into the archive.
5. Update blog, profile, and agent-only notes to reference the archive path.
6. Commit:

```text
coach(problem-slug): archive completed session
```

## Done When

- The archive contains the full session.
- Blogs and memory files reference the archive path.
- Profile updates cite evidence.
- Agent-only progress tracks algorithm-specific learning.
- Root Git history has the closeout commit.
