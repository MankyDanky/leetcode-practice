class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = [0]*(n+1)
        for i in range(n):
            prefixSum[i+1] = prefixSum[i] + nums[i]

        dp = [float("-inf")] * n
        res = float("-inf")
        for i in range(k-1, n):
            s = prefixSum[i+1] - prefixSum[i - k + 1]
            res = max(res, s)
            dp[i] = max(s, s + dp[max(0, i-k)])
        return max(max(dp), res)