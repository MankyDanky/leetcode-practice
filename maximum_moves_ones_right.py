class Solution:
    def maxOperations(self, s: str) -> int:
        count = 0
        res = 0
        n = len(s)
        if s[-1] == '0':
            count = 1
        for i in range(n-2, -1, -1):
            if s[i] == '0' and s[i+1] == '1':
                count += 1
            elif s[i] == '1':
                res += count
        return res