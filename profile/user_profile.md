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
- Invariant articulation (improving): stated the Kadane invariant precisely when asked; correctness argument in merge-intervals blog correctly named why `res[-1]` is the only comparison needed after sorting. In session 6 (first-missing-positive), stated the placement invariant precisely and unprompted: "nums[i] == i+1 wherever i+1 was present."
- Tracing discipline: willing to trace concrete examples when prompted; reached both the sorting insight and the `res[-1]` fix through tracing without direct explanation.
- In-place Python: self-discovered `nums[:] = ...` slice assignment after one rebind prompt (rotate-array, 2026-06-06).
- O(1) space reuse: independently chose to reuse the output array for the prefix/suffix product solution without prompting (product-of-array-except-self, 2026-06-10); jumped straight to O(1) marker approach for set-matrix-zeroes without attempting O(m+n) first (2026-06-15).
- Structural instinct: wrote correct two-pass skeleton (placement + scan) before the swap mechanism was fully worked out (first-missing-positive, 2026-06-11).
- Simulation pattern recognition: independently reached shrinking-boundary simulation for spiral-matrix (2026-06-24) without being guided to it; guard conditions present in first complete attempt.
- Matrix transformation (4-way cycle): independently implemented correct 4-way cycle for rotate-image (2026-06-29) — loop bounds, coordinate pairs, and assignment order all correct on first complete attempt; zero bugs.
- Two-pointer list synchronization: went from `pass` directly to the correct two-pointer redirect solution for intersection-of-two-linked-lists (2026-07-03) in a single attempt — no intermediate hints, zero logical bugs. Strongest first-attempt signal yet on a genuinely novel (non-matrix) pattern.
- Self-reflection during writing: independently caught the `!=` vs `is not` accidental-correctness gap while writing the blog's Mistakes Made section, then fixed the code before being asked (2026-07-03).
- Linked-list pointer rewiring: correct iterative reversal (three-pointer walk with saved `next`) on the first attempt for reverse-linked-list (2026-07-03), zero bugs; stated the loop invariant ("prev holds the reversed sublist, cur holds the remaining unprocessed sublist") precisely and unprompted when asked.
- Constraint-driven approach selection: for palindrome-linked-list (2026-07-03), correctly identified that a singly linked list can't be indexed or walked backward and chose the value-copy-and-compare workaround without prompting; stated O(n) time / O(n) space complexity unprompted.
- Fast/slow pointer reasoning: for linked-list-cycle (2026-07-05), solved with a hash set first (zero bugs), then named "fast and slow pointer" unprompted as the O(1)-space alternative and wrote fully correct code plus an accurate two-case correctness argument for it in the blog — independently verified against the full test suite. First correct production of this specific sub-pattern after two prior declines.

## Active Growth Areas

- Preprocessing recognition: did not immediately sort in merge-intervals; needed one tracing exercise to discover that unsorted input breaks the overlap check. Watch for this in other problems where a sort or preprocessing step is the key unlock.
- Input→algorithm connection: first attempt on rotate-array (2026-06-06) ignored the parameter k entirely — built a loop unrelated to the input. Not self-caught; needed a trace prompt. Watch for this pattern in future first attempts.
- Articulating invariants in writing: blog Key Insight sections describe mechanics well but tend not to name the invariant explicitly as a statement. Improving across sessions — set-matrix-zeroes correctness argument stated the iff condition correctly on first draft.
- Range/index precision: confused which string the window iterates over (`range(len(t))` vs `range(len(s))`) in the first session. No recurrence since.

## Common Failure Modes

