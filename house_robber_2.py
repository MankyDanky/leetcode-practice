class Solution:
    def rob_one(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[1], nums[0])
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[0] + nums[2]

        for i in range(3, n):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3])
        
        return max(dp[-1], dp[-2])

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_one(nums[:-1]), self.rob_one(nums[1:]))