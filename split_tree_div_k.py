class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for edge in edges:
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)
        
        res = 1
        visited = [False] * n

        def dfs(node, prev):
            nonlocal res
            visited[node] = True

            s = values[node]
            for child in graph[node]:
                if child != prev:
                    sub = dfs(child, node)
                    if (sub % k == 0):
                        res += 1
                    else:
                        s += sub
            return s

        
        for i in range(n):
            if not visited[i]:
                dfs(i, -1)
                
        return res