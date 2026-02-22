class Solution:
    def binaryGap(self, n: int) -> int:
        digits = []
        while n != 0:
            digits.append(n&1)
            n>>=1
        
        j = 0
        while digits[j] != 1:
            j += 1

        dist = 0

        for i in range(j+1, len(digits)):
            if digits[i] == 1:
                dist = max(dist, i - j)
                j = i
        return dist