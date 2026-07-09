class Solution {
public:
    vector<bool> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        vector<int> groups(n, 1);
        for (int i = 0; i < n; i++) {
            groups[i] = i;
        }

        int l = 0;
        for (int r = 1; r < n; r++) {
            while (nums[r] - nums[l] > maxDiff) {
                l += 1;
            }
            groups[r] = groups[l];
        }

        vector<bool> res;

        for (vector<int>& q : queries) {
            int u = q[0];
            int v = q[1];

            res.push_back(groups[u] == groups[v]);
        }
        return res;
    }
};
