# Session Notes

- Problem slug: `rotting-oranges`
- Archive path: `archives/2026-08-05-rotting-oranges/`

## Agent Preparation

- Pattern: Multi-source BFS on a grid.
- Key insight: Start BFS simultaneously from every already-rotten cell instead of from a single source. Processing the queue level-by-level naturally corresponds to elapsed minutes, since all cells at BFS depth `t` become rotten at minute `t`.
- Invariant or state: The queue holds `(row, col, minute)` for cells that just became rotten. `minutes` tracks the timestamp of the most recently rotted cell, which equals the final answer once BFS completes. `fresh` counts remaining fresh oranges; if `fresh > 0` after BFS drains, some fresh orange was unreachable, so return `-1`.
- Complexity target: O(rows * cols) time (grid is at most 10x10 per constraints, so trivially fast either way), O(rows * cols) space for the queue.

## Reference Solution Summary

Two-pass approach:
1. Scan the grid once to seed the BFS queue with every rotten cell (minute 0) and count fresh oranges.
2. If there are no fresh oranges, return 0 immediately (matches Example 3).
3. Run BFS: for each cell popped, look at its 4 neighbors; if a neighbor is fresh, rot it, decrement the fresh count, record the current minute, and push it onto the queue.
4. After the queue drains, return `minutes` if all fresh oranges were rotted, else `-1`.

## Edge Cases

- No fresh oranges at all (answer 0, including all-empty or all-rotten grids).
- No rotten oranges but at least one fresh orange (answer -1, since nothing can ever spread).
- A fresh orange isolated by empty cells so it's unreachable (answer -1).
- Multiple rotten sources spreading simultaneously — the multi-source seeding is what makes this different from single-source BFS/shortest-path problems the user has seen before (e.g., staircase search in Search a 2D Matrix II, which was pruning, not spreading).
- 1x1 grid in each of its three states (0, 1, 2).

## User-Facing Takeaways

Pending — to be filled in after the user attempt and blog.

## Follow-Up Candidates

- Walls and Gates (LC 286) as a closely related multi-source BFS variant (distance-to-nearest-gate instead of infection-spread).
- 01 Matrix (LC 542) as another multi-source BFS distance problem, useful if this session goes smoothly and time allows.
