class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(i, j):
            if i >= m or i < 0 or j >= n or j < 0:
                return 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            a = 1
            for direction in directions:
                a += dfs(i + direction[0], j + direction[1])
            return a
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(dfs(i,j), res)
        return res