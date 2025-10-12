class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        MOD = (10**9)+7
        duplicates = m - k

        n = len(nums)
        
        @lru_cache(None)
        def dfs(remaining, odd_needed, index, carry):
            if remaining == 0:
                return 1 if carry.bit_count() == odd_needed else 0
            if index >= n or remaining + carry.bit_count() < odd_needed or odd_needed < 0:
                return 0

            ans = 0
            for take in range(remaining+1):
                ways = (math.comb(remaining, take) * pow(nums[index], take, MOD)) % MOD
                ans += (ways * dfs(remaining - take, odd_needed - ((carry + take) % 2), index + 1, (carry + take)//2)) % MOD
                ans %= MOD
            return ans

        return dfs(m, k, 0, 0) % MOD

                
