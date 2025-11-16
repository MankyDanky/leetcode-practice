class Solution:
    def numSub(self, s: str) -> int:
        MOD = 1000000007
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] == '0':
                l = r
                while l < len(s) and s[l] == '0':
                    l += 1
                continue
            else:
                res = (res + r - l + 1) % MOD
        return res
