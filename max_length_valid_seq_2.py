class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        dp = [[0] * k for _ in range(k)]
        res = 0
        for num in nums:
            rem = num % k
            for j in range(k):
                dp[rem][j] = 1 + dp[j][rem]
                res = max(res, dp[rem][j])
        
        return res