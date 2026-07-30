# Rubric: Path Sum III

## Skills to Observe

- **Brute-force construction**: does the user reach for "DFS from every node, downward, checking sums" as a first correct baseline?
- **Pattern recognition (new)**: prefix-sum-on-a-tree is untested in this arc so far. Watch whether the "prefix sum + hashmap" idea (transferred from array prefix-sum problems, e.g. subarray-sum-equals-k) is recognized independently, or needs the backtracking/decrement hint.
- **Invariant formulation**: can the user state precisely why `prefix_count` must only reflect the current root-to-node path (ancestors), not the whole tree seen so far?
- **Backtracking discipline**: the decrement step (`prefix_count[running_sum] -= 1` after recursing into both children) is easy to omit; omitting it doesn't crash, it silently overcounts. This is a good test of whether the user notices a *wrong answer* bug (not a traceback) and whether they debug it via reasoning or via tracing a small hand example.
- **Complexity analysis**: O(n) vs. brute-force O(n^2)/O(n log n), and explaining *why* the hashmap approach avoids repeated re-summation.
- **Edge-case design**: negative values, target 0 with a zero-chain, path not starting at root.

## Not Yet Scored

- Problem restatement
- Constraint analysis
- Test design (agent writes tests in this workflow)

## Notes

This is the fourteenth tree-arc session and the first requiring an
accumulator (running sum) combined with a hashmap keyed by that accumulator,
rather than a purely structural recursive shape. Expect brute force first
per this user's established pattern (LC 238, LC 148, LC 98 all had a brute
force or wrong-first-strategy before the optimal approach).
