class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n):
            res = n
            print(n)
            while par[res] != res:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return True
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return False
        
        for edge in edges:
            if union(edge[0] - 1, edge[1] - 1):
                return edge
            
