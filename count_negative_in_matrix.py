class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        j = m-1
        res = 0
        for i in range(n):
            while j >= 0 and grid[i][j] < 0:
                j -= 1
            res += m - (j + 1)
        return res
