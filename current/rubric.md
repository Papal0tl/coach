# Rubric — Palindrome Linked List

## Skill Targets

- **Constraint recognition**: identifies that no backward traversal / random access is the core obstacle, motivating either extra space or in-place reversal.
- **Fast/slow pointer mechanics**: correctly finds the middle node, handling even and odd lengths without an off-by-one error.
- **Reversal reuse**: applies the known reversal pattern to a sublist (from the middle onward) rather than the whole list.
- **Comparison correctness**: walks both halves in lockstep and terminates correctly regardless of the (possibly self-paired) middle node in odd-length lists.
- **Space optimization**: reaches or explains the O(1)-space approach, ideally after first stating the O(n)-space brute force.
- **Cleanup awareness**: considers (even if not required) restoring the list to its original structure.

## Evaluation

| Criterion | Result |
|---|---|
| Identifies the no-backward-traversal constraint | Implicitly — worked around it via value copy rather than stating it explicitly. |
| Fast/slow pointer correctly finds middle (even + odd) | Not attempted — O(1)-space follow-up declined. |
| Reversal applied correctly to the second half | Not attempted — O(1)-space follow-up declined. |
| Comparison loop correct, including middle-node case | Yes, via `vals == rev_val`; all 6 manual test cases pass. |
| Reaches O(1) space (vs. O(n) array/stack) | No — user chose to stop at the O(n)-space brute force. |
| Considers restoring the list | N/A — brute force doesn't mutate the list. |

## Bugs Fixed This Session

- `range()` called with 4 arguments instead of 3 (`TypeError`) — fixed after tracing a concrete example to find the correct `stop` value.
- Indexed with `cur.val[i]` instead of `vals[i]` — fixed in the same pass as the range fix.
- Used lowercase `true`/`false` instead of Python's `True`/`False` (`NameError`) — fixed immediately after being asked for the correct literal.
