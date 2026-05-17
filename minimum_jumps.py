class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dp(index):
            if (index == n-1):
                return 0
            res = float("-inf")
            for i in range(index+1, n):
                if abs(nums[i] - nums[index]) <= target:
                    res = max(res, 1 + dp(i))
            return res
        
        res = dp(0)
        return res if (res != float("-inf")) else -1