class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        k -= 1
        first = nums[0]
        n = len(nums)
        l = SortedList()
        for i in range(1, dist+2):
            l.add(nums[i])
        s = 0
        for i in range(k):
            s += l[i]
        res = s + first

        for i in range(dist+2, n):
            ins = l.bisect_left(nums[i])
            if ins < k:
                s -= l[k-1]
                s += nums[i]
            l.add(nums[i])
            


            rem = i - (dist + 1)
            remIn = l.bisect_left(nums[rem])
            if remIn < k:
                s -= nums[rem]
                s += l[k]
            l.remove(nums[rem])
            res = min(s + first, res)
        return res

