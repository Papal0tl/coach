# Rubric

- Problem slug: `copy-list-with-random-pointer`
- Archive path: `archives/2026-07-09-copy-list-with-random-pointer/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Names both `next` and `random` as pointers to reproduce, and that copies must be structurally identical but reference-distinct from the originals | Not stated explicitly in discussion; blog Problem Summary is agent-drafted, pending user confirmation | pending blog |
| Constraint analysis | Recognizes `random` can point forward, backward, to self, or be `None` | Implemented `if cur.next / else` and `if cur.random / else` branches correctly, implying awareness of the `None` case; forward/self cases not discussed explicitly | partial |
| Brute-force construction | Any working approach before optimizing | Went straight to the optimal hash-map approach; no brute force attempted | skipped (jumped to optimal) |
| Pattern recognition | Identifies the need for a mapping from old node identity to new node, likely via hash map | Named "hash map, old node points to new node" unprompted after one guiding question | met |
| Invariant formulation | States why two passes are needed (forward-reference problem) rather than just copying in one pass | Correctly explained the forward-reference problem when prompted ("the copy of that target node doesn't exist yet"), before writing any code | met |
| Complexity analysis | States O(n) time / O(n) space for the map-based solution unprompted | Not yet stated; expected in blog Complexity section (agent-drafted, pending user confirmation) | pending blog |
| Edge-case design | Covers empty list, self-referential random, no-random-pointers cases | Added the empty-list guard independently; other edge cases validated by agent-run tests, not user-authored | partial |
| Debugging discipline | Uses concrete tracing if bugs appear | Did not engage with mental-trace prompts (asked twice); converged much faster once told to actually run the file and read the real error message | partial — prefers empirical running over mental tracing |
| Communication | Clear English reasoning in comments and discussion | Two messages sent in Chinese despite English-only session preference; code comments and structure otherwise clear | needs improvement |

## Intervention Count

- Clarifying questions: 2 (mental-trace prompts, largely unproductive)
- Hints: 1 (forward-reference guiding question, successful)
- Direct explanations: 1 (explicit method-wrapping syntax shown after two failed trace attempts)
- Code-level nudges: 0 (no code written for the user; all fixes were the user's own edits)

## Closeout Assessment

Algorithmic core (hash map, two-pass structure, forward-reference reasoning) was reached independently and quickly — strongest signal yet on recognizing *why* a two-pass structure is required, not just that it's needed. Implementation friction was entirely mechanical/syntax-level (return-outside-function from unwrapped class-body code, wrong constructor arg, missing loop increment, accidental class deletion), not logical, and all were self-fixed. Debugging approach leaned on "run and read the error" rather than mental tracing, which converged faster than the two mental-trace prompts did — worth noting as an effective strategy for this user rather than a gap. All 7 tests pass against `attempt.py` including the deep-copy identity check. Two English-only lapses this session; continue to gently redirect. Full closeout assessment to be finalized after blog review.
