class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        int n = nums.size();
        vector<int> l(n,0);
        vector<int> r(n,0);

        int s1 = 0;
        int s2 = 0;
        for (int i = 0; i < n; i++) {
            l[i] = s1;
            s1 += nums[i];
            r[n-i-1] = s2;
            s2 += nums[n-1-i];
        }

        vector<int> res(n);
        for (int i = 0; i < n; i++) {
            res[i] = abs(l[i] - r[i]);
        }
        return res;
    }
};
