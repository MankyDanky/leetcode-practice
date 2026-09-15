class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        res = 0
        intervals = []
        n = len(s)
        for center in range(2*n + 1):
            l = center//2
            r = l + center % 2
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    intervals.append((l, r))
                    break
                l -= 1
                r += 1
        curr = float("-inf")
        for l, r in intervals:
            if l > curr:
                res += 1
                curr = r
            else:
                curr = min(r, curr)
        return res

        
