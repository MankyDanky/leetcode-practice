class Solution {
public:
    int firstStableIndex(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> pref(n, 0);
        vector<int> suff(n, INT_MAX);
        pref[0] = nums[0];
        suff[n-1] = nums[n-1];
        for (int i = 1; i < n; i++) {
            pref[i] = max(pref[i-1], nums[i]);
            suff[n-1-i] = min(suff[n-i], nums[n-1-i]);
        }
        for (int i = 0; i < n; i++) {
            int ins = pref[i] - suff[i];
            if (ins <= k) return i;
        }
        return -1;
    }
};
