class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        k %= n
        for i in range(m):
            newRow = []
            for j in range(n):
                newRow.append(mat[i][((j+k) % n if j % 2 == 0 else (j - k) % n)])
            if newRow != mat[i]:
                return False
        return True