class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        counts = [[[0, 0] for s in range(n+1)] for t in range(m+1)]

        for i in range(m):
            for j in range(n):
                counts[i+1][j+1][0] += counts[i+1][j][0] + (1 if grid[i][j] == 'X' else 0)
                counts[i+1][j+1][1] += counts[i+1][j][1] + (1 if grid[i][j] == 'Y' else 0)
        
        for i in range(m):
            for j in range(n):
                t = list(counts[i+1][j+1])
                counts[i+1][j+1][0] += counts[i][j+1][0]
                counts[i+1][j+1][1] += counts[i][j+1][1]

        res = 0

        for i in range(m):
            for j in range(n):
                if counts[i+1][j+1][0] >= 1 and counts[i+1][j+1][0] == counts[i+1][j+1][1]:
                    res += 1
        return res
