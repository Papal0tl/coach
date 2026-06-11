# Algorithm Progress

This file is agent-maintained. Track algorithm-specific learning with archive-backed evidence.

## Sliding Window

| Date | Problem | Outcome | Notes |
| --- | --- | --- | --- |
| 2026-06-03 | Minimum Window Substring (LC 76) | Independent solve | Reached coverage counter pattern without hints. One range bug (len(t) vs len(s)). See archives/2026-06-03-minimum-window-substring/ |

**Assessment (2026-06-03):** Strong initial signal on sliding window. The coverage counter (`formed`) is the non-trivial part of this pattern and the user reached it independently. Next step: verify depth with a problem that requires deriving the window validity condition from scratch (e.g., Longest Substring Without Repeating Characters or Fruit Into Baskets).

## Hash Map / Frequency Counting

| Date | Problem | Outcome | Notes |
| --- | --- | --- | --- |
| 2026-06-03 | Minimum Window Substring (LC 76) | Independent solve | Used two frequency maps correctly. See archives/2026-06-03-minimum-window-substring/ |

## Two Pointers

Not yet observed in isolation. Sliding window sessions are partial evidence.

## Interval Sorting / Sort + Linear Scan

| Date | Problem | Outcome | Notes |
| --- | --- | --- | --- |
| 2026-06-05 | Merge Intervals (LC 56) | Solved with scaffolding | Had correct loop shape and overlap condition; missed sort and compared against wrong endpoint. Both fixed via tracing. See archives/2026-06-05-merge-intervals/ |

**Assessment (2026-06-05):** First exposure to the interval sort + scan pattern. The overlap condition (`cur_start <= last_end`) and the merge step (`max(end, cur_end)`) came naturally. The sort and the `res[-1]` vs `intervals[i-1]` distinction required guided tracing. Not a first-attempt independent solve, but scaffolding was light (2-3 hint steps, no direct explanation). Next step: Insert Interval (LC 57) or Meeting Rooms II (LC 253) to test whether sorting is now automatic for this class.

## Array Rotation / Cyclic Shift

| Date | Problem | Outcome | Notes |
| --- | --- | --- | --- |
| 2026-06-06 | Rotate Array (LC 189) | Solved with scaffolding | First attempt ignored k; recovered to slicing approach; slice assignment self-discovered; modulo reduction after one trace. See archives/2026-06-06-rotate-array/ |

**Assessment (2026-06-06):** First exposure to array rotation. The slicing restatement (last k + first n-k) is intuitive once found, but the user did not start there — first attempt iterated over all split positions and ignored k. Recovered in 3-4 hint steps. Solution is O(n) space; the O(1) reversal trick was not explored. Not a pressing gap for this problem, but worth introducing on a follow-up if in-place space constraint appears. Next step: a cyclic-shift variant where k is large or the in-place constraint is explicit (e.g., a problem requiring O(1) space).

## Prefix / Suffix Product (Two-Pass)

| Date | Problem | Outcome | Notes |
| --- | --- | --- | --- |
| 2026-06-10 | Product of Array Except Self (LC 238) | Solved with scaffolding | Brute force correct; left×right decomposition reached via guided tracing; two right-pass bugs fixed with hints; O(1) space independent. See archives/2026-06-10-product-of-array-except-self/ |

**Assessment (2026-06-10):** First exposure to the prefix/suffix product pattern. The O(n²) brute force was correctly identified and implemented. The critical insight — decompose `answer[i]` into a left prefix product and a right suffix product — was not independently discovered; it emerged through 3-4 guided questions and a worked trace table. Once the decomposition was named, the user correctly structured both passes. The O(1) space optimization (reusing the output array rather than allocating two arrays) was chosen independently — a sign of good space-complexity instinct. The invariant was verbalized correctly when asked: "answer[j] holds the product of all elements to the left of index j." Two implementation bugs in the right pass (overwrite instead of multiply-assign, wrong loop variable) were not self-caught. Next step: a problem where a similar left/right or prefix/suffix accumulation is required but less obvious (e.g., Trapping Rain Water uses a comparable two-pass structure) to test whether this decomposition pattern transfers.

## Index-as-Hash-Map (Cyclic Placement)

| Date | Problem | Outcome | Notes |
| --- | --- | --- | --- |
| 2026-06-11 | First Missing Positive (LC 41) | Solved with scaffolding | Two-pass skeleton written independently; swap mechanism reached via 2-3 guided questions; duplicate guard missed then caught via trace; invariant stated precisely and unprompted. See archives/2026-06-11-first-missing-positive/ |

**Assessment (2026-06-11):** First exposure to the index-as-hash-map pattern. The structural insight (two-pass: placement then scan) was independently written before the mechanism was understood — strongest structural instinct shown so far. The bound recognition ([1, n+1] → only care about values in [1, n]) required 2-3 guided questions. Once the bound was clear, the swap was written correctly on first try. The duplicate guard was not independently anticipated but caught immediately after a concrete trace of [1,1]. The invariant ("nums[i] == i+1 wherever i+1 was present") was stated precisely and unprompted in conversation — the best invariant articulation across all sessions. Next step: a problem where values fit in [1, n] but the state is more subtle (e.g., Find All Duplicates in an Array, or Find the Duplicate Number) to test whether the pattern now transfers independently.

## Dynamic Programming (1-D)

| Date | Problem | Outcome | Notes |
| --- | --- | --- | --- |
| 2026-06-03 | Maximum Subarray (LC 53) | Independent solve, first attempt | In-place Kadane's variant. Stated invariant precisely when asked. No bugs. See archives/2026-06-03-maximum-subarray/ |

**Assessment (2026-06-03):** Clean first-attempt solve using the in-place `nums[i] += max(nums[i-1], 0)` form. This is equivalent to canonical Kadane's but slightly less standard — suggests comfort with in-place mutation and DP state reuse. Invariant was correct in code and verbalized precisely on first ask. Next step: a 1-D DP problem where the recurrence is less obvious (e.g., Coin Change, House Robber II, or Jump Game) to test whether the user can derive the state definition from scratch rather than pattern-match to a known template.
