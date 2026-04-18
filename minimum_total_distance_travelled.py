class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        cache = {}
        robot.sort()
        factory.sort()
        n = len(robot)
        m = len(factory)
        def rec(i1, i2):
            if i1 == n:
                return 0
            if i2 == m:
                return float("inf")
            if (i1, i2) in cache:
                return cache[(i1, i2)]
            res = rec(i1, i2+1)
            d = 0
            for i in range(i1, min(n, i1 + factory[i2][1])):
                d += abs(robot[i] - factory[i2][0])
                res = min(res, d + rec(i+1, i2+1))
            cache[(i1, i2)] = res
            return res

        rec(0, 0)
        print(robot)
        print(factory)
        print(cache)
        return cache[(0,0)]
            