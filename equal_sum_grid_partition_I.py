class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        rowSums = []
        columnSums = []


        for i in range(m):
            s = 0
            for j in range(n):
                s += grid[i][j]
            rowSums.append(s)

        for j in range(n):
            s = 0
            for i in range(m):
                s += grid[i][j]
            columnSums.append(s)

        prs = []
        pcs = []

        curr = 0
        for s in rowSums:
            curr += s
            prs.append(curr)
        
        curr = 0
        for s in columnSums:
            curr += s
            pcs.append(curr)

        for i in range(m):
            if prs[i] == prs[m-1] - prs[i]:
                return True
            
        for j in range(n):
            if pcs[j] == pcs[n-1] - pcs[j]:
                return True
        return False