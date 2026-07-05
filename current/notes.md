# Session Notes

- Problem slug: `merge-two-sorted-lists`
- Archive path: TBD

## Agent Preparation

- Pattern: two-pointer merge, the same merge step used in merge sort, adapted to splice existing linked-list nodes instead of copying values.
- Key insight: at each step, compare the current heads of `list1` and `list2`, and splice the smaller one onto the result. A dummy/sentinel head node avoids special-casing which list contributes the first node of the result.
- Invariant or state: at the top of the loop, `tail` points to the last node already spliced into the result, and `list1`/`list2` point to the next unmerged node of each remaining sublist. The result built so far (`dummy.next .. tail`) is sorted and consists entirely of nodes from the original two lists.
- Complexity target: O(n + m) time (each node visited once), O(1) extra space (no new nodes allocated, only existing nodes relinked).

## Reference Solution Summary

Use a dummy head and a `tail` pointer. While both lists have remaining nodes, splice whichever head has the smaller value onto `tail.next`, advance that list's pointer, and advance `tail`. When one list is exhausted, splice the remainder of the other list directly (already sorted, no need to walk it node by node). Return `dummy.next`. Validated locally against 9 cases (`python3 tests.py`), including both-empty, one-empty, duplicate values, and one list fully preceding the other.

## Edge Cases

- Both lists empty → return `None`.
- One list empty, the other non-empty → return the non-empty list unchanged.
- Duplicate values across lists (tie-breaking: `<=` keeps the merge stable, `list1` wins ties).
- One list's values are all smaller/larger than the other's (no interleaving).
- Single-node lists.

## User-Facing Takeaways

(to be filled during feedback step)

## Follow-Up Candidates

(to be filled during feedback step)

## Follow-Up Decisions

(to be filled during feedback step)
