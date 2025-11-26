class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        seen = set()
        remainder = 0
        curr = 1
        l = 0
        if (k % 2 == 0 or k % 5 == 0):
            return -1
        while k > curr:
            curr *= 10
            l += 1
        length = 1
        while True:
            remainder = (remainder + curr) % k
            if remainder == 0:
                return length
            if remainder in seen:
                return -1
            seen.add(remainder)
            remainder *= 10
            length += 1
