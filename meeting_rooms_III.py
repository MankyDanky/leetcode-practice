from sortedcontainers import SortedList

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x: x[0])
        counts = [0] * n

        available = SortedList()
        for i in range(n):
            available.add(i)

        q = []
        for meeting in meetings:
            while q and q[0][0] <= meeting[0]:
                end, room = heapq.heappop(q)
                available.add(room)
            if len(available) != 0:
                room = available[0]
                available.remove(room)
                heapq.heappush(q, (meeting[1], room))
                counts[room] += 1
            else:
                end, room = heapq.heappop(q)
                dur = meeting[1] - meeting[0]
                heapq.heappush(q, (end + dur, room))
                counts[room] += 1
        return counts.index(max(counts))
            
