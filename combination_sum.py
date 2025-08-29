class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(s, curr, i):
            if i >= len(nums):
                return
            if s > target:
                return
            if s == target:
                res.append(curr)
                return
            backtrack(s + nums[i], curr + [nums[i]], i)
            backtrack(s, curr, i+1)
        backtrack(0, [], 0)
        return res
