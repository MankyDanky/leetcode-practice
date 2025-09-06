from itertools import combinations
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        graph = {}
        in_degree = [0] * n
        for relation in relations:
            if relation[0] - 1 not in graph:
                graph[relation[0] - 1] = []
            graph[relation[0] - 1].append(relation[1] - 1)
            in_degree[relation[1] - 1] += 1
        
        @lru_cache(None)
        def rec(not_taken, in_degree):
            if not_taken == 0:
                return 0
            takeable = []
            for i in range(n):
                if (not_taken & (1 << i) != 0) and in_degree[i] == 0:
                    takeable.append(i)
            res = float("inf")
            if len(takeable) <= k:
                in_degree = list(in_degree)
                for node in takeable:
                    not_taken ^= 1 << node
                    for to in graph.get(node, []):
                        in_degree[to] -= 1
                return 1 + rec(not_taken, tuple(in_degree))

            for k_courses in combinations(takeable, k):
                new_not_taken, new_in_degree = not_taken, list(in_degree)
                for node in k_courses:
                    new_not_taken ^= 1 << node
                    for to in graph.get(node, []):
                        new_in_degree[to] -= 1
                res = min(res, 1 + rec(new_not_taken, tuple(new_in_degree)))
            return res
        return rec((1<<n) - 1, tuple(in_degree))