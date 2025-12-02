class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 1000000007
        points.sort(key=lambda x: x[1])
        buckets = []
        n = len(points)
        i = 0
        while i < n:
            ref = points[i][1]
            alike = 1
            while i+1 < n and points[i+1][1] == ref:
                i += 1
                alike += 1
            if alike > 1:
                buckets.append(math.comb(alike, 2) % MOD)
            i += 1
            
        res = 0
        totalPairs = sum(buckets)
        for i in range(len(buckets)):
            totalPairs -= buckets[i]
            res = (res + (totalPairs * buckets[i]) % MOD) % MOD
        return res

