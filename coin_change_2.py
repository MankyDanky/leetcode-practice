class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        memo = [[-1] * (n + 1) for _ in range(amount + 1)]
        for i in range(n+1):
            memo[0][i] = 1

        for i in range(amount + 1):
            memo[i][n] = max(memo[i][n], 0)

        for amt in range(1, amount + 1):
            for start in range(n - 1, -1, -1):
                res = 0
                if amt - coins[start] >= 0:
                    res += memo[amt - coins[start]][start]
                res += memo[amt][start + 1]
                memo[amt][start] = res

        return memo[amount][0]
