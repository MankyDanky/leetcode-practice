class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for prereq in prerequisites:
            graph[prereq[0]] = graph.get(prereq[0], []) + [prereq[1]]
        checked = set()
        def dfs(node, visited):
            print(node)
            if node in checked:
                return True
                
            visited.add(node)
            for edge in graph.get(node, []):
                if edge in visited:
                    return False
                if not dfs(edge, visited):
                    return False
            visited.remove(node)
            checked.add(node)
            return True

        for node in graph:
            if not dfs(node, set()):
                return False
        return True

        