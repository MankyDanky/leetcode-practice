from typing import List

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # prefix[col][r] = sum of grid[0..r-1][col]
        prefix = [[0] * (n + 1) for _ in range(n)]
        for c in range(n):
            for r in range(n):
                prefix[c][r + 1] = prefix[c][r] + grid[r][c]

        # pick[h]: previous column has height h and can score current column
        # skip[h]: previous column has height h but current column should not
        #          count overlap already handled from the left
        pick = [0] * (n + 1)
        skip = [0] * (n + 1)

        for c in range(1, n):
            new_pick = [0] * (n + 1)
            new_skip = [0] * (n + 1)

            for curr in range(n + 1):
                for prev in range(n + 1):
                    if curr > prev:
                        # current column is black deeper than previous column
                        # so white cells in previous column score
                        score = prefix[c - 1][curr] - prefix[c - 1][prev]

                        new_pick[curr] = max(new_pick[curr], skip[prev] + score)
                        new_skip[curr] = max(new_skip[curr], skip[prev] + score)

                    else:
                        # previous column is black deeper than current column
                        # so white cells in current column score
                        score = prefix[c][prev] - prefix[c][curr]

                        new_pick[curr] = max(new_pick[curr], pick[prev] + score)
                        new_skip[curr] = max(new_skip[curr], pick[prev])

            pick, skip = new_pick, new_skip

        return max(pick)