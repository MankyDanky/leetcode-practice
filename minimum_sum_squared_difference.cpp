class Solution {
    bool search(vector<int>& nums1, vector<int>& nums2, int k, int cutoff) {
        int n = nums1.size();
        int used = 0;
        for (int i = 0; i < n; i++) {
            int diff = abs(nums1[i] - nums2[i]);
            if (diff > cutoff) {
                used += diff - cutoff;
            }
            if (used > k) return false;
        }
        return true;
    }

public:
    long long minSumSquareDiff(vector<int>& nums1, vector<int>& nums2, int k1, int k2) {
        int k = k1 + k2;

        int l = 0;
        int r = INT_MAX;
        while (l < r) {
            int m = (l + r) / 2;
            if (search(nums1, nums2, k, m)) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        int n = nums1.size();
        vector<long long> diffs(n);

        for (int i = 0; i < n; i++) {
            if (abs(nums1[i] - nums2[i]) > l) {
                diffs[i] = l;
                k -= abs(nums1[i] - nums2[i]) - l;
            } else {
                diffs[i] = abs(nums1[i] - nums2[i]);
            }
        }

        if (k > 0 && l > 0) {
            for (int i = 0; i < n; i++) {
                if (diffs[i] == l) {
                    diffs[i] -= 1;
                    k -= 1;
                    if (k == 0) break;
                }
            }
        }
        

        long long res = 0;
        for (int i = 0; i < n; i++) {
            res += diffs[i] * diffs[i];
        }

        return res;

    }
};
