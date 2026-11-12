class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        vector<int> curr;
        bool increasing = false;
        int res = 0;

        for (int num : nums) {
            if (curr.size() == 0) {
                curr.push_back(num);
                res = max(res, (int)curr.size());
                continue;
            }

            if (curr.size() == 1) {
                if (num > curr[0]) {
                    increasing = true;
                    curr.push_back(num);
                    res = max(res, (int)curr.size());
                } else if (num < curr[0]) {
                    increasing = false;
                    curr.push_back(num);
                    res = max(res, (int)curr.size());
                }
                continue;
            }

            if (increasing) {
                if (num > curr.back()) {
                    curr.push_back(num);
                    res = max(res, (int)curr.size());
                } else if (num < curr.back()) {
                    increasing = false;
                    curr = {curr.back()};
                    curr.push_back(num);
                } else {
                    curr = {num};
                }
            } else {
                if (num < curr.back()) {
                    curr.push_back(num);
                    res = max(res, (int)curr.size());
                } else if (num > curr.back()) {
                    increasing = true;
                    curr = {curr.back()};
                    curr.push_back(num);
                } else {
                    curr = {num};
                }
            }
        }
        return res;
    }
};
