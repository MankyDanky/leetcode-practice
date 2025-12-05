class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * (n+1)
        for i in range(n):
            prefixSum[i+1] = prefixSum[i] + nums[i]
        
        res = 0
        for i in range(1, n):
            if (2 * prefixSum[i] - prefixSum[n]) % 2 == 0:
                res += 1
        return res