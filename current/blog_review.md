# Blog Review — maximum-subarray

**Date:** 2026-06-03
**Verdict:** Revision required — one incomplete section

---

## Correctness

All filled-in sections are algorithmically correct.

- Brute force: correctly identifies O(n³) with `sum()` and O(n²) with a running sum. ✓
- Key insight: correctly describes the extend-or-restart decision and the role of `max(nums[i-1], 0)`. ✓
- Correctness argument: the two-choices proof (start fresh at `i` vs. extend from `i-1`) is the right argument. ✓
- Complexity: O(n) time, O(1) space — accurate. ✓
- Edge cases: all-negative, single element, all-positive — all handled correctly. ✓

## Key Insight and Invariant

The key insight is explained well. The `max(nums[i-1], 0)` logic and the extend-vs-drop decision are clear.

The invariant (`nums[i]` stores the maximum subarray sum ending at index `i`) appears in the Mistakes section but is not named explicitly in the Key Insight or Correctness Argument. It's present enough to be acceptable — the two-choices argument in Correctness implicitly relies on it.

## Mistakes Made

Honest. The user didn't introduce bugs this session, so there were no real mistakes to report. The observation about `nums[i]` changing meaning is accurate and worth remembering for in-place DP variants.

## Transfer Readiness

The extend-or-restart logic and the two-choices argument are well internalized. The user will recognize this pattern when they see it again.

**One gap:** The "How to Recognize This Pattern Next Time" section is still a `TODO`. This is a required section. Transfer readiness cannot be confirmed without it.

## Required Revision

Complete the **How to Recognize This Pattern Next Time** section. Answer: what problem shapes, keywords, or constraints should trigger "track the best subarray-ending-here value"?

---

Review will be updated after the revision is submitted.
