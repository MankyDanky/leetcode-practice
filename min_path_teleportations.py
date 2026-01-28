class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        INF = float("inf")
        m = len(grid)
        n = len(grid[0])

        order = [(grid[i][j], i, j) for i in range(m) for j in range(n)]

        order.sort()

        index_map = {(i, j): idx for idx, (v, i, j) in enumerate(order)}

        prevDp = [[INF] * (n) for _ in range(m)]


        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    prevDp[i][j] = 0
                elif i == m-1:
                    prevDp[i][j] = prevDp[i][j+1] + grid[i][j+1]
                elif j == n-1:
                    prevDp[i][j] = prevDp[i+1][j] + grid[i+1][j]
                else:
                    prevDp[i][j] = min(prevDp[i+1][j] + grid[i+1][j], prevDp[i][j+1] + grid[i][j+1])

        for t in range(1, k+1):
            dp = [[INF] * (n) for _ in range(m)]

            running_min = INF
            prefix_min = [INF] * (m * n)
            idx = 0
            while idx < len(order):
                idx2 = idx
                while idx2 < len(order) and order[idx2][0] == order[idx][0]:
                    val, i, j = order[idx2]
                    running_min = min(running_min, prevDp[i][j])
                    idx2 += 1
                for poop in range(idx, idx2):
                    prefix_min[poop] = running_min
                idx = idx2

            for i in range(m-1, -1, -1):
                for j in range(n-1, -1, -1):
                    if i == m-1 and j == n-1:
                        dp[i][j] = 0
                    elif i == m-1:
                        dp[i][j] = dp[i][j+1] + grid[i][j+1]
                    elif j == n-1:
                        dp[i][j] = dp[i+1][j] + grid[i+1][j]
                    else:
                        dp[i][j] = min(dp[i+1][j] + grid[i+1][j], dp[i][j+1] + grid[i][j+1])
                    dp[i][j] = min(dp[i][j], prefix_min[index_map[(i, j)]])

            prevDp = dp

        return prevDp[0][0]