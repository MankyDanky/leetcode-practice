class Solution {
public:
    long long gcd(long long a, long long b) {
        if (a < b) {
            return gcd(b, a);
        }
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    long long lcm(long long a, long long b) {
        if (a == 0 || b == 0) return 0;
        long long d = gcd(a,b);
        return abs(a*b)/d;
    }

    int maxLength(vector<int>& nums) {
        for (int l = nums.size(); l >= 1; l--) {
            for (int i = 0; i + l <= nums.size(); i++) {
                long long m = 1;
                long long d = nums[i];
                long long p = 1LL;

                for (int j = i; j < i + l; j++) {
                    m = lcm(m, nums[j]);
                    if (p > LLONG_MAX / nums[j]) break;
                    p *= (long long) nums[j];
                    d = gcd(d, nums[j]);
                }
                if (p == d * m) return l;
            }
            
        }
        return 1;
    }
};
