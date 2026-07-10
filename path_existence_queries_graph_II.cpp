class Solution {
public:
    vector<vector<int>> leaps;

    int distance(int t, int s) {
        int j = 0;
        for (int i = leaps.size() - 1; i >= 0; i--) {
            if (leaps[i][s] > t) {
                s = leaps[i][s];
                j += (1<<i);
            }
        }
        return j + 1;
    }

    vector<int> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        vector<pair<int,int>> numsc(n);
        for (int i = 0; i < n; i++) {
            numsc[i] = {nums[i], i};
        }

        sort(numsc.begin(), numsc.end());
        vector<int> convert(n);
        for (int i = 0; i < n; i++) {
            convert[numsc[i].second] = i;
        }
        vector<int> parent(n);

        int l = 0;
        for (int r = 0; r < n; r++) {
            while (numsc[r].first - numsc[l].first > maxDiff) {
                l += 1;
            }
            parent[r] = l;
        }

        leaps.push_back(parent);

        for (int j = 2; j < n; j<<=1) {
            vector<int> prev = leaps.back();
            vector<int> next(n);

            for (int i = 0; i < n; i++) {
                next[i] = prev[prev[i]];
            }
            leaps.push_back(next);
        }

        vector<int> res;

        for (vector<int>& q : queries) {
            int u = q[0];
            int v = q[1];
            if (u == v) {
                res.push_back(0);
                continue;
            }

            int t = convert[u];
            int s = convert[v];

            if (t > s) {
                swap(t, s);
            }

            int d = distance(t,s);
            if (d >= n) {
                res.push_back(-1);
                continue;
            }
            res.push_back(d);
            
        }
        return res;

        
    }
};
