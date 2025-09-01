class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        n = len(piles)
        def canEatAll(k):
            piles
            t = 0
            p = 0
            while p < n:
                if piles[p] % k != 0:
                    t += 1
                t += piles[p] // k
                p += 1
            return t <= h
        
        while l < r:
            
            m = (l + r)//2

            if canEatAll(m):
                r = m
            else:
                l = m + 1
        return l
