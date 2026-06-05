# Blog Review — merge-intervals

**Date:** 2026-06-05
**Verdict:** Revisions requested

---

## Correctness

All algorithmic content is correct.

- Brute force: O(n²) pairwise comparison — accurate. ✓
- Key insight: sorting by start, then comparing only against `res[-1]` — correct. ✓
- Correctness argument: the claim "it cannot overlap with res[-1] or any earlier interval" is the right claim and is stated clearly. ✓
- Complexity: O(n log n) time, O(n) space — accurate. ✓
- Edge cases: all correct. ✓

## Key Insight and Invariant

The key insight is present: sort by start, then a one-step-back comparison against `res[-1]` suffices. The invariant (`res[-1]` is the fully-merged interval covering all processed intervals that overlap with each other) is implicit in the correctness argument but not named as a statement. Sufficient for this problem — no revision needed here.

## Mistakes Made

Both mistakes are recorded honestly and with correct explanations:
- Comparing against `intervals[i-1][1]` instead of `res[-1][1]` — described clearly. ✓
- Seeding `res = intervals[0]` vs `res = [intervals[0]]` — the explanation is detailed and correct. ✓

## Transfer Readiness — Revision Required

The "How to Recognize" section lists five problem names. That is not transfer readiness — it is a list of answers. A future problem won't announce itself by name; you need to recognize it from its shape.

**Revise this section to answer:** What signals in a problem's statement tell you to try sorting intervals and scanning with a running merged result? Describe the triggers, not the titles.

---

## Summary

Strong blog overall — correctness, insight, and mistakes are all solid. One required revision: rewrite "How to Recognize" to describe the problem signals that indicate this pattern, not just the names of problems that use it.
