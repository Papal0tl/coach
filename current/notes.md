# Session Notes

- Problem slug: `sort-list`
- Archive path: (assigned at closeout)

## Agent Preparation

- Pattern: merge sort on a linked list. Split into two halves with the fast/slow pointer technique (already used in linked-list-cycle, palindrome-linked-list), recursively sort each half, then merge with the exact same two-pointer merge routine as merge-two-sorted-lists (LC 21, 2026-07-05). This session composes two previously-mastered sub-patterns rather than introducing a new mechanism.
- Key insight: a linked list can't be randomly indexed, so array-style sorts (quicksort partition by index, in-place swaps) don't transfer directly. But merge sort only needs sequential splitting (find the midpoint) and sequential merging (walk two lists in lockstep) — both of which are natural on a linked list. This is the reason merge sort is the standard answer here rather than e.g. quicksort or heapsort.
- Invariant or state: at the base case (`head is None or head.next is None`), a list of length 0 or 1 is already sorted. Recursively, `sortList` on any sublist returns that sublist sorted; merging two sorted lists produces a sorted list. The midpoint split must fully sever the first half from the second (`slow.next = None`) or the recursion will not terminate / will double-count nodes.
- Complexity target: O(n log n) time (log n split levels, O(n) work merging at each level), O(log n) space (recursion stack) for the straightforward recursive version submitted here. Follow-up candidate: true O(1) space via bottom-up iterative merge sort (merge sublists of size 1, then 2, then 4, ... using pointer arithmetic instead of recursion) — this matches the problem's official follow-up.

## Reference Solution Summary

`sortList(head)`:
1. Base case: if `head` is `None` or `head.next` is `None`, return `head` unchanged.
2. Split: fast/slow pointer walk to find the midpoint; `fast` starts one step ahead of `slow` so `slow` lands just before the second half's start on even/odd splits. Set `mid = slow.next`, then `slow.next = None` to sever the first half.
3. Recurse: `left = sortList(head)`, `right = sortList(mid)`.
4. Merge: standard two-pointer merge with a dummy head, identical in structure to merge-two-sorted-lists.
5. Return the merged, fully sorted list.

## Edge Cases

- Empty list (`head is None`) -> return `None`.
- Single node -> return as-is (base case, no split/merge needed).
- Two nodes -> exercises the split logic at its smallest non-trivial size.
- Already sorted / reverse sorted -> correctness independent of initial order.
- Duplicate values -> merge must use `<=` (or equivalent) to keep the sort stable and correct with ties.
- All-negative or mixed-sign values -> no special-casing needed since comparisons are value-based.

## User-Facing Takeaways

- Recognizing "can't randomly index a linked list, so pick a sort that only needs sequential access" is the transferable insight — it rules out index-based sorts and points at merge sort specifically.
- This is a direct composition of two prior techniques (fast/slow midpoint-finding, two-list merge) rather than a new one; watch whether the user notices and names the reuse unprompted.

## Follow-Up Candidates

- O(1)-space bottom-up iterative merge sort, if the user finishes the recursive version cleanly and wants the full follow-up.

## Session Log

- Agent solved independently first: recursive merge sort (fast/slow split + two-pointer merge), all 8 reference tests pass.
- First user draft took a different approach than the reference: a single forward pass doing adjacent-node swaps when out of order (bubble-sort-like), using a dummy head. Two issues observed by running it against `[4,2,1,3]`:
  1. Missing `return` statement at the end of `sortList` — the function falls off the end and implicitly returns `None`. Confirmed by running: `sol.sortList(head)` returns `None`.
  2. The swap logic (`tmp = cur.next; cur.next = tmp.next; tmp.next = cur; cur = tmp`) rewires `cur` and its successor but never updates the `.next` pointer of the node *before* `cur` (tracked nowhere in this draft) — the swapped-in node becomes unreachable from the rest of the list. This is also only a single pass, so even with the swap fixed it would only bubble one adjacent inversion per pass, not fully sort in one call.
  - Asked the user to (a) check what their function returns given the missing `return`, and (b) trace what happens to the node before `cur` during a swap, rather than revealing the fix directly.
