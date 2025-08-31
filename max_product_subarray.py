class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = suffix = 1
        n = len(nums)
        res = nums[0]
        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n-i-1] * (suffix or 1)
            res = max(res, prefix, suffix)
        return res




