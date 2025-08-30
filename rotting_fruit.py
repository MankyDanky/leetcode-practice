class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
        
        directions = ((0,1),(0,-1),(-1,0),(1,0))
        time = -1
        def isValid(i,j):
            return i < m and i >= 0 and j < n and j >= 0 and grid[i][j] == 1

        while q:
            print(q)
            for i in range(len(q)):
                pos = q.popleft()
                for direction in directions:
                    i_n,j_n = pos[0] + direction[0], pos[1] + direction[1]
                    if isValid(i_n, j_n):
                        grid[i_n][j_n] = 2
                        q.append((i_n, j_n))

            time += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return max(time,0)