class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_length = 1
        output = s[0]
        for i in range(1, n):
            sub = s[i]
            l = r = i
            while l - 1 >= 0 and r + 1 < n and s[l-1] == s[r+1]:
                sub = s[l-1] + sub + s[r+1]
                l -= 1
                r += 1
            if len(sub) > max_length:
                output = sub
                max_length = len(sub)
            if not s[i-1] == s[i]:
                continue
            sub = s[i-1] + s[i]
            l = i-1
            r = i       
            while l - 1 >= 0 and r + 1 < n and s[l-1] == s[r+1]:
                sub = s[l-1] + sub + s[r+1]
                l -= 1
                r += 1  
            if len(sub) > max_length:
                output = sub
                max_length = len(sub)   
        return output     
