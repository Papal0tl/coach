# Session Notes

- Problem slug: `swap-nodes-in-pairs`
- Archive path: `archives/2026-07-06-swap-nodes-in-pairs/`

## Agent Preparation

- Pattern: dummy node + iterative pairwise pointer rewiring.
- Key insight: keep a `prev` pointer trailing the pair being swapped so the swapped pair can be re-linked into the rest of the list without special-casing the head. A dummy node lets the first pair be swapped the same way as any other pair.
- Invariant or state: before each loop iteration, `prev.next` is the first unswapped node and everything before `prev` (starting from `dummy`) is already correctly swapped and linked.
- Complexity target: O(n) time, O(1) space.

## Reference Solution Summary

`dummy.next = head`, `prev = dummy`. While `prev.next` and `prev.next.next` both exist: let `first = prev.next`, `second = first.next`. Rewire `first.next = second.next`, `second.next = first`, `prev.next = second`. Advance `prev = first` (first is now the second node of the swapped pair, i.e. the new trailing node). Return `dummy.next`.

## Edge Cases

- Empty list (`head = None`): loop condition fails immediately, returns `None`.
- Single node: `prev.next.next` is `None`, loop body never runs, returns list unchanged.
- Odd number of nodes (e.g. `[1,2,3]`): last node has no pair, loop stops when `prev.next.next` is `None`.
- Two nodes: single swap, dummy handles the "new head" case without special-casing.

## User-Facing Takeaways

- This is the fourth linked-list session (after intersection, reverse, palindrome, cycle, cycle-ii, merge-two-sorted-lists, add-two-numbers, remove-nth-node-from-end-of-list). Dummy-node technique has now transferred across five consecutive sessions — expect it to surface again here without prompting.
- New wrinkle vs prior problems: this requires rewiring *pairs* of nodes rather than single-node reversal/removal, so three pointers per iteration (`prev`, `first`, `second`) must be tracked and the order of the three re-links matters (get `first.next` before overwriting `second.next`, or the rest of the list is lost).

## Coaching Log

- First attempt (committed f231ae3): correct dummy-node + three-pointer (`a`, `b`, `prev`) pairwise swap on the first try. All 6 reference tests pass, zero bugs. Re-link order differs slightly from the reference (`prev.next = b` before `a.next = b.next`) but is still correct because `b.next` is read before it gets overwritten — order-of-operations reasoning worth probing.
- Dummy-node technique transferred again without prompting — now six consecutive linked-list sessions using it unprompted.

## Follow-Up Candidates

- Recursive solution (`head.next.next = swapPairs(head.next.next)` style) — good follow-up given prior declines on recursive/optional variants (reverse-linked-list recursion was declined 2026-07-03).
- Generalize to reversing nodes in groups of k (LC 25) as a natural next-session candidate, not this session.
