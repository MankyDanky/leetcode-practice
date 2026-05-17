class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        prefix = [[0] * n for _ in range(m)]
        suffix = [[0] * n for _ in range(m)]
        res = [[0] * n for _ in range(m)]
        curr = 1
        MOD = 12345
        for i in range(m):
            for j in range(n):
                prefix[i][j] = curr
                curr *= grid[i][j]
                curr %= MOD
        curr = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                suffix[i][j] = curr
                curr *= grid[i][j]
                curr %= MOD

        for i in range(m):
            for j in range(n):
                res[i][j] = (suffix[i][j] * prefix[i][j]) % MOD
        return res