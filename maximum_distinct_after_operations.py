class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        r = n-1
        nums[0] -= k
        for i in range(1, n):
            if abs(nums[i-1] + 1 - nums[i]) <= k:
                nums[i] = nums[i-1] + 1
            elif nums[i] > nums[i-1]:
                nums[i] -= k
            else:
                nums[i] = nums[i-1]
        print(nums)
        return len(set(nums))
            
        