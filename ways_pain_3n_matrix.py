class Solution:
    def numOfWays(self, n: int) -> int:
        cache = {}

        MOD = 1000000007

        valid = [(1,2,1), (2,1,2), (3,1,2),
                 (1,2,3), (2,1,3), (3,1,3),
                 (1,3,1), (2,3,1), (3,2,1),
                 (1,3,2), (2,3,2), (3,2,3)]

        def rec(prev, row):
            if (row == n):
                return 1
            
            if (prev, row) in cache:
                return cache[(prev, row)]
            
            res = 0
            for curr in valid:
                flag = False
                for i in range(3):
                    if curr[i] == prev[i]:
                        flag = True
                        break
                if flag:
                    continue
                res = (res + rec(curr, row+1)) % MOD
            cache[(prev, row)] = res
            return res
        return rec((0,0,0), 0)
