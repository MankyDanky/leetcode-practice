class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        q = [(0, 0, 0)]
        INF = float("inf")
        m = len(heights)
        n = len(heights[0])
        max_differences = [[INF] * n for _ in range(m)]
        max_differences[0][0] = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        visited = set()
        while q:
            curr_max_difference, i, j = heapq.heappop(q)
            if (i,j) in visited:
                continue
            visited.add((i,j))
            if i == m-1 and j == n-1:
                return curr_max_difference
            for di, dj in directions:
                if 0 <= di + i < m and 0 <= dj + j < n:
                    next_difference = abs(heights[di + i][dj + j] - heights[i][j])
                    max_difference = max(next_difference, curr_max_difference)
                    if max_difference < max_differences[di + i][dj + j]:
                        max_differences[di + i][dj + j] = max_difference
                        heapq.heappush(q, (max_difference, di + i, dj + j))
        