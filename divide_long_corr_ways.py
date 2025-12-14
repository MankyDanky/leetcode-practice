class Solution:
    def numberOfWays(self, corridor: str) -> int:

        MOD = 1000000007
        n = len(corridor)

        dp = [[-1] * n for _ in range(4)]
        def rec(index, count):
            count += 1 if corridor[index] == 'S' else 0
            if (dp[count][index] != -1):
                return dp[count][index]
            if index == n - 1:
                return 1 if (count == 2) else 0
            if count > 2:
                return 0
            
            res = rec(index+1, count)
            if count == 2:
                res = (res + rec(index+1, 0)) % MOD
            dp[count][index] = res
            return res
        
        return rec(0, 0)


