# Session Notes — merge-intervals

**Date:** 2026-06-05
**Language:** Python
**Mode:** hint-only

## Agent Pre-Solve Notes

### Pattern
Sorting + linear scan. Sort by interval start, then make one pass: compare each interval to the last committed one and either extend it or start a new one.

### Key Insight
After sorting by start time, any interval that overlaps with an earlier interval *must* overlap with the most recently committed interval — because its start is at most as large as the next interval's start. This means we only ever need to look back one step, enabling an O(n) scan after sorting.

### Invariant
`merged[-1]` is the fully-merged interval covering all intervals processed so far that overlap with each other. No already-committed entry in `merged` can be extended by any future interval (because inputs are sorted and future starts are ≥ current starts).

### Overlap Condition
Two intervals `[a, b]` and `[s, e]` (with `a ≤ s`) overlap when `s <= b`. The `<=` is critical: touching counts (Example 2 — `[1,4],[4,5]` → `[1,5]`).

### Merge Step
When overlapping, extend the end: `merged[-1][1] = max(merged[-1][1], e)`. The `max` is necessary for fully-contained intervals: if `[2,5]` follows `[1,10]`, the end must stay at 10, not shrink to 5.

### Algorithm
1. Sort `intervals` by `start`.
2. Seed: `merged = [intervals[0]]`.
3. For each `[s, e]` in `intervals[1:]`:
   - If `s <= merged[-1][1]`: `merged[-1][1] = max(merged[-1][1], e)`
   - Else: `merged.append([s, e])`
4. Return `merged`.

### Complexity
- Time: O(n log n) — sort dominates; the scan is O(n).
- Space: O(n) — output list holds up to n intervals.

### Edge Cases
- Single interval: loop body never executes; seed is returned directly. ✓
- All overlapping: one interval grows to contain everything. ✓
- Touching intervals (`s == current_end`): `<=` catches this. ✓
- Fully-contained interval: `max` on end keeps the wider bound. ✓
- Already sorted: sort is a no-op; algorithm still correct. ✓

### Validation
All 11 tests pass locally with python3.

## Coaching Log

*(Empty — user has not yet attempted.)*
