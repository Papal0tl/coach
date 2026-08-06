# Problem

- Name: Rotting Oranges
- Slug: `rotting-oranges`
- Source: https://leetcode.cn/problems/rotting-oranges/description/?envType=study-plan-v2&envId=top-100-liked (LeetCode 994)
- Archive path: `archives/2026-08-06-rotting-oranges/`

## Statement

You are given an `m x n` grid where each cell can have one of three values:

- `0` representing an empty cell,
- `1` representing a fresh orange,
- `2` representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.

## Examples

Example 1:

```text
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

Example 2:

```text
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

Example 3:

```text
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
```

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10`
- `grid[i][j]` is `0`, `1`, or `2`.

## Clarifications

- Adjacency is 4-directional only (up, down, left, right), not diagonal.
- Multiple oranges can already be rotten at minute 0 (multi-source spread).

## Input / Output Shape

- Input: `grid: List[List[int]]`
- Output: `int` (minutes elapsed, or `-1` if unreachable)
