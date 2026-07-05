# Coaching Notes — Linked List Cycle (LC 141)

## Session Context

- Fourth linked-list session (after intersection-of-two-linked-lists, reverse-linked-list, palindrome-linked-list, all 2026-07-03).
- Fast/slow pointer (Floyd's cycle detection) pattern has not yet been exercised: the O(1)-space follow-up was offered and declined in both reverse-linked-list and palindrome-linked-list sessions.
- Watch for: does the user reach for two-pointer (fast/slow) technique independently, or default to a hash-set/visited-node approach first?

## Reference Solution Summary (agent-only, do not reveal directly)

- **Key insight**: A hash set of visited nodes detects a cycle in O(n) space. The O(1)-space alternative is Floyd's fast/slow pointer: if a cycle exists, a pointer moving 2 steps per iteration will eventually lap a pointer moving 1 step per iteration and they will occupy the same node.
- **Invariant**: At the top of each loop iteration (after the first), `fast` has moved exactly twice as many steps as `slow` from `head`. If there is no cycle, `fast` reaches `None` (or `fast.next` is `None`) before ever coinciding with `slow`, since it always stays strictly ahead. If there is a cycle, once both pointers are inside the cycle, the gap between them (mod cycle length) decreases by 1 each iteration, so they must meet within at most `cycle_length` iterations.
- **Complexity**: O(n) time, O(1) space.
- **Edge cases**: empty list (`head is None`), single node no cycle, single node self-loop (`pos = 0`), two-node cycle.
- **Common wrong turn**: comparing `slow.val == fast.val` instead of identity (`is`) — fails when duplicate values exist. Also must guard `fast.next is not None` before dereferencing `fast.next.next`, or risk `AttributeError` on odd-length non-cyclic lists.

## Observations

(to be filled in during the feedback loop)
