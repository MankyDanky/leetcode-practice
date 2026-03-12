class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        

        rank = [1] * n
        par = [i for i in range(n)]

        def find(node):
            while par[node] != node:
                par[node] = par[par[node]]
                node = par[node]
            return node

        def union(node1, node2):
            p1, p2 = find(node1), find(node2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return True

        stability = float("inf")

        for edge in edges:
            if edge[3] == 1:
                if union(edge[0], edge[1]):
                    stability = min(stability, edge[2])
                else:
                    return -1
        
        edges.sort(key = lambda x: x[2], reverse=True)

        strengths = []

        for edge in edges:
            if edge[3] != 1:
                if union(edge[0], edge[1]):
                    strengths.append(edge[2])

        if max(rank) != n:
            return -1
        print(strengths)
        for i in range(len(strengths) - 1, -1, -1):
            if k == 0:
                break
            k -= 1
            strengths[i] *= 2
        
        return min(min(strengths) if len(strengths) != 0 else float("inf"), stability)
