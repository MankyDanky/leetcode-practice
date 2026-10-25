class Solution {
public:
    void flip(vector<vector<int>>& grid, int i, int j) {
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size()) return;
        if (grid[i][j] != 0) return;
        grid[i][j] = 1;
        flip(grid, i+1, j);
        flip(grid, i-1, j);
        flip(grid, i, j+1);
        flip(grid, i, j-1);
    }

    int closedIsland(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        for (int i = 0; i < m; i++) {
            if (grid[i][0] == 0) flip(grid, i, 0);
            if (grid[i][n-1] == 0) flip(grid, i, n-1);
        }

        for (int j = 0; j < n; j++) {
            if (grid[0][j] == 0) flip(grid, 0, j);
            if (grid[m-1][j] == 0) flip(grid, m-1, j);
        }

        int res = 0;
        for (int i = 1; i < m - 1; i++) {
            for (int j = 1; j < n - 1; j++) {
                if (grid[i][j] == 0) {
                    res++;
                    flip(grid, i, j);
                }
            }
        }
        return res;
        /*
        [[0,0,1,1,0,1,0,0,1,0],
         [1,1,0,1,1,0,1,1,1,0],
         [1,0,1,1,1,0,0,1,1,0],
         [0,1,1,0,0,0,0,1,0,1],
         [0,0,0,0,0,0,1,1,1,0],
         [0,1,0,1,0,1,0,1,1,1],
         [1,0,1,0,1,1,0,0,0,1],
         [1,1,1,1,1,1,0,0,0,0],
         [1,1,1,0,0,1,0,1,0,1],
         [1,1,1,0,1,1,0,1,1,0]]
        */
    }
};
