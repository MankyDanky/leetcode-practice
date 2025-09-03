class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if boardingCost*4 <= runningCost:
            return -1
        if len(customers) == 1:
            return -1
        turns = 0
        max_profit = 0
        max_profit_index = -1
        customers_waiting = 0
        profit = 0
        i = 0
        while i < len(customers):
            customers_waiting += customers[i]
            while customers_waiting >= 4:
                profit += 4 * boardingCost
                customers_waiting -= 4
                if profit > max_profit:
                    max_profit = profit
                    max_profit_index = i
                i += 1
                profit -= runningCost
                customers_waiting += customers[i] if i < len(customers) else 0
            profit += customers_waiting * boardingCost
            customers_waiting = 0
            if profit > max_profit:
                max_profit = profit
                max_profit_index = i
            i += 1
            profit -= runningCost
        return max_profit_index + 1 if max_profit > 0 else -1
