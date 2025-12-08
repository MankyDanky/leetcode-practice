class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                c2 = i*i + j*j
                c = sqrt(c2)
                if c % 1 == 0 and c <= n:
                    res += 1
        return res