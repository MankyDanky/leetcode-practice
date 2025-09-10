class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        x, y = 0, 0
        for i in range(2):
            found = False
            for j in range(3):
                if board[i][j] == 0:
                    found = True
                    x = i
                    y = j
                    break
                if found:
                    break
        state = (tuple(board[0]), tuple(board[1]))

        q = deque([(state, x, y)])
        print(q)
        res = 0
        found = False
        while q:
            
            for _ in range(len(q)):
                state, i, j = q.popleft()
                if state in visited:
                    continue
                if state == ((1,2,3), (4,5,0)):
                    found = True
                    break
                visited.add(state)
                for di, dj in directions:
                    if 0 <= di + i <= 1 and 0 <= dj + j <= 2:
                        new_state = [list(state[0]), list(state[1])]
                        new_state[i][j], new_state[i+di][j+dj] = new_state[i+di][j+dj], new_state[i][j]
                        new_state = (tuple(new_state[0]), tuple(new_state[1]))
                        q.append((new_state, di+i, dj+j))
            if found:
                break
            res += 1
        return res if found else -1

