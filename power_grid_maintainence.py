class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        buckets = defaultdict(SortedList)
        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        added = {}
        currBucket = 0
        def dfs(node, bucket):
            added[node] = bucket
            buckets[bucket].add(node)
            for to in graph[node]:
                if (not to in added):
                    dfs(to, bucket)
            
        for i in range(c+1):
            if not i in added:
                dfs(i, currBucket)
                currBucket += 1
        res = []

        for t, x in queries:
            if t == 1:
                bucket = added[x]
                if (len(buckets[bucket]) == 0):
                    res.append(-1)
                elif x in buckets[bucket]:
                    res.append(x)
                else:
                    res.append(buckets[bucket][0])
            else:
                bucket = added[x]
                if x in buckets[bucket]:
                    buckets[bucket].remove(x)
        return res



