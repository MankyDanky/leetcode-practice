class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        oddCount2 = {}
        oddCount1 = {}
        evenCount2 = {}
        evenCount1 = {}

        n = len(s1)

        for i in range(n):
            if i % 2 == 0:
                oddCount1[s1[i]] = oddCount1.get(s1[i], 0) + 1
                oddCount2[s2[i]] = oddCount2.get(s2[i], 0) + 1
            else:
                evenCount1[s1[i]] = evenCount1.get(s1[i], 0) + 1
                evenCount2[s2[i]] = evenCount2.get(s2[i], 0) + 1
        return oddCount1 == oddCount2 and evenCount1 == evenCount2
                