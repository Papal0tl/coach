# Swap Nodes in Pairs (LC 24)

## Problem Summary
Given the head of a singly linked list, swap every two adjacent nodes and return the new head. The swap must be done by rewiring the nodes themselves, not by changing node values.

## Initial Intuition
User-filled.

## Brute Force
User-filled.

## Key Insight
User-filled.

## Final Algorithm
1. Create a dummy/sentinel node pointing to `head`, so the first pair can be swapped the same way as any other pair (no special-casing the new head).
2. Keep a `prev` pointer trailing the pair currently being swapped; `prev.next` is always the first unswapped node.
3. While `prev.next` and `prev.next.next` both exist, let `a = prev.next` and `b = a.next` be the pair to swap.
4. Rewire: point `prev` at `b`, point `a` at whatever came after `b`, then point `b` at `a`.
5. Advance `prev` to `a` (now the trailing node of the swapped pair) and repeat.
6. Return `dummy.next`.

```python
class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            a = prev.next
            b = a.next

            prev.next = b
            a.next = b.next
            b.next = a

            prev = a
        return dummy.next
```

## Correctness Argument
User-filled.

## Complexity
Time Complexity: O(n), where n is the number of nodes — each node is visited once.
Space Complexity: O(1) auxiliary space (only the dummy node and a few pointers).

## Edge Cases
- Empty list (`head = None`): loop condition fails immediately, returns `None`.
- Single node: `prev.next.next` is `None`, loop body never runs, list is unchanged.
- Odd number of nodes: the trailing unpaired node is left alone once `prev.next.next` is `None`.
- Two nodes: single swap; the dummy node makes the new head come out correctly without special-casing.

## Mistakes I Made
User-filled.

## How I Will Recognize This Pattern Next Time
User-filled.