- User self-caught the missing `return` after being asked to run it and confirmed `None` (matches prior empirical-debugging preference). Added `return dummy.next` unprompted, no direct fix given.
- Ran the updated attempt against all four spot-check inputs; the reachability bug is confirmed and severe: `[4,2,1,3] -> [4]`, `[-1,5,3,4,0] -> [-1,5]`, `[2,1] -> [2]`, `[5,4,3,2,1] -> [5]`. Every swap permanently drops the rest of the list because the node before `cur` never gets re-pointed. Asked the user to hand-trace the first swap on `[4,2,1,3]` (head=4, cur.next=2) line by line and check what still points into the node holding `2` afterward, rather than naming the missing `prev` tracking variable directly.
- Without further discussion, the user abandoned the swap-based approach entirely and pivoted directly to a fast/slow split setup (`prev = None; fast = head; slow = head`), matching the reference solution's overall merge-sort strategy. This is another unprompted transfer of the fast/slow technique from prior sessions (linked-list-cycle, palindrome-linked-list) to a new problem shape — notably, the pivot away from the broken swap approach happened without being told it was a dead end, only after empirically observing the reachability bug. Draft is still incomplete (setup lines only, no loop/split/recursion/merge/return) — falls off the end and returns `None` on `[4,2,1,3]`, as expected for unfinished code, not a new bug. Asked two forward-looking questions: how the fast/slow loop should terminate so `slow` lands at the midpoint, and what needs to happen to the list structurally before the two halves can be treated as independent sortable pieces (nudging toward severing the link without naming it directly).
- Added the fast/slow `while` loop (`fast = head, slow = head` start, matching neither the reference's `fast = head.next` offset nor being flagged yet). `prev` remains declared but unused. Traced by hand (not yet by the user): starting both pointers at `head` causes a degenerate split for small/even-length lists — e.g. on `[2, 1]`, `slow` ends up at the *last* node rather than a true midpoint, so `mid = slow.next` would be `None` and the "first half" would still be the entire unchanged 2-node list, causing infinite recursion (the classic off-by-one in fast/slow midpoint-finding). Not pointed out directly; asked the user to (a) reconsider whether `prev` is still needed, and (b) hand-trace the loop specifically on `[2, 1]` to discover the degenerate case themselves.
- User asked for a hint directly rather than continuing to trace unprompted. Gave a scoped hint (next level in the intervention order, invariant/state level): named the target invariant explicitly ("slow should land on the last node of the first half"), suggested starting `fast = head.next` instead of `fast = head` and re-tracing `[2,1]`, and explained `prev` is unnecessary for this approach (unlike the swap version) since `slow` itself is the cut point. Did not write or show the corrected loop code.
- User did not take the suggested `fast = head.next` offset. Instead found an independently valid alternative: track `prev = slow` inside the loop (before advancing `slow`), then sever with `prev.next = None` after the loop. Verified by hand-tracing `[2,1]` and `[4,2,1,3]`: both produce a correct, non-degenerate split (e.g. `[2,1]` -> `[2]` / `[1]`, `[4,2,1,3]` -> `[4,2]` / `[1,3]`), confirming this is a genuinely correct variant of the midpoint-finding technique, not a mistake — a different but equally valid solution to the same edge case flagged in the previous hint. Ran the current draft and confirmed it returns `None` for any 2+ node list, because the function does nothing after severing the list (no use of `slow` as the second half's head, no recursive calls, no merge, no return for the non-base-case branch). Asked three forward-looking questions rather than revealing the remaining structure: what to do with `head`/`slow` as two halves, whether the previously-solved merge-two-sorted-lists merge routine could be reused, and what the function should return.
