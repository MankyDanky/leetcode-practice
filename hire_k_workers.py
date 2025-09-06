class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ratios = []
        n = len(wage)
        for i in range(n):
            ratios.append((wage[i]/quality[i], quality[i]))
        ratios.sort()
        total_quality = 0
        res = float("inf")
        quality_heap = []
        r = 0
        for i in range(n):
            if i < k:
                heapq.heappush(quality_heap, -ratios[i][1])
                total_quality += ratios[i][1]
                r = i
                continue

            res = min(res, ratios[r][0] * total_quality)
            if ratios[i][1] >= -quality_heap[0]:
                continue
            r = i
            total_quality += heapq.heappop(quality_heap)
            heapq.heappush(quality_heap, -ratios[i][1])
            total_quality += ratios[i][1]
        res = min(res, ratios[r][0] * total_quality)
        return res