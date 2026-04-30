class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[[None] * (k+1) for _ in range(n)] for _ in range(m)]
        def rec(i, j, c):
            if i >= m or j >= n:
                return float("-inf")
            c += 1 if grid[i][j] > 0 else 0

            if c > k:
                return float("-inf")
            
            if i == m-1 and j == n-1:
                return grid[i][j]
            if dp[i][j][c] != None:
                return dp[i][j][c]
            dp[i][j][c] = max(grid[i][j] + rec(i, j+1, c), grid[i][j] + rec(i+1, j, c))
            return dp[i][j][c]
        res = rec(0,0,0)
        return -1 if res == float("-inf") else res
            