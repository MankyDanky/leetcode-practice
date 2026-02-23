class Solution:
    def hasAllCodes(self, p: str, k: int) -> bool:
        if len(p) < k:
            return False
        s = set()
        
        
        curr = 0
        for i in range(k-1):
            curr <<= 1
            curr |= (1 if p[i] == "1" else 0)
        
        for i in range(k-1, len(p)):
            curr &= ((1<<(k-1)) - 1)
            curr <<= 1
            curr |= (1 if p[i] == "1" else 0)
            s.add(curr)

        return len(s) == (1<<k)