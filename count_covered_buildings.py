class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        minRow = defaultdict(lambda: 1000000)
        maxRow = defaultdict(lambda: -1000000)
        minCol = defaultdict(lambda: 1000000)
        maxCol = defaultdict(lambda: -1000000)
        for x, y in buildings:
            minRow[y] = min(minRow[y], x)
            maxRow[y] = max(maxRow[y], x)
            minCol[x] = min(minCol[x], y)
            maxCol[x] = max(maxCol[x], y)
        
        res = 0
        for x, y in buildings:
            if x < maxRow[y] and x > minRow[y] and y < maxCol[x] and y > minCol[x]:
                res += 1
        return res