class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        prefix = [tuple(([0] * 26))]
        curr = [0] * 26
        res = 0
        for i in range(n):
            curr[ord(s[i]) - ord('a')] += 1
            prefix.append(tuple(curr))
            for j in range(len(prefix) - 1):
                copy = list(curr)
                for k in range(26):
                    copy[k] -= prefix[j][k]
                v = -1
                for k in range(26):
                    if copy[k] != 0:
                        v = copy[k]
                        break
                flag = True
                for k in range(26):
                    if copy[k] != 0 and copy[k] != v:
                        flag = False
                        break
                if flag:
                    res = max(res, i - j + 1)
        
        return res
