class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        memo = {}
        def rec(i1, i2):
            if (i1,i2) in memo:
                return memo[(i1,i2)]
            
            if i1 == m and i2 == n:
                memo[(i1,i2)] = 0
                return 0
            if i1 == m:
                memo[(i1,i2)] = n - i2
                return n - i2
            if i2 == n:
                memo[(i1,i2)] = m - i1
                return m - i1
            
            if word1[i1] == word2[i2]:
                memo[(i1,i2)] = rec(i1 + 1, i2 + 1)
                return memo[(i1,i2)]
            res = 1 + min(rec(i1 + 1, i2), # insert
                rec(i1, i2 + 1), # delete
                rec(i1 + 1, i2 + 1)) # replace
            memo[(i1,i2)] = res
            return res
        return rec(0,0)
            
            