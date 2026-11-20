class Solution {
public:
    vector<vector<int>> cache;
    
    int mx(vector<int>& nums, int index, bool incremented) {
        if (index == nums.size()) return 0;
        if (cache[index][incremented] != -1) return cache[index][incremented];

        int res = 1;
        for (int i = index + 1; i < index + 4 && i < nums.size(); i++) {
            if (nums[i] == nums[index] + incremented + 1) {
                res = max(res, 1 + mx(nums, i, false));
            }
            else if (nums[i] == nums[index] + incremented) {
                res = max(res, 1 + mx(nums, i, true));
            }
        }
        cache[index][incremented] = res;
        return res;
    }

    int maxSelectedElements(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> ns;
        int i = 0;
        while (i < nums.size()) {
            int j = i;
            while (j < nums.size() && nums[j] == nums[i]) {
                j++;
            }
            for (int k = i; k < j && k < i + 2; k++) {
                ns.push_back(nums[i]);
            }
            i = j;
        }

        cache.resize(ns.size(), vector<int>(2, -1));

        int res = 0; 
        for (int i = 0; i < ns.size(); i++) {
            res = max(res, mx(ns, i, true));
            res = max(res, mx(ns, i, false));
        }
        return res;
    }
};
