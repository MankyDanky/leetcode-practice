class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        cached = [[-1] * n for _ in range(2)]

        def rec(index, flipped):
            if index == n:
                return 0
            if cached[flipped][index] != -1:
                return cached[flipped][index]
            res = 0
            if s[index] == 'a':
                if flipped:
                    res = 1 + rec(index+1, True)
                else:
                    res = min(rec(index+1, False), 1 + rec(index+1, True))
            else:
                if flipped:
                    res = rec(index+1, True)
                else:
                    res = min(rec(index+1, True), 1 + rec(index+1, False))
            cached[flipped][index] = res
            return res
        return rec(0, False)
