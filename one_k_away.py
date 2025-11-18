class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        diff = k + 1
        for num in nums:
            if num == 0:
                diff += 1
            elif diff < k:
                return False
            else:
                diff = 0
        return True