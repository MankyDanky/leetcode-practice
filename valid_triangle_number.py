class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        r = 0
        res = 0
        for i in range(n):
            for j in range(i+1, n-1):
                r = bisect.bisect_left(nums, nums[i] + nums[j])
                res += (r-j - 1) if r > j else 0
        return res
