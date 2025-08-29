class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(included, curr):
            if len(included) == n:
                res.append(curr)
            for i in range(n):
                if not i in included:
                    backtrack(included | {i}, curr + [nums[i]])
        backtrack(set(), [])

        return res

