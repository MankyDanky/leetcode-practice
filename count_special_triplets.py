class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        seen = {}
        res = 0
        MOD = 1000000007
        for i in range(n):
            if nums[i] not in seen:
                seen[nums[i]] = []
            seen[nums[i]].append(i)

        for i in range(n):
            target = nums[i] * 2
            if target not in seen:
                continue
            
            l_count = bisect.bisect_left(seen[target], i)
            r_count = len(seen[target]) - bisect.bisect_right(seen[target], i)
            res = (res + (l_count * r_count) % MOD) % MOD
        return res
