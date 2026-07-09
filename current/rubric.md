# Rubric

- Problem slug: `copy-list-with-random-pointer`
- Archive path: `archives/2026-07-09-copy-list-with-random-pointer/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Names both `next` and `random` as pointers to reproduce, and that copies must be structurally identical but reference-distinct from the originals | Blog Problem Summary (agent-drafted) confirmed as-is by the user; Initial Intuition independently identified `random` as the source of difficulty | met |
| Constraint analysis | Recognizes `random` can point forward, backward, to self, or be `None` | Correctness Argument in the blog explicitly walked through forward, backward, self-referential, and `None` cases in one paragraph | met |
| Brute-force construction | Any working approach before optimizing | No brute force attempted in code (went straight to optimal); blog Brute Force section describes a genuinely distinct O(n²) index-scan approach with correct complexity | met (in writing only) |
| Pattern recognition | Identifies the need for a mapping from old node identity to new node, likely via hash map | Named "hash map, old node points to new node" unprompted after one guiding question | met |
| Invariant formulation | States why two passes are needed (forward-reference problem) rather than just copying in one pass | Correctly explained the forward-reference problem when prompted, before writing any code; blog Key Insight and Correctness Argument both restate it precisely | met |
| Complexity analysis | States O(n) time / O(n) space for the map-based solution unprompted | Blog Complexity section (agent-drafted) confirmed; not independently re-derived in conversation | met (confirmed, not derived) |
| Edge-case design | Covers empty list, self-referential random, no-random-pointers cases | Added the empty-list guard independently in code; full edge-case set verified by agent-run tests; blog edge-case list (agent-drafted) confirmed | met |
| Debugging discipline | Uses concrete tracing if bugs appear | Did not engage with mental-trace prompts (asked twice); converged much faster once told to actually run the file and read the real error message | partial — prefers empirical running over mental tracing (not a deficiency, a style note) |
| Communication | Clear English reasoning in comments and discussion | Two messages sent in Chinese despite English-only session preference; blog writing itself was entirely in clear English | needs improvement — flagged, not corrected mid-session |

## Intervention Count

- Clarifying questions: 2 (mental-trace prompts, largely unproductive)
- Hints: 1 (forward-reference guiding question, successful)
- Direct explanations: 1 (explicit method-wrapping syntax shown after two failed trace attempts)
- Code-level nudges: 0 (no code written for the user; all fixes were the user's own edits)

## Closeout Assessment

Algorithmic core (hash map, two-pass structure, forward-reference reasoning) was reached independently and quickly — strongest signal yet on recognizing *why* a two-pass structure is required, not just that it's needed. Implementation friction was entirely mechanical/syntax-level (return-outside-function from unwrapped class-body code, wrong constructor arg, near-miss infinite loop, accidental class deletion), not logical, and all were self-fixed. Debugging approach leaned on "run and read the error" rather than mental tracing, which converged faster than the two mental-trace prompts did — worth noting as an effective strategy for this user rather than a gap. All 7 tests pass against `attempt.py` including the deep-copy identity check. Blog's Correctness Argument was the strongest in the linked-list arc, explicitly covering all four `random`-pointer cases. One revision requested (Mistakes Made initially omitted the two most significant bugs) and fully applied on the first pass. Two English-only lapses this session, gently redirected. Overall: strong algorithmic session with a fast, unprompted core insight; the remaining coaching focus areas are process habits (save-before-run, English-only) rather than algorithmic understanding.
