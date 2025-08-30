"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        if node.neighbors == []:
            return Node(val=node.val)

        edges = defaultdict(set)

        def dfs(seen, n):
            if n.val in seen:
                return
            seen.add(n.val)
            for neighbor in n.neighbors:
                edges[n.val].add(neighbor.val)
                dfs(seen, neighbor)

        dfs(set(), node)
        for edge in edges:
            print(edge)
        vertices = {}

        for start in edges:
            if not start in vertices:
                vertices[start] = Node(start, [])
            for end in edges[start]:
                if not end in vertices:
                    vertices[end] = Node(end, [])
                vertices[start].neighbors.append(vertices[end])
        return vertices[node.val]
                
