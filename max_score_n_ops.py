class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def gcd(a, b):
            while a != b:
                if a > b:
                    a = a - b
                else:
                    b = b - a
            return a
        m = len(nums)
        n = m // 2
        mask = 0
        cache = {}
        def rec(iterations):
            
            nonlocal mask
            if iterations == n:
                return 0
            if (mask,iterations) in cache:
                return cache[(mask,iterations)]
            res = 0
            for i in range(m):
                for j in range(i+1, m):
                    if mask&(1<<i) == 0 and mask&(1<<j) == 0:
                        mask^=1<<i
                        mask^=1<<j
                        res = max(res, (iterations+1)*gcd(nums[i], nums[j]) + rec(iterations+1))
                        mask^=1<<i
                        mask^=1<<j
            cache[(mask,iterations)] = res
            return res
        return rec(0)