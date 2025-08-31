class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)
        dp = defaultdict(int)
        
        dp[target] = 1

        for i in range(n-1, -1, -1):
            next_dp = defaultdict(int)
            for s in dp:
                next_dp[s - nums[i]] += dp[s]
                next_dp[s + nums[i]] += dp[s]
            dp = next_dp
        return dp[0]
            