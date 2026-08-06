# Session Notes

- Problem slug: `rotting-oranges`
- Archive path: `archives/2026-08-06-rotting-oranges/`

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

- Independently structured the level-by-level BFS shape (`size = len(queue)`, drain exactly that many before incrementing the minute counter) without being told — this is the core invariant of the pattern and it was self-generated.
- Four real bugs this session, all logic/invariant-level rather than syntax:
  1. `queue.append(rows)` — pushed the row count instead of the `(r, c)` coordinate tuple. Self-diagnosed correctly in one sentence once asked to trace it ("oh it's just pushing the number of rows, not the coordinates"), but did not apply the fix until asked a second time in a later round.
  2. Off-by-one bounds check, `0 < nr < rows` instead of `0 <= nr < rows` — excluded row/col index 0 from ever being treated as a valid neighbor. Self-corrected after being asked to trace a neighbor at index 0.
  3. Missing value check on the neighbor before rotting it (`grid[nr][nc] == 1`) — without it, the code rotted *any* in-bounds neighbor regardless of value, silently corrupting empty (`0`) cells into rotten (`2`) ones and decrementing `fresh` for non-fresh cells. This one was subtle: all 8 of the agent's original tests passed despite the bug, because none of them had an empty cell physically between a rotten and a fresh orange. Only surfaced by constructing a new counterexample (`[[2, 0, 1]]`, expected `-1`) and asking the user to run it themselves.
  4. Missing `fresh == 0` guard on the final return — returned `min` unconditionally instead of `-1` when unreachable fresh oranges remained. Fixed in the same edit as bug 3, without a separate prompt — likely inferred from constructing the fix for bug 3.
- Two consecutive rounds this session where the user asked "check the code" with **no actual diff** — once immediately after being asked a conceptual question rather than making an edit. Treated gently as a possible workflow/mechanical mixup (confirmed via `git status`) rather than assumed intent; worth watching if this recurs.
- Bug 3 is a good teaching moment for test-coverage thinking: passing all existing tests did not mean the code was correct, and the fix required *adding* a test rather than re-running old ones. Flag for the blog's Mistakes Made section.

## Follow-Up Candidates

- Walls and Gates (LC 286) as a closely related multi-source BFS variant (distance-to-nearest-gate instead of infection-spread).
- 01 Matrix (LC 542) as another multi-source BFS distance problem, useful if this session goes smoothly and time allows.
