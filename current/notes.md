# Session Notes

- Problem slug: `number-of-islands`
- Archive path: `archives/2026-08-02-number-of-islands/`

## Agent Preparation

- Pattern: Connected components on an implicit grid graph, found via flood fill (BFS or DFS) from each unvisited land cell.
- Key insight: Every land cell reachable from a starting land cell via 4-directional moves belongs to the same island, so counting islands reduces to counting the number of times a fresh flood fill is triggered on an unvisited `'1'`.
- Invariant or state: Once a land cell has been visited (marked `'0'` in place, or added to a `visited` set), it is never revisited or recounted; the outer scan only starts a new flood fill on cells that are still `'1'`.
- Complexity target: O(rows * cols) time, since every cell is visited a constant number of times; O(rows * cols) space worst case for the BFS queue (or recursion stack for DFS) on an all-land grid, O(1) extra space if mutating the grid in place is acceptable (beyond the queue/stack).

## Reference Solution Summary

Scan every cell in row-major order. Whenever a `'1'` is found, increment the island count and run BFS from that cell, marking every reachable `'1'` (via up/down/left/right) as `'0'` so it is never counted again. BFS (explicit queue) is used instead of recursive DFS to avoid Python's recursion limit on large, snake-shaped islands (grid up to 300x300 = 90,000 cells).

## Edge Cases

- Empty grid or empty row (`grid == []` or `grid[0] == []`) -> 0 islands.
- Single cell, land or water.
- All water -> 0. All land -> 1.
- Diagonally adjacent land cells are NOT connected (only 4-directional adjacency counts) -> must be counted as separate islands.
- Non-square grids (1 row, or 1 column) still need correct bounds checks.
- Mutating the input grid in place is acceptable per problem statement, but worth calling out as a design choice (vs. a separate `visited` set) since it changes the caller-visible grid.

## User-Facing Takeaways

TBD after coaching.

## Follow-Up Candidates

- DFS (recursive or explicit-stack) as an alternate traversal, and why recursion depth matters here given the 300x300 constraint.
- Union-Find (Disjoint Set Union) as an alternative approach, relevant for the related "Number of Islands II" (online/streaming) variant.
- Complexity/space tradeoff: in-place grid mutation vs. a separate `visited` set.
