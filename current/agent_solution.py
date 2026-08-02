"""
Agent reference solution for Number of Islands.

This file is separate from the user's attempt. Do not reveal it by default.
"""

from collections import deque


class Solution:
    def numIslands(self, grid: "list[list[str]]") -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def bfs(sr: int, sc: int) -> None:
            queue = deque([(sr, sc)])
            grid[sr][sc] = "0"
            while queue:
                r, c = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)

        return count
