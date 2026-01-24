class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        for j in range(n):
            num = nums[j]
            t = list(bin(num)[2:])
            if t[-1] == '0':
                continue
            f = False
            for i in range(len(t)-1, -1, -1):
                if t[i] == '0':
                    t[i+1] = '0'
                    f = True
                    break
            if not f:
                t[0] = '0'
            res[j] = int("".join(t), 2)
        return res
