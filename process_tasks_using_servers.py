class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = []
        sq = []
        sq2 = []
        q = deque()
        n = len(servers)
        m = len(tasks)
        for i in range(n):
            heapq.heappush(sq, (servers[i], i))

        for i in range(m):
            while sq2 and sq2[0][0] <= i:
                time, weight, index = heapq.heappop(sq2)
                heapq.heappush(sq, (weight, index))
            q.append(tasks[i])
            for _ in range(min(len(sq), len(q))):
                weight, index = heapq.heappop(sq)
                res.append(index)
                time = q.popleft()
                heapq.heappush(sq2, (i + time, weight, index))
        i += 1
        while q:
            while sq2 and sq2[0][0] <= i:
                time, weight, index = heapq.heappop(sq2)
                heapq.heappush(sq, (weight, index))
            for _ in range(min(len(sq), len(q))):
                weight, index = heapq.heappop(sq)
                res.append(index)
                time = q.popleft()
                heapq.heappush(sq2, (i + time, weight, index))
            i = sq2[0][0] if sq2 else i + 1
        return res
