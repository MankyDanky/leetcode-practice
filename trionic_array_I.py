class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        l = 0
        r = n-1
        
        while l + 1 < n and nums[l+1] > nums[l]:
            l += 1
        while r - 1 >= 0 and nums[r-1] < nums[r]:
            r -= 1
        
        if l == 0 or r == n-1:
            return False
        
        if l >= r:
            return False


        for i in range(l+1, r+1):
            if nums[i] >= nums[i-1]:
                return False
        return True