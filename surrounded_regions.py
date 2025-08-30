class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        
        def dfs(i,j):
            nonlocal board
            if i >= m or i < 0 or j >= n or j < 0 or board[i][j] != 'O':
                return
            board[i][j] = 'U'
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)

        for i in range(m):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][n-1] == 'O':
                dfs(i,n-1)

        for j in range(n):
            if board[0][j] == 'O':
                dfs(0,j)
            if board[m-1][j] == 'O':
                dfs(m-1,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'U':
                    board[i][j] = 'O'       