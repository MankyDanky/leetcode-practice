class Solution {
public:
    int sortPermutation(vector<int>& nums) {
        int mask = INT_MAX;
        int n = nums.size();
        vector<int> sorted = nums;

        sort(sorted.begin(), sorted.end());

        if (sorted == nums) return 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] != i) mask &= nums[i];
        }
        return mask;
    }
};
