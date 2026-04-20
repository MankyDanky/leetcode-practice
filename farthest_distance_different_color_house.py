class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        res = 0
        for i in range(n):
            if colors[i] != colors[-1]:
                res = max(res, n-1 - i)
            if colors[0] != colors[i]:
                res = max(res, i)
        return res