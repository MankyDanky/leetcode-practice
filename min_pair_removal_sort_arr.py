class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0
        while sorted(nums) != nums:
            minPairSum = float("inf")
            minPairStart = -1
            n = len(nums)
            for i in range(n-1):
                if nums[i] + nums[i+1] < minPairSum:
                    minPairSum = nums[i] + nums[i+1]
                    minPairStart = i
            print(minPairSum, minPairStart, nums)
            nums.pop(minPairStart)
            nums[minPairStart] = minPairSum
            
            res += 1
        print(nums)
        return res
