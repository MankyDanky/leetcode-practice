class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = ((0, 1),(1, 0),(-1, 0),(0,-1))

        def scan(visited, pos, s):
            i, j = pos
            if i >= m or j >= n or i < 0 or j < 0:
                return False
            s += board[i][j]
            print(s)
            if len(s) == len(word):
                if s == word:
                    return True
                return False

            for direction in directions:
                newPos = (i + direction[0], j + direction[1])
                if not newPos in visited:
                    if scan(visited | {pos}, newPos, s):
                        return True
            return False
        
        for i in range(m):
            for j in range(n):
                if scan(set(), (i,j), ""):
                    return True
        return False
                
            