class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            if len(h) == k:
                heapq.heappushpop(h, num)
            else:
                heapq.heappush(h, num)
        return h[0]