class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res = float('inf')
        for i in range(n):
            l = nums[i]
            r = nums[i] * k
            bound = bisect.bisect_right(nums, r)
            res = min(res, n - (bound - i))
        return res