# Palindrome Linked List (LC 234)

## Problem Summary
Given the head of a singly linked list, return `true` if the sequence of values reads the same forwards and backwards, `false` otherwise.

## Initial Intuition
Check the first value with the last value, then the second value with the second-to-last value. But linked lists cannot directly access the last or previous nodes easily, so doing this directly on the linked list is inconvenient.

## Brute Force
Copy all linked list values into a normal Python list. Then create another list in reversed order and compare the two lists. If they are the same, the linked list is a palindrome.

## Key Insight
A linked list is hard to check from both ends, but a Python list is easy to reverse and compare. So I can first convert the linked list into a list of values, then compare the original order with the reversed order.

## Final Algorithm
Walk the list once, copying each node's value into a Python list `vals`. Build a second list `rev_val` by walking `vals` from index `n-1` down to `0`. Compare the two lists for equality:
```
vals = []
cur = head
while cur is not None:
    vals.append(cur.val)
    cur = cur.next

rev_val = []
for i in range(len(vals) - 1, -1, -1):
    rev_val.append(vals[i])

return vals == rev_val
```

## Correctness Argument
`vals` stores the linked list values from head to tail. `rev_val` stores the same values from tail to head. If the linked list is a palindrome, every value from the front matches the corresponding value from the back, so `vals == rev_val`. If any mirrored pair is different, the two lists will not be equal, so the linked list is not a palindrome. This works for even-length lists and odd-length lists; in an odd-length list, the middle value just matches itself.


## Complexity
- Time: O(n) — one pass to copy values, one pass to build the reversed list, one comparison.
- Space: O(n) — two auxiliary lists of length n (this is the follow-up-unoptimized version; an O(1)-space approach using fast/slow pointers plus in-place reversal of the second half exists but was not attempted this session).

## Edge Cases
- Single node: `vals` and `rev_val` are both length-1 lists with the same element — trivially equal.
- Even-length list: no middle element; every value must have a mirrored match.
- Odd-length list: middle element compares to itself in the reversed list — harmless.
- Empty list is out of scope per constraints (`1 <= number of nodes`).

## Mistakes Made
- Wrote `range(len(vals) - 1, -1, -1, -1)`, but `range()` only takes up to three arguments: `start, stop, step`. This taught me that reverse looping should be `range(len(vals) - 1, -1, -1)`.
- Wrote `cur.val[i]`, but `cur.val` is just one value, not a list. I should use `cur.val` when adding the current node’s value.
- Wrote lowercase `true` / `false`, but Python uses `True` / `False` with capital letters.

## How to Recognize This Pattern Next Time
Whether a linked list reads the same forward and backward. If I need to compare positions from both ends, an array is much easier than a singly linked list because it supports direct indexing and reversing.
