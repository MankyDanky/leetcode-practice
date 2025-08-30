class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(list)
        characters = set()
        for i in range(1, len(words)):
            w1 = words[i-1]
            w2 = words[i]
            if w2.startswith(w1):
                continue
            flag = False
            for i in range(min(len(w1), len(w2))):
                if w1[i] != w2[i]:
                    graph[w1[i]].append(w2[i])
                    flag = True
                    break
            if not flag:
                if len(w1) > len(w2):
                    return ""
        for word in words:
            for c in word:
                characters.add(c)
        print(graph)
        processed = set()
        visited = set()
        res = ""
        def dfs(node):
            nonlocal res
            visited.add(node)
            for c in graph[node]:
                if c in visited:
                    return False
                if c in processed:
                    continue
                if not dfs(c):
                    return False
            res += node
            visited.remove(node)
            processed.add(node)
            return True
        for c in characters:
            if not c in processed:
                if not dfs(c):
                    return ""
        
        return res[::-1]

            