- Copy-paste artifacts from LeetCode (nested class structure) cause syntax errors that aren't caught until runtime.
- Edits made in IDE don't get saved before reporting "done" — requires a reminder to save.
- Syntax/API-level slips distinct from logic bugs: in palindrome-linked-list (2026-07-03), three bugs were all mechanical rather than conceptual — a 4-argument `range()` call, indexing a scalar (`cur.val[i]`) instead of the intended list, and lowercase `true`/`false` (non-Python capitalization). The underlying algorithm was correct in each case; the bugs were in translating it to valid Python syntax. Each was fixed quickly (one guided question or trace each) but none were self-caught before running.
- Declining hands-on implementation of optional follow-ups once a correct baseline works: reverse-linked-list's recursive variant and palindrome-linked-list's O(1)-space variant (both 2026-07-03) were declined outright; linked-list-cycle's O(1)-space variant (2026-07-05) was not implemented in `attempt.py` either, but this time was reasoned through and coded correctly in the blog instead of skipped — a partial shift from "decline" to "derive without running."

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
| 2026-06-10 | Product of Array Except Self (LC 238) | archives/2026-06-10-product-of-array-except-self/ | First attempt was correct brute force O(n²). Reached left×right decomposition via guided tracing. Two-pass structure written independently once decomposition was clear. Two right-pass bugs fixed after hints. O(1) space (output reuse) achieved independently. Blog accepted after one revision (invariant precision, missing bug). |
| 2026-06-11 | First Missing Positive (LC 41) | archives/2026-06-11-first-missing-positive/ | Two-pass structure written independently before swap mechanism was known. Swap correct on first try. Duplicate guard missed; caught after one concrete trace. Invariant stated precisely and unprompted. Blog accepted after 2 revisions. |
| 2026-06-15 | Set Matrix Zeroes (LC 73) | archives/2026-06-15-set-matrix-zeroes/ | Jumped straight to O(1) marker approach without prompting. Cascade-corruption and variable-swap bugs not self-caught. All fixed through trace hints. Blog accepted after 1 revision (How to Recognize section). |
| 2026-06-24 | Spiral Matrix (LC 54) | archives/2026-06-24-spiral-matrix/ | Independently reached shrinking-boundary simulation. Guard conditions in first complete attempt. Two bugs (typo, wrong boundary direction) not self-caught but fixed after one hint each. Blog accepted (mistakes section removed). |
| 2026-06-29 | Rotate Image (LC 48) | archives/2026-06-29-rotate-image/ | Stated "transpose then flip" but independently implemented correct 4-way cycle. Loop bounds and coordinate pairs correct on first attempt. Zero bugs. Blog accepted first pass (mistakes section kept as-is). |
| 2026-07-02 | Search a 2D Matrix II (LC 240) | archives/2026-07-02-search-a-2d-matrix-ii/ | Drafted incomplete row-pruning loop then pivoted to optimal staircase search independently. Zero bugs in final attempt. Staircase reasoning explained correctly. Blog required 3 revision cycles: 4 blank sections initially, then an English-only violation (Chinese text), then blank correctness argument. Correctness argument accurate once written. |
| 2026-07-03 | Intersection of Two Linked Lists (LC 160) | archives/2026-07-03-intersection-of-two-linked-lists/ | Went from `pass` straight to the correct two-pointer redirect solution in one commit, zero bugs, no hints needed. Used `!=` instead of `is not` (accidentally correct); self-caught this exact gap while writing the blog's Mistakes Made section and fixed the code before closeout. Blog accepted with zero revisions on substantive content. |
| 2026-07-03 | Reverse Linked List (LC 206) | archives/2026-07-03-reverse-linked-list/ | Correct iterative reversal on first attempt, zero bugs. Stated the loop invariant precisely and unprompted when asked. Declined the recursive follow-up when offered. Blog accepted with zero revisions; correctness argument was the strongest section. |
| 2026-07-03 | Palindrome Linked List (LC 234) | archives/2026-07-03-palindrome-linked-list/ | Correctly identified the no-backward-traversal constraint and chose value-copy-and-compare (O(n) space) without prompting. Three syntax-level bugs (4-arg `range()`, wrong index source, lowercase `true`/`false`) fixed via guided questions/traces, not self-caught before running. Declined the O(1)-space (fast/slow pointer + in-place reversal) follow-up. Blog accepted after 1 revision (blank correctness argument, inaccurate "N/A" mistakes section). |
| 2026-07-05 | Linked List Cycle (LC 141) | archives/2026-07-05-linked-list-cycle/ | Correct hash-set solution first, zero bugs. Stated O(n)/O(n) complexity unprompted; named fast/slow pointer unprompted as the O(1) alternative and wrote correct code plus an accurate correctness argument for it in the blog (not implemented in attempt.py, but verified independently against tests). First successful production of the fast/slow sub-pattern after two prior declines. Blog accepted with zero required revisions (one optional `==` vs `is` style note). |
