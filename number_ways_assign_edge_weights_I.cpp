class Solution {
public:
    const int MOD = 1000000007;
    unordered_map<int, long long> cache;

    long long solve(bool p, int i, int n) {
        if (i == n) {
            if (p) return 1;
            return 0;
        }

        if (cache.find((i<<1) | p) != cache.end()) {
            return cache[(i<<1) | p];
        }

        long long res = (solve(p, i+1, n) + solve(!p, i+1, n)) % MOD;
        cache[(i<<1) | p] = res;
        return res;
    }

    int assignEdgeWeights(vector<vector<int>>& edges) {
        int n = 0;
        for (int i = 0; i < edges.size(); i++) {
            n = max(n, edges[i][0]);
            n = max(n, edges[i][1]);
        }
        vector<vector<int>> graph(n);

        for (int i = 0; i < edges.size(); i++) {
            int u = edges[i][0] - 1;
            int v = edges[i][1] - 1;

            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        int maxDepth = 0;

        function<void(int,int, int)> getDepth = [&](int node, int depth, int prev) {
            maxDepth = max(maxDepth, depth);
            for (int to : graph[node]) {
                if (to == prev) {continue;}
                getDepth(to, depth+1, node);
            }
        };

        getDepth(0, 0, -1);

        cout<<maxDepth<<endl;

        return solve(0, 0, maxDepth);
    }
};
