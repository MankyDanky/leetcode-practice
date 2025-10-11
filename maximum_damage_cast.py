class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        n = len(power)
        power.sort()
        dp = [power[i] for i in range(n)]
        r = n
        max_val = 0
        for i in range(n-2, -1, -1):
            while power[r-1] > power[i] + 2:
                max_val = max(dp[r-1], max_val)
                r -= 1
            if power[i+1] == power[i]:
                dp[i] += dp[i+1]
            else:
                dp[i] += max_val
        return max(dp)