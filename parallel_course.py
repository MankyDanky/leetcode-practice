class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {}
        in_degree = [0] * n
        for relation in relations:
            if relation[0] - 1 not in graph:
                graph[relation[0] - 1] = []
            graph[relation[0] - 1].append(relation[1] - 1)
            in_degree[relation[1] - 1] += 1
        
        q = deque()
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)
            
        res = 0
        visited = set()
        while q:
            res += 1
            for i in range(len(q)):
                node = q.popleft()
                if node in visited:
                    return -1
                visited.add(node)
                if not node in graph:
                    continue
                for to in graph[node]:
                    in_degree[to] -= 1
                    if in_degree[to] == 0:
                        q.append(to)
        return res if len(visited) == n else -1