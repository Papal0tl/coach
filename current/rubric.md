# Rubric — Reverse Linked List

## Skill Targets

- **Pointer-save discipline**: saves `cur.next` before overwriting it, avoiding losing the rest of the list.
- **Correct initialization**: starts `prev` at `None` so the original head terminates correctly.
- **Invariant articulation**: can state that `prev` holds the reversed-so-far sublist and `cur` holds the remaining sublist.
- **Empty/single-node handling**: no special-case branching needed if the loop condition is written correctly.
- **Recursive variant**: attempts or explains the recursive approach and its invariant (reverse the rest, then relink).
- **O(1) space**: achieves this with the iterative approach.

## Evaluation

| Criterion | Result |
|---|---|
| Saves `cur.next` before rewiring | Yes — correct on first attempt. |
| `prev` initialized to `None` | Yes. |
| Can state the loop invariant | Yes — stated precisely and unprompted: "prev holds the reversed sublist, cur holds the remaining unprocessed sublist." |
| Empty list handled without special-casing | Yes — loop naturally skips when `head is None`. |
| Attempts or explains recursive version | Not yet — to be probed next. |
| O(1) space (iterative) achieved | Yes. |
