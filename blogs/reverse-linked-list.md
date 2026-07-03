# Reverse Linked List (LC 206)

## Problem Summary
Given the head of a singly linked list, reverse the list in place and return the new head.

## Initial Intuition
Create a new linked list and insert each node at the front, since that naturally reverses the order. However, this uses extra space, while the problem asks to reverse the original list in place.

## Brute Force
Create a new linked list. Traverse the original list once, and for each node, create a new node and insert it at the front of the new list.

## Key Insight
Only need to change each node's `next` pointer. Before changing `cur.next`, save the original next node so the rest of the list is not lost. Then reverse the pointer, move `prev` forward, and continue from the saved next node. At every step, `prev` is the head of the already reversed part, while `cur` is the head of the remaining unreversed part.


## Final Algorithm
Walk the list once, rewiring each node's `next` pointer to point backward, using three references (`prev`, `cur`, and a saved `next`) so no node is lost:
```
prev, cur = None, head
while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
return prev
```

## Correctness Argument
Maintain the following invariant throughout the loop:

- `prev` is the head of the reversed portion of the list.
- `cur` is the first node of the unreversed portion.
- All nodes before `cur` have already had their `next` pointers reversed.
- All nodes from `cur` onward remain unchanged.

Each iteration saves `cur.next`, reverses the link from `cur` to `prev`, and advances both pointers. This preserves the invariant while moving exactly one node from the unreversed portion to the reversed portion. When `cur` becomes `None`, every node has been reversed, so `prev` points to the new head of the fully reversed list.


## Complexity
- Time: O(n) — each node visited exactly once.
- Space: O(1) — iterative, no extra data structure.

## Edge Cases
- Empty list (`head = None`): loop never runs, returns `None`.
- Single node: loop runs once, `cur.next` becomes `None` (already was), returns the same node.
- Two nodes: confirms the pointer swap direction, not just a no-op.

## Mistakes Made
N/A

## How to Recognize This Pattern Next Time
- The problem asks you to reverse a linked list in place.
- You need to change the direction of `next` pointers instead of creating new nodes.
- The list only needs to be traversed once.
- The problem requires O(1) extra space.
- You need to maintain connections while modifying pointers, so saving the next node before rewiring is essential.
