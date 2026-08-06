# Rotting Oranges

- Problem slug: `rotting-oranges`
- Archive path: `archives/2026-08-05-rotting-oranges/`

## Problem

Given an `m x n` grid where each cell is `0` (empty), `1` (fresh orange), or
`2` (rotten orange), every minute any fresh orange 4-directionally adjacent
to a rotten orange becomes rotten. Return the minimum number of minutes
until no cell has a fresh orange, or `-1` if some fresh orange can never
rot.

## My Initial Intuition

Rotten oranges can spread to nearby fresh oranges, and multiple rotten oranges can spread at the same time. use grid BFS

## Brute Force

Repeatedly scan the whole grid every minute and rot fresh oranges next to rotten ones. This would keep scanning cells that were already processed, so it is less efficient than BFS.

## Key Insight

The key is to put all rotten oranges into the queue at the beginning and use level-order BFS. Each BFS level represents one minute.

## Final Algorithm

Scan the grid once to seed a queue with the coordinates of every already-rotten cell (these are the multiple BFS sources) and count the fresh oranges. If there are no fresh oranges, the answer is immediately 0. Otherwise, run BFS level by level: on each iteration, drain exactly the number of cells currently in the queue (`size = len(queue)`), and for each one check its four neighbors; any neighbor that is still fresh (`grid[nr][nc] == 1`) gets marked rotten, has the fresh count decremented, and is pushed onto the queue for the next level. After fully draining one level, increment the minute counter. Once the queue empties, return the minute counter if the fresh count reached 0, otherwise return -1, since some fresh orange was never reached.

## Correctness Argument

size = len(queue) records all rotten oranges that exist at the start of the current minute. Any oranges that become rotten during this level are added to the queue, but they are not processed until the next level. Therefore, each BFS level represents exactly one minute. If we increased minutes for every popped cell, the time would depend on how many oranges were processed, instead of how many minutes actually passed.

## Complexity

- Time: O(m * n) — the initial scan visits every cell once, and BFS visits each cell at most once (a cell is only pushed onto the queue the first time it turns from fresh to rotten, since the `grid[nr][nc] == 1` check prevents revisiting it).
- Space: O(m * n) worst case for the queue, if most of the grid starts as rotten oranges (all seeded into the queue in the first scan) or becomes rotten during BFS.

## Edge Cases

Agent-filled as a checklist; user should add any cases they personally missed.

- No fresh oranges at all (already-solved grid, including all-empty or all-rotten) -> 0.
- Fresh oranges present but no rotten oranges anywhere -> -1, since nothing can ever start spreading.
- A fresh orange separated from every rotten orange by an empty (`0`) cell -> -1, since rot only spreads to *adjacent* fresh oranges, not through empty cells. (This was the case that exposed a real bug in the first draft — see Mistakes below.)
- Multiple rotten oranges spreading at once, where the answer is governed by the *slowest* fresh orange to be reached, not the fastest.
- 1x1 grid in each of its three possible states.

## Mistakes I Made

- I initially allowed rot to spread through empty cells (0), instead of only spreading to directly adjacent fresh oranges (1). This caused oranges that should stay fresh to become rotten.

## How I Will Recognize This Pattern Next Time

If something spreads from multiple starting points at the same time and I need to find how long it takes, I should think of multi-source BFS.
