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

## Coaching Log

### First attempt (sequential pairwise merge, folds `lists` one at a time into `merge`)

- Approach chosen: sequential fold — reduce `merge` (accumulated result) against each `cur_list` in turn using a dummy-node merge loop. Valid O(Nk) strategy, structurally close to merge-two-sorted-lists's core loop, reused unprompted.
- Bug: inside the merge loop, the code does `cur.val = list1.val; cur = cur.next; list1 = list1.next` — copying a value into the current node and then advancing `cur` via `cur.next`, but `cur.next` was never pointed at a new node, so `cur.next` is always `None` (from `dummy = ListNode(0)`). This makes `cur` become `None` after the very first assignment inside the loop, crashing with `AttributeError: 'NoneType' object has no attribute 'val'` on the second inner-loop iteration of the second outer-loop pass onward. Confirmed empirically with the example input: crashes exactly at `cur.val = list2.val` when merging list 2 (`[1,4,5]`) with list 3... actually crashes merging accumulated `merge=[1,4,5]` against `cur_list=[1,3,4]`.
- This is a departure from the technique the user has used successfully in every prior linked-list session (merge-two-sorted-lists, add-two-numbers, etc.): attach the actual existing node (`cur.next = list1; cur = cur.next`) rather than copy `.val` into a pre-existing dummy chain. Worth watching whether they self-diagnose by tracing `cur` across iterations, or need the invariant ("cur.next must point at a real node before you advance into it") surfaced directly.
- Intervention used: asked user to run the code themselves and trace what `cur` is bound to right before the crash (step 1 of default intervention order — clarifying/trace request). No hint given yet.
