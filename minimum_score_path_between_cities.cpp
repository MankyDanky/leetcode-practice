class Solution {
public:
    vector<vector<pair<int,int>>> graph;

    int dfs(int node, vector<bool>& visited) {
        int res = 1000000000;
        visited[node] = true;

        for (auto[b, d] : graph[node]) {
            res = min(res, d);
            if (!visited[b]) {
                res = min(res, dfs(b, visited));
            }
        }
        return res;
    }

    int minScore(int n, vector<vector<int>>& roads) {
        graph.resize(n);

        for (vector<int>& v : roads) {
            int a = v[0];
            int b = v[1];
            int d = v[2];
            a--; b--;

            graph[a].push_back({b, d});
            graph[b].push_back({a, d});
        }

        vector<bool> visited(n, false);
        return dfs(0, visited);

    }
};
