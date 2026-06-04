# Rubric — maximum-subarray

## Target Skills

| Skill | Weight | Notes |
|---|---|---|
| Recognizing the DP / Kadane's pattern | High | Does the user reach for a running max or try O(n²) brute force? |
| Defining state: "max subarray ending here" | High | The key conceptual step — can the user name what `current_sum` represents? |
| The extend-or-restart decision | High | `max(num, current_sum + num)` — understanding when to drop the prefix |
| Correct initialization (not 0, but `nums[0]`) | Medium | Failing to handle all-negative arrays |
| Tracking a separate global max | Medium | Conflating running sum with answer |
| O(n) time, O(1) space | Medium | Can they state and justify the complexity? |

## Acceptance Criteria

- Correct output for all three provided examples. ✓
- Handles all-negative input (returns the largest element, not 0). ✓
- O(n) time, O(1) space. ✓
- Can state the invariant: `current_sum` is the best subarray sum ending at the current index. ✓ (stated precisely when asked)

## Coaching Watch-Points

- Does the user start with brute force (O(n²) or O(n³)) before optimizing?
- Do they initialize to 0 instead of `nums[0]` (common all-negative bug)?
- Do they confuse `current_sum` with `max_sum` (single-variable error)?
- Can they articulate *why* restarting is correct when `current_sum + num < num`?
- Do they need the DP framing, or do they find the greedy intuition more natural?
