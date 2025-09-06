class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        day = 1
        count = 0
        n = len(events)
        r = 0
        q = []
        for day in range(max(event[1] for event in events) + 1):
            while r < n and events[r][0] <= day:
                heapq.heappush(q, events[r][1])
                r += 1

            while q and q[0] < day:
                heapq.heappop(q)
            
            if q:
                heapq.heappop(q)
                count += 1
            day += 1
        return count