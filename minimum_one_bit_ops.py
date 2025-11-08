class Solution:
    @lru_cache(None)
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        
        lsb = n & (-n)
        msb = 1<<(n.bit_length() - 1)

        if (lsb<<1 == msb):
            return 1 + self.minimumOneBitOperations(lsb)
        
        if (lsb == msb):
            return 1 + self.minimumOneBitOperations(lsb ^ 1)
        
        if (((msb>>1) & n) > 0):
            return  self.minimumOneBitOperations((n^msb)^(msb>>1)) + self.minimumOneBitOperations(msb^(msb>>1))
        newNum = n^msb
        nsb = 1<<(newNum.bit_length()-1)
        return 1 + self.minimumOneBitOperations(msb^(nsb<<1)^nsb) + self.minimumOneBitOperations(n^msb^nsb)

        


        


