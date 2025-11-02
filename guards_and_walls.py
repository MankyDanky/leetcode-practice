class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        res = m * n
        for wall in walls:
            grid[wall[0]][wall[1]] = 1
            res -= 1

        for guard in guards:
            grid[guard[0]][guard[1]] = 2
            res -= 1

        for guard in guards:
            for di, dj in directions:
                i, j = guard[0], guard[1]
                while i+di >= 0 and i+di < m and j+dj >= 0 and j+dj < n and grid[i+di][j+dj] != 1 and grid[i+di][j+dj] != 2:
                    if (grid[i+di][j+dj] == 0):
                        res -= 1
                        grid[i+di][j+dj] = 3
                    i+=di
                    j+=dj
                    
        return res