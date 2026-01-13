class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        l = 0.0
        r = 1000000000.0
        eps = 0.00001
        totalArea = 0.0
        squares.sort(key=lambda x: x[1])
        for square in squares:
            totalArea += square[2]*square[2]
        while l + eps < r:
            mid = (l+r)/2
            area = 0.0
            for square in squares:
                if square[1] > mid:
                    break
                area += (min(mid, square[1] + square[2]) - square[1]) * square[2]
            if area >= totalArea/2:
                r = mid
            else:
                l = mid
        return l
