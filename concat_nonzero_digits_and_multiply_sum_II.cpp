class Solution {
public:
    const long long MOD = 1000000007;
    const long long INV = 700000005;
    vector<int> sumAndMultiply(string s, vector<vector<int>>& queries) {
        int n = s.size();

        vector<long long> ss(n, 0);
        ss[n-1] = s[n-1] - '0';

        vector<long long> sx(n, 0);
        sx[n-1] = s[n-1] - '0';

        vector<long long> sd(n, 1);
        vector<long long> sm(n, 1);
        if (s[n-1] == '0') {
            sd[n-1] = 1;
            sm[n-1] = 1;
        } else {
            sd[n-1] = INV;
            sm[n-1] = 10;
        }

        for (int i = n-2; i >= 0; i--) {
            ss[i] = (ss[i+1] + (s[i] - '0')) % MOD;

            if (s[i] == '0') {
                sx[i] = sx[i+1];
                sd[i] = sd[i+1];
                sm[i] = sm[i+1];
            } else {
                sx[i] = ((sm[i+1] * (s[i] - '0')) + sx[i+1]) % MOD;
                sm[i] = (sm[i+1] * 10) % MOD;
                sd[i] = (sd[i+1] * INV) % MOD;
            }
        }

        vector<int> res;

        for (vector<int>& q : queries) {
            int l = q[0];
            int r = q[1];

            long long s = (ss[l] + MOD - (r+1 < n ? ss[r+1] : 0)) % MOD;

            long long x = sx[l];
            if (r+1 < n) {
                x = (x - sx[r+1] + MOD) % MOD;
                x = (x * sd[r+1]) % MOD;
            }

            res.push_back(((s * x) % MOD));
        }

        return res;

    }
};
