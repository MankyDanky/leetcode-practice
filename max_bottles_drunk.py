class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        def rec(empty, rate):
            if empty < rate:
                return 0
            return 1 + rec(empty + 1 - rate, rate + 1)
        return numBottles + rec(numBottles, numExchange)
