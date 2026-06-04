# Blog Review — maximum-subarray

**Date:** 2026-06-03
**Verdict:** Accepted

---

## Correctness

All sections are algorithmically correct.

- Brute force: correctly identifies O(n³) with `sum()` and O(n²) with a running sum. ✓
- Key insight: correctly describes the extend-or-restart decision and the role of `max(nums[i-1], 0)`. ✓
- Correctness argument: the two-choices proof (start fresh at `i` vs. extend from `i-1`) is the right argument. ✓
- Complexity: O(n) time, O(1) space — accurate. ✓
- Edge cases: all-negative, single element, all-positive — all handled correctly. ✓

## Key Insight and Invariant

The key insight is explained well. The `max(nums[i-1], 0)` logic and the extend-vs-drop decision are clear. The invariant (`nums[i]` stores the maximum subarray sum ending at `i`) appears explicitly in the Mistakes section, which is sufficient.

## Mistakes Made

Honest: no bugs were introduced, so the observation about the in-place mutation changing the meaning of `nums[i]` is the right thing to record. It's worth remembering for any in-place DP variant.

## Transfer Readiness

The "How to Recognize" section identifies the right triggers: contiguous subarray, optimization (max/min), and the "best ending at previous position" signal that points to the DP structure. The pattern is well-internalized.

One extension worth noting: the same "best ending here" structure shows up in variants like maximum subarray product, maximum circular subarray, and longest increasing subarray — wherever local optimality at each position can be computed from the previous position in O(1).

---

## Summary

Session complete. Correct solution on the first attempt, correct invariant stated when asked, and a sound blog covering all required sections. The extend-or-restart decision and the two-choices correctness argument are well understood.
