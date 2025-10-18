class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        n = len(words)
        prev = {}
        for i in range(n):
            if collections.Counter(words[i]) == prev:
                continue
            res.append(words[i])
            prev = collections.Counter(words[i])
        
        return res
