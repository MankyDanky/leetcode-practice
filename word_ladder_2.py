from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        wordSet = set(wordList)
        if beginWord in wordSet:
            wordSet.remove(beginWord)
        
        # Build graph using BFS
        graph = defaultdict(list)
        queue = deque([beginWord])
        visited = set([beginWord])
        found = False
        
        while queue and not found:
            # Process all nodes at current level
            current_level = set()
            level_size = len(queue)
            
            for _ in range(level_size):
                word = queue.popleft()
                
                # Get all valid neighbors
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == word[i]:
                            continue
                        
                        next_word = word[:i] + c + word[i+1:]
                        
                        if next_word in wordSet:
                            if next_word == endWord:
                                found = True
                            
                            if next_word not in visited:
                                if next_word not in current_level:
                                    current_level.add(next_word)
                                    queue.append(next_word)
                                graph[next_word].append(word)
            
            # Mark all nodes at this level as visited
            for node in current_level:
                visited.add(node)
                wordSet.discard(node)
        
        # DFS to find all paths
        result = []
        current_path = [endWord]
        def dfs(node):
            if node == beginWord:
                path_copy = current_path.copy()
                result.append(path_copy[::-1])
                return
            
            for neighbor in graph[node]:
                current_path.append(neighbor)
                dfs(neighbor)
                current_path.pop()
        
        dfs(endWord)
        return result