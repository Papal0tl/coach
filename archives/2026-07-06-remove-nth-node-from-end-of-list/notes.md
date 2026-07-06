# Session Notes: Remove Nth Node From End of List

## Timeline

- Intake complete. Problem: LC 19, Python, hint-only mode.
- Agent solved independently: dummy-node + two-pointer gap (one-pass), 6/6 tests pass.

## Agent Reference Notes (do not reveal directly)

- Key insight: to remove the nth node from the end without knowing list length up front, create a gap of `n` nodes between two pointers, then advance both together until the leading pointer hits the end. The trailing pointer then sits just before the node to remove.
- Invariant: after the initial `n`-step advance of `fast`, the gap between `fast` and `slow` stays exactly `n` nodes throughout the second loop. When `fast.next is None`, `slow` is the node immediately before the target.
- Dummy node handles the edge case where the head itself must be removed (n == length) — without it, `slow` would have no valid predecessor to update.
- Complexity: O(L) time (single pass over the list length L), O(1) space.
- Edge cases: single-node list (n=1), removing the head (n == length), removing the tail (n=1).
- One-pass follow-up: the gap technique above already is one-pass (no separate length-counting pass), so this should be the natural end state to look for, not a bonus.

## User Attempt Log

- First draft: two-pass length-counting approach (count `length`, then walk `length - n` steps from a dummy node). Crashes with `AttributeError: 'NoneType' object has no attribute 'next'` on `[1,2,3,4,5], n=2`.
- Root cause: `dummy = ListNode(0)` is created without linking `next=head`, so `dummy.next` is `None` instead of `head`. Asked user to trace what `dummy` points to right after construction rather than revealing directly.
- Fix: user immediately identified the bug (`dummy.next` should be `head`) unprompted after being asked to trace it, and applied `dummy.next = head`. 6/6 tests pass. Two-pass approach (count length, then walk `length - n` steps).

## Closeout

- One-pass gap-pointer follow-up offered, declined in favor of moving to the blog.
- Blog review requested two revisions (Mistakes Made described reasoning instead of the real bug; Brute Force duplicated Final Algorithm). Both fully and accurately applied on the first pass — ends the 2-session decline streak from merge-two-sorted-lists and add-two-numbers.
- Archived at archives/2026-07-06-remove-nth-node-from-end-of-list/.
