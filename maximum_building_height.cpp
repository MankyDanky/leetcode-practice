class Solution {
public:
    int maxBuilding(int n, vector<vector<int>>& restrictions) {
        sort(restrictions.begin(), restrictions.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });

        map<int,int> r;
        r[1] = 0;
        r[2*n - 1] = 0;

        for (vector<int>& restriction : restrictions) {
            auto right = r.upper_bound(restriction[0]);
            auto left = prev(right);
            int rpos = right->first;
            int rval = right->second;
            int lpos = left->first;
            int lval = left->second;

            int pos = restriction[0];
            int val = restriction[1];
            if ((val >= lval + (pos - lpos)) || (val >= rval + (rpos - pos))) {
                continue;
            }
            r[pos] = val;
        }

        auto it = r.begin();
        auto prev = r.begin();
        it++;
        int res = 0;
        while (it != r.end()) {
            int val = it->second;
            int pos = it->first;

            int lval = prev->second;
            int lpos = prev->first;
            if (pos == 2*n-1) {
                res = max(res, n - lpos + lval);
                break;
            }
            int diff = pos - lpos;
            int val_diff = abs(val - lval);
            int rem = diff - val_diff;

            int increase = rem / 2;
            

            res = max(res, increase + max(lval, val));

            prev++;
            it++;
        }

        return res;
    }
};
