class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        cache = {}
        n = len(s1)
        m = len(s2)

        def rec(i1, i2):
            if (i1,i2) in cache:
                return cache[(i1,i2)]
            if i1 == n and i2 == m:
                return 0
            if i1 == n:
                res = ord(s2[i2]) + rec(i1, i2+1)
                cache[(i1,i2)] = res
                return res
            if i2 == m:
                res = ord(s1[i1]) + rec(i1 + 1, i2)
                cache[(i1,i2)] = res
                return res
            if s1[i1] == s2[i2]:
                res = rec(i1+1, i2+1)
                cache[(i1, i2)] = res
                return res
            res = min(ord(s1[i1]) + rec(i1+1, i2), ord(s2[i2]) + rec(i1, i2+1))
            cache[(i1, i2)] = res
            return res
        return rec(0,0)