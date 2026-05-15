class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        if nums[0] < nums[-1]: return nums[0]
        while l < r - 1:
            mid = (l+r)//2
            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
        return nums[r]