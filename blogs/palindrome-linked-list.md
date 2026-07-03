# Palindrome Linked List (LC 234)

## Problem Summary
Given the head of a singly linked list, return `true` if the sequence of values reads the same forwards and backwards, `false` otherwise.

## Initial Intuition
_TODO: write in your own words._

## Brute Force
_TODO: write in your own words._

## Key Insight
_TODO: write in your own words._

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
_TODO: write in your own words. (Hint: why does comparing `vals` to its reverse decide the palindrome question correctly, for both even- and odd-length lists?)_

## Complexity
- Time: O(n) — one pass to copy values, one pass to build the reversed list, one comparison.
- Space: O(n) — two auxiliary lists of length n (this is the follow-up-unoptimized version; an O(1)-space approach using fast/slow pointers plus in-place reversal of the second half exists but was not attempted this session).

## Edge Cases
- Single node: `vals` and `rev_val` are both length-1 lists with the same element — trivially equal.
- Even-length list: no middle element; every value must have a mirrored match.
- Odd-length list: middle element compares to itself in the reversed list — harmless.
- Empty list is out of scope per constraints (`1 <= number of nodes`).

## Mistakes Made
_TODO: write in your own words. (You hit three separate bugs before this ran — worth naming them and what each taught you.)_

## How to Recognize This Pattern Next Time
_TODO: write in your own words._
