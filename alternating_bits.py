class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = []
        while n != 0:
            b.append(n&1)
            n>>=1
        for i in range(1, len(b)):
            if b[i] == b[i-1]:
                return False
        return True