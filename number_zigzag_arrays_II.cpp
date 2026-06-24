class Solution {
public:
    const int MOD = 1000000007;
    unordered_map<int,vector<vector<long long>>> cache;

    vector<vector<long long>> rec(int n, int m) {
        if (cache.find(n) != cache.end()) {
            return cache[n];
        }
        if (n == 1) {
            vector<vector<long long>> res(m, vector<long long>(m, 0));
            for (int i = 0; i < m; i++) {
                res[i][i] = 1;
            }
            cache[n] = res;
            return res;
        }
        
        
        vector<vector<long long>> res(m,vector<long long>(m, 0));
        if (n % 2) {
            vector<vector<long long>> sub = rec(n-1, m);
            for (int i = 0; i < m; i++) {
                for (int j = i+1; j < m; j++) {
                    for (int k = 0; k < m; k++) {
                        res[i][k] = (res[i][k] + sub[j][k]) % MOD;
                    }
                }
            }
        } else {
            if ((n / 2) % 2) {
                vector<vector<long long>> sub = rec(n/2, m); 
                vector<vector<long long>> mirrored(m, vector<long long>(m, 0));
                for (int i = 0; i < m; i++) {
                    for (int j = 0; j < m; j++) {
                        mirrored[i][j] = sub[m - 1 - i][m - 1 - j];
                    }
                }
                vector<vector<long long>> pref(m, vector<long long>(m, 0));
                for (int i = 0; i < m; i++) {
                    pref[0][i] = sub[0][i];
                }

                for (int i = 1; i < m; i++) {
                    for (int j = 0; j < m; j++) {
                        pref[i][j] = (sub[i][j] + pref[i-1][j]) % MOD;
                    }
                }

                for (int i = 0; i < m; i++) {
                    for (int j = 0; j < m; j++) {
                        // Calculate res[i][j]

                        for (int k = 1; k < m; k++) {
                            res[i][j] = (res[i][j] + (mirrored[i][k] * pref[k-1][j]) % MOD) % MOD;
                        }
                        

                    }
                }
            } else {
                vector<vector<long long>> sub = rec(n/2, m); 
                vector<vector<long long>> pref(m, vector<long long>(m, 0));
                for (int i = 0; i < m; i++) {
                    pref[0][i] = sub[0][i];
                }

                for (int i = 1; i < m; i++) {
                    for (int j = 0; j < m; j++) {
                        pref[i][j] = (sub[i][j] + pref[i-1][j]) % MOD;
                    }
                }

                for (int i = 0; i < m; i++) {
                    for (int j = 0; j < m; j++) {
                        // Calculate res[i][j]

                        for (int k = 0; k < m; k++) {
                            res[i][j] = (res[i][j] + (sub[i][k] * ( (pref[m-1][j] - pref[k][j] + MOD) % MOD)) % MOD) % MOD;
                        }
                        

                    }
                }
            }
        }
        cache[n] = res;
        return res;

    }

    int zigZagArrays(int n, int l, int r) {
        int m = r - l + 1;

        vector<vector<long long>> res = rec(n, m);

        long long rs = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                rs = (rs + res[i][j]) % MOD;
            }
        }
        return (2 * rs) % MOD;
    }
};
