# Coaching Notes — Palindrome Linked List

## Session

- Date: 2026-07-03
- Problem: LC 234 Palindrome Linked List
- Language: Python
- Mode: hint-only

## Key Insight

Checking a palindrome normally means comparing values from both ends inward, but a singly linked list has no backward pointer and no O(1) random access — you can't walk from the end. The O(1)-space trick is to physically reverse the second half of the list in place, so the "from the end" comparison becomes a forward walk on the reversed segment, run in parallel with a forward walk on the first half.

This composes three patterns already seen this session series: fast/slow pointer to find the middle (new here), and the pointer-reversal mechanics from reverse-linked-list (reused directly, applied to only half the list).

## Invariant

- **Middle-finding**: `fast` moves two nodes for every one `slow` moves; when `fast` reaches the end (or `None`), `slow` is at the middle (upper middle for even length, exact middle for odd length).
- **Comparison walk**: after reversing from `slow` onward, walking `first` from `head` and `second` from the new second-half head in lockstep visits mirrored positions of the original list. The list is a palindrome iff every paired value matches until `second` (the shorter or equal-length half) is exhausted.

## Complexity

- Time: O(n) — middle-finding, reversal, comparison, and restoration are each a single O(n) pass.
- Space: O(1) — only a constant number of pointers; no auxiliary array or recursion stack.

## Edge Cases

- Single node: `fast.next` is `None` immediately, `slow` stays at head; reversing a 1-node list is a no-op; comparison loop with `second` at that node trivially matches. ✓
- Even length (e.g. `[1,2]`): `fast` becomes `None` after one step, `slow` lands on the first node of the second half — reversal and comparison split the list into two equal halves.
- Odd length (e.g. `[1,2,3,2,1]`): `slow` lands on the true middle node; the middle node ends up compared against itself, which is harmless (any value equals itself).
- Restoring the list: LeetCode doesn't require it, but flagging as good practice — mutating input structures silently is a footgun to avoid in interviews.

## Coaching Targets

- Does the user recognize that reversing a copy/portion of the list is the way around "no backward traversal," rather than reaching for an O(n)-space array/stack first?
- Does the user use fast/slow pointers to find the middle correctly (off-by-one on even vs. odd length is the classic bug here)?
- Does the user reuse the reversal mechanics from the earlier session correctly when applied to a sublist rather than the whole list?
- Does the user notice or care about restoring the list after comparison?
- Can the user state why the middle node being compared to itself (odd-length case) doesn't break correctness?

## Follow-Up Candidates

- O(n) space brute force (copy values into a list/array, two-pointer compare) as a natural first step before the O(1) optimization.

## Observations — First Attempt (2026-07-03)

Went straight for the O(n)-space brute force (collect values, build reversed list, compare) — matches the anticipated first step. Not yet run; has not been self-tested. Several issues present:

- `range(len(vals), -1, -1, -1)` — 4 arguments; `range()` only accepts up to 3 (start, stop, step). Will raise `TypeError` immediately.
- Inside that loop, indexes with `cur.val[i]` instead of `vals[i]` — `cur` is `None` by this point (loop above already exhausted it), so this would fail even if the `range` call were fixed.
- Uses `true`/`false` (lowercase) instead of Python's `True`/`False` — `NameError`, since JS/Java capitalization habits don't carry over.
- Not yet run against `tests.py`, so none of this has been surfaced by execution.

Asked the user to run it against `tests.py` themselves rather than pointing out each bug directly, to see what they self-diagnose from the traceback.
