class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int n = arr.size();
        int res = n;
        for (int i = n-1; i >= 0; i--) {
            res = min(res, min(arr[i] + (n - 1 - i), n));
        } 
        return res;
    }
};
