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

## Coaching Watch-Points

- Does the user reach for a sliding window independently, or do they try brute force first?
- Do they track `formed` / a satisfaction counter, or check all counts on each step (O(52) overhead — acceptable but worth discussing)?
- Do they correctly handle the "shrink while valid" loop direction?
- Do they handle duplicates in `t` without special-casing them?
- Can they state the invariant in words before coding it?
