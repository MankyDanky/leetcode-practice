class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        res = []
        graph = {}
        for ticket in tickets:
            if not ticket[0] in graph:
                graph[ticket[0]] = list()
            graph[ticket[0]].append(ticket[1])

        def dfs(node):
            res.append(node)
            if node not in graph or len(graph[node]) == 0:
                if len(res) == len(tickets) + 1:
                    return True
                else:
                    res.pop()
                    return False
            for i in range(len(graph[node])-1, -1, -1):
                s = graph[node].pop(i)
                if dfs(s):
                    return True
                graph[node].insert(i, s)
            res.pop()
            return False
        
        dfs("JFK")
        return res

            
