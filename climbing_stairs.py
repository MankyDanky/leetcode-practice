from functools import lru_cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def rec(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            return rec(n-1) + rec(n-2)
        return rec(n)