class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(points) - 1):
            for j in range(i+1, len(points)):
                p1 = points[i]
                p2 = points[j]
                cost = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                graph[i].append((cost, j))
                graph[j].append((cost, i))
        
        mst = {0}
        not_mst = set(range(1, len(points)))
        q = []
        cost = 0
        for edge in graph[0]:
            heapq.heappush(q, edge)

        while len(not_mst) != 0:
            edge = heapq.heappop(q)
            if edge[1] in mst:
                continue
            cost += edge[0]
            mst.add(edge[1])
            not_mst.remove(edge[1])
            for e in graph[edge[1]]:
                heapq.heappush(q, e)
        return cost
        
