class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        def isPalindrome(start, end):
            if palindrome_cache[start][end] != -1:
                return palindrome_cache[start][end]
            sub = s[start:end]
            palindrome_cache[start][end] = (sub == sub[::-1])
            return palindrome_cache[start][end]

        palindrome_cache = [[-1] * (n+1) for _ in range(n + 1)]
        cache = {}
        def dfs(start):
            if start == n:
                return 0
            if start in cache:
                return cache[start]
            if isPalindrome(start, n):
                return 1
            min_cuts = float("inf")
            for end in range(start+1, n+1):
                if isPalindrome(start, end):
                    min_cuts = min(min_cuts, 1 + dfs(end))
            cache[start] = min_cuts
            return cache[start]
        return dfs(0) - 1