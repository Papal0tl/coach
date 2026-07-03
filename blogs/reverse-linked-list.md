# Reverse Linked List (LC 206)

## Problem Summary
Given the head of a singly linked list, reverse the list in place and return the new head.

## Initial Intuition
(to be filled by user)

## Brute Force
(to be filled by user)

## Key Insight
(to be filled by user)

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
(to be filled by user)

## Complexity
- Time: O(n) — each node visited exactly once.
- Space: O(1) — iterative, no extra data structure.

## Edge Cases
- Empty list (`head = None`): loop never runs, returns `None`.
- Single node: loop runs once, `cur.next` becomes `None` (already was), returns the same node.
- Two nodes: confirms the pointer swap direction, not just a no-op.

## Mistakes Made
(to be filled by user)

## How to Recognize This Pattern Next Time
(to be filled by user)
