class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        cache = {}
        
        def rec(index, prev):
            if (index == m):
                return 0
            if (index, prev) in cache:
                return cache[(index, prev)]
            valid = True
            if (prev != -1):
                for i in range(n):
                    if strs[i][index] < strs[i][prev]:
                        valid = False
                        break
            res = 1 + rec(index+1, prev)
            if valid:
                res = min(res, rec(index+1, index))
            cache[(index, prev)] = res
            return res
        return rec(0, -1)