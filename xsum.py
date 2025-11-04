class Solution:
    def xSum(self, nums: List[int], x):
        c = Counter(nums)
        nums.sort(key = lambda x: (c[x], x))
        seen = set()
        res = 0
        j = len(nums) - 1
        seen.add(nums[j])
        while len(seen) <= x and j >= 0:
            res += nums[j]
            j -= 1
            if (j >= 0):
                seen.add(nums[j])
        return res


    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = [0] * (len(nums) - k + 1)
        for i in range(len(nums) - k + 1):
            res[i] = self.xSum(nums[i:i+k], x)
        return res