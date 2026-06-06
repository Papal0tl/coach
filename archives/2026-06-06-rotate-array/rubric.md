# Rubric — rotate-array

## Target Skills

| Skill | Description | Watch For |
|---|---|---|
| Modulo reduction | Apply `k %= n` before any logic | Missing this causes index errors or wrong output when k ≥ n |
| In-place thinking | Avoid allocating an extra array | Allocating a copy is acceptable but watch whether the user considers the in-place constraint |
| Reversal trick | Three reversals achieve O(1) space rotation | User may not reach this directly — probe whether they can derive it from first principles |
| Segment boundary | `reverse(0, k-1)` and `reverse(k, n-1)` — off-by-one risk | Check whether k or k-1 is used as the split point |
| Edge case: k = 0 | No rotation; output equals input | Often not explicitly tested but caught by modulo step |
| Edge case: k ≥ n | Same as k % n | User may hardcode an early-return check instead of using modulo |

## Acceptance Criteria

- Modifies `nums` in-place (no returning a new list).
- Produces correct output for k = 0, k = n, k > n.
- Time: O(n). Space: ideally O(1), but O(n) with extra array is accepted.

## Session Outcome

- Modulo reduction: reached independently after one trace prompt. ✓
- In-place thinking: reached `nums[:] = ...` independently after one rebind prompt. ✓
- k → algorithm connection: first attempt ignored k entirely — needed prompting to notice.
- Slicing approach: O(n) space; reversal trick (O(1) space) not explored.

## Coaching Priority

1. First probe whether the user sees "last k elements move to front" as the restatement.
2. Then probe how they plan to do it in-place without a temporary copy.
3. If they reach reversal: verify they know where the segment boundary is.
4. If they use an extra array: that is fine; do not push toward reversal unless they ask.
