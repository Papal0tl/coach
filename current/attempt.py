"""
User attempt for Rotting Oranges.

Write your reasoning in English comments when useful.
"""
from collections import deque

class Solution:
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0
        min = 0
        dir = [(1,0), (-1,0), (0,1), (0,-1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        while queue and fresh > 0:
            size = len(queue)
            for i in range(size):
                r, c = queue.popleft()
                for dr, dc in dir:
                    nr = r + dr
                    nc = c + dc
                    if (0 <= nr < rows and 0 <= nc < cols):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            min += 1
        return min

