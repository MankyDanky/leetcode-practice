class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, w in edges:
            graph[a].append((b, w))
            graph[b].append((a, 2*w))
        
        dist = [float("inf")] * n
        q = [(0, 0)]

        while q:
            d, node = heapq.heappop(q)

            if dist[node] != float("inf"):
                continue
            dist[node] = d

            for to, w in graph[node]:
                if dist[to] == float("inf"):
                    heapq.heappush(q, (d + w, to))
        return dist[n-1] if dist[n-1] != float("inf") else -1