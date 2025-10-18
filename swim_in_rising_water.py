class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        q = [(grid[0][0], 0, 0)]
        visited = set()
        res = grid[0][0]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(grid)
        n = len(grid[0])
        height_cache = [[float("inf") for _ in range(n)] for _ in range(m)]

        while q:
            height, i, j = heapq.heappop(q)

            if i == m-1 and j == n-1:
                return height
            visited.add((i,j))

            for di, dj in directions:
                
                if 0 <= i + di < m and 0 <= j + dj < n:
                    new_height = max(grid[i+di][j+dj], height)
                    if (i+di, j+dj) not in visited and new_height < height_cache[di+i][dj+j]:
                        heapq.heappush(q, (new_height, i+di, j+dj))
                        height_cache[di+i][dj+j] = new_height


    