class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            if edge[1] not in graph:
                graph[edge[1]] = []
            graph[edge[0]].append((edge[1], True)) # Correct direction
            graph[edge[1]].append((edge[0], False)) # Incorrect direction
        visited = set()
        n = len(graph)
        def dfs(start):
            res = 0
            visited.add(start)
            for end, correct_way in graph[start]:
                if end in visited:
                    continue
                
                if not correct_way:
                    res += 1
                res += dfs(end)
            return res
        
        res = [0] * n
        res[0] = dfs(0)
        calculated = set()
        def dfs2(start):
            calculated.add(start)
            for end, correct_way in graph[start]:
                if end in calculated:
                    continue
                
                if not correct_way:
                    res[end] = res[start] - 1
                else:
                    res[end] = res[start] + 1
                dfs2(end)
        dfs2(0)
        return res