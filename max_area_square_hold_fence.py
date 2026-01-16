class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        inH = set(hFences)
        inV = set(vFences)
        inH.add(1)
        inV.add(1)
        inH.add(m)
        inV.add(n)
        res = -1

        diagonalMax = {}
        diagonalMin = {}

        MOD = 1000000007

        for h in inH:
            for v in inV:
                d = h - v
                if d in diagonalMax:
                    if h > diagonalMax[d][0]:
                        diagonalMax[d] = (h, v)
                else:
                    diagonalMax[d] = (h, v)

                if d in diagonalMin:
                    if h < diagonalMin[d][0]:
                        diagonalMin[d] = (h, v)
                else:
                    diagonalMin[d] = (h, v)

        res = 0
        for d in diagonalMax:
            l = diagonalMax[d][0] - diagonalMin[d][0]
            res = max(res, l * l)
        return res % MOD if res != 0 else -1