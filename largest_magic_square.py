class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 1
        for i in range(n):
            for j in range(m):
                count = 1
                while i + count < n and j + count < m:
                    s = 0
                    for k in range(i, i+count+1):
                        s += grid[k][j]
                    flag = False
                    for k in range(i, i+count+1):
                        t = 0
                        for l in range(j, j+count+1):
                            t += grid[k][l]
                        if t != s:
                            flag = True
                            break
                    if flag:
                        count += 1
                        continue
                    
                    for k in range(j, j+count+1):
                        t = 0
                        for l in range(i, i+count+1):
                            t += grid[l][k]
                        if t != s:
                            flag = True
                            break
                    if flag:
                        count += 1
                        continue
                    
                    t = 0
                    r = 0
                    for k in range(count+1):
                        t += grid[i+k][j+k]
                        r += grid[i + count - k][j+k]
                    if t != s or r != s:
                        count += 1
                        continue
                    count += 1
                    res = max(res, count)
        return res