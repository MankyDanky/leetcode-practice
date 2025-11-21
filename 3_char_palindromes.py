class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        firstOccurrence = {}
        prevOccurrence = {}
        res = 0
        added = set()
        n = len(s)
        for i in range(n):
            ch1 = s[i]
            if ch1 in firstOccurrence:
                for ch2 in prevOccurrence:
                    if prevOccurrence[ch2] > firstOccurrence[ch1]:
                        if (ch1 + ch2 + ch1 not in added):
                            res += 1
                            added.add(ch1 + ch2 + ch1)
            else:
                firstOccurrence[ch1] = i
            prevOccurrence[ch1] = i
        return res