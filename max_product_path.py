class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        MOD=int(1e9) + 7

        @lru_cache(None)
        def dfs(i, j):
            if (i == m-1 and j == n-1):
                return (grid[i][j], grid[i][j])
            
            g = grid[i][j]

            sub1 = (0,0)
            if i+1 < m:
                sub1 = dfs(i+1, j)
            
            sub2 = (0,0)
            if j+1 < n:
                sub2 = dfs(i, j+1)
            

            ms1 = min(g * sub1[0], g * sub1[1]) if i+1 < m else float("inf")
            ms2 = min(g * sub2[0], g * sub2[1]) if j+1 < n else float("inf")
            xs1 = max(g * sub1[0], g * sub1[1]) if i+1 < m else float("-inf")
            xs2 = max(g * sub2[0], g * sub2[1]) if j+1 < n else float("-inf")

            r = (min(ms1, ms2),
                max(xs1, xs2))
            return r

        res = dfs(0,0)
        r = max(res[0], res[1])
        return r % MOD if r >= 0 else -1