class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int res = 0;
        int n = nums.size();
        if (nums[0] && nums[1] < 0) {
            res = nums[0] * nums[1] * nums[n-1];
        }
        res = max(res, nums[n-1] * nums[n-2] * nums[n-3]);
        return res;
    }
};
