class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        node = self.root
        for c in word:
            if not c in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.endOfWord = True
    


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add_word(word)
        
        m, n = len(board), len(board[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        res = set()

        def scan(visited, pos, s, node):
            i, j = pos
            if i >= m or i < 0 or j >= n or j < 0:
                return
            s += board[i][j]

            if not board[i][j] in node.children:
                return
            node = node.children[board[i][j]]
            if node.endOfWord:
                res.add(s)
            visited.add(pos)
            for direction in directions:
                new_pos = (i + direction[0], j + direction[1])
                if not new_pos in visited:
                    scan(visited, new_pos, s, node)
            visited.remove(pos)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.root.children:
                    scan(set(), (i,j), "", trie.root)
        
        return list(res)
            