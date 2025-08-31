class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        NINF = float("-inf")
        
        memo = [[-1, -1] for _ in range(n+2)]
        memo[n][0], memo[n][1] = 0, 0
        memo[n+1][0], memo[n+1][1] = 0, 0
        for i in range(n-1, -1, -1):
            memo[i][0] = max(memo[i+1][1] - prices[i], memo[i+1][0])
            memo[i][1] = max(memo[i+2][0] + prices[i], memo[i+1][1])
        return memo[0][0]