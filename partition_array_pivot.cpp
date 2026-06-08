class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> low;
        vector<int> equal;
        vector<int> high;

        int n = nums.size();

        for (int num : nums) {
            if (num < pivot) {
                low.push_back(num);
            } else if (num == pivot) {
                equal.push_back(num);
            } else {
                high.push_back(num);
            }
        }

        vector<int> res;
        while (!high.empty()) {
            res.push_back(high.back());
            high.pop_back();
        }

        while (!equal.empty()) {
            res.push_back(equal.back());
            equal.pop_back();
        }

        while (!low.empty()) {
            res.push_back(low.back());
            low.pop_back();
        }

        reverse(res.begin(), res.end());

        return res;
    }
};
