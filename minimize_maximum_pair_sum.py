class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        r = n-1

        res = 0
        while l < r:
            res = max(nums[l] + nums[r], res)
            l += 1
            r -= 1
        return res
