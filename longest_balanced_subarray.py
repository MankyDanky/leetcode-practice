class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        
        res = 0
        n = len(nums)
        for i in range(n):
            counts = {}
            currOdd = 0
            currEven = 0
            for j in range(i, n):
                counts[nums[j]] = counts.get(nums[j], 0) + 1
                if counts[nums[j]] == 1:
                    if nums[j] % 2:
                        currOdd += 1
                    else:
                        currEven += 1
                if currOdd == currEven:
                    res = max(res, j - i + 1)
        return res