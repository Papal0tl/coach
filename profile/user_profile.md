# User Profile

## Preferences

- Preferred language: Python
- Default coaching mode: hint-only
- English-only practice: yes

## Current Goals

- Learn to solve LeetCode-style and complex programming problems through guided practice.

## Observed Strengths

- Pattern recognition: independently chose sliding window + coverage counter on first attempt for a Hard problem (minimum-window-substring, 2026-06-03); independently applied in-place Kadane's variant for a Medium DP problem (maximum-subarray, 2026-06-03).
- Data structure selection: correctly reached for two frequency maps without prompting.
- Logical structure: while-loop body logic (including correct order of operations for coverage counter decrement) was written correctly on first try.
- Invariant articulation (improving): stated the Kadane invariant precisely when asked — "nums[i] represents the maximum subarray sum ending exactly at index i" — without a revision cycle.

## Active Growth Areas

- Articulating invariants in writing: blog Key Insight sections describe mechanics well but tend not to name the invariant explicitly as a statement. Improving across sessions (no blog revision needed for invariant this time).
- Range/index precision: confused which string the window iterates over (`range(len(t))` vs `range(len(s))`) in the previous session. No recurrence this session.

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
