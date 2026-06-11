# Rubric — First Missing Positive

## Skills to Observe

| Skill | What to Watch For |
| --- | --- |
| Bound recognition | Does the user notice the answer is bounded in [1, n+1]? |
| Index-as-hash insight | Does the user reach "use the array itself as a presence map"? |
| In-place placement | Does the user correctly implement cyclic swap / while-loop swap? |
| Duplicate guard | Does the user include `nums[nums[i]-1] != nums[i]` to avoid infinite loop? |
| Final scan | Does the user correctly scan and return `i+1` / `n+1`? |
| O(1) space discipline | Does the user avoid sorting or allocating extra arrays? |
| Invariant articulation | Can the user state what the array looks like after the placement pass? |

## Watch-For Patterns (from profile)

- May not immediately see the bound [1, n+1] — if stuck on "how to do it without extra space," ask about the range of possible answers.
- First attempt may try sorting (O(n log n)) or a set (O(n) space) — nudge toward the space constraint.
- May build a correct-shaped loop but miss the duplicate guard.
