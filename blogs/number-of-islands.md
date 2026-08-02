# Number of Islands

- Problem slug: `number-of-islands`
- Archive path: `archives/2026-08-02-number-of-islands/`

## Problem

Given an `m x n` grid of `'1'` (land) and `'0'` (water), count the number of
islands, where an island is a maximal group of `'1'` cells connected
horizontally or vertically (not diagonally).

## My Initial Intuition

User-filled. What did the grid remind you of when you first read the problem — what kind of structure or prior problem did you connect it to?

## Brute Force

User-filled. Is there a slower approach you considered before settling on flood fill (even if you didn't write it), or was flood fill the immediate approach? Why would a naive approach (e.g. checking every cell against every other cell) not make sense here?

## Key Insight

User-filled. What is the one idea that lets a single scan-and-flood-fill correctly count islands without ever double-counting a cell?

## Final Algorithm

Scan every cell of the grid in row-major order (`for i in range(m): for j in range(n)`). Whenever a `'1'` is found, increment the island count and call a recursive `dfs(i, j)` that marks that cell and every cell reachable from it via up/down/left/right moves over `'1'` cells as `'0'` (visited), using out-of-bounds and `'0'` checks as the base cases. Because `dfs` exhausts an entire island before the outer scan continues, each island is only ever counted once, at the moment its first (top-left-most, in scan order) cell is reached.

## Correctness Argument

User-filled, with agent prompts if needed. Why is it enough to mark a cell as `'0'` once visited — what would go wrong if `dfs` did not do this?

## Complexity

- Time: O(m * n) — every cell is visited by the outer loop once, and by `dfs` at most once (each cell is marked `'0'` the first time it is visited, so `dfs` never revisits a cell).
- Space: O(m * n) worst case — the recursion stack depth equals the number of cells in the largest island, since `dfs` calls itself once per cell along the flood-fill path. On the largest allowed grid (300 x 300 = 90,000 cells), a single winding island could exceed Python's default recursion limit (1000) and raise a `RecursionError`, even though the algorithm is logically correct. Converting to an iterative approach (explicit stack, or BFS with a queue) removes this risk.

## Edge Cases

Agent-filled as a checklist; user should add any cases they personally missed.

- Empty grid or empty row -> 0 islands (not exercised by this problem's constraints, since `m, n >= 1`, but worth noting).
- Single cell, land or water.
- All water -> 0 islands. All land -> 1 island.
- Diagonally adjacent land cells are separate islands (only 4-directional adjacency connects).
- Non-square grids (a single row or a single column).
- A large, winding island that stresses recursion depth (see Complexity above).

## Mistakes I Made

User-filled.

## How I Will Recognize This Pattern Next Time

User-filled. When you see a grid of `'1'`/`'0'` (or similar) and are asked to count/label connected regions, what should that immediately suggest as the approach?
