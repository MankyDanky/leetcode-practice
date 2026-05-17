class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        res = float("inf")
        n = len(nums)
        nums.sort()
        for i in range(k-1, n):
            res = min(res, nums[i] - nums[i-k+1])
        return res
