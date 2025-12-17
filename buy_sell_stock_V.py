class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        dp = [[[[-1] * n for _ in range(k)] for _ in range(2)] for _ in range(2)]
        def rec(index, done, running, t):
            if index == n or done == k:
                if (running):
                    if (t == 0):
                        return -1000000000
                    else:
                        return 0
                else:
                    return 0
            if dp[t][running][done][index] != -1:
                return dp[t][running][done][index]
            res = 0
            if running:
                if t == 1:
                    res = max(prices[index] + rec(index+1, done+1, False, 0), rec(index+1, done, running, t))
                else:
                    res = max(-prices[index] + rec(index+1, done+1, False, 0), rec(index+1, done, running, t))
                dp[t][running][done][index] = res
                return res
            else:
                res = rec(index+1, done, False, 0)
                res = max(res, rec(index+1, done, True, 1) - prices[index])
                res = max(res, rec(index+1, done, True, 0) + prices[index])
                dp[t][running][done][index] = res
                return res
        return rec(0, 0, False, 0)
