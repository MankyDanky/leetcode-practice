class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        increasingLength = [0] * n
        prev = float("-inf")
        curr = 0
        for i in range(n-1, -1, -1):
            if nums[i] < prev:
                curr += 1
            else:
                curr = 1
            prev = nums[i]
            increasingLength[i] = curr
        print(increasingLength)

        def checkK(k):
            for i in range(k, n):
                if increasingLength[i-k] >= k and increasingLength[i] >= k:
                    return True
            return False
        
        l = 1
        r = n//2
        while l < r:
            mid = math.ceil((l+r)/2)
            if checkK(mid):
                l = mid
            else:
                r = mid - 1

        return l
