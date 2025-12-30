class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        for i in range(n-2):
            for j in range(m-2):
                seen = set()
                valid = True
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if grid[k][l] in seen or not (1 <= grid[k][l] <= 9):
                            valid = False
                            break
                        seen.add(grid[k][l])
                    if not valid:
                        break
                if not valid:
                    continue
                
                s = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != s or grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2] != s:
                    continue
                for k in range(i, i+3):
                    if grid[k][j] + grid[k][j+1] + grid[k][j+2] != s:
                        valid = False
                        break
                if not valid:
                    continue
                for k in range(j, j+3):
                    if grid[i][k] + grid[i+1][k] + grid[i+2][k] != s:
                        valid = False
                        break
                if not valid:
                    continue
                res += 1
        return res
                