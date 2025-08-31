class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        memo = {}
        def rec(i1, i2):
            if (i1,i2) in memo:
                return memo[(i1,i2)]
            if i2 == n:
                memo[(i1, i2)] = 1
                return 1
            if i1 == m:
                memo[(i1, i2)] = 0
                return 0

            res = 0
            if s[i1] == t[i2]:
                res += rec(i1 + 1, i2 + 1)
            res += rec(i1 + 1, i2)
            memo[(i1, i2)] = res
            return res
        return rec(0,0)
            
