class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])

        p = [None] * m * n * 3

        def dp(i,j,k):
            res = float("-inf")

            if i >= m:
                return res
            if j >= n:
                return res
            index = i + j * m + k * (m * n)
            if p[index] != None:
                return p[index]
            
            if k > 0 and coins[i][j] < 0:

                if i == m-1 and j == n-1:
                    p[index] = 0
                    return 0
                
                res = max(dp(i+1, j, k-1), dp(i,j+1, k-1))
            
            if i == m-1 and j == n-1:
                p[index] = coins[i][j]
                return coins[i][j]

            res = max(res, dp(i+1, j, k) + coins[i][j])
            res = max(res, dp(i, j+1, k) + coins[i][j])
            
            p[index] = res
            return res
        
        return dp(0,0,2)

            