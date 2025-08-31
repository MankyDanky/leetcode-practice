from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
        return dp[amount] if dp[amount] != float("inf") else -1

        '''
        @lru_cache(maxsize=None)
        def rec(amt):

            if amt == 0:
                return 0
            
            least = float("inf")
            for coin in coins:
                
                if amt - coin >= 0:
                    v = 1 + rec(amt - coin)
                    least = min(least, v)
            return least'''
        res = rec(amount)
        return res if res != float("inf") else -1