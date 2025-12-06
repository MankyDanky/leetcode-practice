class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 1000000007
        n = len(nums)

        dp = [0] * (n + 1)
        dp[0] = 1

        prefixSum = [0] * (n+1)
        prefixSum[0] = 1

        maxWindow = deque([])
        minWindow = deque([])
        j = 0

        for i in range(n):
            while maxWindow and nums[i] > maxWindow[-1][0]:
                maxWindow.pop()
            while minWindow and nums[i] < minWindow[-1][0]:
                minWindow.pop()
            maxWindow.append((nums[i], i))
            minWindow.append((nums[i], i))
            while maxWindow[0][0] - minWindow[0][0] > k:
                j += 1
                if maxWindow[0][1] < j:
                    maxWindow.popleft()
                if minWindow[0][1] < j:
                    minWindow.popleft()
            dp[i+1] = (prefixSum[i] - (prefixSum[j-1] if j-1 >= 0  else 0) + MOD) % MOD
            prefixSum[i+1] = (prefixSum[i] + dp[i+1]) % MOD
        return dp[n]

