class Solution {
public:
    const int MOD = 1000000007;
    vector<vector<int>> lift;
    vector<int> depths;

    long long modPow(long long base, int k) {

        if (k == 0) return 1;
        if (k % 2) {
            return (base * modPow(base, k-1)) % MOD;
        } else {
            return modPow((base * base) % MOD, k/2);
        }
    }

    int jump(int u, int k) {

        for (int i = 0; i < lift.size(); i++) {
            if (k&(1<<i)) {
                u = lift[i][u];
            }
        }

        return u;
    }

    int lca(int u, int v) {
        if (depths[v] > depths[u]) {
            v = jump(v, depths[v]-depths[u]);
        } else {
            u = jump(u, depths[u]-depths[v]);
        }

        if (u == v) return v;

        for (int i = lift.size() - 1; i >= 0; i--) {
            if (lift[i][u] != lift[i][v]) {
                u = lift[i][u];
                v = lift[i][v];
            }
        }
        return lift[0][u];
    }

    vector<int> assignEdgeWeights(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        int n = 0;
        for (int i = 0; i < edges.size(); i++) {
            n = max(n, edges[i][0]);
            n = max(n, edges[i][1]);
        }
        vector<vector<int>> graph(n);
        vector<int> parent(n, 0);

        for (int i = 0; i < edges.size(); i++) {
            int u = edges[i][0] - 1;
            int v = edges[i][1] - 1;

            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        depths.resize(n);

        function<void(int,int, int)> getDepth = [&](int node, int depth, int prev) {
            depths[node] = depth;
            for (int to : graph[node]) {
                if (to == prev) {continue;}
                parent[to] = node;
                getDepth(to, depth+1, node);
            }
        };
        
        getDepth(0, 0, -1);

        lift.push_back(parent);
        vector<int> prev = parent;

        for (int i = 2; i < n; i<<=1) {
            vector<int> addition(n, 0);
            for (int j = 0; j < n; j++) {
                addition[j] = prev[prev[j]];
            }
            lift.push_back(addition);
            prev = addition;
        }

        vector<int> res;
        for (int i = 0; i < queries.size(); i++) {
            int u = queries[i][0] - 1;
            int v = queries[i][1] - 1;
            if (u == v) {
                res.push_back(0);
                continue;
            }
            int p = lca(u, v);

            int dist = depths[v] + depths[u] - 2 * depths[p];
            res.push_back(modPow(2, dist-1));
        }

        return res;

    }
};
