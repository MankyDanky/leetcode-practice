class Solution {
public:
    int shortestPath(int n, vector<vector<int>>& edges, string labels, int k) {
        priority_queue<vector<int>> q;
        vector<vector<pair<int,int>>> adjacent(n);

        for (vector<int>& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];

            adjacent[u].push_back({v, w});
        }

        vector<vector<int>> dist(n, vector<int>(k+1, INT_MAX));

        dist[0][1] = 0;

        q.push({0, 0, 1});

        while (!q.empty()) {
            vector<int> v = q.top();
            q.pop();

            int d = -1*v[0];
            int node = v[1];
            int consec = v[2];

            if (d > dist[node][consec]) continue;

            for (pair<int,int> p : adjacent[node]) {
                int nk;
                if (labels[p.first] == labels[node]) {
                    nk = consec + 1;
                    if (nk > k) continue;
                } else {
                    nk = 1;
                }
                if (dist[p.first][nk] > d + p.second) {
                    q.push({-1*(d + p.second), p.first, nk});
                    dist[p.first][nk] = d + p.second;
                }       
            }
        }
        int res = INT_MAX;
        for (int i = 1; i <= k; i++) {
            res = min(res, dist[n-1][i]);
        }
        return res != INT_MAX ? res : -1;
    }
};
