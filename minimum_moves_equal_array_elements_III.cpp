class Solution {
public:
    int minMoves(vector<int>& nums) {
        int m = *max_element(nums.begin(), nums.end());

        int res = 0;
        for (int num : nums) {
            res += (m - num);
        }
        return res;
    }
};
