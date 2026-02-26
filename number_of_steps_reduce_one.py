class Solution:
    def numSteps(self, s: str) -> int:
        s = list(s)
        n = len(s)
        res = 0
        sub2 = True
        for i in range(n-1, -1, -1):
            if i == 0 and s[i] == '0':
                return res + 1
            elif i == 0:
                return res
            if s[i] == '0':
                res += 1
                continue
            else:
                j = i
                while j >= 0 and s[j] == '1':
                    s[j] = '0'
                    j -= 1
                res += 2
                if j >= 0:
                    s[j] = '1'
                else:
                    sub2 = False
        return res