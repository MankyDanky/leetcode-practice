class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        n = len(moves)
        flex = 0
        pos = 0
        res = 0
        for move in moves:
            if move == 'L':
                pos -= 1
            elif move == 'R':
                pos += 1
            else:
                flex += 1
        return abs(pos) + flex