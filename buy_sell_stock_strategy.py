class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        prefixSum = [prices[0]]
        curr = prices[0]
        n = len(prices)
        for i in range(1, n):
            curr += prices[i]
            prefixSum.append(curr)
        
        prefixStrategySum = [prices[0] * strategy[0]]
        curr = prices[0] * strategy[0]
        for i in range(1, n):
            curr += prices[i] * strategy[i]
            prefixStrategySum.append(curr)
        res = prefixStrategySum[-1]
        for i in range(n-k + 1):
            leftReg = prefixStrategySum[i-1] if (i-1) >= 0 else 0
            rightReg = prefixStrategySum[n-1] - prefixStrategySum[i+k-1]

            midRight = prefixSum[i+k-1] - prefixSum[i+ k//2 - 1]
            res = max(res, leftReg+rightReg+midRight)
        return res