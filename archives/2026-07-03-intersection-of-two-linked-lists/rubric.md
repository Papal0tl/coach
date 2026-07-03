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
| Uses `is` (not `==`) for node comparison | Initially used `!=` (accidentally correct since `ListNode` has no `__eq__`); self-identified the gap while writing the blog and corrected to `is not` before closeout. |
| Reaches two-pointer redirect (independently or with hints) | Independent — went from `pass` to the full correct redirect solution in a single attempt, no intermediate hints needed. |
| No-intersection case handled correctly | Yes — passes all test cases including simultaneous-`None` termination. |
| Can explain why path lengths equalize after redirect | Yes — blog correctness argument precisely states the m + n cancellation and cites the shared-suffix timing. |
| O(1) space achieved | Yes, from the first attempt. |
| Edge cases pass | Yes — full test suite (8 cases) passes against `attempt.py`. |
