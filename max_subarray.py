class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = float("-inf")
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        curr = 0
        for i in range(len(nums)):
            if curr < 0:
                curr = 0
            curr += nums[i]
            res = max(curr, res)
        res = max(curr, res)
        return res