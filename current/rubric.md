# Rubric — minimum-window-substring

## Target Skills

| Skill | Weight | Notes |
|---|---|---|
| Sliding window with two pointers | High | Core technique |
| Frequency counting with hash map | High | Tracking character coverage |
| Coverage invariant — knowing when window is valid | High | The key insight |
| Shrinking the window from the left | Medium | Optimization step |
| Handling duplicates in t | Medium | Edge-case awareness |
| O(m + n) time, O(1) / O(52) space | Medium | Complexity awareness |

## Acceptance Criteria

- Correct output for all three provided examples.
- Handles duplicates in `t`.
- Handles no-solution case (return `""`).
- Time complexity O(m + n).
- Can explain the invariant: the window is valid when all required character counts are satisfied.
