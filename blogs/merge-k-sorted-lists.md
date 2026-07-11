# Merge k Sorted Lists (LC 23)

## Problem Summary
Given an array of `k` linked lists, each already sorted in ascending order, merge them all into a single sorted linked list and return its head.

## Initial Intuition
_(Your words: what was your first instinct when you saw the problem?)_

## Brute Force
_(Your words: what's a simple, non-optimal approach you could have started with — e.g. collecting all values and sorting them? What's its time/space complexity?)_

## Key Insight
_(Your words: what let you go from k separate sorted lists to one merge strategy? Why does folding the lists together one at a time work?)_

## Final Algorithm
1. If `lists` is empty (or falsy), return `None`.
2. Maintain a running `merge` result, initialized to `None`.
3. For each list `cur_list` in `lists`, merge it with the current `merge` result using a dummy-node two-pointer merge (the same routine as merge-two-sorted-lists): walk `list1 = merge` and `list2 = cur_list` together, always attaching the smaller head to the result, then attach whichever list is left over once one is exhausted.
4. After merging in `cur_list`, set `merge` to the new combined result and continue to the next list.
5. Return `merge` once all `k` lists have been folded in.

```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        merge = None
        for cur_list in lists:
            dummy = ListNode(0)
            cur = dummy
            list1 = merge
            list2 = cur_list
            while list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    cur.next = list1
                    list1 = list1.next
                    cur = cur.next
                else:
                    cur.next = list2
                    list2 = list2.next
                    cur = cur.next
            if list1 is not None:
                cur.next = list1
            else:
                cur.next = list2
            merge = dummy.next
        return merge
```

## Correctness Argument
_(Your words, agent prompt if needed: why does merging one list at a time into the running `merge` result produce a fully sorted list at the end? What invariant holds true about `merge` after each iteration of the outer loop?)_

## Complexity
Time Complexity: O(N·k), where N is the total number of nodes across all lists and k is the number of lists. Each of the k outer-loop merges can touch up to O(N) nodes in the worst case (the accumulated `merge` list grows as more lists are folded in), so the total work sums to O(N·k) rather than O(N log k).
Space Complexity: O(1) auxiliary space beyond the output — nodes are relinked in place, only a constant number of pointers are used per merge.

## Edge Cases
- `lists = []`: returns `None` immediately via the `not lists` guard.
- `lists` containing only `None` entries: each merge against `None` leaves `merge` unchanged, final result is `None`.
- A mix of empty (`None`) and non-empty lists.
- A single list in `lists`: the loop runs once, `merge` becomes that list unchanged.
- Duplicate values across lists: the `<=` comparison must not drop or reorder ties.
- Negative and boundary values (`-10^4`, `10^4`).

## Mistakes I Made
_(Your words: what actually went wrong while you were writing this, and how did you find and fix it?)_

## How I Will Recognize This Pattern Next Time
_(Your words: what about this problem's shape should cue you toward a merge-based approach next time?)_
