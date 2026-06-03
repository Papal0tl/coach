# Session Notes — maximum-subarray

**Date:** 2026-06-03
**Language:** Python
**Mode:** hint-only

## Agent Pre-Solve Notes

### Pattern
Dynamic programming (Kadane's algorithm). Classic "maximum subarray sum" shape — a 1-D DP that runs in a single pass.

### Key Insight
At every index `i`, the maximum subarray sum *ending at* `i` is either:
- Just `nums[i]` alone (drop everything before it), or
- `nums[i]` added to the best subarray ending at `i-1`.

Choose whichever is larger: `current_sum = max(nums[i], current_sum + nums[i])`.  
Track the global best alongside it.

### Invariant
`current_sum` always equals the maximum subarray sum ending exactly at the current index.

When `current_sum` would become negative by extending, it is cheaper to start a new subarray at the next element than to carry the dead weight forward.

### Algorithm Sketch
1. Initialize `current_sum = max_sum = nums[0]`.
2. For each `num` in `nums[1:]`:
   - `current_sum = max(num, current_sum + num)`
   - `max_sum = max(max_sum, current_sum)`
3. Return `max_sum`.

### Complexity
- Time: O(n) — single pass.
- Space: O(1) — two scalars.

### Edge Cases
- All negative: returns the largest (least negative) element. Initialization to `nums[0]` and the `max(num, ...)` branch handle this without special-casing.
- Single element: loop body never executes; `nums[0]` is returned directly.
- All positive: `current_sum` grows monotonically; entire array is the answer.

### Validation
Tests written in `tests.py`. Not run locally (user declined shell execution); solution is a textbook application of Kadane's algorithm and is correct by inspection.

## Coaching Log

<!-- Entries added per turn -->
