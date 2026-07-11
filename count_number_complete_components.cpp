class Solution {
public:
    int countCompleteComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n);

        for (vector<int>& v : edges) {
            int a = v[0];
            int b = v[1];

            graph[a].push_back(b);
            graph[b].push_back(a);
        }
        
        function<void(int, vector<int>&, vector<bool>&)> dfs = [&](int node, vector<int>& cur, vector<bool>& visited) {
            if (visited[node]) return;
            visited[node] = true;

            cur.push_back(node);
            for (int child : graph[node]) {
                dfs(child, cur, visited);
            }
        };
        
        vector<vector<int>> components;
        vector<bool> visited(n, false);
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                vector<int> comp;
                dfs(i, comp, visited);
                components.push_back(comp);
            }
        }

        int res = 0;

        for (vector<int>& comp : components) {
            int s = comp.size();
            bool valid = true;
            for (int node : comp) {
                if (graph[node].size() != s-1) {
                    valid = false;
                    break;
                }
            }
            if (valid) res += 1;
        }
        return res;
    }
};
