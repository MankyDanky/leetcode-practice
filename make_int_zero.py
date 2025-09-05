class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        k = 1
        while True:
            x = num1 - k * num2
            if k > x:
                return -1
            elif k >= x.bit_count():
                return k
            k += 1