class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = collections.deque([])
        counts = collections.Counter(tasks)
        h = [-cnt for cnt in counts.values()]
        heapq.heapify(h)
        t = 0
        while len(q) != 0 or len(h) != 0:
            while len(q) != 0:
                if q[0][1] == t:
                    heapq.heappush(h, q.popleft()[0])
                else:
                    break
            if len(h) != 0:
                c = heapq.heappop(h)
                c += 1
                if c == 0:
                    t += 1
                    continue
                else:
                    q.append((c, t + n + 1))
            t += 1
        return t
