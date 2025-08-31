class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+2)
        dp[-1], dp[-2] = 1, 1

        for i in range(n-1, -1, -1):
            if s[i] == '0':
                dp[i] = float("-inf")
            elif i == n-1:
                dp[i] = 1
            elif s[i] >= '3':
                dp[i] = dp[i+1]
            elif s[i] == '2' and s[i+1] >= '7':
                dp[i] = dp[i+1]
            elif s[i+1] == '0':
                dp[i] = dp[i+2]
            else:
                dp[i] = max(0, dp[i+1]) + max(0, dp[i+2])
                if dp[i] == 0:
                    dp[i] = float("-inf")
        return dp[0] if dp[0] > 0 else 0
        '''
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= n:
                memo[i] = 1
                return 1
            if s[i] == '0':
                return float("-inf")
            if i == n-1:
                memo[i] = 1
                return 1
            
            if s[i] >= '3':
                v = dfs(i+1)
                memo[i] = v
                return v
            
            if s[i] == '2' and s[i+1] >= '7':
                v = dfs(i+1)
                memo[i] = v
                return v
            
            if s[i+1] == '0':
                v = dfs(i+2)
                memo[i] = v
                return v
            
            v = 0 
            d1 = dfs(i+1)
            if d1 > 0:
                v += d1
            d2 = dfs(i+2)
            if d2 > 0:
                v += d2
            memo[i] = v
            return v'''