class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        int res = 0;
        if (nums.size() <= 2) return nums.size();
        
        for (int num : nums) {
            int x = num;
            int l = 0;
            while (x != 0) {
                l++;
                x>>=1;
            }
            res = max(res, 1<<(l));
        }
        return res;
    }
};
