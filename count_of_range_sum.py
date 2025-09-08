class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        sums = [0] * n
        sums[0] = nums[0]
        if n == 1:
            return 1 if lower <= nums[0] <= upper else 0
        for i in range(1, n):
            sums[i] = sums[i-1] + nums[i]
        
        sums_wrapped = [(sums[i], i) for i in range(n)]

        res = 0
        for s in sums:
            res += 1 if lower <= s <= upper else 0

        def mergeSort(nums):
            r = len(nums)
            if r < 2:
                return nums
            mid = r // 2

            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])

            res = merge(left, right)
            return res
        
        def merge(nums1, nums2):
            nonlocal res
            l = 0
            r = 0
            len1 = len(nums1)
            len2 = len(nums2)
            merged = []

            while l < len1 and r < len2:
                if nums1[l][0] < nums2[r][0]:
                    merged.append(nums1[l])
                    l += 1
                else:
                    merged.append(nums2[r])
                    r += 1
                
            while l < len1:
                merged.append(nums1[l])
                l += 1
            
            while r < len2:
                merged.append(nums2[r])
                r += 1
            
            l = 0
            r = 0

            high = 0
            low = 0
            for l in range(len1):
                while low < len2 and nums2[low][0] - nums1[l][0] < lower:
                    low += 1
                
                while high < len2 and nums2[high][0] - nums1[l][0] <= upper:
                    high += 1
                res += high - low
            return merged
        mergeSort(sums_wrapped)
        return res
            

            
