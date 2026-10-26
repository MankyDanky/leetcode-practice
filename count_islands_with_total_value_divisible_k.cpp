class Solution {
public:
    long long getTotal(vector<vector<int>>& grid, int i, int j) {
        int m = grid.size();
        int n = grid[0].size();
        if (i < 0 || i >= m || j < 0 || j >= n) return 0;
        if (grid[i][j] == 0) return 0;
        long long s = grid[i][j];
        grid[i][j] = 0;
        return s + getTotal(grid, i+1, j) + getTotal(grid, i-1, j) + getTotal(grid, i, j+1) + getTotal(grid, i, j-1);
    }
    int countIslands(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();
        int res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != 0) {
                    long long t = getTotal(grid, i, j);
                    if (t % k == 0) res++;
                }
            }
        }
        return res;
    }
};
