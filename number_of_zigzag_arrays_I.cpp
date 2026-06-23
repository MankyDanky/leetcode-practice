class Solution {
public:
    const long long MOD = 1000000007;
    int n;
    int m;
    vector<long long> cache;
    vector<long long> pref;

    long long prefSum(int l, int r) {
        if (r >= m || r < 0 || l >= m) {
            return 0;
        }
        if (l <= 0) {
            return pref[r];
        }
        return (pref[r] - pref[l-1] + MOD) % MOD;
    }

    int zigZagArrays(int n, int l, int r) {
        this->n = n;
        this->m = (r - l + 1);
        cache.resize(m);
        pref.resize(m);
        long long res = 0;
        cache[0] = 1;
        pref[0] = 1;


        for (int j = 1; j < m; j++) {
            cache[j] = 1;
            pref[j] = 1 + pref[j-1];
        }


        for (int i = n-2; i >= 0; i--) {
            for (int j = 0; j < m; j++) {
                long long sub = 0;
                if (i % 2) {
                    sub = prefSum(j+1, m-1);
                } else {
                    sub = prefSum(0, j-1);
                }
                cache[j] = sub;
            }
            pref[0] = cache[0];
            for (int j = 1; j < m; j++) {
                pref[j] = (cache[j] + pref[j-1]) % MOD;
            }
        }

        for (int j = 0; j < m; j++) {
            res = (res + cache[j]) % MOD;
        }
        return (int)(2 * res) % MOD;
    }
};
