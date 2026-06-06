# Blog Review — rotate-array

**Date:** 2026-06-06
**Verdict:** Accepted with one fix required (typo)

---

## Correctness

- Final algorithm: correct.
- Complexity: correct — O(n) time, O(n) space.
- Edge cases: correct and complete.
- Correctness argument: solid. The user correctly identifies that `nums[-k:]` extracts exactly the elements that belong at the front after reducing k, and `nums[:-k]` covers the rest.

## Key Insight

Present and correct. The user names the two core observations — rotating by n is the identity, and the result is `last_k + first_(n-k)` — and connects them to the implementation. Acceptable depth for a concise blog.

## Invariant

Implicit but sufficient. The user's correctness argument shows understanding that after `k %= n`, the slice boundaries are exact.

## Mistakes Section

Strong. Three distinct mistakes are named with concrete examples:
1. Loop that ignored k entirely.
2. `nums[:k]` vs `nums[:-k]` — traced with a specific example showing element 4 is lost.
3. k > n causing unexpected Python slice behavior.

This level of specificity is useful for future recall.

## Transfer Readiness

Ready. The pattern recognition section correctly identifies the two signals: cyclic shift framing and the two-part split structure. Could add one more signal (k mod n appearing in constraints), but not required for acceptance.

## Required Revisions

One fix needed before commit:

- **Typo in Key Insight:** "Rotatr" → "Rotate".

Fix the typo and save. No other changes needed.
