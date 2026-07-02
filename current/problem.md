# LC 160 — Intersection of Two Linked Lists

https://leetcode.cn/problems/intersection-of-two-linked-lists/description/?envType=study-plan-v2&envId=top-100-liked

## Problem

Given the heads of two singly linked lists `headA` and `headB`, return the node at which the two lists intersect. If the two linked lists have no intersection, return `null`.

The intersection is defined by reference, not value — both lists share the same node object from the intersection point onward.

The judge will accept your solution if it returns the intersecting node; it will not check your solution if no intersection exists and you return `null`.

## Examples

**Example 1:**
```
listA: 4 → 1 → 8 → 4 → 5
listB:      5 → 6 → 1 → 8 → 4 → 5
                    ↑
              intersection at node with val=8
Output: Intersected at '8'
```

**Example 2:**
```
listA: 2 → 6 → 4
listB:      1 → 5
Output: No intersection (null)
```

## Constraints

- The number of nodes in listA is `m`.
- The number of nodes in listB is `n`.
- `1 <= m, n <= 3 * 10^4`
- `1 <= Node.val <= 10^5`
- `0 <= skipA <= m`
- `0 <= skipB <= n`
- If `intersectVal` is 0, then `listA` and `listB` do not intersect.
- If `intersectVal` is not 0, then `listA` and `listB` will intersect on some node.

## Notes

- Do not modify the linked lists.
- The solution should ideally use O(1) memory.
- Time complexity should be O(m + n).
