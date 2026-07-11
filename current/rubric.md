# Rubric

- Problem slug: `merge-k-sorted-lists`
- Archive path: `archives/2026-07-10-merge-k-sorted-lists/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Names this as a generalization of merge-two-sorted-lists to k lists | Blog Problem Summary and Key Insight both frame it this way unprompted | met |
| Constraint analysis | Notes k can be 0 or contain empty lists; total N bounded at 10^4 | Edge cases (agent-filled, user-confirmed) cover empty `lists`, all-`None` lists, mixed empty/non-empty | met |
| Brute-force construction | Names collect-all-then-sort (O(N log N)) or naive pairwise scan (O(Nk)) before optimizing | Blog Brute Force section names collect-and-sort with correct O(N log N)/O(N) complexity | met |
| Pattern recognition | Reaches for a min-heap or divide-and-conquer pairwise merge for the k-way minimum-extraction pattern | Not met — reused the two-list merge routine as a sequential fold (O(N·k)) instead; did not spontaneously reach for divide-and-conquer or a heap. Declined the offer to implement the faster alternative | not met |
| Invariant formulation | States that the heap holds at most one current head per list, and that the global min must be one of those heads | N/A — user's approach doesn't use a heap; instead correctly stated the fold invariant ("merge contains all nodes from lists processed so far, and remains sorted") precisely and unprompted in the blog | met (alternate invariant) |
| Complexity analysis | States O(N log k) time and O(k) auxiliary space, and why log k beats scanning k heads | Correctly named O(N log k) for divide-and-conquer vs. O(N·k) for own sequential fold; needed one guided trace (count rounds and per-round work for k=8) to isolate the log k factor before deriving it fully unassisted | met (guided) |
| Edge-case design | Covers empty `lists`, `lists` of all `None`, single list, duplicate values | All 8 local test cases pass, including these; blog Edge Cases section lists them accurately | met |
| Debugging discipline | Runs code / traces concrete example rather than guessing on heap-tuple comparison errors | N/A (no heap used); the one real bug (`.val` copy instead of relink) was fixed correctly after being asked to run the code and trace `cur` — consistent with established empirical-debugging preference | met (adapted) |
| Communication | Explains tradeoff between heap and divide-and-conquer approaches if asked | Correctly explained the O(N·k) vs. O(N log k) tradeoff when asked, after one guided round-counting question | met (guided) |

## Intervention Count

- Clarifying questions: 2 (complexity round-counting trace; sequential-fold trace-to-crash)
- Hints: 0
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

Correct, fully tested solution (O(N·k) sequential fold) reached with a single trace-based intervention for the one real bug. Complexity comparison to the optimal O(N log k) approach was fully self-derived once broken into a concrete counting exercise, though the faster approach itself was not implemented (declined) and was not the user's spontaneous first choice — this generalizes merge-two-sorted-lists cleanly but does not yet show the sort-list-style divide-and-conquer instinct transferring to a k-way problem where a sequential fallback is available. Session's clearest gap is unrelated to algorithm skill: the Mistakes Made blog section fabricated a bug that never occurred (per git history) and omitted the two real ones, continuing the pattern from the immediately preceding session (sort-list) for a second consecutive time. See `agent_only/user_assessment.md` (session 23) for full detail.
