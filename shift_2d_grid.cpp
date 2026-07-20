class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();

        k %= (m*n);
        
        vector<vector<bool>> vis(m, vector<bool>(n, false));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (vis[i][j]) continue;
                deque<vector<int>> q;
                q.push_back({grid[0][0], (i + (k / n) + (j + k % n) / n) % m, (j + k) % n});
                while (!q.empty()) {
                    vector<int> v = q.front();
                    q.pop_front();
                    int val = v[0];
                    int i = v[1];
                    int j = v[2];

                    if (!vis[i][j]) {
                        int ni = (i + (k / n) + (j + k % n) / n) % m;
                        int nj = (j + k) % n;
                        q.push_back({grid[i][j], ni, nj});
                        vis[i][j] = true;
                    }
                    grid[i][j] = val;
                }
            }
        }
        
        return grid;
    }
};
