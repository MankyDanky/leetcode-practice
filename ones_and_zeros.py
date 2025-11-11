class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l = len(strs)
        cache = {}
        def rec(index, ms, ns):
            if (index, ms, ns) in cache:
                return cache[(index, ms, ns)]

            if index == l or (ms == 0 and ns == 0):
                cache[(index, ms, ns)] = 0
                return 0
            newMs = ms
            newNs = ns
            for c in strs[index]:
                if c == '0':
                    newMs -= 1
                else:
                    newNs -= 1
            
            if newMs >= 0 and newNs >= 0:
                cache[(index, ms, ns)] = max(1 + rec(index+1, newMs, newNs), rec(index+1, ms, ns))
                return cache[(index, ms, ns)]
            cache[(index, ms, ns)] = rec(index+1, ms, ns)
            return cache[(index, ms, ns)]
        return rec(0, m, n)