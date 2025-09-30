class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) != 1:
            nextNums = [0] * (len(nums) - 1)
            for i in range(len(nums) - 1):
                nextNums[i] = (nums[i] + nums[i+1]) % 10
            nums = nextNums
        return nums[0]