class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows

        res = []
        for j in range(cols):
            i = 0
            while i < rows:
                if j + i < cols:
                    res.append(encodedText[(i) * cols + (i + j)])
                else:
                    break
                i += 1
        return "".join(res).rstrip(" ")
