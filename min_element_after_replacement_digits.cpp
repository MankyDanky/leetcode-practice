class Solution {
public:
    int minElement(vector<int>& nums) {
        int res = 1000000000;
        for (int i = 0; i < nums.size(); i++) {
            int x = nums[i];
            int curr = 0;
            while (x != 0) {
                curr += x % 10;
                x /= 10;
            }
            res = min(res, curr);
        }
        return res;
    }
};
