class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def canReach(target):
            s = 0
            for battery in batteries:
                s += min(target, battery)

            return s >= n*target
        
        l = 0
        r = sum(batteries)//n
        while l < r:
            mid = math.ceil((l+r)/2)

            if canReach(mid):
                l = mid
            else:
                r = mid - 1
        return l