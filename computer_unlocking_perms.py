class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 1000000007

        n = len(complexity)
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0
        
        curr = 1
        res = 1
        for i in range(1, n):
            res = (res * curr) % MOD
            curr = (curr+1) % MOD
        return res