class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topoSort(edges):
            graph = defaultdict(list)
            in_degree = defaultdict(int)
            for edge in edges:
                graph[edge[0]].append(edge[1])
                in_degree[edge[1]] += 1

            q = deque()
            
            for i in range(1, k+1):
                if in_degree[i] == 0:
                    q.append(i)
            seen = set()
            res = []
            while q:
                node = q.popleft()
                seen.add(node)
                res.append(node)
                for to in graph[node]:
                    if in_degree[to] == 0:
                        return []
                    in_degree[to] -= 1
                    if in_degree[to] == 0:
                        q.append(to)
            return res if len(seen) == k else []
        row_order = topoSort(rowConditions)
        col_order = topoSort(colConditions)
        if col_order == [] or row_order == []:
            return []
        res = [[0] * k for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if row_order[i] == col_order[j]:
                    res[i][j] = row_order[i]
        return res
