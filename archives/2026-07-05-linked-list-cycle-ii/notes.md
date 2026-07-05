# Session Notes

- Problem slug: `linked-list-cycle-ii`
- Archive path: `archives/2026-07-05-linked-list-cycle-ii/`

## Agent Preparation

- Pattern: Floyd's cycle detection, extended to locate the cycle entry point.
- Key insight: after slow/fast meet inside the cycle, resetting one pointer to `head` and advancing both one step at a time makes them meet exactly at the cycle's start node. This follows from the distance relationship between the pre-cycle length and the meeting point.
- Invariant or state: let the distance from head to cycle start be `a`, from cycle start to the meeting point be `b`, and the remaining cycle length be `c`. When slow and fast meet, slow has traveled `a + b`, and it can be shown `a = c - b` (mod cycle length), so walking `a` steps from head and `a` steps from the meeting point land on the same node.
- Complexity target: O(n) time, O(1) space (the hash-set approach is an acceptable first pass but the O(1) variant is the real target here since it directly builds on the prior session's fast/slow work).

## Reference Solution Summary

Fast/slow pointers detect a cycle by meeting inside it. Once they meet, reset one pointer (`ptr`) to `head` and advance both `ptr` and `slow` one step at a time; they meet again exactly at the cycle's entry node. Proof sketch: let `a` = distance from head to cycle start, `b` = distance from cycle start to the meeting point, `c` = remaining cycle length after the meeting point (so cycle length = `b + c`). Slow has traveled `a + b` when they meet; fast has traveled `2(a + b)` and is also `a + b` steps ahead of slow within the cycle relative to a lap, giving `a + b ≡ 0 (mod b + c)` from `fast_dist - slow_dist = a + b` being a multiple of the cycle length. This reduces to `a ≡ c (mod cycle length)`, i.e. walking `a` more steps from the meeting point (mod cycle length) lands back at the cycle start — which is exactly what walking `a` steps from `head` does. Validated locally against 7 cases (no `pytest` needed; ran directly with `python3 tests.py`).

If the O(1)-space two-pointer approach isn't reached, a hash-set fallback also works: walk the list, and the first node seen twice is the cycle entry (O(n) space). Useful as a stepping stone if hinting is needed, since the user already used hash sets for LC 141.

## Edge Cases

- Empty list (`head = None`) → return `None`.
- Single node, no cycle → return `None`.
- Single node pointing to itself → return that node.
- Cycle starts at head (`pos = 0`).
- Cycle starts at the last node (tail points to itself effectively via a short cycle).
- No cycle, long list.

## User-Facing Takeaways

- First attempt: hash-set approach, logic is correct (first repeated node = cycle entry). This matches the fallback noted in prep above.
- Bug: `return null` on the final line — `null` is not a Python keyword (JS/Java carryover), will raise `NameError`. Same category as the palindrome-linked-list session's `true`/`false` capitalization slip — mechanical, not conceptual. Fixed after one guided question ("what does the loop actually return?") — recognized `None` vs `null` immediately once prompted to look at that line; not self-caught before being asked, but no further hint needed.
- Fixed attempt (hash-set, O(n) time / O(n) space) passes all 7 reference tests.

## Follow-Up Candidates

- Prove why `a = c - b` holds (math derivation), if not already covered in the blog.
- Compare against the hash-set approach the user already knows from LC 141.

## Follow-Up Decisions

- O(1)-space two-pointer variant (finding meeting point then resetting one pointer to head) was offered after the working hash-set solution passed all tests. User declined and moved straight to the blog. Consistent with the established pattern of declining optional space-optimization follow-ups (reverse-linked-list recursion, palindrome-linked-list O(1) space) — this is the fourth such decline across linked-list sessions. Unlike linked-list-cycle (2026-07-05), where the O(1) variant was at least reasoned through and written in the blog, here the hash-set version is the final submitted solution with no O(1) variant attempted in any form yet.
