class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        const int MOD = 1e9+7;

        int n = arr.size();

        vector<int> pref(n+1, 0);
        for (int i = 1; i <= n; i++) {
            pref[i] = (pref[i-1] + arr[i-1] % 2) % 2;
        }

        vector<long long> counts = {1, 0};

        long long res = 0;
        for (int i = 1; i <= n; i++) {
            res += (counts[1 - pref[i]]) % MOD;

            counts[pref[i]]++;
        }
        return res % MOD;
    }
};
