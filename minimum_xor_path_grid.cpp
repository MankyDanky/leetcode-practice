class Solution {
public:
    vector<vector<optional<vector<bool>>>> dp;
    int m, n;

    vector<bool> search(vector<vector<int>>& grid, int i, int j) {
        
        if (i >= m || j >= n) return vector<bool>(1024, false);
        if (i == m-1 && j == n-1) {
            vector<bool> res(1024, false);
            res[grid[i][j]] = true;
            return res;
        };
        if (dp[i][j].has_value()) return dp[i][j].value();
        vector<bool> res(1024, false);
        vector<bool> right = search(grid, i, j+1);
        vector<bool> down = search(grid, i+1, j);
        
        for (int k = 0; k < 1024; k++) {
            if (right[k] || down[k]) {
                res[k ^ grid[i][j]] = true;
            }
            
        }

        dp[i][j] = res;
        return res;
    }

    int minCost(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();
        dp.resize(m, vector<optional<vector<bool>>>(n, nullopt));
        vector<bool> res = search(grid, 0, 0);
        
        for (int i = 0; i < 1024; i++) {
            if (res[i] == true) return i;
        }
        return 1024;
    }
};
