class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        memo = {}

        def solve(l, r):
            if (r - l + 1) == 3:
                return values[r] * values[r-1] * values[l]
            if (r - l) == 1:
                return 0
            if (l,r) in memo:
                return memo[(l,r)]
            res = float("inf")
            for i in range(l+1, r):
                res = min(res, values[l] * values[r] * values[i] + solve(l, i) + solve(i, r))
            memo[(l,r)] = res
            return res
        return solve(0, len(values) - 1)