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

## Two Pointers / Fast-Slow (Floyd's)

| Date | Problem | Outcome | Notes |
| --- | --- | --- | --- |
| 2026-07-05 | Linked List Cycle (LC 141) | Hash-set solved independently first, zero bugs; fast/slow written correctly in blog (not run) | Named fast/slow unprompted when asked for an O(1)-space alternative; wrote correct guard conditions, meeting check, and two-case correctness argument. Verified independently against tests. See archives/2026-07-05-linked-list-cycle/ |
| 2026-07-05 | Linked List Cycle II (LC 142) | Hash-set solved independently (entry-node variant), zero logical bugs; O(1)-space Floyd's follow-up declined entirely, not even derived in prose | Correctly scoped the problem as finding the entry node, not just detecting a cycle. One mechanical `null`→`None` bug fixed after one guided question. Declined the O(1)-space two-pointer-reset technique outright when offered — no mention of it anywhere, unlike LC 141 same day. See archives/2026-07-05-linked-list-cycle-ii/ |

**Assessment (2026-07-05, LC 141):** First exposure with an actual result, after being declined as a follow-up in both the reverse-linked-list and palindrome-linked-list sessions (2026-07-03). Reached for the hash-set/visited-node approach first (consistent with the extra-space-first ordering seen in every prior linked-list session), zero bugs. When asked directly if an O(1)-space approach exists, named "fast and slow pointer" immediately and — rather than declining outright as in the two prior sessions — wrote fully correct code for it in the blog: proper `fast is not None and fast.next is not None` guard, correct meeting check, and a two-case correctness argument (no-cycle: fast reaches `None` strictly ahead of slow; cycle: the gap between fast and slow shrinks by one each iteration once both are inside the loop, so they must meet). This was not typed into `attempt.py` or run by the user, but was independently verified against the full reference test suite and passed. Repeated the same `==` vs `is` node-identity gap seen in the intersection-of-two-linked-lists blog (session 11) — that time self-caught, this time not, flagged as a non-blocking review note. Remaining gap: hands-on, typed-and-run implementation of fast/slow (as opposed to written derivation) is still unobserved.

**Assessment (2026-07-05, LC 142, same day, immediately following):** This was the direct test of whether the fast/slow hands-on gap would close, since LC 142's canonical solution is exactly this technique extended to locate the cycle entry (meet inside the cycle, reset one pointer to head, advance both one step at a time). Instead of progress, this session reverted further than LC 141: the user again reached for the hash-set solution first (correct, one mechanical `null`/`None` bug), and when offered the O(1)-space follow-up, declined it outright with no prose derivation at all — a step back from LC 141's "declined the code but reasoned it through in the blog" middle ground. The technique remains completely unobserved as typed-and-run code after two consecutive dedicated opportunities. Given this is now the second dedicated attempt to elicit it (not just the fourth generic follow-up decline), recommend not offering it as an optional next step again — either make it the explicit primary task in a future session framed around it, or ask directly why the O(1) variant is consistently declined once a working solution exists, since the pattern is stable enough now that guessing at the cause (confidence vs. low interest vs. fatigue) isn't productive without asking. Next step: Middle of the Linked List (LC 876), or revisit LC 142 later, but frame the O(1)-space approach as required rather than optional.

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

## Matrix Marker / First Row+Col as Marker Space

| Date | Problem | Outcome | Notes |
| --- | --- | --- | --- |
| 2026-06-15 | Set Matrix Zeroes (LC 73) | Solved with scaffolding (implementation bugs only) | Jumped to O(1) approach independently. Cascade-corruption, variable swap, range error fixed via hints. See archives/2026-06-15-set-matrix-zeroes/ |

**Assessment (2026-06-15):** First exposure to the border-as-marker pattern. The O(1) space instinct was unprompted — the user went straight to the advanced approach, which is stronger than any prior "O(1) independently chosen" signal (LC 238 and rotate-array were also O(1) but the path was more scaffolded). The structural insight (first row/col as marker arrays, saved booleans for the border itself) was correctly grasped. Implementation bugs were mechanical: cascade-corruption when zeroing included j=0, variable names swapped in detection loops, range(n) vs range(m). None were self-caught, but all resolved in 2-4 hint steps. The "repurpose input structure under strict space constraint" generalisation in the blog was the clearest pattern-recognition statement across all sessions. Next step: a matrix problem where the O(1) trick involves something other than the border (e.g., Rotate Image in-place, or a problem using sign-flipping as markers) to test whether the abstraction "repurpose existing structure" now transfers, or if it's still tied to the first-row/col specific case.

