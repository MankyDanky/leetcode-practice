from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        s = sum(nums)
        if s % 2 != 0:
            return False
        t = s//2
        memo = [[False] * (t+1) for _ in range(n+1)]
        memo[n][0] = True
        
        for i in range(n - 1, -1, -1):
            for j in range(t + 1):
                memo[i][j] = memo[i+1][j] or (False if (j-nums[i] < 0) else (memo[i+1][j - nums[i]]))
        
        for row in memo:
            print(row)
        return memo[0][t]
        
        
        '''def rec(target, ind):
            if ind == n:
                return target == 0
            if target < 0:
                return False
            if memo[ind][target] != -1:
                return memo[ind][target]
            
            memo[ind][target] = rec(target, ind + 1) or rec(target - nums[ind], ind + 1)
            return memo[ind][target]'''


