# Session Notes — First Missing Positive

## Problem Pattern

Index-as-hash-map (cyclic placement / index marking). The array is used as its own hash table by placing value `x` at index `x-1`.

## Key Insight

The answer to "smallest missing positive" for an array of length `n` must lie in `[1, n+1]`. Any number outside `[1, n]` is irrelevant. This bound lets us use the array indices themselves as a presence table — no extra space needed.

## Invariant

After the placement phase: `nums[i] == i + 1` for every index `i` where the value `i+1` was present in the original array. The first index that violates this gives the answer.

## Algorithm Sketch

1. For each position `i`, swap `nums[i]` to its "home" index `nums[i]-1` while the value is in `[1, n]` and the home slot doesn't already hold the correct value.
2. Scan left to right; return the first `i+1` where `nums[i] != i+1`.
3. If the full array satisfies the invariant, return `n+1`.

## Complexity

- Time: O(n) — each element is moved to its home at most once; the while loop does O(n) total swaps.
- Space: O(1) auxiliary — in-place.

## Edge Cases

| Case | Expected |
| --- | --- |
| All non-positive | 1 |
| `[1]` | 2 |
| `[2]` | 1 |
| Complete `[1..n]` | n+1 |
| Duplicates | handled by `nums[nums[i]-1] != nums[i]` guard |
| All values > n | 1 |

## Coaching Observations

- User independently reached two-pass structure (placement + scan) and correct scan/return logic. While condition lower bound written; upper bound and swap body still missing. Good structural instinct, needs to fill in the mechanism.
- Swap written correctly on first try. Duplicate guard (`nums[nums[i]-1] != nums[i]`) added after one trace of [1,1] showing infinite loop. Solution passes all tests.
- Invariant stated precisely and unprompted: "after the placement loop, nums[i] == i+1 wherever i+1 was present." Best invariant articulation observed so far across all sessions.
- Blog accepted after 2 revisions (brute force constraint reason + pattern name). Minor phrasing issue in Mistakes Made accepted by user.
