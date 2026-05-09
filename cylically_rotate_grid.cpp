class Solution {
    int m, n;
    int layers;

    void rotateLayer(vector<vector<int>>& grid, int k, int layer) {
        vector<int> curr;
        for (int i = layer; i < n - layer; i++) {
            curr.push_back(grid[layer][i]);
        }

        for (int i = layer + 1; i < m - layer - 1; i++) {
            curr.push_back(grid[i][n - layer - 1]);
        }

        for (int i = n - layer - 1; i >= layer; i--) {
            curr.push_back(grid[m - layer - 1][i]);
        }

        for (int i = m - 2 - layer; i >= layer + 1; i--) {
            curr.push_back(grid[i][layer]);
        }

        cout<<"Layer: "<<layer<<endl;
        for (int v : curr) {
            cout<<v<<' ';
        }
        cout<<endl;

        int s = curr.size();

        for (int i = layer; i < n - layer; i++) {
            grid[layer][i] = curr[((i - layer) + k) % s];
        }

        for (int i = layer + 1; i < m - layer - 1; i++) {
            grid[i][n - layer - 1] = curr[((i - (layer + 1)) + (n - 2 * layer) + k) % s];
        }

        for (int i = n - layer - 1; i >= layer; i--) {
            grid[m - layer - 1][i] = curr[(((n - layer - 1) - i) + (s / 2) + k) % s];
        }

        for (int i = m - 2 - layer; i >= layer + 1; i--) {
            grid[i][layer] = curr[(((m - 2 - layer) - i) + (s / 2) + (n - 2 * layer) + k) % s];
        }
    }
public:
    vector<vector<int>> rotateGrid(vector<vector<int>>& grid, int k) {
        m = grid.size();
        n = grid[0].size();
        layers = min(m, n) / 2;

        for (int i = 0; i < layers; i++) {
            rotateLayer(grid, k, i);
        }
        return grid;
    }
};