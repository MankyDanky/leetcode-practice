
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        memo = [[-1] * (n + 1) for _ in range(m + 1)]
        memo[m][n] = 0

        def rec(i1, i2):
            if memo[i1][i2] != -1:
                return memo[i1][i2]
            if i1 >= m or i2 >= n:
                memo[i1][i2] = 0
                return 0
            if text1[i1] == text2[i2]:
                memo[i1][i2] = 1 + rec(i1 + 1, i2 + 1)
                return memo[i1][i2]
            
            memo[i1][i2] =  max(rec(i1, i2 + 1), rec(i1 + 1, i2))
            return memo[i1][i2]
        
        rec(0, 0)
        return memo[0][0]