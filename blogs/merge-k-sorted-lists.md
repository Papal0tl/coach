# Merge k Sorted Lists (LC 23)

## Problem Summary
Given an array of `k` linked lists, each already sorted in ascending order, merge them all into a single sorted linked list and return its head.

## Initial Intuition
Reuse the same idea as merging two sorted linked lists. I could keep a running merged list and combine each new list into it one at a time.

## Brute Force
Traverse every linked list, collect all node values into an array, sort the array, and then build a new linked list from the sorted values.

If there are N total nodes, collecting the values takes O(N), sorting takes O(N log N), and rebuilding the list takes O(N). Therefore, the total time complexity is O(N log N), and the extra space complexity is O(N).

## Key Insight
Every individual linked list is already sorted, do not need to sort all values again. Repeatedly apply the merge-two-sorted-lists technique.

After each outer-loop iteration, merge contains all nodes from the lists processed so far, and it remains sorted.

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
After each outer-loop iteration, merge is a sorted linked list containing all nodes from the lists processed so far.

During each two-list merge, the smaller current node is always attached next, so the new result remains sorted. Once one list is exhausted, the remaining nodes of the other list can be attached directly because they are already sorted and are no smaller than the last attached node.

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
- Wrote `cur.val = list1.val` or `cur.val = list2.val`. This only changed the value stored in the current node and did not connect any node to the result list.
- Moved with `cur = cur.next` before setting `cur.next`. Since dummy.next was still None, cur became None, causing an AttributeError.
- The correct linked-list order is: first connect the node with cur.next = ..., and then move forward with cur = cur.next.
- Placed return merge inside the outer for loop. This caused the function to return after merging only the first list, so the remaining lists were never processed.
- Used 1if lists is None1, which only checks for None. Using if not lists is clearer because it also handles an empty array.

## How I Will Recognize This Pattern Next Time
- Every input list is already sorted.
- Need to compare the current head nodes.
- The merge-two-sorted-lists pattern can be reused.
- A dummy node avoids special handling for the first result node.
- Always connect a node before moving the result pointer.
