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

User-filled. What did this problem remind you of when you first read it — a grid you'd seen before, or something new? Was it obvious from the start that this needed to spread from *multiple* starting points at once, rather than just one?

## Brute Force

User-filled. Is there a slower approach you considered — for example, repeatedly scanning the whole grid minute-by-minute and rotting any fresh orange next to a rotten one, until nothing changes? Why is that more expensive than the BFS approach you wrote?

## Key Insight

User-filled. What is the one idea that lets you compute the answer in a single pass instead of repeatedly rescanning the whole grid minute-by-minute?

## Final Algorithm

Scan the grid once to seed a queue with the coordinates of every already-rotten cell (these are the multiple BFS sources) and count the fresh oranges. If there are no fresh oranges, the answer is immediately 0. Otherwise, run BFS level by level: on each iteration, drain exactly the number of cells currently in the queue (`size = len(queue)`), and for each one check its four neighbors; any neighbor that is still fresh (`grid[nr][nc] == 1`) gets marked rotten, has the fresh count decremented, and is pushed onto the queue for the next level. After fully draining one level, increment the minute counter. Once the queue empties, return the minute counter if the fresh count reached 0, otherwise return -1, since some fresh orange was never reached.

## Correctness Argument

User-filled, with agent prompts if needed. Why does draining the queue exactly `size` cells at a time (rather than popping and pushing in the same unbounded loop) guarantee that the minute counter equals the true number of elapsed minutes? What would go wrong if you incremented the minute counter once per popped cell instead of once per fully-drained level?

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

User-filled.

## How I Will Recognize This Pattern Next Time

User-filled. When you see a grid where something spreads outward simultaneously from more than one starting point, and you need to know how long the spread takes, what should that immediately suggest as the approach?
