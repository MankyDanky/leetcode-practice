class Solution {
public:
    int n;
    vector<vector<pair<int,long long>>> graph;
    const long long INF = 1000000000000000;
    long long maxDist = 0;

    bool canDo(long long minS) {
        priority_queue<vector<long long>> q;
        q.push({0, 0});
        vector<bool> visited(n);

        while (!q.empty()) {
            vector<long long> v = q.top();
            q.pop();
            
            long long dist = -1*v[0];
            long long u = v[1];
            if (visited[u]) continue;
            visited[u] = true;

                

            if (u == n-1) return true;

            for (auto [v, c] : graph[u]) {
                if (c < minS || c + dist > maxDist) continue;
                q.push({-1*(c+dist), v});
            }
        }
        return false;
    }

    int findMaxPathScore(vector<vector<int>>& edges, vector<bool>& online, long long k) {
        
        n = online.size();
        graph.resize(n);
        int l = 1000000000;
        int r = 0;
        maxDist = k;
        for (vector<int>& e : edges) {
            int u = e[0];
            int v = e[1];
            int c = e[2];
            r = max(r, c);
            l = min(l, c);
            if (online[u] && online[v]) {
                graph[u].push_back({v, (long long)c});
            }
        }

        
        while (l < r) {
            int m = (l+r)/2;
            if ((l+r) % 2) {
                m += 1;
            }

            if (canDo(m)) {
                l = m;
            } else {
                r = m - 1;
            }
        }
        if (canDo(l)) return l;

        
        return -1;
    }
};
