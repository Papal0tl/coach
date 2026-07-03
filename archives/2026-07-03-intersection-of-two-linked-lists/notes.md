# Coaching Notes — Intersection of Two Linked Lists

## Session

- Date: 2026-07-02
- Problem: LC 160 Intersection of Two Linked Lists
- Language: Python
- Mode: hint-only

## Key Insight

The core observation: if two lists intersect, they share a common suffix. The challenge is that the two prefixes before the intersection may have different lengths, so walking both pointers in parallel won't naturally align them.

The two-pointer trick: when pointer A finishes list A, redirect it to the head of list B. When pointer B finishes list B, redirect it to the head of list A. Both pointers now travel the same total distance: `len(A) + len(B)`. They arrive at the intersection simultaneously.

If there is no intersection, both pointers reach `None` at the same step (after `m + n` steps), so the loop exits correctly.

## Invariant

After the redirect, pointer A has traveled: `(m - c) + c + (n - c)` steps to reach the intersection, where `c` is the length of the shared tail. Pointer B has traveled: `(n - c) + c + (m - c)` steps. Both equal `m + n - c`. They are synchronized.

## Algorithm

```
a, b = headA, headB
while a is not b:
    a = a.next if a else headB
    b = b.next if b else headA
return a
```

## Complexity

- Time: O(m + n) — each pointer traverses at most m + n nodes.
- Space: O(1).

## Edge Cases

- No intersection: both pointers reach `None` simultaneously after m + n steps; `None is None` is True, returns `None`. ✓
- Lists of equal length that intersect: pointers meet on the first pass without needing the redirect.
- Intersection at the very first node (skipA = 0, skipB = 0): headA is headB; loop condition is false immediately, returns headA. ✓
- One list is longer than the other: redirect handles the offset automatically.
- Single-node lists, no intersection: both reach `None` after 2 steps. ✓

## Alternative Approaches

- **Hash set**: store all nodes from listA, scan listB for first match. O(m + n) time, O(m) space. Simple but uses extra memory.
- **Length difference**: compute lengths of both lists, advance the longer pointer by the difference, walk both until they meet. O(m + n) time, O(1) space. Correct but more code than the two-pointer redirect.

## Coaching Targets

- Will the user reach the hash set approach first?
- Will the user discover the two-pointer redirect independently, or will they need a nudge about equal total path length?
- Can the user explain *why* the redirect equalizes the paths (the m + n - c argument)?
- Does the user correctly handle the no-intersection case (both reach None)?
- Does the user use `is` (identity) rather than `==` (value equality)?

## Outcome (2026-07-03)

Went from `pass` straight to a fully correct two-pointer redirect solution in one commit — no intermediate hints or bugs. Only gap was using `!=` instead of `is not`; this worked by accident (no `__eq__` override on `ListNode`) but wasn't the explicit identity comparison the rubric targets. The user self-identified this exact issue while writing the blog's "Mistakes Made" section and then fixed `attempt.py` to use `is not` before closeout — self-catching happened during reflection/writing rather than during initial coding, a new variant worth tracking. Blog required zero revision cycles on the substantive sections; only the code fix was needed.
