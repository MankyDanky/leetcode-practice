class Solution {
public:
    const long long B = 64;
    vector<long long> BE;
    const long long MOD = 1e9+7;


    bool exists(vector<int>& nums, int l) {
        long long curr = 0;
        unordered_map<long long, int> seen;

        for (int i = 0; i < l; i++) {
            curr *= B;
            curr %= MOD;
            curr += nums[i];
            curr %= MOD;
        }
        seen[curr] = 1;

        for (int i = l; i < nums.size(); i++) {
            curr = (curr - (nums[i-l] * BE[l-1]) % MOD + MOD) % MOD;
            curr *= B;
            curr %= MOD;
            curr += nums[i];
            curr %= MOD;
            if (!seen.contains(curr)) {
                seen[curr] = 0;
            }
            seen[curr] += 1;
        }
        for (pair<long long, int> p : seen) {
            if (p.second == 1) return true;
        }
        return false;
    }

    int smallestUniqueSubarray(vector<int>& nums) {
        BE.resize(nums.size() + 1);
        BE[0] = 1;
        for (int i = 1; i <= nums.size(); i++) {
            BE[i] = (BE[i-1] * B) % MOD;
        }

        int l = 1;
        int r = nums.size();

        while (l < r) {
            int m = (l + r) / 2;
            if (exists(nums, m)) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return l;
    }
};
