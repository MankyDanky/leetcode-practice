class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(num):
            if num == 1:
                return False
            if num == 2 or num == 3:
                return True
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True
        res = 0
        for num in range(left, right+1):
            if is_prime(num.bit_count()):
                res += 1
        return res
