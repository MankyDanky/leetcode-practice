class Solution {
    int getRotateFunction(vector<int>& nums, int k) {
        int n = nums.size();
        int res = 0;
        for (int i = 0; i < n; i++) {
            res += ((i + k) % n) * nums[i];
        }
        return res;
    }
public:
    int maxRotateFunction(vector<int>& nums) {
        int res = getRotateFunction(nums, 0);
        int prev = res;

        int sum = std::accumulate(nums.begin(), nums.end(), 0);

        int n = nums.size();

        for (int k = 1; k < nums.size(); k++) {
            int curr = prev + sum - n * (nums[n-k]);
            prev = curr;
            res = max(res, curr);
        }
        return res;
    }
};