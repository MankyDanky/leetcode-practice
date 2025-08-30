class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))
        
        costs = [float("inf")] * n
        costs[src] = 0
        q = deque([src])
        temp_costs = [float("inf")] * n
        for i in range(k+1):
            for j in range(len(q)):
                node = q.popleft()
                for to, weight in graph[node]:
                    if costs[node] + weight < temp_costs[to]:
                        q.append(to)
                        temp_costs[to] = costs[node] + weight
            for j in range(n):
                costs[j] = temp_costs[j]

        if costs[dst] == float("inf"):
            return -1
        
        return costs[dst]