## Matrix Rotation / 4-Way Cycle

| Date | Problem | Outcome | Notes |
| --- | --- | --- | --- |
| 2026-06-29 | Rotate Image (LC 48) | Independent solve, zero bugs | Stated "transpose+flip" but implemented 4-way cycle correctly. Loop bounds and coordinate pairs correct on first attempt. See archives/2026-06-29-rotate-image/ |

**Assessment (2026-06-29):** First exposure to in-place matrix rotation. Two valid approaches exist (transpose+reverse-rows; 4-way cycle) — the user verbally named one but coded the other, suggesting awareness of both. The 4-way cycle was implemented with correct ring bounds (`range(n//2)`, `range(i, n-i-1)`) and all four coordinate pairs on the first complete attempt. No bugs. This is the strongest matrix-specific performance yet: the prior matrix sessions (LC 73, LC 54) both had mechanical bugs not self-caught; this session had none. Blog correctness argument explicitly named the four cycle positions. The invariant (each ring processed exactly once from outside in) was not explicitly stated. Next step: a matrix transformation or traversal problem with a less symmetric structure (e.g., Diagonal Traverse, Spiral Matrix II, or Search a 2D Matrix II) to determine whether the spatial instinct now generalises beyond symmetric n×n operations.

## Matrix Traversal / Shrinking Boundary Simulation

| Date | Problem | Outcome | Notes |
| --- | --- | --- | --- |
| 2026-06-24 | Spiral Matrix (LC 54) | Independent reach, implementation bugs | Reached shrinking-boundary approach without prompting. Guard conditions in first complete attempt. Typo and wrong boundary direction (`right += 1`) not self-caught but fixed after one hint each. See archives/2026-06-24-spiral-matrix/ |

**Assessment (2026-06-24):** First exposure to spiral/layer traversal. This is the cleanest independent-reach signal across all novel patterns so far: the user reached for four shrinking boundaries without being told, and the guard conditions (`if top <= bottom`, `if left <= right`) appeared correctly in the first complete attempt. The only bugs were mechanical (a typo and a sign error on one boundary update) — not structural. The blog explained the guard conditions correctly. The invariant was not named explicitly, consistent with the persistent gap in blog writing.

**Follow-up (2026-06-29 — LC 48 Rotate Image):** The adjacent matrix problem (in-place rotation) was solved independently and bug-free, with correct ring and position logic on the first attempt. Spatial instinct across matrix problems is now demonstrably generalising. See archives/2026-06-29-rotate-image/. Next step: a traversal problem with non-square or irregular structure to probe the limit of this generalisation.

## Matrix Search / Staircase Search

| Date | Problem | Outcome | Notes |
| --- | --- | --- | --- |
| 2026-07-02 | Search a 2D Matrix II (LC 240) | Independent reach, zero bugs | Initial row-pruning draft abandoned before completion. Pivoted to staircase search independently. Correct implementation on first complete attempt. See archives/2026-07-02-search-a-2d-matrix-ii/ |

**Assessment (2026-07-02):** First exposure to the staircase search pattern. The initial approach (row-by-row pruning by truncating rows when an element exceeds target) was incomplete — no equality check, no return value, would have caused IndexError on truncated rows under continued iteration. The user abandoned it before submitting and pivoted to the correct staircase approach independently. The staircase reasoning was explained correctly in conversation: top-right corner has opposing move directions, each comparison eliminates a full row or column, O(m+n) follows. Zero bugs in final implementation. Blog correctness argument required explicit prompting but was accurate once written. Next step: LC 74 (Search a 2D Matrix) to compare — that matrix has a stronger sorted property (each row's first element > previous row's last), enabling binary search; the contrast would test whether the user can select the right approach based on which property holds.

## Two Pointers / Linked List Synchronization

| Date | Problem | Outcome | Notes |
| --- | --- | --- | --- |
| 2026-07-03 | Intersection of Two Linked Lists (LC 160) | Independent solve, zero bugs | Went from `pass` to the correct two-pointer redirect in a single attempt, no intermediate hints. See archives/2026-07-03-intersection-of-two-linked-lists/ |

