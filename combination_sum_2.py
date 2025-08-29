class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()
        def backtrack(s, curr, i):
            if i >= len(candidates):
                if s == target:
                    res.append(curr)
                return
            if s > target:
                return
            if s == target:
                res.append(curr)
                return
            j = i
            while j < len(candidates):
                if candidates[i] == candidates[j]:
                    j += 1
                else:
                    break
            backtrack(s, curr, j)
            backtrack(s + candidates[i], curr + [candidates[i]], i + 1)
        backtrack(0, [], 0)
        return res