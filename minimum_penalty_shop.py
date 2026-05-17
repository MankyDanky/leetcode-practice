class Solution:
    def bestClosingTime(self, customers: str) -> int:
        res = 0
        curr = 0
        n = len(customers)
        for r in range(n):
            if customers[r] == 'Y':
                curr += 1
            else:
                curr -= 1
            if curr > 0:
                res = r+1
                curr = 0
        return res