**Assessment (2026-07-03):** First exposure to linked-list two-pointer synchronization and the first linked-list problem overall. The core insight (redirect each pointer to the other list's head to equalize total path length at m + n) was applied correctly with no scaffolding — the strongest first-attempt signal yet on a non-matrix novel pattern, with no intermediate commits showing trial and error. The only gap was using `!=` instead of `is not` for node comparison; this is accidentally correct only because `ListNode` has no `__eq__` override. The user identified this exact issue independently while writing the blog's Mistakes Made section, then corrected `attempt.py` to `is not` before the agent's review even required it — the first observed instance of self-catching a gap during reflective writing rather than through a coaching trace prompt. Correctness argument (m + n - c equalization) was precise and complete on first blog submission; zero revision cycles needed. Next step: a single-list two-pointer problem (e.g., Linked List Cycle II — LC 142, or Middle of the Linked List) to test whether pointer-synchronization reasoning transfers to a different list topology, and whether the `is`/`==` distinction is now applied by default without a rubric prompt.

## Linked List Reversal / In-Place Pointer Rewiring

| Date | Problem | Outcome | Notes |
| --- | --- | --- | --- |
| 2026-07-03 | Reverse Linked List (LC 206) | Independent solve, zero bugs | Correct three-pointer walk (prev/cur/saved-next) on first attempt. Loop invariant stated precisely and unprompted when asked. See archives/2026-07-03-reverse-linked-list/ |

**Assessment (2026-07-03):** Second linked-list problem, same day as the Two Pointers / Linked List Synchronization session above (LC 160), testing a distinct sub-skill: in-place pointer rewiring rather than cross-list synchronization. The three-pointer pattern (save `cur.next` before overwriting, advance `prev` and `cur`) was correct on the first attempt with no scaffolding, including correct `prev = None` initialization and empty-list handling with no special-casing. When asked directly "can you state the invariant," the answer was immediate and precise: "prev holds the reversed sublist, cur holds the remaining unprocessed sublist." This is the cleanest on-demand invariant articulation yet — no hedging, no partial answer. The user declined the recursive-variant follow-up when offered — first explicit opt-out of an optional extension observed in any session. Next step: a fast/slow two-pointer problem on a single list (Linked List Cycle II — LC 142, or Middle of the Linked List — LC 876) to test a third linked-list sub-pattern (cycle/midpoint detection) distinct from both intersection-sync and reversal.

## Palindrome Check / Structure Conversion (Linked List → Array)

| Date | Problem | Outcome | Notes |
| --- | --- | --- | --- |
| 2026-07-03 | Palindrome Linked List (LC 234) | Independent approach, syntax-level bugs | Correctly identified no-backward-traversal constraint and converted to a value list to enable comparison. Three syntax bugs (4-arg `range()`, wrong index source, lowercase `true`/`false`) fixed via guided questions. O(1)-space fast/slow-pointer variant declined. See archives/2026-07-03-palindrome-linked-list/ |

**Assessment (2026-07-03):** Third linked-list problem of the day, testing a new sub-skill: recognizing that a structural limitation (no backward/random access on a singly linked list) can be worked around by converting to a more capable structure (a Python list), rather than needing pointer-level cleverness. This constraint recognition was unprompted and correctly articulated in the blog's Initial Intuition. The reversed-list-building loop is the actual novel logic here, and it held one off-by-one-adjacent bug (4-argument `range()` call) — resolved by tracing a concrete 3-element example rather than being told the fix directly. The other two bugs (`cur.val[i]` vs `vals[i]`, lowercase `true`/`false`) were copy/paste or cross-language habits, not reasoning errors. The O(1)-space optimization (fast/slow pointer to find the middle, then reverse and compare in place, reusing the exact reversal mechanics from the same day's LC 206 session) was proposed by the user, then declined in favor of moving to the blog — meaning the fast/slow-pointer technique specifically remains completely unobserved across all 13 sessions to date, despite two adjacent sessions (this one and LC 206) that could have naturally led into it. Next step: make Linked List Cycle (LC 141) or Middle of the Linked List (LC 876) a required rather than optional next problem, specifically to close this gap before it accumulates further as "the one two-pointer sub-pattern never tested."

## Dynamic Programming (1-D)

| Date | Problem | Outcome | Notes |
| --- | --- | --- | --- |
| 2026-06-03 | Maximum Subarray (LC 53) | Independent solve, first attempt | In-place Kadane's variant. Stated invariant precisely when asked. No bugs. See archives/2026-06-03-maximum-subarray/ |

**Assessment (2026-06-03):** Clean first-attempt solve using the in-place `nums[i] += max(nums[i-1], 0)` form. This is equivalent to canonical Kadane's but slightly less standard — suggests comfort with in-place mutation and DP state reuse. Invariant was correct in code and verbalized precisely on first ask. Next step: a 1-D DP problem where the recurrence is less obvious (e.g., Coin Change, House Robber II, or Jump Game) to test whether the user can derive the state definition from scratch rather than pattern-match to a known template.
