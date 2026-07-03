# Intersection of Two Linked Lists (LC 160)

## Problem Summary
Given the heads of two singly linked lists, return the node where they intersect (by reference, not value), or `None` if they never intersect.

## Initial Intuition
Compare node values, but this is wrong because intersection means two pointers refer to the exact same node object, not just nodes with the same value.

## Brute Force
For every node in list A, scan every node in list B and check whether they are the same node reference.

Time: O(mn)  
Space: O(1)

## Key Insight
#### Important: the two lists may have different lengths, so the two pointers may reach the shared part at different times.

By switching each pointer to the other list's head after reaching `None`, both pointers walk the same total path length: A + B and B + A. This cancels out the length difference and aligns them at the intersection.


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
- First thought intersection meant two nodes had the same value.
- Forgot that `a != b` compares node references when `ListNode` has no custom `__eq__`.
- Did not immediately see why redirecting to the other head cancels the length difference.
- Almost compared `a.val` and `b.val`, which would be incorrect.

## How to Recognize This Pattern Next Time
- The problem asks for intersection of two linked lists.
- Intersection means same node object, not same value.
- The two lists may have different lengths.
- You need O(1) space.
- You need to align two pointers without explicitly computing both lengths.
