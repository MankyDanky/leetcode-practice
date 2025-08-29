class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(curr, i, sh):
            if i >= len(s):
                if sh == "":
                    res.append(curr)
                return
            sh += s[i]
            backtrack(curr, i+1, sh)
            if (sh == sh[::-1]):
                backtrack(curr + [sh], i+1, "")
        backtrack([], 0, "")
        return res