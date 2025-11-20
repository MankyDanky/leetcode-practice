class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))

        n = len(intervals)
        
        newIntervals = []
        for i in range(n):
            add = True
            for j in range(i+1, n):
                if intervals[i][1] >= intervals[j][1]:
                    add = False
                    break
                if intervals[i][1] < intervals[j][0]:
                    break
            if add:
                newIntervals.append(intervals[i])
        print(newIntervals)
        s = len(newIntervals)
        res = 0
        curr = [0] * s

        @lru_cache(None)
        def rec(i, end):
            if i == s:
                return 0
            if (i < s-1 and newIntervals[i+1][0] > newIntervals[i][1]):
                res = 2 - (1 if end > i else 0) + rec(i+1, end)
                return res

            res = float("inf")
            j = i+1
            while j < s and newIntervals[j][0] <= newIntervals[i][1]:
                j += 1

            k = i+1
            while k < s and k < end and newIntervals[k][0] <= newIntervals[i][1]:
                k += 1

            if end > i:
                res = min(1 + rec(k, j), res)
            else:
                res = min(2 + rec(k, j), res)
            
            k = i+1
            while k < s and newIntervals[k][0] < newIntervals[i][1]:
                k += 1

            res = min(2 + rec(k, j), res)
            return res


        return rec(0, 0)
            
            
            
            

            
            