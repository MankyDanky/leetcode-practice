class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        res = 0
        for col in range(m):
            prev = strs[0][col]
            for row in range(1, n):
                if strs[row][col] < prev:
                    res += 1
                    break
                prev = strs[row][col]
        return res