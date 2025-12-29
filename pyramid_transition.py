class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        a = set(allowed)
        prev = list(bottom)
        cur = []
        tried = set()

        def backtrack(index, rowSize):
            
            nonlocal prev
            nonlocal cur

            if (("".join(prev), "".join(cur))) in tried:
                return False
            
            if (rowSize == 0):
                return True
            if (index == rowSize):
                p = prev
                prev = cur
                cur = []
                if backtrack(0, rowSize - 1):
                    return True
                cur = prev
                prev = p
                return False

            for c in "ABCDEF":
                if (prev[index] + prev[index+1] + c) in a:
                    cur.append(c)
                    if (backtrack(index+1, rowSize)):
                        return True
                    cur.pop()
            tried.add(("".join(prev), "".join(cur)))
            return False
        return backtrack(0, len(bottom) - 1)
