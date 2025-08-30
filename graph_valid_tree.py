class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if n == 1:
            return True

        graph = {}
        for edge in edges:
            if not edge[0] in graph:
                graph[edge[0]] = list()
            graph[edge[0]].append(edge[1])

            if not edge[1] in graph:
                graph[edge[1]] = list()
            graph[edge[1]].append(edge[0])
            
        if len(graph) != n:
            return False
            
        checked = set()
        dfs_ran = False

        def dfs(visited, node, origin):
            visited.add(node)
            for dest in graph[node]:
                if dest == origin:
                    continue
                if dest in visited:
                    return False
                if not dfs(visited, dest, node):
                    return False
            visited.remove(node)
            checked.add(node)
            return True
        
        for node in graph:
            if not node in checked:
                if dfs_ran == True:
                    return False
                if not dfs(set(), node, 101):
                    return False
                dfs_ran = True
        return True
                
            