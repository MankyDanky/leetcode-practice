class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        increases = {}
        for row1, col1, row2, col2 in queries:
            if (row1, col1) not in increases:
                increases[(row1, col1)] = list()
            increases[(row1, col1)].append((row2, col2))


        res = [[0] * n for _ in range(n)]

        curr = 0

        decreases = defaultdict(int)

        for i in range(n):
            for j in range(n):
                
                if (i,j) not in increases:
                    increases[(i, j)] = list()
                for row2, col2 in increases[(i,j)]:
                    curr += 1
                    decreases[(i, col2)] += 1
                if (i > 0):
                    if (i,j) not in increases:
                        increases[(i-1, j)] = list()
                    for row2, col2 in increases[(i-1, j)]:
                        if row2 >= i:
                            increases[(i,j)].append((row2, col2))
                            curr += 1
                            decreases[(i, col2)] += 1
                res[i][j] = curr
                curr -= decreases[(i,j)]
        return res