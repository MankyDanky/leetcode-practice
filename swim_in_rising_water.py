class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        q = [(grid[0][0], 0, 0)]
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        visited = set()

        n = len(grid)
        visited.add((0,0))
        while q:
            height, i, j = heapq.heappop(q)
            if i == n-1 and j == n-1:
                return height
            for di, dj in directions:
                i_n = i + di
                j_n = j + dj
                if (i_n, j_n) in visited or i_n >= n or i_n < 0 or j_n >= n or j_n < 0:
                    continue
                visited.add((i_n,j_n))
                heapq.heappush(q, (max(height, grid[i_n][j_n]), i_n, j_n))
                        
    