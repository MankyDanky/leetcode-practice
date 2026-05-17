class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        bits = []
        while n != 0:
            bits.append(n&1)
            n>>=1
        
        bits.reverse()
        print(bits)
        res = 0
        for bit in bits:
            res <<= 1
            res |= (0 if (bit == 1) else 1)
        return res