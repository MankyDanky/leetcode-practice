class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int minV = 100001;
        int minP = -1;
        int maxV = -100001;
        int maxP = -1;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > maxV) {
                maxV = nums[i];
                maxP = i;
            }
            if (nums[i] < minV) {
                minV = nums[i];
                minP = i;
            }
        }
        int a = min(minP, maxP);
        int b = max(minP, maxP);
        int n = nums.size();
        if (a == b) {
            return min(n - a, a + 1);
        }
        return min(n - b + a + 1, min(a + 1 + (b - a), n - b + (b - a)));
    }
};
