class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(i, j):
            if i >= m or i < 0 or j >= n or j < 0:
                return
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for direction in directions:
                dfs(i + direction[0], j + direction[1])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i,j)
        return res
                