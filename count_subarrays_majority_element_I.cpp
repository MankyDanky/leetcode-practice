class Solution {
public:
    int countMajoritySubarrays(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int> counts(n, 0);
        counts[0] = nums[0] == target ? 1 : 0;
        for (int i = 1; i < n; i++) {
            counts[i] = counts[i-1] + (nums[i] == target ? 1 : 0);
        }

        int res = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                int s = i - j + 1;
                int c = counts[i] - (j > 0 ? counts[j-1] : 0);
                if (c > (s / 2)) {
                    res += 1;
                }
            }
        }
        return res;
    }
};
