class Solution {
public:
    int minMoves2(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int median = nums[n / 2];

        long long res = 0;

        for (int num : nums) {
            res += abs(num - median);
        }
        return res;
    }
};
