class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums) + 2
        memo = {}
        def rec(l, r):
            if l > n - 2:
                return 0
            if r < 1:
                return 0
            if (l,r) in memo:
                return memo[(l,r)]
            res = 0
            for i in range(l, r+1):
                res = max(
                    res, 
                    nums[i] * nums[l-1] * nums[r+1] + 
                    rec(l,i-1) + rec(i+1, r)
                )
            memo[(l,r)] = res
            return res
        
        nums = [1] + nums + [1]
        
        return rec(1, n - 2)