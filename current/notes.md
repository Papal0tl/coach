# Session Notes

- Problem slug: `merge-k-sorted-lists`
- Archive path: `archives/2026-07-10-merge-k-sorted-lists/`

## Agent Preparation

- Pattern: k-way merge via a min-heap (also solvable via divide-and-conquer pairwise merge, or brute-force collect-and-sort).
- Key insight: at any point, the next smallest overall element must be the head of one of the k lists (since each list is individually sorted). A min-heap holding at most one "current head" per list gives that minimum in O(log k) instead of O(k) per pop.
- Invariant or state: the heap always contains at most one node per still-active list — specifically each list's current unconsumed head. Popping the minimum and pushing its `.next` (if any) maintains this.
- Complexity target: O(N log k) time (N = total nodes across all lists, k = number of lists), O(k) extra space for the heap (output list reuses input nodes).

## Reference Solution Summary

Push `(val, index, node)` for each list's head into a heap (index used purely as a heap tiebreaker so `ListNode` objects are never compared). Repeatedly pop the minimum, append it to a dummy-headed result list, and push its successor back onto the heap if one exists.

## Edge Cases

- `lists = []` → return `None`.
- `lists = [None]` / list of all `None`s → return `None`.
- Single non-empty list → return it unchanged (heap degenerates to size 1).
- Mix of empty and non-empty lists.
- Duplicate values across lists (heap tiebreak on index must not compare `ListNode`s directly, and equal values must both come out — order between equal values is not specified by the problem but must not crash or drop nodes).
- Negative and boundary values (`-10^4`, `10^4`).
- Large k with short lists vs. small k with one long list (motivates why O(N log k) beats brute-force O(Nk)).

## User-Facing Takeaways

- This generalizes merge-two-sorted-lists (2026-07-05) from k=2 to arbitrary k.
- Natural first instinct is likely a pairwise-merge loop (reduce k lists two at a time, similar structurally to sort-list's merge step) — that is a valid O(N log k) divide-and-conquer alternative. Watch whether the user reaches for that or for collect-all-then-sort (O(N log N), also valid but not pattern-matching to "merge").
- Heap/priority-queue as a way to repeatedly extract a running minimum across multiple sorted sources has not been used yet in this arc — first opportunity to observe whether `heapq` is reached for independently.

## Follow-Up Candidates

- Ask for the divide-and-conquer pairwise-merge alternative and compare its complexity/constant-factor tradeoffs to the heap approach.
- Ask why comparing raw `ListNode` objects in the heap would fail on tie (Python has no default `<` for arbitrary objects) — connects to the index-tiebreak trick.
