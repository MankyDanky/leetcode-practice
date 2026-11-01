class Solution {
public:
    int minMoves(vector<int>& nums) {
        int n = nums.size();
        int m = *(min_element(nums.begin(), nums.end()));

        int res = 0;
        for (int i = 0; i < n; i++) {
            res += nums[i] - m;
        }
        return res;
    }
};
