# Rubric — Product of Array Except Self

## Target Skills

| Skill | What to observe |
|---|---|
| Prefix/suffix decomposition | Does the user break the problem into left product × right product? |
| Two-pass scan | Does the user recognise that two linear passes suffice (no nested loop)? |
| O(1) space optimisation | Does the user reuse the output array instead of allocating two separate prefix/suffix arrays? |
| Invariant articulation | Can the user state what the running variable represents at each step? |
| Edge-case awareness | Does the user consider zeros and negatives without being prompted? |

## Known Growth Areas to Watch

- Input→algorithm connection: watch for a first attempt that ignores or misuses the relationship between position i and the surrounding elements.
- Preprocessing recognition: watch for a brute-force nested-loop approach before recognising the two-pass pattern.
- Invariant articulation in writing: blog Key Insight section should name the invariant explicitly.

## Acceptance Criteria

- Correct output on all provided examples.
- O(n) time — no nested loops.
- No division used.
- In-place output (O(1) extra space) is a stretch goal; two-array solution also accepted.
