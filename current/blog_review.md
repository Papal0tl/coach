# Blog Review — merge-intervals

**Date:** 2026-06-05
**Verdict:** Accepted

---

## Correctness

All algorithmic content is correct.

- Brute force: O(n²) pairwise — accurate. ✓
- Key insight: sort by start, compare only against `res[-1]` — correct. ✓
- Correctness argument: states that after sorting, if `cur_start > res[-1][1]` then no earlier interval in `res` can be affected either — the right claim. ✓
- Complexity: O(n log n) time, O(n) space — accurate. ✓
- Edge cases: all correct. ✓

## Key Insight and Invariant

The key insight is clear. The invariant (`res[-1]` holds the fully-merged result of all processed intervals so far) is implicit in the correctness argument. Sufficient.

## Mistakes Made

Both mistakes are recorded honestly and explained correctly:
- Comparing against `intervals[i-1][1]` instead of `res[-1][1]` — clear. ✓
- Seeding with `intervals[0]` vs `[intervals[0]]` — detailed and correct. ✓

## Transfer Readiness

The revised "How to Recognize" section is a clear improvement. It describes the structural signals:
- Input is intervals/ranges of the form `[start, end]`.
- Goal is to merge or simplify overlapping ranges.
- Intervals are in arbitrary order.
- After sorting, the decision at each step depends only on `res[-1]`.

And it names the strategy: sort by start → scan left to right → maintain current merged interval → merge or append. This is transferable.

---

## Summary

Session complete. Correct solution reached through guided tracing. The two key bugs (comparing `intervals[i-1][1]` vs `res[-1][1]`, and seeding `res` correctly) were both diagnosed by the user through concrete examples. Blog covers all required sections with accurate content. Pattern recognition is now described in terms of signals, not problem names.
