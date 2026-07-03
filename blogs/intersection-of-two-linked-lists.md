# Intersection of Two Linked Lists (LC 160)

## Problem Summary
Given the heads of two singly linked lists, return the node where they intersect (by reference, not value), or `None` if they never intersect.

## Initial Intuition
(to be filled by user)

## Brute Force
(to be filled by user)

## Key Insight
(to be filled by user)

## Final Algorithm
Redirect each pointer to the other list's head once it reaches the end:
```
a, b = headA, headB
while a is not b:
    a = a.next if a else headB
    b = b.next if b else headA
return a
```

## Correctness Argument
Redirecting each pointer to the other list's head makes both pointers traverse exactly the same total distance (len(A) + len(B)). Any initial offset caused by different list lengths is canceled out after the switch. Therefore, if the lists intersect, the pointers enter the shared suffix at the same time and meet at the first common node. If the lists do not intersect, both pointers reach None after traversing the same total distance, so they terminate together.

## Complexity
- Time: O(m + n) — each pointer traverses at most m + n nodes.
- Space: O(1).

## Edge Cases
- No intersection: both pointers reach `None` simultaneously after m + n steps.
- Intersection at the very first node: loop condition is false immediately, returns headA.
- Equal-length lists that intersect: pointers meet on the first pass, no redirect needed.
- Single-node lists, no intersection: both reach `None` after 2 steps.

## Mistakes Made
(to be filled by user)

## How to Recognize This Pattern Next Time
(to be filled by user)
