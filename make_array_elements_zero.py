class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        def valid(index, direction):
            new_nums = list(nums)
            while 0 <= index < n:
                if (new_nums[index] == 0):
                    index += direction
                else:
                    new_nums[index] -= 1
                    direction *= -1
                    index += direction
            return sum(new_nums) == 0
        res = 0
        for i in range(n):
            if nums[i] == 0:
                if valid(i, -1):
                    res += 1
                if valid(i, 1):
                    res += 1
        return res