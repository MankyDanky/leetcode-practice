class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        requirements.sort()
        m = requirements[-1][0]
        cache = {}
        MOD = 10**9 + 7

        def rec(i, req):
            
            if req < 0:
                return 0
            if (i,req) in cache:
                return cache[(i,req)]
            r_i = bisect.bisect_left(requirements, [i, 0])
            if r_i < len(requirements):
                if requirements[r_i][0] == i and req != requirements[r_i][1]:
                    cache[(i,req)] = 0
                    return 0
                if requirements[r_i][0] > i and req > requirements[r_i][1]:
                    cache[(i,req)] = 0
                    return 0
            
            
            if i == 0:
                cache[(i,req)] = 1 if req == 0 else 0
                return cache[(i,req)]
            res = 0
            for j in range(i+1):
                res += rec(i-1, req - (i - j)) % MOD
            cache[(i,req)] = res % MOD
            return res % MOD
        return rec(requirements[-1][0], requirements[-1][1]) % MOD
            
