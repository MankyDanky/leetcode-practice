class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def rec(n, curr, opened, closed):
            if closed > opened or opened > n or closed > n:
                return []
            if len(curr) == 2*n:
                return [curr]
            return rec(n, curr + "(", opened+1, closed) + rec(n, curr + ")", opened, closed + 1)
        return rec(n, "", 0, 0)
