class Solution {
public:
    vector<vector<vector<long long>>> cache;
    int m, n;
    const int MOD = 1e9 + 7;

    long long valid(vector<vector<int>>& grid, int i, int j, bool d) {
        if (i >= m || j >= n) return 0;
        if (cache[i][j][d] != -1) return cache[i][j][d];
        if (i == m-1 && j == n-1) return 1;

        if (grid[i][j] == 1) {
            long long res;
            if (d) {
                res = valid(grid, i, j+1, false);
                
            } else {
                res = valid(grid, i+1, j, true);
            }
            cache[i][j][d] = res;
            return res;
        } else {
            long long res = (valid(grid, i+1, j, true) + valid(grid, i, j+1, false)) % MOD;
            cache[i][j][0] = res;
            cache[i][j][1] = res;
            return res;
        }
    }

    int uniquePaths(vector<vector<int>>& grid) {
        m = grid.size();
        n = grid[0].size();
        cache.resize(m, vector<vector<long long>>(n, vector<long long>(2, -1))); 
        return valid(grid, 0, 0, 0);
    }
};
