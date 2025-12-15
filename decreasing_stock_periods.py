class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 1
        res = 1
        n = len(prices)
        for r in range(1, n):
            if prices[r] == prices[r-1] - 1:
                count += 1
            else:
                count = 1
            res += count
        return res