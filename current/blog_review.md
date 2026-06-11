# Blog Review — Product of Array Except Self

**Date:** 2026-06-10  
**Status:** Accepted

---

## Correctness

- Problem summary, algorithm, complexity, and edge cases: all correct.
- Brute force description matches the code written. O(n²) correctly identified.
- Correctness argument is solid: correctly states that the left pass stores the exclusive prefix product, and that the right pass updates after processing each index.

---

## Missing or Imprecise

### Key Insight — invariant not stated explicitly

The blog says "can build them incrementally" but does not state *what the running variable holds at each step* as a precise property.

The invariant is:

- **During the left pass**, at the moment `answer[i] = left` executes, `left` = product of `nums[0..i-1]` (exclusive of `nums[i]`).
- **During the right pass**, at the moment `answer[j] *= right` executes, `right` = product of `nums[j+1..n-1]` (exclusive of `nums[j]`).

Without naming this, the Key Insight section reads as mechanics rather than understanding. The correctness argument section does cover this implicitly, but the Key Insight section should state the invariant as a short, precise property.

### Mistakes — one bug missing

The blog names two mistakes:
1. O(n²) brute force.
2. `answer[j] = right` overwriting the left product.

There was a third bug: `right *= nums[i]` used the wrong loop variable (`i` from the outer loop rather than `j`). This caused the suffix to multiply by the same element every iteration instead of advancing. It should be included.

---

## Clarity

Good overall. The correctness argument is clearer than most previous blogs. The pattern-recognition section is one of the strongest yet — the "operation is associative" generalisation is a genuine transfer insight.

---

## Transfer Readiness

Almost there. The pattern-recognition bullets are strong. The missing piece is the invariant: being able to precisely state what the running variable holds at each step is what lets you adapt this pattern when the pass direction or accumulation order changes. Add it to Key Insight and this blog is complete.

---

## Required Revisions

1. **Key Insight**: add a precise statement of what `left` and `right` hold at the moment they are used — not just "build incrementally" but the exact boundary (`exclusive of index i`, etc.).
2. **Mistakes**: add the `nums[i]` → `nums[j]` variable bug in the right pass.
