class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        exchange = 0
        while numBottles != 0:
            res += numBottles
            exchange += numBottles
            numBottles = exchange//numExchange
            exchange -= numBottles*numExchange
        return res