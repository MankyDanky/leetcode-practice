class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (k+1) for _ in range(n+1)] #[n][k]
        for i in range(n+1):
            dp[i][0] = 1
        
        for i in range(1, n+1): 
            s = dp[i-1][0]
            for j in range(1, k+1): 
                s += dp[i-1][j] % MOD
                if j >= i:
                    s -= dp[i-1][j-i]
                dp[i][j] += s % MOD
                
                
                
                '''
                for p in range(i):
                    if j - p >= 0:
                        dp[i][j] += dp[i-1][j-p]'''
        return dp[n][k] % MOD

        """
        def rec(target, last):
            if target <= 0:
                return 1 if target == 0 else 0
            if (target, last) in cache:
                return cache[(target, last)]
            res = 0
            for i in range(1, last+1):
                lesser = 0
                res += rec(target - i + 1, last - 1)
            cache[(target, last)] = res
            return res
        return rec(k, n)"""