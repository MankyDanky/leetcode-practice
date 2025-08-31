class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n = len(s3)
        if n != n1 + n2:
            return False

        memo = [[-1] * (n2 + 1) for _ in range(n1 + 1)]
        memo[n1][n2] = True
        def rec(i1, i2):
            if memo[i1][i2] != -1:
                return memo[i1][i2]
            
            if i1 == n1:
                if s3[i1 + i2] != s2[i2]:
                    memo[i1][i2] = False
                    return False
                memo[i1][i2] = rec(i1, i2+1)
                return memo[i1][i2]
            
            if i2 == n2:
                if s3[i1 + i2] != s1[i1]:
                    memo[i1][i2] = False
                    return False
                memo[i1][i2] = rec(i1 + 1, i2)
                return memo[i1][i2]
            
            res = False
            if s3[i1 + i2] == s1[i1]:
                res = res or rec(i1 + 1, i2)
            
            if s3[i1 + i2] == s2[i2]:
                res = res or rec(i1, i2 + 1)
            memo[i1][i2] = res
            return res
        return rec(0,0)