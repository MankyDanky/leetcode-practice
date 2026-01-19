class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        sqrSum = [[mat[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(1, n):
                sqrSum[i][j] = sqrSum[i][j-1] + sqrSum[i][j]

        for j in range(n):
            for i in range(1, m):
                sqrSum[i][j] = sqrSum[i-1][j] + sqrSum[i][j]

        def getSqrSum(i, j, l):
            res = sqrSum[i+l-1][j+l-1]
            if i > 0:
                res -= sqrSum[i-1][j+l-1]
            if j > 0:
                res -= sqrSum[i+l-1][j-1]
            if i > 0 and j > 0:
                res += sqrSum[i-1][j-1]
            return res

        res = 0
        for i in range(m):
            for j in range(n):
                count = 0
                while i + count + 1 <= m and j + count + 1 <= n:
                    count += 1
                    if getSqrSum(i, j, count) <= threshold:
                        res = max(res, count)
                    else:
                        break
        return res
