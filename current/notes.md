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

- First attempt: correct hash-set (visited-node) solution on the first try, zero bugs. Passed all reference tests including empty list and single-node self-loop.
- Consistent with prior pattern: reached for hash-set/extra-space approach before considering the fast/slow pointer alternative (same order as reverse-linked-list and palindrome-linked-list, both 2026-07-03).
- Stated complexity correctly (O(n) time, O(n) space) unprompted, and named "fast and slow pointer" as the O(1)-space alternative without being shown it — but chose not to implement it in `attempt.py`, moving straight to the blog instead.
- Revised finding after the blog was written: the user did not skip the fast/slow approach — they wrote fully correct fast/slow code and a two-case correctness argument directly in the blog's Final Algorithm section, independently verified by the agent against the full test suite. So this is not simply a third decline; it's the first successful production of the fast/slow pattern, just not as a typed-and-run `attempt.py` solution. The remaining gap is specifically hands-on implementation practice, not conceptual understanding.
- Recurring gap: used `slow == fast` instead of `slow is fast` in the blog code. Harmless here since `ListNode` has no custom `__eq__`, but this is the same category of gap self-caught in the intersection-of-two-linked-lists blog (`!=` vs `is not`) — this time not self-caught, flagged in review as a non-blocking style note.
- Session closed: blog accepted with zero required revisions.
