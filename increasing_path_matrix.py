class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = ((0,1), (0,-1), (1,0), (-1,0))
        m = len(matrix)
        n = len(matrix[0])

        memo = [[-1]*n for _ in range(m)]
        def dfs(i,j):
            res = 1
            if memo[i][j] != -1:
                return memo[i][j]
            
            for di, dj in directions:
                if 0 <= di + i < m and 0 <= dj+j < n:
                    if matrix[di + i][dj + j] > matrix[i][j]:
                        res = max(res, 1 + dfs(i + di, j + dj))
            memo[i][j] = res
            return res
        
        res = 1
        for i in range(m):
            for j in range(n):
                res = max(dfs(i,j), res)
        return res