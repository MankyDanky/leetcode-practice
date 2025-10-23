class Solution:
    def hasSameDigits(self, s: str) -> bool:
        newS = []
        while len(s) != 2:
            for i in range(len(s)-1):
                newS.append(chr((ord(s[i]) - ord('0') + ord(s[i+1]) - ord('0'))%10 + ord('0')))
            s = "".join(newS)
            newS = []
        return s[0] == s[1]