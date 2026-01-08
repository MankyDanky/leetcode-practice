class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        cache = {}
        n = len(nums1)
        m = len(nums2)

        def rec(index1, index2, empty):
            if (index1, index2, empty) in cache:
                return cache[(index1, index2, empty)]
            
            if index1 == n or index2 == m:
                return float("-inf") if empty else 0

            res = nums1[index1] * nums2[index2] + rec(index1+1, index2+1, False)
            res = max(res, rec(index1+1, index2, empty))
            res = max(res, rec(index1, index2+1, empty))
            cache[(index1, index2, empty)] = res
            return res
        return rec(0,0, True)