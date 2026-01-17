class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                bx = max(bottomLeft[i][0], bottomLeft[j][0])
                by = max(bottomLeft[i][1], bottomLeft[j][1])
                tx = min(topRight[i][0], topRight[j][0])
                ty = min(topRight[i][1], topRight[j][1])

                dx = tx - bx
                dy = ty - by

                if dx < 0 or dy < 0:
                    continue
                
                l = min(dx, dy)
                res = max(res, l*l)
        return res