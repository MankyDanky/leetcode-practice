class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        l = 0
        prev = -1001
        curr = 0
        start = [False] * n
        for r in range(n):
            if nums[r] > prev:
                curr += 1
                if curr > k:
                    l += 1
                    curr -= 1
            else:
                l = r
                curr = 1
            if curr == k:
                start[l] = True
            prev = nums[r]
        print(start)
        for r in range(2 * k - 1, n):
            if start[r-k + 1] and start[r - 2*k + 1]:
                return True
        return False

