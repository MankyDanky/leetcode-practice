class Solution {
public:
    bool valid(int i, int j, int n) {
        if (i >= n || i < 0 || j >= n || j < 0) return false;
        return true;
    }

    long long hash_pair(int i, int j) {
        return ((long long) i + ((long long)j<<31));
    }

    int maximumSafenessFactor(vector<vector<int>>& grid) {
        int n = grid.size();

        deque<pair<int,int>> bfs;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    bfs.push_back({i, j});
                }
                grid[i][j] -= 1;
            }
        }

        int dist = 1;

        while (!bfs.empty()) {
            int s = bfs.size();
            for (int c = 0; c < s; c++) {
                auto [i, j] = bfs.front();
                bfs.pop_front();

                if (valid(i+1, j, n) && grid[i+1][j] == -1) {
                    grid[i+1][j] = dist;
                    bfs.push_back({i+1, j});
                }
                if (valid(i-1, j, n) && grid[i-1][j] == -1) {
                    grid[i-1][j] = dist;
                    bfs.push_back({i-1, j});
                }
                if (valid(i, j+1, n) && grid[i][j+1] == -1) {
                    grid[i][j+1] = dist;
                    bfs.push_back({i, j+1});
                }
                if (valid(i, j-1, n) && grid[i][j-1] == -1) {
                    grid[i][j-1] = dist;
                    bfs.push_back({i, j-1});
                }
            }
            dist ++;
        }
        
        priority_queue<vector<int>> q;
        q.push({grid[0][0], 0, 0});
        unordered_set<long long> visited;
        visited.insert(hash_pair(0,0));
        while (!q.empty()) {
            vector<int> v = q.top();
            auto [dist, i, j] = tie(v[0], v[1], v[2]);
            q.pop();
            if (i == n-1 && j == n-1) return dist;

            if (valid(i+1, j, n) && !visited.contains(hash_pair(i+1, j))) {
                visited.insert(hash_pair(i+1, j));
                q.push({min(dist, grid[i+1][j]), i+1, j});
            }
            if (valid(i-1, j, n) && !visited.contains(hash_pair(i-1, j))) {
                visited.insert(hash_pair(i-1, j));
                q.push({min(dist, grid[i-1][j]), i-1, j});
            }
            if (valid(i, j+1, n) && !visited.contains(hash_pair(i, j+1))) {
                visited.insert(hash_pair(i, j+1));
                q.push({min(dist, grid[i][j+1]), i, j+1});
            }
            if (valid(i, j-1, n) && !visited.contains(hash_pair(i, j-1))) {
                visited.insert(hash_pair(i, j-1));
                q.push({min(dist, grid[i][j-1]), i, j-1});
            }
        }
        return 0;
    }
};
