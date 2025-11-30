class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        target = s % p
        if target == 0:
            return 0
        
        n = len(nums)
        prefixSum = [0] * n
        prefixSum[0] = nums[0] % p
        for i in range(1, n):
            prefixSum[i] = (prefixSum[i - 1] + nums[i]) % p

        lastOccurence = {}
        lastOccurence[0] = -1
        # target = (prefixSum[r] - prefixSum[l-1]) % p
        res = n
        for i in range(n):
            leftTarget = (-(target-prefixSum[i])) % p
            if leftTarget in lastOccurence:
                res = min(res, i - lastOccurence[leftTarget])
            lastOccurence[prefixSum[i]] = i

        if res == n:
            return -1
        return res
            