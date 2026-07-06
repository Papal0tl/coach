# Remove Nth Node From End of List (LC 19)

- Archive: archives/2026-07-06-remove-nth-node-from-end-of-list/

## Problem Summary
Given the head of a singly linked list, remove the nth node counting from the end of the list, and return the head of the resulting list. `n` is guaranteed to be between 1 and the length of the list.

## Initial Intuition
Find the length of the linked list first. If know the total length, then convert the "nth node from the end" into its position from the beginning, then walk to that position and remove it.

## Brute Force
Copy all node values into an array first. Then remove the value at index length - n, and rebuild a new linked list from the remaining values.

This works because arrays make it easy to access the node position directly, but it is less efficient in space because it stores all values and creates new nodes instead of changing the original links.

Time Complexity: O(L)
Space Complexity: O(L)

## Key Insight
The key idea is to convert the position from the end into a position from the front.

If the list length is L, then the node before the one we want to remove is at position L - n (starting from the dummy node). Using a dummy node makes removing the head node exactly the same as removing any other node, so no special case is needed.

## Final Algorithm
1. Create a dummy/sentinel node pointing to `head`, so the head itself can be removed without special-casing it.
2. First pass: walk the real list from `head` to count its length.
3. Starting from `dummy`, walk `length - n` steps forward. This lands on the node immediately before the one to remove.
4. Skip the target node: `cur.next = cur.next.next`.
5. Return `dummy.next` (the real head, skipping the sentinel).

```python
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        cur = head

        while cur:
            length += 1
            cur = cur.next

        cur = dummy
        for i in range(length - n):
            cur = cur.next

        cur.next = cur.next.next
        return dummy.next
```

## Correctness Argument
After the first traversal, length equals the number of nodes in the list.

Starting from the dummy node and moving length - n steps always places cur immediately before the node that should be removed. Setting cur.next = cur.next.next removes that node while keeping the rest of the list connected. Since the dummy node is before the real head, this also works when the head itself is removed. Therefore, the algorithm always returns the correct linked list.

## Complexity
Time Complexity: O(L), where L is the length of the list — one pass to count the length, one pass to walk to the removal point.
Space Complexity: O(1) auxiliary space (only the dummy node and a few pointers).

## Edge Cases
- Removing the head node (`n == length`), handled by the dummy node so `cur` always has a valid predecessor.
- Removing the tail node (`n == 1`).
- Single-node list (`length == 1`, `n == 1`).

## Mistakes Made
- Created the dummy node with dummy = ListNode(0), but forgot to connect it to the original list with dummy.next = head. Because dummy.next was still None, the code later tried to access .next from a None value and crashed with an AttributeError. The fix was to add dummy.next = head immediately after creating the dummy node, so the dummy node actually points to the real list.

## How to Recognize This Pattern Next Time
- Delete or insert a node in a linked list, so need a pointer to the previous node.
- If deleting the head node is possible, use a dummy node to avoid special cases.
- If the problem gives a position from the end, consider converting it into a position from the front by first finding the list length.
- "remove the kth/nth node" in a linked list => whether finding the previous node first will make the operation easier.
