class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        bool foundNonZero = false;
        int x = 0;
        for (int num : nums) {
            x ^= num;
            if (num != 0) foundNonZero = true;
        }
        if (x != 0) return nums.size();

        if (foundNonZero) return nums.size() - 1;

        return 0;
    }
};
