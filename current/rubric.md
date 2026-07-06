# Rubric: Remove Nth Node From End of List

## Skill Targets

- Two-pointer gap technique (advance one pointer n steps ahead, then move both).
- Dummy-node usage for edge case where the head itself is removed.
- One-pass vs two-pass tradeoff awareness.

## Expected Signals

- Correct handling of removing the head node (n == length).
- No off-by-one errors in the gap size.
- Stated time/space complexity unprompted.

## Observed Outcome (2026-07-06)

- Used the two-pass length-counting approach (not the one-pass gap technique); dummy-node technique reused independently for the third consecutive session.
- One bug: `dummy.next` never linked to `head`, causing an `AttributeError`. Diagnosed correctly in one reply after a trace prompt.
- Complexity stated correctly in the blog (O(L) time, O(1) space) without prompting.
- Declined the one-pass gap-pointer follow-up, consistent with the established pattern of moving to the blog once a working solution passes tests.
- Archived at archives/2026-07-06-remove-nth-node-from-end-of-list/.
