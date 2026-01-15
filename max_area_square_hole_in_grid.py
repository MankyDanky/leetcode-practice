class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        res = 1
        hBars.sort()
        vBars.sort()
        for i in range(0, len(hBars)):
            for j in range(0, len(vBars)):
                count = 1
                while i + count < len(hBars) and j + count < len(vBars):
                    if hBars[i+count] == hBars[i] + count and vBars[j+count] == vBars[j] + count:
                        count+=1
                    else:
                        break
                count += 1

                res = max(res, count*count)
        return res
        