# User Profile

## Preferences

- Preferred language: Python
- Default coaching mode: hint-only
- English-only practice: yes

## Current Goals

- Learn to solve LeetCode-style and complex programming problems through guided practice.

## Observed Strengths

- Pattern recognition (established patterns): independently chose sliding window + coverage counter on first attempt for a Hard problem (minimum-window-substring, 2026-06-03); independently applied in-place Kadane's variant for a Medium DP problem (maximum-subarray, 2026-06-03).
- Data structure selection: correctly reached for two frequency maps without prompting.
- Logical structure: while-loop body logic (including correct order of operations for coverage counter decrement) was written correctly on first try.
- Invariant articulation (improving): stated the Kadane invariant precisely when asked; correctness argument in merge-intervals blog correctly named why `res[-1]` is the only comparison needed after sorting.
- Tracing discipline: willing to trace concrete examples when prompted; reached both the sorting insight and the `res[-1]` fix through tracing without direct explanation.
- In-place Python: self-discovered `nums[:] = ...` slice assignment after one rebind prompt (rotate-array, 2026-06-06).

## Active Growth Areas

- Preprocessing recognition: did not immediately sort in merge-intervals; needed one tracing exercise to discover that unsorted input breaks the overlap check. Watch for this in other problems where a sort or preprocessing step is the key unlock.
- Input→algorithm connection: first attempt on rotate-array (2026-06-06) ignored the parameter k entirely — built a loop unrelated to the input. Not self-caught; needed a trace prompt. Watch for this pattern in future first attempts.
- Articulating invariants in writing: blog Key Insight sections describe mechanics well but tend not to name the invariant explicitly as a statement. Improving across sessions.
- Range/index precision: confused which string the window iterates over (`range(len(t))` vs `range(len(s))`) in the first session. No recurrence since.

## Common Failure Modes

- Copy-paste artifacts from LeetCode (nested class structure) cause syntax errors that aren't caught until runtime.
- Edits made in IDE don't get saved before reporting "done" — requires a reminder to save.

## Coaching Preferences

- Ask guiding questions before giving direct explanations.
- Require English reasoning and writing.

## Recent Session Summaries

| Date | Problem | Archive | Summary |
| --- | --- | --- | --- |
| 2026-06-03 | Minimum Window Substring (LC 76) | archives/2026-06-03-minimum-window-substring/ | Independently reached sliding window + coverage counter. One range bug, one paste artifact. Blog accepted after one revision. |
| 2026-06-03 | Maximum Subarray (LC 53) | archives/2026-06-03-maximum-subarray/ | Correct in-place Kadane's on first attempt. No bugs. Stated invariant precisely when asked. Blog accepted after one revision (missing pattern-recognition section). |
| 2026-06-05 | Merge Intervals (LC 56) | archives/2026-06-05-merge-intervals/ | Had correct loop shape but missing sort and comparing against wrong endpoint. Both fixed through tracing. Complexity stated correctly after one prompt. Blog accepted after one revision (pattern recognition section). |
| 2026-06-06 | Rotate Array (LC 189) | archives/2026-06-06-rotate-array/ | First attempt ignored k entirely. Recovered to correct slicing approach; independently chose slice assignment for in-place. Modulo reduction reached after one trace. Blog accepted after typo fix; pattern-recognition section written meaningfully on first attempt. |
