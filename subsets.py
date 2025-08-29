class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, so_far):
            nonlocal res
            if i == len(nums):
                res.append(so_far)
            else:
                backtrack(i+1, so_far)
                backtrack(i+1, so_far + [nums[i]])
        backtrack(0, [])
        return res
