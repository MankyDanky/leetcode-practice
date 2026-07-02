class Solution {
public:
    bool valid(int i, int j, int m, int n) {
        return (i >= 0 && i < m && j >= 0 && j < n);
    }

    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        int m = grid.size();
        int n = grid[0].size();

        vector<vector<bool>> visited(m, vector<bool>(n, false));

        if (grid[0][0] == 1) health -= 1;

        visited[0][0] = true;

        deque<pair<int,int>> q;
        vector<pair<int,int>> dirs = {{0,1}, {1, 0}, {0, -1}, {-1, 0}};
        q.push_back({0,0});
        for (int h = 0; h < health; h++) {
            // 0 cost expansion
            deque<pair<int,int>> qc(q);
            while (!qc.empty()) {
                int s = qc.size();

                for (int k = 0; k < s; k++) {
                    auto [i, j] = qc.front();
                    qc.pop_front();
                    for (auto [di, dj] : dirs) {
                        if (valid(di+i, dj+j, m, n) && visited[i+di][j+dj] == false && grid[i+di][j+dj] == 0) {
                            visited[i+di][j+dj] = true;
                            qc.push_back({i+di, j+dj});
                            q.push_back({i+di, j+dj});
                        }
                    }
                }

            }
            

            if (h == health-1) break;
            // 1 cost expansion
            int pee = q.size();
            for (int k = 0; k < pee; k++) {
                auto [i, j] = q.front();
                q.pop_front();
                for (auto [di, dj] : dirs) {
                    if (valid(di+i, dj+j, m, n) && visited[i+di][j+dj] == false) {
                        visited[i+di][j+dj] = true;
                        q.push_back({i+di, j+dj});
                    }
                }
            } 
        }

        return visited[m-1][n-1];
    }
};
