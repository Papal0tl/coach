# Number of Islands

- Problem slug: `number-of-islands`
- Archive path: `archives/2026-08-02-number-of-islands/`

## Problem

Given an `m x n` grid of `'1'` (land) and `'0'` (water), count the number of
islands, where an island is a maximal group of `'1'` cells connected
horizontally or vertically (not diagonally).

## My Initial Intuition

A matrix where need to check each cell and look at its neighbors.

## Brute Force

Checking every land cell and its neighbors. A naive approach that repeatedly checks the same cells would do unnecessary work, so flood fill makes more sense.

## Key Insight

When find a '1', count one island and use DFS to turn the whole connected island into '0'. This prevents from counting the same island again.

## Final Algorithm

Scan every cell of the grid in row-major order (`for i in range(m): for j in range(n)`). Whenever a `'1'` is found, increment the island count and call a recursive `dfs(i, j)` that marks that cell and every cell reachable from it via up/down/left/right moves over `'1'` cells as `'0'` (visited), using out-of-bounds and `'0'` checks as the base cases. Because `dfs` exhausts an entire island before the outer scan continues, each island is only ever counted once, at the moment its first (top-left-most, in scan order) cell is reached.

## Correctness Argument

Marking each visited cell as '0' makes sure DFS does not visit the same land cell again. Without this, the same island could be counted multiple times.

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

N/A

## How I Will Recognize This Pattern Next Time

See a grid and need to count connected groups, should think of DFS or BFS flood fill. Find one unvisited cell, count it, and explore the whole connected region.
