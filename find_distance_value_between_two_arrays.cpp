class Solution {
public:
    int findTheDistanceValue(vector<int>& arr1, vector<int>& arr2, int d) {
        sort(arr2.begin(), arr2.end());
        int n = arr2.size();
        int s = 0;

        for (int num : arr1) {
            auto it = lower_bound(arr2.begin(), arr2.end(), num);
            if (it == arr2.end()) {
                s += abs(arr2[n-1] - num) > d;
                continue;
            }
            if (it == arr2.begin()) {
                s += abs(arr2[0] - num) > d;
                continue;
            }
            int u = *(it--);
            int l = *it;

            s += ((u - num > d) && (num - l > d));
        }
        return s;
    }
};
