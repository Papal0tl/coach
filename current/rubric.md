# Rubric — Intersection of Two Linked Lists

## Skill Targets

- **Identity vs. equality**: uses `is` to compare nodes by reference, not `==` by value.
- **Two-pointer redirect**: discovers or applies the redirect-at-end trick to equalize path lengths.
- **No-intersection handling**: correctly returns `None` when both pointers reach the end simultaneously.
- **Path-length argument**: can explain that after redirect both pointers travel m + n - c steps to the intersection.
- **O(1) space**: avoids storing visited nodes in a set (if the user reaches O(1) space independently).
- **Edge cases**: handles equal-length lists, intersection at head, single-node lists.

## Evaluation

| Criterion | Result |
|---|---|
| Uses `is` (not `==`) for node comparison | |
| Reaches two-pointer redirect (independently or with hints) | |
| No-intersection case handled correctly | |
| Can explain why path lengths equalize after redirect | |
| O(1) space achieved | |
| Edge cases pass | |
