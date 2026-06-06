# Session Notes — rotate-array

**Date:** 2026-06-06
**Language:** Python
**Mode:** hint-only

## Agent Pre-Solve Notes

### Pattern
Three-reversal trick. Rotate right by k ≡ move the last k elements to the front.
Rather than physically relocating elements in one pass (which requires a temporary buffer),
three in-place reversals achieve the same permutation with O(1) extra space.

### Key Insight
Reversing the entire array puts the last k elements at the front and the first n-k at the back,
but both segments are in reversed order. Reversing each segment independently corrects their order.
The net effect is exactly a right rotation by k.

### Invariant
After `reverse(0, n-1)` and `reverse(0, k-1)`:
`nums[0:k]` is already in its final correct state.
After `reverse(k, n-1)`:
`nums[k:]` is in its final correct state.
No element is visited more than twice across all three passes.

### Modulo Reduction
`k %= n` is required. Rotating by n is the identity; rotating by k and k+n are identical.
k can be up to 10^5 while n can be as small as 1, so k % n can be 0 even when k > 0.
When k % n == 0, every reverse is a no-op and the array is unchanged — correct.

### Algorithm
1. `k %= n`
2. `reverse(0, n-1)`
3. `reverse(0, k-1)`
4. `reverse(k, n-1)`

### Complexity
- Time: O(n) — each element is swapped at most twice (once per relevant reversal).
- Space: O(1) — all reversals are in-place.

### Edge Cases
- k = 0 or k % n = 0: all three reverses are no-ops or empty ranges; array unchanged. ✓
- k = n - 1: first segment of length n-1, second segment of length 1 (single element). ✓
- n = 1: k % 1 = 0 always; reverse on a single element is a no-op. ✓
- k > n: reduced to k % n; see above. ✓

### Alternative Approaches
- Extra array: `result[i] = nums[(i - k) % n]`. O(n) time, O(n) space. Simpler but uses extra memory.
- Cyclic replacements: follow each displacement cycle. O(n) time, O(1) space but trickier to implement correctly.
- Naive k rotations: O(n·k) — too slow for large k.

### Validation
All 10 tests pass locally with python3.

## Coaching Log
