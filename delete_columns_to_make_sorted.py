class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        n = len(strs)
        m = len(strs[0])
        sizes = [n]
        res = 0
        for j in range(m):
            curr = 0
            valid = True
            for s in sizes:
                if (s == 1):
                    curr += s
                    continue
                prev = strs[curr][j]
                for i in range(curr+1, curr+s):
                    if (strs[i][j] < prev):
                        res += 1
                        valid = False
                        break
                    prev = strs[i][j]
                if (not valid):
                    break
                curr += s
            if valid:
                newSizes = []
                curr = 0
                for s in sizes:
                    a = 1
                    if s == 1:
                        newSizes.append(1)
                        curr += s
                        continue
                    prev = strs[curr][j]
                    for i in range(curr+1, curr+s):
                        if strs[i][j] == prev:
                            a += 1
                        else:
                            newSizes.append(a)
                            a = 1
                            prev = strs[i][j]
                    newSizes.append(a)
                    curr += s
                sizes = newSizes
        return res
