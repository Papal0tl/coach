# Rubric — merge-intervals

## Target Skills

| Skill | Weight | Notes |
|---|---|---|
| Recognizing that sorting by start time enables a linear scan | High | The key unlock — unsorted input makes comparisons intractable |
| Overlap condition: `current_end >= next_start` | High | Touching counts; must use >= not > |
| Merge step: extend `current_end` to `max(current_end, next_end)` | High | Must handle fully-contained intervals correctly |
| Initializing the result with the first interval | Medium | Common off-by-one: forgetting to seed the merge list |
| Handling a single interval | Low | Trivial if structure is correct |
| O(n log n) time, O(n) space | Medium | Sorting dominates; output list is O(n) |

## Acceptance Criteria

- Correct output for all three provided examples.
- Handles touching intervals (e.g., [1,4],[4,5] → [1,5]).
- Handles unsorted input correctly.
- Handles a fully-contained interval (e.g., [1,10],[2,5] → [1,10]).
- O(n log n) time, O(n) space — user can state and justify.

## Coaching Watch-Points

- Does the user realize sorting is needed before trying to scan?
- Do they use `>` instead of `>=` for the overlap check (missing touching case)?
- Do they forget to extend with `max(current_end, next_end)` (missing contained intervals)?
- Do they attempt an O(n²) approach before seeing the sorted-scan structure?
