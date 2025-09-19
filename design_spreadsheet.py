class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        row = int(cell[1:]) - 1
        col = ord(cell[0]) - ord('A')
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        row = int(cell[1:]) - 1
        col = ord(cell[0]) - ord('A')
        self.grid[row][col] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        A, B = formula.split("+")
        aVal, bVal = None, None
        if A[0].isdigit():
            aVal = int(A)
        else:
            row = int(A[1:]) - 1
            col = ord(A[0]) - ord('A')
            aVal = self.grid[row][col]
        
        if B[0].isdigit():
            bVal = int(B)
        else:
            row = int(B[1:]) - 1
            col = ord(B[0]) - ord('A')
            bVal = self.grid[row][col]
        return aVal + bVal
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)