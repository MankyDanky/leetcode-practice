class Solution {
public:
    vector<int> countServers(int n, vector<vector<int>>& logs, int x, vector<int>& queries) {
        vector<int> usingTill(n, -1);
        priority_queue<array<int, 3>, vector<array<int,3>>, greater<array<int,3>>> q;
        int zero = n;

        for (vector<int>& log : logs) {
            q.push({log[1], 0, log[0] - 1});
            q.push({log[1] + x, 2, log[0] - 1});
        }
        int index = 0;
        for (int query : queries) {
            q.push({query, 1, index++});
        }
        

        vector<int> res(queries.size(), -1);
        while (!q.empty()) {
            array<int,3> t = q.top();
            q.pop();

            if (t[1] == 0) {
                int s = t[2];
                if (usingTill[s] == -1) {
                    zero -= 1;
                }
                usingTill[s] = t[0] + x;
            } else if (t[1] == 1) {
                res[t[2]] = zero;
            } else {
                int s = t[2];
                if (usingTill[s] == t[0]) {
                    zero += 1;
                    usingTill[s] = -1;
                }
            }
        }
        return res;
    }
};
