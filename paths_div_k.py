class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        dp = {}
        m = len(grid)
        n = len(grid[0])
        MOD = 1000000007
        dp[(0,0)] = {grid[0][0]%k : 1}
        for i in range(1, n):
            res = {}
            for rem in dp[(0, i-1)]:
                res[(rem + grid[0][i]) % k] = 1
            dp[(0, i)] = res
        
        for i in range(1, m):
            res = {}
            for rem in dp[(i-1, 0)]:
                res[(rem + grid[i][0]) % k] = 1
            dp[(i, 0)] = res

        for i in range(1, m):
            for j in range(1, n):
                res = {}
                for rem in dp[(i-1, j)]:
                    res[(rem + grid[i][j]) % k] = res.get((rem + grid[i][j]) % k, 0) + dp[(i-1, j)][rem]
                    res[(rem + grid[i][j]) % k] %= MOD
                
                for rem in dp[(i, j-1)]:
                    res[(rem + grid[i][j]) % k] = res.get((rem + grid[i][j]) % k, 0) + dp[(i, j-1)][rem]
                    res[(rem + grid[i][j]) % k] %= MOD
                dp[(i, j)] = res

        return dp[(m-1, n-1)].get(0, 0)
                