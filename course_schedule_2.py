class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for prereq in prerequisites:
            graph[prereq[0]] = graph.get(prereq[0], []) + [prereq[1]]
        
        checked = set()
        def dfs(node, visited, order):
            if node in checked:
                return []
                
            visited.add(node)
            for edge in graph.get(node, []):
                if edge in visited:
                    return None
                if edge in checked:
                    continue
                if not dfs(edge, visited, order):
                    return None
            visited.remove(node)
            order.append(node)
            checked.add(node)
            return order

        res = []

        for i in range(numCourses):
            o = dfs(i, set(), [])
            if o == None:
                return []
            res += o
        return res