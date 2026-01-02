class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == nums[(i+1)%n] or nums[i] == nums[(i-1)%n]:
                return nums[i]
            if nums[(i-1)%n] == nums[(i+1)%n]:
                return nums[(i+1)%n]