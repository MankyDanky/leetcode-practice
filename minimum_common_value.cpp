class Solution {
public:
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        int l = 0;
        int r = 0;
        int n = nums1.size();
        int m = nums2.size();
        while (l < n && r < m) {
            if (nums1[l] == nums2[r]) {
                return nums1[l];
            }
            if (nums1[l] < nums2[r]) {
                l += 1;
            } else {
                r += 1;
            }
        }
        return -1;
    }
};