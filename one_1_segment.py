class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        i = 0
        n = len(s)
        while i < n and s[i] == '1':
            i += 1
        
        for j in range(i, n):
            if s[j] == '1':
                return False
        return True