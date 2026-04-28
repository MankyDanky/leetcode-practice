class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m = len(grid)
        n = len(grid[0])
        t = grid[0][0] % x
        for i in range(m):
            for j in range(n):
                if grid[i][j] % x != t:
                    return -1
        l = [grid[i][j] for i in range(m) for j in range(n)]
        l.sort()
        c = m*n
        ind = c // 2
        targ = l[ind]
        res = 0
        for v in l:
            res += abs(targ - v) // x
        return res