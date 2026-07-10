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
