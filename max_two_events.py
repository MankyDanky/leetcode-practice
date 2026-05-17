class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: x[0])
        n = len(events)
        max_val = [0] * (n+1)
        cur_max = 0
        for i in range(n-1, -1, -1):
            cur_max = max(events[i][2], cur_max)
            max_val[i] = cur_max
        res = 0
        for i in range(n):
            temp = events[i][2]
            index = bisect.bisect_left(events, events[i][1] + 1, key=lambda x: x[0])
            temp += max_val[index]
            res = max(res, temp)
        return res