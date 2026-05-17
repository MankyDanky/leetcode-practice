class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        while n != 0:
            bits.append(n&1)
            n>>=1

        while len(bits) != 31:
            bits.append(0)
        
        bits.reverse()
        res = 0
        while bits:
            res |= bits.pop()
            res<<=1
        return res