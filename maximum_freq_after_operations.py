class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        c = Counter(nums)
        nums.sort()
        curr = 0
        q = deque([])
        minElement = min(nums)
        maxElement = max(nums)

        res = 0

        def makeSame(i):
            l = bisect.bisect_left(nums, i-k)
            r = bisect.bisect_right(nums, i+k)
            elements = r - l
            if elements - c.get(i, 0) > numOperations:
                return numOperations + c.get(i,0)
            return elements

        for i in range(minElement, maxElement + 1):
            res = max(res, makeSame(i))
        return res
                
