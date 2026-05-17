class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        counterR = [0] * m
        counterC = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    counterR[i] += 1
                    counterC[j] += 1

        res = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and counterR[i] == 1 and counterC[j] == 1:
                    res += 1
        return res
                    