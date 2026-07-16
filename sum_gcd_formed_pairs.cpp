class Solution {
public:
    long long gcdSum(vector<int>& nums) {
        int curr = 0;
        int n = nums.size();
        vector<int> prefixGcd(n, 0);
        for (int i = 0; i < n; i++) {
            curr = max(curr, nums[i]);
            prefixGcd[i] = gcd(curr, nums[i]);
        }

        sort(prefixGcd.begin(), prefixGcd.end());
        
        int l = 0;
        int r = n-1;
        long long res = 0;
        while (l < r) {
            res += gcd(prefixGcd[l], prefixGcd[r]);
            l += 1;
            r -= 1;
        }
        return res;
    }

    long long gcd(int a, int b) {
        
        if (a < b) swap(a, b);
        if (b == 0) return a;
        return gcd(b, a % b);
    }
};
