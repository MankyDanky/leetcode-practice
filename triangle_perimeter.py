class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        nums.sort()
        k = n-1
        for i in range(n-2, -1, -1):
            j = i + 1
            while nums[k] >= nums[i] + nums[j]:
                k -= 1
            if k == j:
                continue
            return nums[k] + nums[i] + nums[j]
        return res