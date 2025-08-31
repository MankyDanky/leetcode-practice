class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        memo = {}
        def rec(i1, i2):
            if (i1,i2) in memo:
                return memo[(i1,i2)]
            if i1 == m and i2 == n:
                memo[(i1,i2)] = True
                return True
            if i2 == n:
                memo[(i1,i2)] = False
                return False
            if i1 == m:
                i = i2
                while i < n:
                    if i < n - 1 and p[i+1] == "*":
                        i += 2
                        continue
                    else:
                        memo[(i1,i2)] = False
                        return False
                memo[(i1,i2)] = True
                return True
            
            if s[i1] == p[i2]:
                if i2 < n - 1 and p[i2 + 1] == "*":
                    while i1 < m and s[i1] == p[i2]:
                        if rec(i1, i2 + 2):
                            memo[(i1,i2)] = True
                            return True
                            
                        i1 += 1
                    if i1 == m and i2 + 2 == n:
                        memo[(i1,i2)] = True
                        return True
                    memo[(i1,i2)] = rec(i1, i2 + 2)
                    return memo[(i1,i2)]
                else:
                    memo[(i1,i2)] = rec(i1 + 1, i2 + 1)
                    return memo[(i1,i2)]
            elif p[i2] not in ".*":
                if i2 < n - 1 and p[i2 + 1] == "*":
                    memo[(i1,i2)] = rec(i1, i2 + 2)
                    return memo[(i1,i2)]
                else:
                    memo[(i1,i2)] = False
                    return False
            elif p[i2] == ".":
                if i2 < n - 1 and p[i2 + 1] == "*":
                    while i1 < m:
                        if rec(i1, i2 + 2):
                            memo[(i1,i2)] = True
                            return True
                        i1 += 1
                    if i1 == m and i2 + 2 == n:
                        memo[(i1,i2)] = True
                        return True
                    memo[(i1,i2)] = rec(i1, i2 + 2)
                    return memo[(i1,i2)]
                else:
                    memo[(i1,i2)] = rec(i1 + 1, i2 + 1)
                    return memo[(i1,i2)]
            else:
                raise Exception("Unhandled")
        return rec(0,0)

