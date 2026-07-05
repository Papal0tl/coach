# Session Notes

- Problem slug: `linked-list-cycle-ii`
- Archive path: `archives/2026-07-05-linked-list-cycle-ii/` (pending)

## Agent Preparation

- Pattern: Floyd's cycle detection, extended to locate the cycle entry point.
- Key insight: after slow/fast meet inside the cycle, resetting one pointer to `head` and advancing both one step at a time makes them meet exactly at the cycle's start node. This follows from the distance relationship between the pre-cycle length and the meeting point.
- Invariant or state: let the distance from head to cycle start be `a`, from cycle start to the meeting point be `b`, and the remaining cycle length be `c`. When slow and fast meet, slow has traveled `a + b`, and it can be shown `a = c - b` (mod cycle length), so walking `a` steps from head and `a` steps from the meeting point land on the same node.
- Complexity target: O(n) time, O(1) space (the hash-set approach is an acceptable first pass but the O(1) variant is the real target here since it directly builds on the prior session's fast/slow work).

## Reference Solution Summary

(fill after solving independently — do not expose to user by default)

## Edge Cases

- Empty list (`head = None`) → return `None`.
- Single node, no cycle → return `None`.
- Single node pointing to itself → return that node.
- Cycle starts at head (`pos = 0`).
- Cycle starts at the last node (tail points to itself effectively via a short cycle).
- No cycle, long list.

## User-Facing Takeaways

(fill during/after coaching)

## Follow-Up Candidates

- Prove why `a = c - b` holds (math derivation), if not already covered in the blog.
- Compare against the hash-set approach the user already knows from LC 141.
