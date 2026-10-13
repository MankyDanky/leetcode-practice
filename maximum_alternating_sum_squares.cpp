class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        sort(nums.begin(), nums.end(), [](const int& a, const int& b) {
            return a*a < b*b;
        });
   
        int n = (nums.size());

        long long res = 0;
        for (int i = 0; i < n / 2 + (n % 2); i++) {
            res += nums[n-i-1]*nums[n-i-1];
        }
        for (int i = n/2 + (n % 2); i < n; i++) {
            res -= nums[n-i-1]*nums[n-i-1];
        }
        return res;
    }
};
