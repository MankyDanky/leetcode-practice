class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        q = []

        visited = set()

        for i in range(m):
            heapq.heappush(q, (heightMap[i][0], i, 0))
            heapq.heappush(q, (heightMap[i][n-1], i, n-1))
            visited.add((i,0))
            visited.add((i, n-1))

        for j in range(1, n - 1):
            heapq.heappush(q, (heightMap[0][j], 0, j))
            heapq.heappush(q, (heightMap[m-1][j], m-1, j))
            visited.add((0, j))
            visited.add((m-1, j))

        res = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minBoundaryHeight = 0
        while q:
            height, i, j = heapq.heappop(q)
            minBoundaryHeight = max(minBoundaryHeight, height)
            
            for di, dj in directions:
                if (di + i, dj + j) not in visited and (0 <= di + i < m) and (0 <= dj + j < n):
                    
                    newHeight = heightMap[di+i][dj+j]
                    heapq.heappush(q, (newHeight, di+i, dj+j))
                    visited.add((di+i, dj+j))
                    if newHeight < minBoundaryHeight:
                        res += minBoundaryHeight - newHeight
        return res