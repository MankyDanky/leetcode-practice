class Solution:
    def minOperations(self, s: str) -> int:
        startsWith0 = 0
        flag = 0

        for c in s:
            if int(c) != flag:
                startsWith0 += 1

            flag = not flag # alternates b/w 0 & 1

        startsWith1 = len(s) - startsWith0

        return min(startsWith0, startsWith1)