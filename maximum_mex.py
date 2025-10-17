class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        counts = {}
        for num in nums:
            counts[num%value] = counts.get(num%value, 0) + 1


        min_count = float("inf")
        min_count_val = -1
        for i in range(value):
            if counts.get(i, 0) < min_count:
                min_count = counts.get(i, 0)
                min_count_val = i
        return min_count * value + min_count_val
