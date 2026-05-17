class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for j in range(y, y+k):
            t = x
            b = x + k - 1
            while t < b:
                grid[t][j], grid[b][j] = grid[b][j], grid[t][j]
                t += 1
                b -= 1
        return grid