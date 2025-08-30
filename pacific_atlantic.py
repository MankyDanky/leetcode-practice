class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights),len(heights[0])
        pac, atl = set(), set()

        def dfs(r,c,visit,prevHeight):
            if (r,c) in visit or r < 0 or c < 0 or r == m or c == n or heights[r][c] < prevHeight:
                return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        for i in range(m):
            dfs(i,0,pac,float("-inf"))
            dfs(i,n-1,atl,float("-inf"))
        
        for j in range(n):
            dfs(0,j,pac,float("-inf"))
            dfs(m-1,j,atl,float("-inf"))
        
        res = []
        for i in range(m):
            for j in range(n):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res

        

            