# Swap Nodes in Pairs (LC 24)

## Problem Summary
Given the head of a singly linked list, swap every two adjacent nodes and return the new head. The swap must be done by rewiring the nodes themselves, not by changing node values.

## Initial Intuition
Swapping the values of every two adjacent nodes.

## Brute Force
Traverse the linked list, create a new linked list, and append every pair of nodes in reversed order (e.g. append 2 then 1, 4 then 3, etc.). If there is a final unpaired node, append it unchanged.

This approach is straightforward but requires creating new nodes or using extra memory, which is unnecessary because the original list can be modified directly.

Time: O(n)
Space: O(n)

## Key Insight
Only three next pointers need to be changed to swap two adjacent nodes.

Using a dummy node makes every pair look the same, including the first pair, so there is no need to handle the head node as a special case. After swapping one pair, simply move prev to the end of that swapped pair and repeat the same process.

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
Each iteration correctly swaps one adjacent pair while preserving the rest of the list.

Before each iteration, prev.next points to the first node of the next pair to swap.
Let `a = prev.next` and `b = a.next`. The three pointer updates change
`prev -> a -> b -> next` into `prev -> b -> a -> next` without losing any nodes.
After the swap, setting prev = a moves prev to the node immediately before the next unswapped pair.

The loop stops when fewer than two nodes remain, so every possible pair has been swapped exactly once, while any remaining single node is left unchanged. Therefore, the returned list is correct.

## Complexity
Time Complexity: O(n), where n is the number of nodes — each node is visited once.
Space Complexity: O(1) auxiliary space (only the dummy node and a few pointers).

## Edge Cases
- Empty list (`head = None`): loop condition fails immediately, returns `None`.
- Single node: `prev.next.next` is `None`, loop body never runs, list is unchanged.
- Odd number of nodes: the trailing unpaired node is left alone once `prev.next.next` is `None`.
- Two nodes: single swap; the dummy node makes the new head come out correctly without special-casing.

## Mistakes I Made
- Initially found it difficult to keep track of which pointer represented the "previous node", the first node, and the second node during the swap.
- Confused about why the pointer updates must happen in the specific order prev.next = b, a.next = b.next, then b.next = a. Changing the order can lose part of the list or even create a cycle.

## How I Will Recognize This Pattern Next Time
- Asks to swap, reorder, or reverse nodes in a linked list without modifying node values.
- The operation is performed on fixed-size groups (pairs, groups of k, etc.).
- The head node might change after the operation, suggesting that a dummy/sentinel node will simplify the implementation.
- The solution only needs to rewire next pointers instead of creating new nodes or changing values.
