from itertools import combinations

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        times = [0] * k
        def canFinish(maxTime, index):
            if index == n:
                return True
            for i in range(k):
                if i == 0 or times[i] != times[i-1]:
                    if times[i] + jobs[index] <= maxTime:
                        times[i] += jobs[index]
                        if canFinish(maxTime, index + 1):
                            times[i] -= jobs[index]
                            return True
                        times[i] -= jobs[index]
            return False
        l = max(jobs)
        r = sum(jobs)
        while l < r:
            mid = (l+r)//2
            c = canFinish(mid, 0)
            print(c, mid)
            if c:
                r = mid
            else:
                l = mid + 1
        return l

