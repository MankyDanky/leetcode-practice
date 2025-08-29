class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if not c in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        def scan(node, index):
            if index >= len(word):
                return node.endOfWord
            elif word[index] != ".":
                if word[index] in node.children:
                    return scan(node.children[word[index]], index + 1)
                else:
                    return False
            else:
                for c in node.children:
                    if scan(node.children[c], index + 1):
                        return True
            return False
        return scan(self.root, 0)
        
