class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        while n != 0:
            if n % 2 == 1:
                bits += 1
            n = n >>1
        return bits