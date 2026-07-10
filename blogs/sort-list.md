# Sort List (LC 148)

## Problem Summary
Given the head of a singly linked list, return the list after sorting it in ascending order by node value. Follow-up: do it in O(n log n) time and O(1) extra space.

## Initial Intuition
Walk through the linked list, compare each node with the next node, and swap them whenever they were in the wrong order.

## Brute Force
Copy every node value into a list, sort the list with built-in sorting algorithm, and then write the sorted values back into the linked-list nodes.

For example: 
1. Traverse the linked list and append every value to an array.
2. Sort the array.
3. Traverse the linked list again and replace each node's value with the corresponding sorted value.

Time complexity: O(n log n) 
Space complexity: O(n)

## Key Insight
Linked lists do not support direct indexing or efficient random access. Reaching the node at index i requires walking through all previous nodes.

Merge sorts:
1. Use fast and slow pointers to find the middle.
2. Cut the list into two halves.
3. Recursively sort each half.
4. Merge the two sorted halves by rewiring their existing nodes.

merge: Nodes can be appended to the result by changing only next pointers. Each recursion level processes all n nodes once, and there are O(log n) levels, O(n log n) total time.

## Final Algorithm
1. Base case: if `head` is `None` or `head.next` is `None`, return `head` unchanged (already sorted).
2. Split: use a fast/slow pointer walk to find a cut point, then sever the list into two independent halves.
3. Recurse: sort each half with the same function.
4. Merge: combine the two sorted halves into one sorted list (same merge routine as merge-two-sorted-lists).
5. Return the merged, fully sorted list.

```python
class Solution:
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        prev = None
        fast = head
        slow = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        left = head
        right = slow
        left = self.sortList(left)
        right = self.sortList(right)
        dummy = ListNode(0)
        cur = dummy
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
                cur = cur.next
            else:
                cur.next = right
                right = right.next
                cur = cur.next
        if left:
            cur.next = left
        else:
            cur.next = right
        return dummy.next
```

## Correctness Argument
Base case: returns an empty list or a one-node list unchanged, which is already sorted.

For a longer list, it splits it into two smaller halves and recursively sorts each half. By the time the recursion returns, both left and right are sorted.

During merge step, it always appends the smaller front node from the two sorted lists. Therefore, the merged list remains sorted. When one list is exhausted, the remaining nodes in the other list are already sorted and can be attached directly.

Thus, the algorithm returns all original nodes in ascending order.

## Complexity
Time Complexity: O(n log n) — each of the O(log n) levels of recursion does O(n) total work merging.
Space Complexity: O(log n) — the recursion stack depth, since this is the recursive (not the O(1)-space iterative) variant.

## Edge Cases
- Empty list (`head = None`): returns `None` immediately.
- Single node: returns as-is via the base case.
- Two-node list: exercises the split logic at its smallest non-trivial size.
- Duplicate values: merge must not drop or reorder ties.
- Already sorted or reverse-sorted input: correctness doesn't depend on initial order.

## Mistakes I Made
- Tried to solve the problem like bubble sort by comparing cur.val with cur.next.val. This would eventually access cur.next.val when cur.next was None, causing an AttributeError. It also would have taken O(n²) time.
- Used a temporary variable without preserving the nodes that actually needed to be reconnected. Assignments such as tmp = cur and then cur = tmp did not change anything because both variables referred to the same node.
- Called self.sortList(fast) instead of self.sortList(right). Since fast could already be None, this discarded the entire right half instead of sorting it.
- After finding the middle with fast and slow pointers, wrote right = fast. For an even-length list such as [4,2,1,3], fast is None when the loop ends. The right half must begin at slow, not fast.

## How I Will Recognize This Pattern Next Time
- The data structure is a linked list, so random access is inefficient.
- The list can be split using fast and slow pointers.
- Two sorted linked lists can be merged efficiently by rewiring nodes.
- The problem naturally has the divide-and-conquer shape: split, recursively solve each half, and merge the results.
