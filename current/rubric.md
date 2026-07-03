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
| Identifies the no-backward-traversal constraint | |
| Fast/slow pointer correctly finds middle (even + odd) | |
| Reversal applied correctly to the second half | |
| Comparison loop correct, including middle-node case | |
| Reaches O(1) space (vs. O(n) array/stack) | |
| Considers restoring the list | |
