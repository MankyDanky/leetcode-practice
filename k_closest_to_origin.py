class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for point in points:
            d = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(res, (-d, (point[0], point[1])))
            if len(res) > k:
                heapq.heappop(res)
        
        return list(map(lambda x: list(x[1]), res))