class Solution {
public:
    vector<vector<vector<bool>>> cache;
    vector<vector<vector<bool>>> cached;
    bool hasValid(vector<vector<char>>& grid, int i, int j, int curr) {
        if (i < 0 || i >= grid.size() || j < 0 || j >= grid[0].size()) return false;
        curr += (grid[i][j] == '(' ? 1 : -1);
        if (curr < 0 || curr > (grid.size() + grid[0].size() - 1)/2) return false;
        if (i == grid.size() - 1 && j == grid[0].size() - 1) return curr == 0;
        if (cached[i][j][curr]) return cache[i][j][curr];

        cache[i][j][curr] = hasValid(grid, i+1, j, curr) || hasValid(grid, i, j+1, curr);
        cached[i][j][curr] = true;
        return cache[i][j][curr];
    }

    bool hasValidPath(vector<vector<char>>& grid) {
        cached.resize(grid.size(), vector<vector<bool>>(grid[0].size(), vector<bool>(10000, false)));
        cache.resize(grid.size(), vector<vector<bool>>(grid[0].size(), vector<bool>(10000, false)));
        return hasValid(grid, 0, 0, 0);
    }
};
