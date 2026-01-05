class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        vals = []
        minAbs = float("inf")
        hasZ = False
        negCount = 0
        for i in range(n):
            for j in range(n):
                vals.append(abs(matrix[i][j]))
                if matrix[i][j] == 0:
                    hasZ = True
                minAbs = min(minAbs, abs(matrix[i][j]))
                if matrix[i][j] < 0:
                    negCount += 1
        s = sum(vals)

        if negCount % 2 == 0 or hasZ:
            return s
        return s - 2*minAbs