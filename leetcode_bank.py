class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        for i in range(n):
            addition = i//7 + 1
            dayAddition = i % 7
            res += addition + dayAddition
        return res

        