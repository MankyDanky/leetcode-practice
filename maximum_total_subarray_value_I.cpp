class Solution {
public:
    long long maxTotalValue(vector<int>& nums, int k) {
        int m = 1000000000;
        int res = -1000000000;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            m = min(m, nums[i]);
            res = max(res, (nums[i] - m));
        }
        m = 1000000000;
        for (int i = n-1; i >= 0; i--) {
            m = min(m, nums[i]);
            res = max(res, (nums[i] - m));
        }
        return (long long)res * k;
    }
};
