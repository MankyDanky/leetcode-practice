class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<int> colSum(n, 0);
        vector<int> rowSum(m, 0);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                colSum[j] += grid[i][j];
                rowSum[i] += grid[i][j];
            }
        }

        int res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j]) {
                    res += (colSum[j] > 1 || rowSum[i] > 1);
                }
            }
        }
        return res;
    }
};
