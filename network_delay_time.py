import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for time in times:
            if not time[0] in graph:
                graph[time[0]] = list()
            graph[time[0]].append((time[1], time[2]))

        visited = set()
        q = [(0, k)]
        heapq.heapify(q)
        t = 0

        while q:
            distance, node = heapq.heappop(q)
            if node in visited:
                continue
            visited.add(node)
            t = max(distance, t)
            if not node in graph:
                continue
            for edge in graph[node]:
                to, weight = edge
                heapq.heappush(q, (weight + distance, to))
        if len(visited) != n:
            return -1
        return t