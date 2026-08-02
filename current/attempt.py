"""
User attempt for Number of Islands.

Write your reasoning in English comments when useful.
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        count = 0
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        for i in range(m):
            for i in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count

