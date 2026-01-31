class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_id = -1

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = int(1e11)
        n = len(source)

        s_to_id = {}
        root = TrieNode()

        def get_or_create_id(s):
            if s in s_to_id:
                return s_to_id[s]
            
            node = root
            for c in s:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word_id = len(s_to_id)
            s_to_id[s] = node.word_id
            return node.word_id

        for s in original + changed:
            get_or_create_id(s)

        m = len(s_to_id)

        graph = [[INF] * m for _ in range(m)]
        
        
        for i in range(len(original)):
            u = s_to_id[original[i]]
            v = s_to_id[changed[i]]
            graph[u][v] = min(graph[u][v], cost[i])
        
        for i in range(m):
            graph[i][i] = 0

        for k in range(m):
            for i in range(m):
                if graph[i][k] == INF:
                    continue
                for j in range(m):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        
        
        @lru_cache(None)
        def rec(index):
            if index >= n:
                return 0
            res = INF
            node_s = root
            node_t = root

            if source[index] == target[index]:
                res = rec(index+1)

            for i in range(index, n):
                cs = source[i]
                ct = target[i]

                if cs in node_s.children and ct in node_t.children:
                    node_s = node_s.children[cs]
                    node_t = node_t.children[ct]
                    if node_s.word_id != -1 and node_t.word_id != -1:
                        res = min(res, graph[node_s.word_id][node_t.word_id] + rec(i+1))
                else:
                    break
            return res
        res = rec(0)
        return res if res != INF else -1
