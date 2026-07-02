# Agent-Only User Assessment

This file is agent-maintained. Keep it candid, evidence-backed, and in English.

## Longitudinal Summary

Ten sessions observed (2026-06-03 through 2026-07-02). Sessions 1 and 2 (LC 76, LC 53) were first-attempt solves on familiar patterns. Session 3 (LC 56) revealed a missing preprocessing instinct. Session 4 (LC 189, rotate-array) introduced a new failure mode: the first attempt completely ignored the input parameter k. Session 5 (LC 238, product-of-array-except-self) was the first clean test on a genuinely novel decomposition; required 3-4 guided questions but recovered fast and chose O(1) space independently. Session 6 (LC 41, first-missing-positive) is notable for two things: the user wrote the correct two-pass skeleton before knowing the mechanism — the strongest structural instinct shown yet — and stated the invariant precisely and unprompted. Session 7 (LC 73, set-matrix-zeroes) showed a new strength: the user jumped straight to the O(1) marker approach without attempting the O(m+n) solution first, showing the O(1) space instinct is now a default rather than a prompted choice. Session 8 (LC 54, spiral-matrix) is the clearest independent pattern-reach yet for a novel traversal structure: shrinking-boundary simulation reached without any prompting, and guard conditions present in the first complete attempt. Two bugs (typo, wrong boundary direction) were not self-caught. Session 9 (LC 48, rotate-image) is notable for being the first session with zero bugs: the user implemented the 4-way cycle with correct loop bounds and coordinate pairs on the first complete attempt. Verbally stated "transpose then flip" but wrote a 4-way cycle — suggesting awareness of both approaches. The planned self-catching intervention (trace before feedback) was not exercised because there were no bugs to catch. Self-catching over the full history: 6 of 9 sessions had uncaught bugs; sessions 2 and 9 were bug-free. Session 10 (LC 240, search-a-2d-matrix-ii): user initially drafted an incomplete row-by-row pruning approach (no equality check, no return value, would crash on truncated rows), then pivoted to the staircase search before submitting a complete first attempt. Zero bugs in final implementation. Blog required 3 revision cycles — initial 4 blank sections, one English-only violation (Chinese text inserted then corrected), and a blank correctness argument that required repeated prompting. The correctness argument was accurate once written. A new recurring pattern: the correctness argument section is consistently the last section to be written and requires explicit prompting each session.

## Strengths

- **Pattern recognition**: Two independent first-attempt solves across different algorithmic families (sliding window, DP/greedy). Reached non-trivial variants (coverage counter, in-place Kadane) without hints.
- **Data structure instinct**: Frequency maps, in-place mutation — selected without prompting.
- **Invariant understanding in code**: Implementations are correct and reveal internalized invariants even when the user doesn't verbalize them.
- **Improving verbalization**: Stated the Kadane invariant precisely when asked in session 2, without a blog revision cycle (contrast with session 1 where blog needed one revision).

## Recurring Weaknesses

- **Range/index slips**: `range(len(t))` instead of `range(len(s))` in session 1. Not repeated in sessions 2 or 3 (no two-sequence problems). Watch for recurrence.
- **Preprocessing step recognition**: Did not immediately sort in merge-intervals (session 3). The sort is the critical unlock for this problem class. Needed one tracing exercise to discover it. Watch whether this recurs on other "sort first" problems (meeting rooms, insert interval, etc.).
- **Invariant in writing**: Blog Key Insight sections explain the mechanics correctly but tend not to name the invariant as an explicit statement. Revision needed in sessions 1 and 5 (LC 76, LC 238). Sessions 2-4 did not require invariant revisions (no novel invariant in those problems). Still a recurring gap to watch.
- **Pattern-recognition section discipline**: Required revision in sessions 1-3. Sessions 4 and 5 both had meaningful signals written on first attempt. Trend positive — appears to be stabilizing.
- **Self-catching bugs before reporting done**: Sessions 1, 4, 5, 6, 7, and 8 all had bugs not self-caught. 6 of 8 sessions. Session 8: typo and wrong boundary direction — neither caught before asking for feedback. Consistent "submit early and rely on feedback" habit. The planned intervention (ask user to trace before feedback) was not executed in session 8. Must execute this in the next session: hold back any hint until the user has traced through a concrete example themselves.

## Communication Habits

- Terse. Accurate. No hedging.
- Chat-as-editor habit (typing edits into chat) has not recurred since session 1.

## Debugging Habits

- Session 2: zero bugs. No debugging needed.
- Session 1: range bug not self-caught; needed trace prompt. Syntax error not caught before reporting done. These may be artifacts of unfamiliarity with the file-based workflow rather than weak debugging instincts. Monitor in future sessions.

## Confidence and Pacing

- Fast. Submitted working solutions in both sessions before asking questions. Appropriate confidence — not over-explaining, not hedging.

## Blog Quality Trends

- Session 1 (LC 76): Key Insight needed one revision (coverage counter mechanics not fully explained). One TODO left in place.
- Session 2 (LC 53): All substantive sections correct on first submit. Completeness gap only (missing pattern-recognition section). Trend positive.
- Session 3 (LC 56): All substantive sections correct on first submit. Pattern-recognition section listed problem names instead of signals — revised correctly on first request. Correctness argument was the strongest yet: explicitly stated why `res[-1]` suffices after sorting.

## Spaced Repetition Needs

- `range(len(s))` vs `range(len(t))` — watch for recurrence in next two-sequence problem.
- Preprocessing / sorting as a first step — probe again on next interval-family problem (e.g., Insert Interval, Meeting Rooms II) to see if the sort is now automatic.
- Input→algorithm connection — confirmed stable over 3 sessions (LC 238, LC 41, LC 73). Close this concern.
- Self-catching bugs — 6 of 10 sessions with uncaught bugs. Sessions 2, 9, and 10 were bug-free in the final attempt. Session 10 initial attempt was incomplete (no equality check, no return value) — submitted early without catching it. Next session with a real bug: hold back all feedback until the user has traced a concrete example themselves. Do not skip.
- Correctness argument in blog — blank on initial submission every session. Session 10 required 3 saves and explicit prompting before the section appeared. Consider reminding the user to write this section specifically before they say "done."
- Invariant articulation — LC 48 and LC 240 blogs both passed without explicitly naming the invariant as a formal statement. The reasoning is implicit but correct. Still the most consistent writing gap.
- Matrix search transfer — LC 240 showed the staircase search reached independently. Next matrix problem should test a non-uniform search structure (e.g., binary search on sorted matrix LC 74, or a problem requiring row/column binary search rather than staircase) to probe how general the spatial reasoning now is.
