class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        int l = 0;
        unordered_map<int,int> freq;
        int res = 1;
        for (int r = 0; r < nums.size(); r++) {
            if (!freq.contains(nums[r])) {
                freq[nums[r]] = 0;
            }
            freq[nums[r]] += 1;
            while (freq[nums[r]] > k) {
                freq[nums[l]] -= 1;
                l += 1;
            }
            res = max(res, r - l + 1);
        }
        return res;
    }
};
