class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        cache = {}
        def rec(prev1, prev2, index):
            if index == n:
                return 0
            if (prev1, prev2, index) in cache:
                return cache[(prev1, prev2, index)]

            if (nums1[index] <= prev1 and nums2[index] <= prev1) or (nums2[index] <= prev2 and nums1[index] <= prev2):
                cache[(prev1, prev2, index)] = -1
                return -1
            res = float("inf")
            if nums1[index] > prev1 and nums2[index] > prev2:
                sub = rec(nums1[index], nums2[index], index + 1)
                if sub != -1:
                    res = sub
            if nums1[index] > prev2 and nums2[index] > prev1:
                sub = rec(nums2[index], nums1[index], index + 1)
                if sub != -1:
                    res = min(res, 1 + sub)
            cache[(prev1, prev2, index)] = res
            return res
       
        return rec(float("-inf"), float("-inf"), 0)
            